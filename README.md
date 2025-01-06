# Chat with Langchain - Streamlit Demo App

## Project Description
This is a demo application built using Streamlit and Langchain that allows users to interact with a GPT-based AI assistant. The AI is powered by OpenAI's GPT-4 model and is designed to provide answers based on user queries. The application integrates various components such as environment variable management, dynamic responses, and real-time interaction with the user.

## Features
- Environment Variable Management: Loads API keys and configurations from a .env file.
- User Interaction: Provides an input field for users to type their questions and receive AI-generated responses.
- Real-time AI Responses: The backend leverages the GPT-4 model from OpenAI to answer user queries in real-time.
- Customizable Interface: Displays a personalized image on the homepage and guides users on how to interact with the AI.
- Error Handling: Displays error messages when environment variables are missing or an issue occurs during API communication.
  
## Steps Taken to Build the Application
- 1. **Set up Environment Variables**
The app begins by loading environment variables from a .env file using the python-dotenv library. This includes sensitive information such as API keys for OpenAI and Langchain.
The environment variables are checked for completeness, and the app stops execution if any variables are missing, ensuring proper configuration before the app starts.
- 2. **Load and Display Image**
The app loads and displays a personalized image (Langchain.jpg) using the Pillow library. This image enhances the visual appearance of the interface and engages users when they first visit the app.
- 3. **Set up Chat Prompt Template**
Langchain is used to create a prompt template that defines the structure of the conversation. The system message sets the role of the AI as an "Expert AI Assistant", and the user message will dynamically incorporate the user's input.
- 4. **Streamlit User Interface**
The user interface is designed using Streamlit. It includes:
A title to introduce the app.
A text input box where users can type their questions.
A button that triggers the submission of the question to the AI assistant.
Display of the AI-generated response after processing.
- 5. **Set up LLM (Language Model)**
The app is powered by OpenAI’s GPT-4 model via Langchain. The model is set up with the necessary parameters and connected to the defined prompt template.
Langchain’s output parser processes the AI response and presents it to the user.
- 6. **Error Handling**
Proper error handling is implemented to catch any issues during runtime, including missing environment variables or API communication errors.
If an error occurs, the app displays a user-friendly message with the error details.

## Technologies Used
- Streamlit: For building the interactive web application interface.
- Python-dotenv: For loading environment variables securely from a .env file.
- Pillow: For handling and displaying images in the app.
- Langchain: For prompt management and connecting to OpenAI’s GPT models.
- OpenAI GPT-4: The language model used to generate responses to user queries.









![image](https://github.com/user-attachments/assets/e12e05cb-945b-4651-a365-8d02c91503f8)
