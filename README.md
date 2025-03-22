# word-definer
from PyDictionary import PyDictionary

def define_word(word):
    dictionary = PyDictionary()
    
    # Get the meaning of the word
    meaning = dictionary.meaning(word)
    
    if meaning:
        print(f"Definitions for '{word}':")
        for part_of_speech, definitions in meaning.items():
            print(f"{part_of_speech.capitalize()}:")
            for idx, definition in enumerate(definitions, 1):
                print(f"  {idx}. {definition}")
    else:
        print(f"Sorry, no definitions found for '{word}'.")

if __name__ == "__main__":
    word = input("Enter a word to define: ")
    define_word(word)
