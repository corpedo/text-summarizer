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
The owners of a New Zealand volcano that erupted in 2019, killing 22 people, have had their conviction over the disaster thrown out by the country's High Court.
Whakaari Management Limited (WML) was found guilty in 2023 of failing to keep visitors safe and fined just over NZ$1m ($560,000; £445,000). They were also ordered to pay NZ$4.8m in reparation to the victims.
However, following an appeal, the High Court ruled on Friday that the company only owned the land and were not responsible for people's safety.
White Island, which is also known by its Māori name, Whakaari, is New Zealand's most active volcano and has been erupting in some form since 2011.
It had been showing signs of heightened unrest for weeks before the fatal December 2019 eruption, which killed almost half of the people who were on it at the time. Most were tourists, including 17 from Australia and three from the US.
Another 25 people were injured, with many suffering extensive burns.
High Court Justice Simon Moore said on Friday that while WML licensed tours of the volcano, there was nothing in these agreements that gave the company control of what was happening on the island day to day.
He agreed that it was reasonable for the company to rely on tour operators, as well as emergency management and science organisations, to assess risks to safety.
Justice Moore added that, in coming to his decision, he had not ignored the pain and grief of the families that had been affected.
"It is impossible not to be deeply moved and affected by the sheer scale and nature of the human loss in this case," he said.
Thirteen parties in total, including tour operators, were charged over the disaster. WML was the last to receive a verdict after six had pleaded guilty, while six more had their charges dismissed.
The case against WML was the largest action of its kind brought by New Zealand's regulator, Worksafe NZ, who said it acknowledged the High Court ruling and was considering whether to appeal.
James Cairney, a lawyer for James, Andrew and Peter Buttle - three brothers who own the company - said the family welcomed the decision, Radio New Zealand reported. He added that the Buttles hoped it would "bring certainty for all landowners who grant others recreational access to their land".
The Buttle family has owned Whakaari/White Island since the 1930s, when their grandfather bought it and placed it in a family trust. It is one of only a few privately owned islands in New Zealand.
The brothers had previously been on trial in relation to the 2019 disaster as individuals over alleged breaches of New Zealand's workplace health and safety legislation. Those charges were dismissed in 2023.
"""

summary = text_summarizer(text)
print(summary)