
source myenv/bin/activate
pip install requests


import requests

# Function to get the definition of a word using the Free Dictionary API
def get_definition(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    
    try:
        # Make the API request
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        
        # Parse the JSON response
        data = response.json()
        
        # Extract the definition from the API response
        meanings = data[0]["meanings"]
        
        # Print the definitions
        print(f"\nDefinitions for '{word}':")
        for idx, meaning in enumerate(meanings, 1):
            part_of_speech = meaning["partOfSpeech"]
            definition = meaning["definitions"][0]["definition"]
            example = meaning["definitions"][0].get("example", "No example available.")
            
            print(f"\n{idx}. ({part_of_speech}) {definition}")
            print(f"   Example: {example}")
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")

# Main function to run the app
def main():
    print("Welcome to the Word Definition App!")
    
    while True:
        # Ask the user to input a word
        word = input("\nEnter a word to define (or type 'exit' to quit): ").strip()
        
        if word.lower() == "exit":
            print("Goodbye!")
            break
        
        get_definition(word)

# Run the app
if __name__ == "__main__":
    main()
