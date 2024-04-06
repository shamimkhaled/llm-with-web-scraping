
import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.chains import create_extraction_chain


# Load the .env variables
load_dotenv()

# Access the API key from .env
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


def llm_extraction(schemas):

    llm_model = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-16k", openai_api_key=OPENAI_API_KEY, max_tokens=4000)

    langchain_extraction_chain = create_extraction_chain(schemas, llm_model)

    return langchain_extraction_chain




# langchain_extraction_chain.run()
