# importing the necessary Libraries for the program
import re
from collections import Counter

# function to Count the number of times a word appears in the text
def count_specific_word(article, word):
    words = re.findall(r"\b\w+\b", article.lower())
    return words.count(word.lower())

# function that finds the most commmon word in the whole text
def identify_most_common_word(article):
    words = re.findall(r"\b\w+\b", article.lower())
    word_counts = Counter(words)
    return word_counts.most_common(1)[0]

# function that Calculates the average length of words in the text
def calculate_average_length_word(article):
    words = re.findall(r"\b\w+\b", article.lower())
    total_length = 0

    for word in words:
        total_length += len(word)

    return total_length / len(words)

# function that Counts the number of paragraphs in the text
def count_paragraphs(article):
    paragraphs = re.split(r"\n\s*\n", article.strip())
    return len(paragraphs)

# function that Counts the number of sentences in the text
def count_sentences(article):
    sentences = re.findall(r"[.!?]+", article)
    return len(sentences)

# The Main function that is used to actually run the program, get the needed input and display Results
def main():
    # loading the file for analysis
    file = open("News Article for Python Assessment.txt", "r", encoding="utf-8")
    article = file.read()
    file.close()

    # section for calling the functions, and assigning the result values in given Variables
    word = input("Enter a word to search for: ")
    specific_count = count_specific_word(article, word)
    most_common_word, most_common_count = identify_most_common_word(article)
    average_length = calculate_average_length_word(article)
    paragraphs = count_paragraphs(article)
    sentences = count_sentences(article)

    # Displays the result to the end-user of all the parameters needed
    print(f"\nThe Number of Times [{word}] appears in the Text is: {specific_count} times.")
    print(f"The most common word is '{most_common_word.capitalize()}'; appearing {most_common_count} times.")
    print(f"The average length of words in the text is: {average_length}")
    print(f"The number of paragraphs in the text is: {paragraphs}")
    print(f"The number of sentences in the text is: {sentences}")

main()