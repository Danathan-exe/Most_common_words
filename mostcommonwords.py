import os
import sys
from collections import Counter

text = input("Please enter the file location of the text that you would like to read from: ")

try:
    with open(text, "r") as file:
        words = file.read().split()
        counter = Counter(words)
        most_common_words = counter.most_common(5)
        print("The most common words in this text are:")
        for word, count in most_common_words:
            print(f"{word}: {count}")
except FileNotFoundError:
    print(f"File not found: {text}")
except Exception as e:
    print(f"An error occurred: {e}")
