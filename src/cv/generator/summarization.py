import google.generativeai as genai
import os
import sys

# Set up the API key for Generative AI
genai.configure(api_key="AIzaSyAgq0yvib3_NNgeliiaVeSJa8rN4deQUyo")

# Get the skills input from command-line arguments
skills_input = sys.argv[1]  # Read the skills from the command line

# Use the Generative Model to generate content based on the skills
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content(f"Summarize the following for resume : {skills_input} just give the summary don't bold it and don't write any extra thing just the summarized form in 300 words")

# Print the generated text response
print(response.text)
