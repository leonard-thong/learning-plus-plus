import nltk
import re
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer
from string import punctuation
from autocorrect import spell
from unidecode import unidecode
import json

snowball_stemmer = SnowballStemmer('english')
wordnet_lemmatizer = WordNetLemmatizer()


class Preprocess:
    def __init__(self):
        pass

    def autospell(self, text):
        spells = [spell(w) for w in (nltk.word_tokenize(text))]
        return " ".join(spells)

    def to_lower(self, text):
        return text.lower()

    def remove_numbers(self, text):
        output = ''.join(c for c in text if not c.isdigit())
        return output

    def remove_punct(self, text):
        text = unidecode(text)
        return ''.join(c for c in text if c not in punctuation)

    def remove_Tags(self, text):
        cleaned_text = re.sub('<[^<]+?>', '', text)
        return cleaned_text

    def sentence_tokenize(self, text):
        sent_list = []
        for w in nltk.sent_tokenize(text):
            sent_list.append(w)
        return sent_list

    def word_tokenize(self, text):
        return [w for sent in nltk.sent_tokenize(text) for w in nltk.word_tokenize(sent)]

    def remove_stopwords(self, sentence):
        stop_words = stopwords.words('english')
        return ' '.join([w for w in nltk.word_tokenize(sentence) if not w in stop_words])

    def stem(self, text):
        stemmed_word = [snowball_stemmer.stem(word) for sent in nltk.sent_tokenize(text) for word in
                        nltk.word_tokenize(sent)]
        return " ".join(stemmed_word)

    def lemmatize(self, text):
        lemmatized_word = [wordnet_lemmatizer.lemmatize(word) for sent in nltk.sent_tokenize(text) for word in
                           nltk.word_tokenize(sent)]
        return " ".join(lemmatized_word)

    def preprocess(self, text):
        lower_text = self.to_lower(text)
        sentence_tokens = self.sentence_tokenize(lower_text)
        wordlist = []
        for each_sent in sentence_tokens:
            lemmatizzed_sent = self.lemmatize(each_sent)
            clean_text = self.remove_numbers(lemmatizzed_sent)
            clean_text = self.remove_punct(clean_text)
            clean_text = self.remove_Tags(clean_text)
            clean_text = self.remove_stopwords(clean_text)
            word_tokens = self.word_tokenize(clean_text)
            for i in word_tokens:
                wordlist.append(i)
        return wordlist


def main():
    file = open("input.txt", "rb")
    s = file.read().decode('utf-8')
    process = Preprocess()
    word_list = process.preprocess(s)
    json_file = open('/Users/leonard/Projects/lecturepp/engine/words_dictionary.json', 'rb')
    json_string = json_file.read()
    data = (json.loads(json_string))
    rare_words = data.keys()
    final_words = list(set(word_list).intersection(rare_words))
    return final_words


if __name__ == '__main__':
    main()
