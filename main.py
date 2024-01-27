from openai import OpenAI
from dotenv import load_dotenv
import os
from sys import argv


# Load environment variables from .env file
load_dotenv()

# Retrieve the API key
API_KEY = os.getenv("OPENAI_API_KEY")

def readFromFile(filename):
    """Reads the prompt from a file and returns it as a string."""
    path = "prompt_source/" + filename
    
    try:
        with open(path, "r", encoding="utf-8") as f:
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
    prompt = readFromFile(filename)

    setupPrompt = readFromFile("_setup.prompt")
    
    if prompt:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            # model="gpt-4-0125-preview",
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
    total_tokens = response.usage.total_tokens
    
    print(f"Prompt:\n{filename}\n")
    
    print(f"Total tokens: {total_tokens}\n")
    
    print(f"Sentiment: {sentiment}\n")
    
    print()
    print(response)
    
    outFile = filename.split(".")[0] + "_output.json"
    writeToFile(outFile, sentiment)
    

if __name__ == "__main__":
    main()