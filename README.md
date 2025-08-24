# Medi-RAG Chatbot 🏥🤖

A Retrieval-Augmented Generation (RAG) chatbot specifically designed for medical inquiries and healthcare information. This project combines advanced language models with medical knowledge bases to provide accurate and contextual responses to healthcare-related questions.

## 🚀 Features

- **Medical RAG System**: Retrieval-Augmented Generation for accurate medical information
- **Groq API Integration**: Fast inference using Groq's high-performance API
- **Vector Database**: Efficient storage and retrieval of medical documents using FAISS
- **Web Interface**: User-friendly chat interface built with HTML templates
- **CI/CD Pipeline**: Automated deployment using Jenkins
- **Containerized Deployment**: Docker-based deployment on AWS infrastructure
- **Scalable Architecture**: Modular components for easy maintenance and scaling

## 🏗️ Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   User Query    │───▶│   RAG System    │───▶│   LLM (Groq)    │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                              │
                              ▼
                       ┌─────────────────┐
                       │ Vector Database │
                       │    (FAISS)      │
                       └─────────────────┘
```

## 📁 Project Structure

```
medi-rag-chatbot/
├── app/
│   ├── common/
│   │   ├── __init__.py
│   │   ├── custom_exception.py
│   │   └── logger.py
│   └── components/
│       ├── __init__.py
│       ├── data_loader.py
│       ├── embeddings.py
│       ├── llm.py
│       ├── pdf_loader.py
│       ├── retriever.py
│       └── vector_store.py
├── config/
│   ├── __init__.py
│   └── config.py
├── templates/
│   ├── index.html
│   ├── __init__.py
│   └── application.py
├── custom_jenkins/
│   ├── Dockerfile
│   └── Jenkinsfile
├── data/
├── logs/
├── vectorstore/
│   └── db_faiss/
├── .env
├── .gitignore
├── Dockerfile
├── requirements.txt
├── setup.py
└── README.md
```

## 🛠️ Technology Stack

- **Backend**: Python Flask
- **LLM**: Groq API
- **Vector Database**: FAISS (Facebook AI Similarity Search)
- **Document Processing**: PyPDF2/LangChain
- **Containerization**: Docker
- **CI/CD**: Jenkins
- **Cloud Infrastructure**: AWS (EC2, App Runner)
- **Frontend**: HTML/CSS

## 📦 Installation

### Prerequisites

- Python 3.8+
- Docker Desktop (installed and running)
- AWS CLI configured
- Jenkins (Docker-in-Docker setup)
- Groq API key
- GitHub Personal Access Token

### Local Development Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/1morshed1/Medi-RAG-Chatbot.git
   cd Medi-RAG-Chatbot
   ```

2. **Create virtual environment**

   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -e .
   ```

4. **Set up environment variables**

   ```bash
   cp .env.example .env
   # Edit .env with your API keys and configurations
   ```

5. **Run the application**
   ```bash
   python setup.py
   ```

### Docker Setup

1. **Build the Docker image**

   ```bash
   docker build -t medi-rag-chatbot .
   ```

2. **Run the container**
   ```bash
   docker run -p 8080:8080 --env-file .env medi-rag-chatbot
   ```

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_groq_api_key
AWS_REGION=us-east-1
ECR_REPO=medi-rag-chatbot
IMAGE_TAG=latest
SERVICE_NAME=llmops-medical-service
LOG_LEVEL=INFO
```

### Component Configuration

The `config/config.py` file contains all the necessary configurations for:

- API endpoints
- Model parameters
- Vector store settings
- Logging configurations

## 🚀 Deployment

### CI/CD Pipeline

The project uses Jenkins for automated CI/CD with the following stages:

1. **Clone Repository**: Pulls the latest code from GitHub
2. **Build Docker Image**: Creates a containerized version of the application
3. **Security Scanning**: Uses Trivy for vulnerability scanning
4. **Push to ECR**: Uploads the Docker image to AWS Elastic Container Registry
5. **Deploy to App Runner**: Automatically deploys to AWS App Runner

### Jenkins Setup

For detailed Jenkins setup including Docker-in-Docker configuration, follow these steps:

1. **Create Custom Jenkins with Docker**

   ```bash
   cd custom_jenkins
   docker build -t jenkins-dind .
   docker run -d --name jenkins-dind --privileged -p 8080:8080 -p 50000:50000 -v /var/run/docker.sock:/var/run/docker.sock -v jenkins_home:/var/jenkins_home jenkins-dind
   ```

2. **Install Required Tools in Jenkins Container**

   ```bash
   docker exec -u root -it jenkins-dind bash
   apt update -y && apt install -y python3 python3-pip
   # Install Trivy for security scanning
   curl -LO https://github.com/aquasecurity/trivy/releases/download/v0.62.1/trivy_0.62.1_Linux-64bit.deb
   dpkg -i trivy_0.62.1_Linux-64bit.deb
   # Install AWS CLI
   curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
   unzip awscliv2.zip && ./aws/install
   exit
   ```

3. **Configure Credentials**
   - GitHub token: For repository access
   - AWS credentials: For ECR and App Runner deployment

### Manual Deployment

1. **AWS ECR Setup**

   ```bash
   aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin <account-id>.dkr.ecr.us-east-1.amazonaws.com
   ```

2. **Push to ECR**
   ```bash
   docker tag medi-rag-chatbot:latest <account-id>.dkr.ecr.us-east-1.amazonaws.com/medi-rag-chatbot:latest
   docker push <account-id>.dkr.ecr.us-east-1.amazonaws.com/medi-rag-chatbot:latest
   ```

## 📊 Components Overview

### Core Components

- **Data Loader** (`data_loader.py`): Handles loading and preprocessing of medical documents
- **Embeddings** (`embeddings.py`): Generates vector embeddings for documents and queries
- **LLM** (`llm.py`): Interface for Groq API integration
- **PDF Loader** (`pdf_loader.py`): Specialized PDF document processing
- **Retriever** (`retriever.py`): Implements similarity search and document retrieval
- **Vector Store** (`vector_store.py`): Manages FAISS vector database operations

### Supporting Infrastructure

- **Logger** (`logger.py`): Centralized logging system
- **Custom Exception** (`custom_exception.py`): Application-specific error handling
- **Config** (`config.py`): Configuration management

## 🧪 Testing

Run tests using:

```bash
python -m pytest tests/ -v
```

## 📝 Usage

1. **Start the application**
2. **Navigate to** `http://localhost:8080`
3. **Ask medical questions** in the chat interface
4. **Receive AI-powered responses** based on the uploaded knowledge base

### Example Queries

- "What are the symptoms of diabetes?"
- "Explain the side effects of aspirin"
- "What is the recommended dosage for hypertension medication?"

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 🔒 Security

- All API keys are stored as environment variables
- Docker images are scanned for vulnerabilities using Trivy
- AWS IAM roles are used for secure cloud access
- Input validation and sanitization implemented

## 🙏 Acknowledgments

- Groq for high-performance LLM inference
- FAISS for efficient vector similarity search
- AWS for cloud infrastructure
- Jenkins for CI/CD automation

---

**⚠️ Disclaimer**: This chatbot is for informational purposes only and should not replace professional medical advice. Always consult with qualified healthcare providers for medical decisions.
