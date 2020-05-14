from nltk import word_tokenize, WordNetLemmatizer
from re import match


def strict_preprocessor(corpus):
    # strip non-ascii characters
    tokenized = [i for i in word_tokenize(
        corpus) if not match(r'(^\W*$)', i)]
    lemmatizer = WordNetLemmatizer()
    return [lemmatizer.lemmatize(i) for i in tokenized]
