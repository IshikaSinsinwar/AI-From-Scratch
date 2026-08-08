#Lesson 1: Vocabulary and token IDs
#1. Raw Text
text = """
the cat drinks milk
the dog drinks milk
the cat sleeps
the dog sleeps
"""

#2. Split Into Words
words = text.split()
print(words)

#3. Remove duplicates using set
print(f"Total words: {len(words)}")
print(f"Unique words: {set(words)}")
print(f"Vocabulary size: {len(set(words))}")

#4. Sorted Vocabulary so that everyone gets the same output
vocab = sorted(list(set(words)))
print(vocab)

#5. Assign every word an ID
word_to_id={}

for i, word in enumerate(vocab):
    word_to_id[word]=i

print(word_to_id)

#6. make computer actually read a sentence
sentence = "the cat drinks milk"

output_list =[] #this is what computer will see

sentence_processed= sentence.split()
for word in sentence_processed:
    output_list.append(word_to_id[word])
output_list

#Lesson 2: Reverse Mapping and Decoding (Convert Numbers Back to Text)

print(word_to_id)

id_to_word={}

for word, id in word_to_id.items():
    id_to_word[id]=word

print(id_to_word)

encoded_sentence = [5,0,2,3]
decoded_words=[]

for word_id in encoded_sentence:
    decoded_words.append(id_to_word[word_id])

print(decoded_words)

decoded_sentence = " ".join(decoded_words)
print(decoded_sentence)




