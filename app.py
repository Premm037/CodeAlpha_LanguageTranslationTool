import streamlit as st
from googletrans import Translator

# Page title
st.title("🌍 Language Translation Tool")

# Translator object
translator = Translator()

# Supported languages
languages = {
    "English": "en",
    "Hindi": "hi",
    "Telugu": "te",
    "French": "fr",
    "Spanish": "es",
    "German": "de"
}

# User input
text = st.text_area("Enter text to translate:")

# Language selection
source_lang = st.selectbox("Source Language", list(languages.keys()))
target_lang = st.selectbox("Target Language", list(languages.keys()))

# Translate button
if st.button("Translate"):
    if text.strip() == "":
        st.warning("Please enter some text.")
    else:
        try:
            translated = translator.translate(
                text,
                src=languages[source_lang],
                dest=languages[target_lang]
            )

            st.success("Translation Completed!")
            st.write("### Translated Text:")
            st.write(translated.text)

        except Exception as e:
            st.error(f"Error: {e}")