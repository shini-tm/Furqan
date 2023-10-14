from gensim.scripts import word2vec2tensor

# Convert the binary model to the text format
word2vec2tensor('models/GoogleNews-vectors-negative300.bin', 'models/GoogleNews-vectors-negative300.txt')
