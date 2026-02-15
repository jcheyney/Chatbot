import streamlit as st
import ollama

st.title("🦙 Ollama Model Switcher")

def get_local_models():
    try:
        models_info = ollama.list()
        model_names = []

        for m in models_info.models:
            model_names.append(m.model)
            
        return model_names
    except Exception as e:
        st.error(f"Error fetching models: {e}")
        return []


available_models = get_local_models()

if available_models:
    selected_model = st.sidebar.selectbox("Choose a model:", available_models)
    st.sidebar.info(f"Currently chatting with: **{selected_model}**")
else:
    st.sidebar.warning("No models found. Run 'ollama pull llama3' in your terminal.")
    selected_model = None


if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Say something..."):
    if not selected_model:
        st.error("Please select a model first!")
    else:
        st.chat_message("user").markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            
            for chunk in ollama.generate(model=selected_model, prompt=prompt, stream=True):
                full_response += chunk['response']
                message_placeholder.markdown(full_response + "▌")
            
            message_placeholder.markdown(full_response)
        
        st.session_state.messages.append({"role": "assistant", "content": full_response})