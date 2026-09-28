# function to Count the number of times a word appears in the text
def count_specific_word(article, word):
    words = article.lower().split()
    word = word.lower()
    count = 0

    for current_word in words:
        current_word = current_word.strip(".,!?;:'\"()[]{}-")
        if current_word == word:
            count += 1
    return count

# function that finds the most common word in the whole text
def identify_most_common_word(article):
    words = article.lower().split()
    word_counts = {}

    for current_word in words:
        current_word = current_word.strip(".,!?;:'\"()[]{}-")
        if current_word != "":
            if current_word in word_counts:
                word_counts[current_word] += 1
            else:
                word_counts[current_word] = 1

    most_common_word = ""
    highest_count = 0

    for current_word in word_counts:
        if word_counts[current_word] > highest_count:
            most_common_word = current_word
            highest_count = word_counts[current_word]
    return most_common_word, highest_count

# function that Calculates the average length of words in the text
def calculate_average_word_length(article):
    words = article.lower().split()
    total_length = 0
    word_count = 0

    for word in words:
        word = word.strip(".,!?;:'\"()[]{}-")
        if word != "":
            total_length += len(word)
            word_count += 1
    if word_count == 0:
        return 0
    return total_length / word_count

# function that Counts the number of paragraphs in the text
def count_paragraphs(article):
    if article.strip() == "":
        return 1
    lines = article.strip().splitlines()
    paragraphs = 0
    inside_paragraph = False

    for line in lines:
        if line.strip() != "":
            if inside_paragraph == False:
                paragraphs += 1
                inside_paragraph = True
        else:
            inside_paragraph = False
    return paragraphs

# function that Counts the number of sentences in the text
def count_sentences(article):
    if article.strip() == "":
        return 1

    sentences = 0
    position = 0

    while position < len(article):
        if article[position] in ".!?":
            sentences += 1
            while position + 1 < len(article) and article[position + 1] in ".!?":
                position += 1
        position += 1
    return sentences