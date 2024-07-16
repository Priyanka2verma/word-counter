def count_words(text):
   
    # Split the text into words using whitespace as the delimiter
    words = text.split()
    # Count the number of words
    num_words = len(words)
    return num_words

def main():
    
    # Prompt the user to enter a sentence or paragraph
    input_text = input("Please enter a sentence or paragraph: ").strip()
    
    # Check if the input is empty
    if not input_text:
        print("Error: No input provided. Please enter some text.")
    else:
        # Count the number of words in the input text
        word_count = count_words(input_text)
        # Print the word count to the console
        print(f"The number of words in the given text is: {word_count}")

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()
