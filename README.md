
# ChatBOT using OpenAI GPT-3.5 Turbo

This project is a chatbot that uses the OpenAI GPT-3.5 Turbo model to answer user queries based on the content of uploaded PDF files. The chatbot extracts text from the uploaded document, processes it into manageable chunks, and leverages OpenAI embeddings and FAISS vector store for efficient similarity search. Finally, the chatbot provides responses using a LangChain-based Question Answering pipeline.

---

## Features
- Upload PDF files and extract text for processing.
- Use OpenAI embeddings to convert text chunks into vector representations.
- Store and retrieve vectors efficiently with FAISS.
- Generate human-like responses using the GPT-3.5 Turbo model.
- Supports architecture as shown below:  
  ![Architecture](./architecture.png)

---

## Requirements
### Prerequisites:
1. **Python (3.8+)**
2. **Python IDE** (e.g., VS Code, PyCharm, or Jupyter Notebook)
3. **OpenAI account** for API access

### Python Libraries:
Install the required libraries using the following command:
```bash
pip install -r requirements.txt
```

---

## Local Setup
### Steps to Run:
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/chatbotopenai.git
   cd chatbotopenai
   ```

2. **Install Dependencies:**
   Ensure you have all required libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up OpenAI API Key:**
   - Obtain your API key from OpenAI.  
   - Replace `YOUR_API_KEY` in the code with your actual OpenAI API key.

4. **Run the Application:**
   Start the Streamlit app:
   ```bash
   streamlit run chat.py
   ```

5. **Test the Application:**
   - Upload the provided `Constitution_India_subset.pdf` file using the sidebar.
   - Ask questions related to the uploaded document and receive responses.

---

## Input File
The repository includes the sample PDF file:
- `Constitution_India_subset.pdf`  
Use this file to test the chatbot functionality.

---

## Example Usage
### Step 1: Upload a PDF
- Use the file uploader in the sidebar to upload `Constitution_India_subset.pdf` or any PDF.

### Step 2: Ask Questions
- Input your query in the chatbot UI, such as:
  ```text
  What is the preamble of the Constitution of India?
  ```
- Get relevant and accurate responses powered by GPT-3.5 Turbo.

---

## How It Works
1. **PDF Parsing:** Extracts text from uploaded PDFs.
2. **Text Chunking:** Breaks down the text into smaller, manageable chunks for embedding.
3. **Vector Store:** Converts chunks into vector embeddings using OpenAI's embedding model and stores them in FAISS for similarity search.
4. **Question Answering:** Matches user queries with relevant chunks and generates human-like responses using GPT-3.5 Turbo via LangChain's QA pipeline.

---

## Contribution
Feel free to contribute to this project by creating pull requests or submitting issues.

---

## License
This project is licensed under the MIT License.
