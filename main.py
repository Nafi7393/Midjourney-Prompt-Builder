import google.generativeai as genai
import os
from dotenv import load_dotenv


class MidjourneyPromptGenerator:
    """
    This class helps generate a single high-quality Midjourney prompt.
    """

    def __init__(self, api_key=None, model_name="gemini-1.5-flash"):
        """
        Initializes the generator, loading the API key and configuring the API.

        Args:
            api_key (str): The API key for Gemini. If not provided, it will be loaded from the GEMINI_API_KEY environment variable.
            model_name (str): The model name to use for generating content.
        """
        if api_key:
            self.api_key = api_key
        else:
            raise ValueError("Error: Please set your Gemini API key in the GEMINI_API_KEY environment variable.")

        self.model_name = model_name
        genai.configure(api_key=self.api_key)

        self.model = genai.GenerativeModel(model_name=self.model_name)

    def get_user_input(self, prompt):
        """
        Helper function to get input from the user.

        Args:
            prompt (str): The prompt to display to the user.

        Returns:
            str: The user's input.
        """
        return input(prompt).strip()

    def generate_prompt(self, base_idea, art_style, mood_or_theme=None,
                        specific_elements=None, emotion_or_feeling=None, color_palette=None,
                        additional_details=None, composition_style=None):
        """
        Generates a refined Midjourney prompt based on provided parameters or user input.

        Args:
            base_idea: The base idea for the artwork.
            art_style: The desired art style.
            mood_or_theme: The mood or theme to capture.
            specific_elements: Any specific elements to include.
            emotion_or_feeling: The emotion or feeling to evoke.
            color_palette: The color palette to focus on.
            additional_details: Any additional details to enhance impact.
            composition_style: The composition style.

        Returns:
            str: The generated high-quality Midjourney prompt.
        """
        # Craft a high-quality prompt combining creativity and technical aspects
        prompt = f"Create a Midjourney prompt where the main idea is {base_idea}. The art style should be {art_style}."
        if mood_or_theme:
            prompt += f" Make sure to capture the essence of {mood_or_theme}."
        if specific_elements:
            prompt += f" Incorporate elements of {specific_elements}."
        if emotion_or_feeling:
            prompt += f" The scene should evoke {emotion_or_feeling}."
        if color_palette:
            prompt += f" The color palette should focus on {color_palette}."
        if additional_details:
            prompt += f" Include details like {additional_details} to enhance the overall impact."
        if composition_style:
            prompt += f" The composition should be {composition_style}."

        prompt += f"""\n \n HERE ARE SOME EXAMPLE OUTPUT:
        1. /imagine prompt:A bulldog wearing sunglasses, riding a bicycle with a basket full of flowers, pop art style, vibrant colors, bold outlines, comic book aesthetic, dynamic pose, cityscape background
        2. /imagine prompt:A kawaii anime cat wearing a pink and white sailor-style high school uniform, with large, sparkling eyes, a blush on her cheeks, and a cute little heart-shaped purse. The cat is holding a single pink rose in her paw, surrounded by sparkling hearts and a soft, pastel pink background. Focus on the cat's adorable features and create a design suitable for a t-shirt

Please note that the output should be in this format and only in this format: '/imagine prompt: [YOUR PROMPT]"""

        response = self.model.generate_content(prompt)

        return response


if __name__ == "__main__":
    load_dotenv()
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    generator = MidjourneyPromptGenerator(api_key=GEMINI_API_KEY, model_name="gemini-1.5-flash")
    midjourney_prompt = generator.generate_prompt(base_idea="skeleton riding bike",
                                                  art_style="pop art",
                                                  mood_or_theme="",
                                                  specific_elements="",
                                                  emotion_or_feeling="",
                                                  color_palette="",
                                                  additional_details="",
                                                  composition_style="bright illustration")
    print(midjourney_prompt.text)
