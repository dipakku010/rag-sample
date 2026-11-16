# RAG Chatbot 🙌

A powerful **Retrieval Augmented Generation (RAG)** chatbot built with Streamlit that enables intelligent question-answering over PDF documents. Upload any PDF file and get accurate, context-based answers powered by advanced language models.

---

## 🌟 Features

- **PDF Upload & Processing**: Seamlessly upload PDF files for instant processing
- **Intelligent Q&A**: Ask questions about your PDF content and get accurate, context-aware responses
- **Vector Database Integration**: Uses FAISS for efficient similarity search over document embeddings
- **Advanced Embeddings**: Leverages HuggingFace embeddings (all-mpnet-base-v2) for semantic understanding
- **Production-Ready LLM**: Powered by Groq's OpenAI-compatible API for fast, reliable responses
- **Safety Guardrails**: Comprehensive prompt injection and hallucination prevention mechanisms
- **Maximum Marginal Relevance Search**: Diversified retrieval to reduce redundancy and improve answer quality
- **Streaming UI**: Real-time processing feedback with status indicators
- **Wide Layout Support**: Optimized for desktop and large screen viewing

---

## 🚀 Quick Start

### Prerequisites

Before you begin, ensure you have:

- **Python 3.8+** installed on your system
- **pip** (Python package manager)
- A **Groq API key** (get one free at [console.groq.com](https://console.groq.com))

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/rag-sample.git
   cd rag-sample
   ```

2. **Create a Virtual Environment** (Recommended)

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Configuration

#### Set Up Your Groq API Key

**Option 1: Environment Variable (Recommended for Production)**

```bash
export GROQ_API_KEY="your-groq-api-key-here"
```

**Option 2: Interactive Prompt (Development)**
When you run the application, you'll be prompted to enter your Groq API key if it's not set in the environment.

#### Get Your Groq API Key

1. Visit [console.groq.com](https://console.groq.com)
2. Sign up or log in to your account
3. Navigate to the API Keys section
4. Create a new API key
5. Copy and save it securely

---

## 📖 Usage

### Running the Application

```bash
streamlit run rag/ragchatbot.py
```

The application will open in your default browser at `http://localhost:8501`

### Step-by-Step Guide

1. **Upload a PDF**
   - Click "Upload a PDF file" in the left sidebar
   - Select your PDF document
   - Wait for processing to complete (you'll see progress indicators)

2. **Ask Questions**
   - Once processing is done, type your question in the input field
   - Press Enter to submit
   - The chatbot will return context-based answers from your PDF

3. **Interpret Results**
   - Answers are always based on PDF content only
   - References and page information are derived from the document
   - If information isn't in the PDF, the chatbot will clearly state this

### Example Questions

- "What is the main topic of this document?"
- "Summarize the key findings mentioned in the document"
- "Can you explain the methodology used in this research?"
- "What are the recommendations provided in this document?"

---

## 🏗️ Project Structure

```
rag-sample/
├── README.md                          # Project documentation
├── requirements.txt                   # Python dependencies
├── rag/
│   ├── ragchatbot.py                 # Main Streamlit application
│   └── tab_style.py                  # UI styling components
├── layouts/
│   └── sentiment_analysis_page_layout.py  # Layout templates
└── sample-file/                       # Sample PDFs for testing
```

---

## 🔄 How RAG Works

### The RAG Pipeline

This chatbot implements a sophisticated Retrieval Augmented Generation pipeline:

```
User PDF → Extract Text → Split into Chunks → Generate Embeddings
                                                        ↓
User Question → Convert to Embeddings → Vector Similarity Search
                                                ↓
                                    Retrieved Relevant Chunks
                                                ↓
                            LLM (ChatGroq) + System Prompt
                                                ↓
                                        Final Answer
```

### Key Components

1. **Text Extraction**: `pdfplumber` extracts text from each PDF page
2. **Chunking**: `RecursiveCharacterTextSplitter` creates meaningful chunks with overlap
   - Chunk size: 1000 characters
   - Overlap: 200 characters (for context continuity)

3. **Embeddings**: HuggingFace's `all-mpnet-base-v2` model converts text to semantic vectors

4. **Vector Store**: FAISS (Facebook AI Similarity Search) enables fast similarity searches

5. **Retrieval**: Maximum Marginal Relevance (MMR) search returns diverse, relevant chunks

6. **Generation**: Groq's LLM generates answers based on retrieved context

---

## 🔒 Safety Features & Guardrails

This application includes **comprehensive safety mechanisms** to prevent misuse:

### Hallucination Prevention

- Explicitly prevents AI from fabricating information outside the PDF
- Blocks usage of general knowledge or external sources
- Requires all responses to be grounded in document context

### Prompt Injection Defense

- Prevents context injection attacks
- Blocks adversarial follow-up requests attempting to override instructions
- Maintains strict scope boundaries

### Scope Limitation

- Refuses to provide professional advice (legal, medical, financial)
- Won't generate code or system commands
- Won't process requests for current events or real-time data
- Blocks role-playing as professionals

### Response Integrity

- No fabricated citations or sources
- Clear statements when information is unavailable
- Flagged ambiguous questions for clarification

### Key Safety Prompt Rules

```
✅ DO: Answer only based on PDF context
✅ DO: Provide complete, well-explained answers
✅ DO: Include relevant details and numbers from the document

❌ DON'T: Make up or invent information
❌ DON'T: Use general knowledge or external sources
❌ DON'T: Provide professional advice
❌ DON'T: Claim expertise or credentials
❌ DON'T: Execute code or generate scripts
```

---

## 🛠️ Technologies Used

| Technology      | Purpose                                             |
| --------------- | --------------------------------------------------- |
| **Streamlit**   | Web UI framework for rapid development              |
| **LangChain**   | Orchestration of LLM chains and RAG pipelines       |
| **FAISS**       | Vector database for efficient similarity search     |
| **HuggingFace** | Pre-trained embeddings and NLP models               |
| **Groq API**    | Fast LLM inference with OpenAI-compatible interface |
| **pdfplumber**  | PDF text extraction                                 |
| **Python 3.8+** | Core programming language                           |

---

## 📋 Requirements

All dependencies are listed in `requirements.txt`:

```
pdfplumber
streamlit
langchain-text-splitters
langchain-community
langchain-core
langchain-groq
langchain-huggingface
faiss-cpu  # Use faiss-gpu if you have CUDA support
```

---

## 🔑 API Keys & Credentials

### Groq API

1. **Create Account**: Visit [console.groq.com](https://console.groq.com)
2. **Generate API Key**: Go to API Keys section
3. **Set Environment Variable**:
   ```bash
   export GROQ_API_KEY="your-key-here"
   ```

**Note**: Keep your API key secure. Never commit it to version control.

---

## 🚨 Troubleshooting

### Common Issues

#### Issue: "GROQ_API_KEY not found"

**Solution**: Ensure your Groq API key is set:

```bash
export GROQ_API_KEY="your-key-here"
```

#### Issue: "Module not found" errors

**Solution**: Install dependencies:

```bash
pip install -r requirements.txt
```

#### Issue: PDF processing takes too long

**Solution**: This is normal for large PDFs. The app shows progress:

- Text extraction time depends on PDF size
- Embedding generation takes 1-2 seconds per 1000 chunks
- First query might take longer as embeddings are generated

#### Issue: Low-quality answers

**Solution**:

- Ensure your PDF has extractable text (not scanned images)
- Try asking more specific questions
- Break complex questions into simpler ones

#### Issue: Connection timeout to Groq API

**Solution**:

- Check your internet connection
- Verify your API key is valid
- Ensure you haven't exceeded API rate limits

---

## 🎯 Performance Tips

- **Smaller PDFs**: Faster processing (< 50 pages recommended for optimal performance)
- **Specific Questions**: More precise answers than vague questions
- **Temperature Setting**: Currently set to 0.3 for deterministic answers
- **Max Tokens**: Limited to 1024 for faster responses

---

## 📝 Customization

### Modifying Chunking Strategy

Edit the chunk parameters in `ragchatbot.py`:

```python
text_splitter = RecursiveCharacterTextSplitter(
    separators=["\n\n", "\n", ". ", " ", ""],
    chunk_size=1000,      # Increase for larger chunks
    chunk_overlap=200     # Increase for more context overlap
)
```

### Changing the Embedding Model

Replace the model in the embeddings section:

```python
embeddings = HuggingFaceEmbeddings(model_name="your-model-name")
```

### Adjusting LLM Parameters

```python
llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.3,      # 0=deterministic, 1=creative
    max_tokens=1024,      # Increase for longer responses
    timeout=60,
    max_retries=2,
)
```

---

## 🤝 Contributing

We welcome contributions! Here's how to help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### Contribution Areas

- Bug fixes and improvements
- Performance optimizations
- Better error handling
- Documentation enhancements
- New features or integrations

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 📚 Learning Resources

- [LangChain Documentation](https://python.langchain.com/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [FAISS Documentation](https://github.com/facebookresearch/faiss)
- [Groq API Docs](https://console.groq.com/docs)
- [HuggingFace Models](https://huggingface.co/models)

---

## 🙋 Support & Questions

If you encounter issues or have questions:

1. Check the **Troubleshooting** section above
2. Review existing [GitHub Issues](https://github.com/yourusername/rag-sample/issues)
3. Create a new issue with:
   - Clear description of the problem
   - Steps to reproduce
   - Error messages or logs
   - Your environment (OS, Python version, etc.)

---

## 🎓 About RAG (Retrieval Augmented Generation)

RAG is a technique that enhances LLM responses by:

1. **Retrieving** relevant information from a knowledge base (your PDF)
2. **Augmenting** the LLM prompt with this retrieved context
3. **Generating** accurate answers grounded in real documents

This approach significantly reduces hallucination and ensures all answers are based on factual document content.

---

## 🌟 Acknowledgments

- Built with [LangChain](https://www.langchain.com/)
- UI powered by [Streamlit](https://streamlit.io/)
- Vector storage by [FAISS](https://github.com/facebookresearch/faiss)
- LLM provided by [Groq](https://www.groq.com/)

---

**Star this repository if you find it helpful!** ⭐
