# This is a very short python script

# This program is meant to find anagrams.

print("You are about to find anagrams!!!!")


def find_anagram(word, anagram):
    if sorted(word) == sorted(anagram):
        return True
    return False


# Collect user input.
word = input("Enter the word: ")
anagram = input("Enter the anagram: ")
print(find_anagram(word, anagram))
