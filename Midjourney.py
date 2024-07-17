import google.generativeai as genai
import os
from dotenv import load_dotenv

class MidjourneyPromptGenerator:
    """
    This class helps generate a single high-quality Midjourney prompt.
    """

    def __init__(self):
        """
        Loads the API key from environment variable and configures the API.
        """
        load_dotenv()
        self.api_key = os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            print("Error: Please set your Gemini API key in the GEMINI_API_KEY environment variable.")
            exit(1)
        genai.configure(api_key=self.api_key)

    def get_user_input(self, prompt):
        """
        Helper function to get input from the user.
        """
        return input(prompt).strip()

    def generate_prompt(self):
        """
        Prompts the user for a single concept and generates a refined Midjourney prompt.
        """
        base_idea = self.get_user_input("Enter the base idea for your artwork: ")
        art_style = self.get_user_input("Enter the desired art style (e.g., surreal, cyberpunk): ")
        additional_info = self.get_user_input("Enter any additional information (optional): ")
        mood_or_theme = self.get_user_input("Enter the mood or theme you want to capture (optional): ")
        specific_elements = self.get_user_input("Enter any specific elements to include (optional): ")
        emotion_or_feeling = self.get_user_input("Enter the emotion or feeling you want to evoke (optional): ")
        color_palette = self.get_user_input("Enter the color palette to focus on (optional): ")
        additional_details = self.get_user_input("Enter any additional details to enhance impact (optional): ")
        composition_style = self.get_user_input("Enter the composition style (optional): ")

        # Craft a high-quality prompt combining creativity and technical aspects
        prompt = f"Create total of 3 Midjourney prompt where the main idea is {base_idea}. The art style should be {art_style}."

        if additional_info:
            prompt += f" It should include {additional_info}."
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

        prompt += f"\n EXAMPLE OUTPUT: /imagine prompt:A bulldog wearing sunglasses, riding a bicycle with a basket full of flowers, pop art style, vibrant colors, bold outlines, comic book aesthetic, dynamic pose, cityscape background"
        # Use Gemini to refine the prompt further
        model_name = "gemini-1.5-flash"  # Replace with your preferred model
        model = genai.GenerativeModel(model_name)
        response = model.generate_content(prompt)

        # Leverage the generated text to potentially improve the prompt (optional)
        # You can analyze the response.text and modify the prompt here (e.g., add keywords)

        return response.text


if __name__ == "__main__":
    generator = MidjourneyPromptGenerator()
    midjourney_prompt = generator.generate_prompt()
    print("Your high-quality Midjourney prompt:")
    print(midjourney_prompt)
