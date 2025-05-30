sentence = input("Enter a sentence to count words: ").strip()
if not sentence:
    print("No words entered.")
else:
    words = sentence.split()
    word_count = len(words)
    print(f"Total words: {word_count}")


