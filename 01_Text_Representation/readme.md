# Chapter 1: Text Representation

## Goal
Understand how a computer converts human language into numbers.

## What I learned in Lesson 1
- Text is first split into individual words (tokenization).
- A vocabulary is created by collecting unique words.
- Each unique word is assigned a unique integer ID.
- A dictionary (word_to_id) maps words to their IDs.
- Any sentence can now be represented as a sequence of integers.

Example:

"The cat drinks milk"

↓

["the", "cat", "drinks", "milk"]

↓

[5, 0, 2, 3]

## Key Python concepts revised
- split()
- set()
- list()
- sorted()
- dictionary
- for loops
- enumerate()

## Important realization
Word IDs are only labels. They do *not* capture meaning. To a computer, "cat" and "dog" are no more similar than "cat" and "milk". This limitation motivates vector embeddings such as Word2Vec.