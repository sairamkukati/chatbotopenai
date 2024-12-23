import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain_community.chat_models import ChatOpenAI
from langchain.chains.question_answering import load_qa_chain

# OPENAI_API_KEY = "YOUR_API_KEY"
st.header("my first chatbot")
# Upload PDF files
with st.sidebar:
    st.title("my docs")
    file = st.file_uploader("Upload your PDF files here and start asking questions!", type="pdf")

# Extract the text
if file is not None:
    pdf_reader = PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    # st.write(text) # To show the test in UI

# Break it into chunks with langchain
    #create a text_splitter with following config
    text_splitter = RecursiveCharacterTextSplitter(
        separators="\n",
        chunk_size=1000, # Means 1000 chars for a chunk. play around here to get best output
        chunk_overlap=150, # last 150 chars of prevoius chunk will overlap with next chunk to preserve continuity
        length_function=len # using length function to split
    )
    chunks = text_splitter.split_text(text)

    # create an instance of Embeddings using OpenAI embeddings
    embeddings = OpenAIEmbeddings(openai_api_key= OPENAI_API_KEY)
    # Create vectore store using FAISS by passing chunks and embeddings
    # This chunks will convert to embeddings here and stored in vector database.
    vector_store = FAISS.from_texts(chunks, embeddings)
    """chunks and thier embeddings will be stored in vector database like this
    embeddings = [
        [0.23, 0.45, 0.67, ...],  # Embedding for "The cat sat on the mat."
        [0.12, 0.34, 0.56, ...],  # Embedding for "Dogs are loyal animals."
        [0.78, 0.89, 0.90, ...],  # Embedding for "AI is transforming the world."
        [0.25, 0.47, 0.68, ...],  # Embedding for "Cats love to chase laser pointers."
    ]
    """

    # Get the user question
    user_question = st.text_input("ask the question here:")
    # Do similarity search and get relavent docs
    if user_question:
        match = vector_store.similarity_search(user_question)
        
        # Define LLM and use it to get human like responses
        llm = ChatOpenAI(
            openai_api_key=OPENAI_API_KEY, 
            temperature=0, # Allowing randomness in output. (0 means no randomness)
            max_token = 1000, # Response size in tokens
            model_name= 'gpt-3.5-turbo', #LLM Model that is being used for human like response
            )
        # converting into human like response
        #chain > get question and relavent docs > pass it to LLM > get output
        chain = load_qa_chain(llm, chain_type="stuff") # defining the chain
        response = chain.run(input_documents=match, question=user_question)  # passing relavent docs and user_question
        st.write(response)


    # Display the results in a chatbot-like UI