# vowel_counter.py
# Author: Nadiya Safeer
# A simple Python project for analysing vowel frequency in text.

import matplotlib.pyplot as plt

def count_vowels(text):
    vowels = "aeiou"
    text = text.lower()
    return {v: text.count(v) for v in vowels}

def plot_vowel_counts(vowel_counts):
    plt.bar(vowel_counts.keys(), vowel_counts.values(), color='skyblue')
    plt.title("Vowel Frequency in Text")
    plt.xlabel("Vowels")
    plt.ylabel("Count")
    plt.show()

if __name__ == "__main__":
    print("🔤 Vowel Counter Tool")
    text = input("Enter your text: ")
    counts = count_vowels(text)
    print("Vowel Counts:", counts)
    plot_vowel_counts(counts)
