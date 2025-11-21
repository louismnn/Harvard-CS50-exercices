"""word = input("Input: ")

word = word.replace("a", "").replace("e", "").replace("i", "").replace("o", "").replace("u", "")

print("Output: ", word)"""

word = input("Input: ")

letters = [('a', ''), ('e', ''), ('i', ''), ('o', ''), ('u', '')]

for letter, blanc in letters:
    if letter in word:
        word = word.replace(letter, blanc)

print("Output: ", word)