import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.probability import FreqDist

def text_summarizer(text, num_sentences=3):
    # Text into sentences
    sentences = sent_tokenize(text)
    
    # Text into words
    words = word_tokenize(text.lower())
    
    # Removing stop words
    stop_words = set(stopwords.words("english"))
    filtered_words = [word for word in words if word.casefold() not in stop_words]
    
    # Calculate word frequencies
    fdist = FreqDist(filtered_words)
    
    # Assign scores to sentences based on word frequencies
    sentence_scores = {}
    for i, sentence in enumerate(sentences):
        for word in word_tokenize(sentence.lower()):
            if word in fdist:
                if i in sentence_scores:
                    sentence_scores[i] += fdist[word]
                else:
                    sentence_scores[i] = fdist[word]
    
    # Sort sentences by scores in descending order
    sorted_sentences = sorted(sentence_scores, key=lambda x: sentence_scores[x], reverse=True)
    
    # Select the top `num_sentences` sentences for the summary
    summary_sentences = sorted(sorted_sentences[:num_sentences])
    
    # Create the summary
    summary = ' '.join([sentences[i] for i in summary_sentences])
    
    return summary

# Example usage
text = """
Exciting news! I've been working on a Python script for text summarization as part of #100DaysOfCode! 🐍📝

With this script, you can quickly summarize lengthy texts while preserving the main points. It uses NLP techniques, such as tokenization, stop word removal, and word frequency analysis, to generate concise summaries. 📚✂️

Check out my GitHub repository to see the code in action and start creating your own text summarizer! Let's level up our NLP skills together! 💪🔥 #Python #NLP #TextSummarization
"""

summary = text_summarizer(text)
print(summary)