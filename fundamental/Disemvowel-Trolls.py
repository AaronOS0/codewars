#!/usr/bin/env python
# -*- coding : utf-8 -*-


def disemvowel(string):
    vowel = 'aAeEiIoOuU'
    sentence_list = list(string)
    [sentence_list.remove(character) for character in string if character in vowel]
    new_string = "".join(sentence_list)
    return new_string


if __name__ == '__main__':
    result = disemvowel("What are you, a communist?")
    print(result)

