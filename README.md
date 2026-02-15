1. Prerequisites
Ollama: Download and install from ollama.com.

Python 3.11+: Ensure Python is added to your System PATH.
2. Installation
Clone this repository or navigate to your project folder and install the dependencies:
pip install ollama streamlit
3 Create Custom Models
Before running the app, you need to build the custom personas using their respective Modelfiles:
# Create Mario
ollama create mario -f ModelfileMario

# Create Grandma
ollama create grandma -f ModelfileGrandma

Running the App
Launch the Streamlit interface:
python -m streamlit run app.py

Project Structure
app.py: The main Streamlit application logic and UI.

Mariofile: Configuration for the Mario persona.

GrandmaFile: Configuration for the Grandma persona.

Chatbot/: The directory containing the source code.

The Backend: Ollama runs as a local server on port 11434.

The Logic: The Python ollama library fetches the list of available models and handles the streaming generation.

The Frontend: Streamlit provides a sidebar for model selection and a chat interface that maintains session state for the conversation.
