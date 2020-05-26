#!/usr/bin/env python
# -*- coding : utf-8 -*-


def dna_strand(dna):
    complementary_dna = dna.translate(str.maketrans('ATCG', 'TAGC'))
    return complementary_dna


if __name__ == '__main__':
    result = dna_strand('GTAT')
    print(result)