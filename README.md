# 🤖 IntelliChat - AI-Powered File Analysis Chatbot

An intelligent chatbot application that enables natural language conversations with uploaded documents using advanced AI models including Google Gemini and local language models.

## 🚀 Features

### 🔥 Core Capabilities
- **Multi-Format File Support**: PDF, DOCX, TXT, CSV file processing
- **Dual AI Integration**: Google Gemini LLM + Local SLM models
- **Intelligent Summarization**: Automatic text summarization for large files (50K+ characters)
- **Real-time Translation**: Hindi translation for accessibility
- **Interactive Chat**: Persistent conversation history with timestamps
- **Smart Response Modes**: Simple vs Detailed answer styles
- **Download Functionality**: Export chat history as text files

### 🎯 Key Highlights
- **🧠 Smart Processing**: Handles files up to 50K+ characters with auto-summarization
- **🌐 Multi-language**: Built-in Hindi translation support
- **💬 Memory Management**: Maintains context throughout conversations
- **📱 Responsive UI**: Clean, modern Streamlit interface
- **⚡ Real-time**: Instant AI responses with loading indicators
- **🔄 Flexible Models**: Switch between Gemini and local models

## 🛠️ Technology Stack

### Backend
- **Python 3.8+** - Core programming language
- **Streamlit** - Web application framework
- **Google Generative AI** - Gemini LLM integration
- **LangChain** - AI model orchestration
- **Transformers** - Local model support
- **PyTorch** - Deep learning framework

### File Processing
- **PyPDF2** - PDF document processing
- **python-docx** - Word document handling
- **pandas** - CSV data analysis
- **Google API Client** - Google services integration

### AI Models
- **Google Gemini** - Advanced large language model
- **Local SLM** - Self-hosted small language model
- **Translation API** - Hindi language translation

## 📁 Project Structure\
intellichat/
│
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── test.txt              # Sample test file
│
├── utils/                # Utility modules
│   ├── init.py
│   ├── file_reader.py    # File processing utilities
│   ├── gemini_utils.py   # Google Gemini integration
│   ├── slm_utils.py      # Local model utilities
│   ├── summarizer.py     # Text summarization
│   └── translator.py     # Hindi translation
│
├── config/               # Configuration files
│   ├── api_keys.py       # API key management
│   └── model_config.py   # Model configurations
│
├── data/                 # Sample data files
│   ├── sample.pdf
│   ├── sample.docx
│   └── sample.csv
│
└── docs/                 # Documentation
├── user_guide.md
└── api_reference.md
