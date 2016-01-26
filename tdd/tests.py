#!/usr/bin/env python3

def rcomplement(dna) :
    '''
    Returns a string with the reverse complement of a DNA sequence.
    Sequences containing non-DNA will return an empty string.
    '''
    return None

def test_rcomplement() :
    assert rcomplement('AACGGT') == 'ACCGTT'
    assert rcomplement('ACGTZ') == ''
