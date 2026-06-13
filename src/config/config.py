import os
from dotenv import load_dotenv

load_dotenv() #Loading the env variable from "".env"

GROQ_API_KEY = os.getenv("GROQ_API_KEY")  #These converting GROQ_API_KEY to normal API key