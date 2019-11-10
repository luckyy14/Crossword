Description

This is a project on a crossword solver which takes inputs as clues and uses their synonyms from a dictionary and fills it in an empty crossword. This uses recussive-back-tracking approach to solve the empty crossword.

Requirement

    Python 2.7
    nltk.corpus wordnet

Run

    python Crossword.py


Configuration

    First line contains N size of crossword puzzles N x N
    Next line contains configuration of puzzles
        - indicates free space
        = indicates blocked space
    Next line contains list of words whose synonyms need to be fitted to the crossword puzzles delimited by ;
    Next line contains list of size of solution respectively that need to be fitted to the crossword puzzles delimited by ;

Example

7
=======
=-----=
=-=====
=-=====
-------
=======
=======
bad;accept;red
5;4;7

Using Dictionary.py

    python Dictionary.py
    input a word to display its synonyms

Copyright (c) 2019 by Lakshay Baheti, Saurabh Mohata, Keshav Garg.
Authors:

    Lakshay Baheti
    Saurabh Mohata
    Keshav Garg
    
