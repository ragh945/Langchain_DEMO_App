import os
import dotenv
from dotenv import load_dotenv
from PIL import Image
import streamlit as st
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# Load environment variables
load_dotenv()

# Check if the environment variables are loaded correctly
openai_api_key = os.getenv("OpenAI_api_key")
langchain_api_key = os.getenv("Langchain_api_key")
langchain_project = os.getenv("Langchain_project")

# Handle missing environment variables
if not openai_api_key or not langchain_api_key or not langchain_project:
    st.error("Environment variables are missing. Please check your .env file.")
    st.stop()  # Stop execution if environment variables are missing

# Set environment variables
os.environ["OpenAI_api_key"] = openai_api_key
os.environ["Langchain_api_key"] = langchain_api_key
os.environ["Langchain_project"] = langchain_project
os.environ["Langchain_Tracing_V2"] = "true"

# Load image for the app
img = Image.open(r"C:\Users\RAGHAVENDRA KUMAR\Downloads\Langchain.jpg")
st.image(img,use_container_width=True)

# Chat prompt template setup
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an Expert AI Assistant. Provide responses based on the questions realted to AI field."),
        ("user", "Question: {input}")
    ]
)

# Streamlit interface setup
st.title("🤖 Chat with Langchain Demo")
st.markdown("Enter your question below and click the button to get a response:")

# Input box for user prompt
user_input = st.text_input("Your question", placeholder="Type your question here...")

# Submit button with emoji
submit_button = st.button("🚀 Ask the AI")

# LLM setup with OpenAI Chat model
llm = ChatOpenAI(model="gpt-4")
output_parser = StrOutputParser()

# Chain setup
chain = prompt | llm | output_parser

# Display response when user submits a question
if submit_button and user_input:
    with st.spinner("Thinking..."):
        try:
            response = chain.invoke({"input": user_input})
            st.write("### 🤔 AI's Response:")
            st.write(response)
        except Exception as e:
            st.error(f"An error occurred: {e}")
