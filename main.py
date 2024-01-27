from openai import OpenAI
from dotenv import load_dotenv
import os
from sys import argv

# Load environment variables from .env file
load_dotenv()

# Retrieve the API key
API_KEY = os.getenv("OPENAI_API_KEY")

def readPrompt(filename):
    """Reads the prompt from a file and returns it as a string."""
    path = "prompt_source/" + filename
    
    try:
        with open(path, "r") as f:
            return f.read()
    except FileNotFoundError:
        print("File not found.")
        return None

def writeToFile(filename, text):
    """Writes the text to a file."""
    path = "prompt_outputs/" + filename
    
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
    except FileNotFoundError:
        print("File not found.")
        return None

def main():
    filename = argv[1] if len(argv) > 1 else "neutral.txt"
    
    # Configure OpenAI API key
    client = OpenAI(
        api_key=API_KEY
    )

    # Get the prompt from a file
    prompt = readPrompt(filename)

    setupPrompt = """Analyze the sentiment of the following news article in a scale from 1-10 (1 = negative, 10 = positive). ONLY OUTPUT A SINGLE NUMBER AND AN EMOTION (e.g. 5, neutral). You are designed to output in json format."""
    
    if prompt:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            response_format={
                "type": "json_object"
            },
            messages=[
                {"role": "system", "content": setupPrompt},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=150,
        )
        # print(response)
        print()
    else:
        print("No prompt available to process.")
    
    sentiment = response.choices[0].message.content
    
    print("Prompt:", prompt)
    
    print("Sentiment:", sentiment)
    
    
    outFile = filename.split(".")[0] + "_output.json"
    writeToFile(outFile, sentiment)
    

if __name__ == "__main__":
    main()