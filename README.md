# Word Definer

This is a simple Python script that allows users to enter a word and fetch its definition using the Free Dictionary API.

## Features
- Fetches definitions for any word.
- Displays part of speech and example usage.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/jackshaojiewei/word-definer.git
   cd word-definer
   ```

2. Install dependencies:
   ```sh
   pip install requests
   ```

## Usage

Run the script using Python:

```sh
python codethatmayormaynotwork.py
```

Then enter a word when prompted, and the script will return its definition.

## Example Output
```
Enter a word to define (or type 'exit' to quit): word

Definitions for 'word':
1. (noun) The smallest unit of language that has a particular meaning and can be expressed by itself; the smallest discrete, meaningful unit of language. (contrast morpheme.)
   Example: No example available.
2. (verb) To say or write (something) using particular words; to phrase (something).
   Example: I’m not sure how to word this letter to the council.
3. (interjection) Truth, indeed, that is the truth! The shortened form of the statement "My word is my bond."
   Example: "Yo, that movie was epic!" / "Word?" ("You speak the truth?") / "Word." ("I speak the truth.")
```

## API Used
This project uses the [Free Dictionary API](https://dictionaryapi.dev/) to fetch word definitions.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributions
Feel free to fork the repository, open issues, or submit pull requests to enhance the script!

