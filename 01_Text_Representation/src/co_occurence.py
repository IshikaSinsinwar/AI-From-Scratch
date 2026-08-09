# Lesson 3: Couccurence and Word Relationships 
# Co-occurence: words that appear together are probably related

sentences = [
    "the cat drinks milk",
    "the dog drinks milk",
    "the cat sleeps",
    "the dog sleeps"
]

for sentence in sentences:
    words = sentence.split()
    print(words)

co_occurence ={}

for sentence in sentences:
    words = sentence.split()
    for word in words:
        if word not in co_occurence:
            co_occurence[word]=[]
            print(co_occurence)


#all possible pairings
for sentence in sentences:
    words = sentence.split()

    for word in words:
        for other_word in words:
            if other_word!=word:
                co_occurence[word].append(other_word)

print(co_occurence)

#Building ACtual Co-occurence matrix

co_occurence = {}


for sentence in sentences:
    words = sentence.split()

    for word in words:
        if word not in co_occurence:
            co_occurence[word]={}

        for other_word in words:
                if other_word!=word:
                    if other_word not in co_occurence[word]:
                        co_occurence[word][other_word]=1
                    else:
                        co_occurence[word][other_word]+=1

print(co_occurence)

#Next We want to build co_occurence matrix

vocab = list(co_occurence.keys())
print(vocab)
co_matrix = []
for word in vocab:
    row = []
    for other_word in vocab:
        count=co_occurence[word].get(other_word,0)
        row.append(count)

    co_matrix.append(row)
    print(co_matrix)


cat_index=vocab.index("cat")

cat_vector = co_matrix[cat_index]
print("cat:", cat_vector) #word vectors for cat using co_occurence from vocab