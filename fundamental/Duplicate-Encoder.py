#!/usr/bin/env python
# -*- coding : utf-8 -*-


def duplicate_encode(word):
    # Ignore capitalization
    word = word.lower()
    # Get all the character, remove duplication
    all_character = set(word)
    # Count the number of each character
    num_iter = map(lambda character: word.count(character), all_character)
    # Use a dict to store character:num
    dic = dict(zip(all_character, num_iter))
    # Replace word with )/(
    result = "".join(['(' if dic[character] == 1 else ')' for character in word])
    return result


if __name__ == '__main__':
    string = duplicate_encode('dIi@&  ')
    print(string)
