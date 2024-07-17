import streamlit as st
from Midjourney import MidjourneyPromptGenerator
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Set Page Title
st.set_page_config(page_title="Midjourney Prompt Generator")


# Define the Streamlit app
def main():
    # Custom CSS
    with open("style.css", "r") as file:
        content = file.read()
    custom_css = f"<style>{content}</style>"
    st.markdown(custom_css, unsafe_allow_html=True)

    # Title and Sidebar Header
    st.title("Midjourney Prompt Generator")
    st.sidebar.header("Settings")

    # Input for Gemini API Key
    api_key_env = os.getenv("GEMINI_API_KEY")
    api_key = st.sidebar.text_input("Enter your Gemini API Key", value=api_key_env if api_key_env else "", type="password")

    # Slider for number of prompts
    num_prompts = st.sidebar.slider("Number of Prompts to Generate", min_value=1, max_value=5, value=1)

    # Row 1: Base Idea, Art Style
    row1_col1, row1_col2 = st.columns(2)
    base_idea = row1_col1.text_input("Base Idea", "")
    art_style = row1_col2.text_input("Art Style", "")

    # Row 2: Additional Details
    additional_details = st.text_input("Additional Details", "")

    # Row 3: Specific Elements, Composition Style
    row3_col1, row3_col2 = st.columns(2)
    specific_elements = row3_col1.text_input("Specific Elements", "")
    composition_style = row3_col2.text_input("Composition Style", "")

    # Row 4: Mood or Theme, Emotion or Feeling, Color Palette
    row4_col1, row4_col2, row4_col3 = st.columns(3)
    mood_or_theme = row4_col1.text_input("Mood or Theme", "")
    emotion_or_feeling = row4_col2.text_input("Emotion or Feeling", "")
    color_palette = row4_col3.text_input("Color Palette", "")

    # Session state initialization for storing prompts
    if "prompts" not in st.session_state:
        st.session_state.prompts = []

    if st.sidebar.button("Generate Prompts", key='generate-button'):
        # Validate API key
        if api_key.strip() == "":
            st.error("Please enter your Gemini API Key.")
        else:
            try:
                # Initialize the generator with user-provided API key
                generator = MidjourneyPromptGenerator(api_key=api_key, model_name="gemini-1.5-flash")

                # Clear previous prompts
                st.session_state.prompts.clear()

                # Generate the specified number of prompts based on user inputs
                for i in range(1, num_prompts + 1):
                    try:
                        prompt = generator.generate_prompt(base_idea=base_idea,
                                                           art_style=art_style,
                                                           mood_or_theme=mood_or_theme,
                                                           specific_elements=specific_elements,
                                                           emotion_or_feeling=emotion_or_feeling,
                                                           color_palette=color_palette,
                                                           additional_details=additional_details,
                                                           composition_style=composition_style)
                        # Add each generated prompt to session state
                        st.session_state.prompts.append(prompt.text)
                    except Exception as e:
                        st.error(f"Error generating prompt {i}: {str(e)}")
            except Exception as e:
                st.error(f"Error initializing MidjourneyPromptGenerator: {str(e)}")

    # Display the prompts stored in session state
    if st.session_state.prompts:
        st.success("Generated Midjourney Prompts:")
        for i, prompt in enumerate(st.session_state.prompts, 1):
            st.markdown(f'<div class="prompt-output">'
                        f'<div class="prompt-number">Prompt {i}</div>'
                        f'<div class="prompt-text">{prompt}</div>'
                        f'</div>', unsafe_allow_html=True)


if __name__ == "__main__":
    main()
