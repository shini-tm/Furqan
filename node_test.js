const Word2Vec = require('word2vec');
const fs = require('fs');
const cosine = require('cosine-similarity');

// Sample translations
const translations = ['the God of humankind,', 'the God of mankind,', 'The God of mankind,', 'the God of mankind,', /* ... */ ];

// Load a pre-trained Word2Vec model (you need to download and load a model here)
const modelFilePath = 'models/GoogleNews-vectors-negative300.bin';

Word2Vec.loadModel(modelFilePath, (model) => {
    if (!model) {
        console.error('Failed to load the Word2Vec model.');
        return;
    }

    // Function to convert a sentence to a vector using Word2Vec
    function sentenceToVector(sentence, model) {
        const words = sentence.toLowerCase().split(' ');
        const vector = words
            .map(word => model.getVector(word))
            .filter(vector => vector); // Filter out words not in the model
        const dimension = vector[0].length;
        if (vector.length === 0) {
            return new Array(dimension).fill(0);
        }
        return vector.reduce((sum, current) => sum.map((value, i) => value + current[i]), new Array(dimension).fill(0)).map(value => value / vector.length);
    }

    // Calculate similarity scores
    const similarityScores = [];

    translations.forEach((translationI, i) => {
        const scoresI = [];
        const vectorI = sentenceToVector(translationI, model);

        translations.forEach((translationJ, j) => {
            const vectorJ = sentenceToVector(translationJ, model);
            const score = cosine(vectorI, vectorJ);
            scoresI.push(score);
        });

        similarityScores.push(scoresI);
    });

    // Print the similarity scores
    similarityScores.forEach((scores, i) => {
        console.log(`Translation ${i + 1}:`);
        scores.forEach((score, j) => {
            console.log(`Similarity to Translation ${j + 1}: ${score.toFixed(2)}`);
        });
        console.log();
    });
});
