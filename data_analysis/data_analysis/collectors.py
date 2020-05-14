from nltk import word_tokenize, WordNetLemmatizer
from re import match


def strict_pre_processor(corpus):
    # strip non-ascii characters
    tokenized = [i for i in word_tokenize(
        corpus) if not match(r'(^\W*$)', i)]
    lemmatizer = WordNetLemmatizer()
    print(tokenized)
    lemmatized = [lemmatizer.lemmatize(i) for i in tokenized]
    return lemmatized
