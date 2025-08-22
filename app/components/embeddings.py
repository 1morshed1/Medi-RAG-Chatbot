from langchain_huggingface import HuggingFaceEmbeddings

from app.common.logger import get_logger
from app.common.custom_exception import CustomException

logger = get_logger(__name__)

def get_embedding_model():
    try:
        logger.info("Initializing HuggingFace embeddings model.")

        model = HuggingFaceEmbeddings( 
            model_name = "sentence-transformers/all-MiniLM-L6-v2"
        )
        logger.info("HuggingFace embeddings model initialized successfully.")

        return model
    
    except Exception as e:
        error_message = CustomException(f"Error initializing HuggingFace embeddings model: {str(e)}")
        logger.error(str(error_message))
        raise error_message
