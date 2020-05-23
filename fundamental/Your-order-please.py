#!/usr/bin/env python
# -*- coding : utf-8 -*-


def order(sentence):
    # Transform str to list, split by space
    word_list = sentence.split(" ")
    # Extract the number of each word and make tuple, then Sort it
    sorted_list = sorted([(character, word) for word in word_list for character in word if character.isdigit()])
    # Make the new string
    result = " ".join([item[1] for item in sorted_list])
    return result


if __name__ == '__main__':
    string = order("4of Fo3r pe6ople g3ood th5e the2")
    print(string)
