import pandas

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
dic_alphabet = {row.letter:row.code for (_, row) in alphabet.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ")
res = [dic_alphabet[letter.upper()] for letter in word]
print(res)
