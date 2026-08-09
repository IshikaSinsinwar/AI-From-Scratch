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

## What I learned in Lesson 2

- A dictionary can be reversed to generate and ID to word mapping
- .items() return key-value pairs from a dictionary
- Encoded word IDs can be converted back to words
- join() combines list of string into a single sentence
- split() and join() are opposite operations

Example:

Word -> ID:
{
    "cat": 0,
    "dog": 1,
    "drinks": 2
}

ID -> Word:
{
    0: "cat",
    1: "dog",
    2: "drinks"
}

## What I learned in Lesson 3

- Words that appear together in the same sentence can be considered co-occurring words.
- A co-occurrence dictionary can store relationships between words.
- A nested dictionary can be used to represent these relationships.
- A dictionary inside another dictionary can be accessed using:
  dictionary[key][value]
- Co-occurrence can be counted instead of simply storing whether a relationship exists.
- A co-occurrence matrix represents these relationships numerically.
- Rows and columns of the matrix represent words from the vocabulary.
- Each cell contains the number of times two words co-occur.
- A row of the co-occurrence matrix can be treated as a numerical vector representing a word.
- These numerical vectors are an early step toward representing words in a way that a neural network can process.

Example:

Sentences:

"The cat drinks milk"
"The dog drinks milk"
"The cat sleeps"
"The dog sleeps"

↓

Vocabulary:

["the", "cat", "drinks", "milk", "dog", "sleeps"]

↓

Co-occurrence relationships:

"cat" appears with:
- "the"
- "drinks"
- "milk"
- "sleeps"

↓

Numerical representation:

cat → [2, 0, 1, 1, 0, 1]

The position of each number corresponds to a word in the vocabulary.

## Key Python concepts revised

- nested dictionaries
- dictionary .get()
- .index()
- list of lists
- .append()
- nested for loops
- if / else
- counting occurrences

## Important realization

A word can now be represented by a vector of numbers based on the words it appears with.

For example, instead of representing "cat" only as:

cat → 0

we can represent it using its relationships with other words:

cat → [2, 0, 1, 1, 0, 1]

This contains information about the context in which the word appears.

However, these vectors are still based on simple word counts. They are large and sparse, and they do not yet capture semantic meaning in a sophisticated way.

This motivates the next step: *word embeddings*, where words are represented by smaller, dense vectors learned from data.