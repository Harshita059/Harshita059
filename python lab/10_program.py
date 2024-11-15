def word_count():
    # Take input from the user
    text = input("Enter some text: ")
    
    # Split the text into words
    words = text.split()
    
    # Count and print the number of words
    print(f"Word count: {len(words)}")

# Run the function
word_count()
