import nltk.corpus
import nltk.tokenize.punkt
import nltk.stem.snowball
import string

target_sentence = "In the eighteenth century it was often convenient to regard man as a clockwork automaton."

sentences = ["In the eighteenth century it was often convenient to regard man as a clockwork automaton.",
             "in the eighteenth century    it was often convenient to regard man as a clockwork automaton",
             "In the eighteenth century, it was often convenient to regard man as a clockwork automaton.",
             "In the eighteenth century, it was not accepted to regard man as a clockwork automaton.",
             "In the eighteenth century, it was often convenient to regard man as clockwork automata.",
             "In the eighteenth century, it was often convenient to regard man as clockwork automatons.",
             "It was convenient to regard man as a clockwork automaton in the eighteenth century.",
             "In the 1700s, it was common to regard man as a clockwork automaton.",
             "In the 1700s, it was convenient to regard man as a clockwork automaton.",
             "In the eighteenth century.",
             "Man as a clockwork automaton.",
             "In past centuries, man was often regarded as a clockwork automaton.",
             "The eighteenth century was characterized by man as a clockwork automaton.",
             "Very long ago in the eighteenth century, many scholars regarded man as merely a clockwork automaton.",]


stopwords = nltk.corpus.stopwords.words('english')
stopwords.extend(string.punctuation)
stopwords.append('')

def get_wordnet_pos(pos_tag):
    if pos_tag[1].startswith('J'):
        return (pos_tag[0], wordnet.ADJ)
    elif pos_tag[1].startswith('V'):
        return (pos_tag[0], wordnet.VERB)
    elif pos_tag[1].startswith('N'):
        return (pos_tag[0], wordnet.NOUN)
    elif pos_tag[1].startswith('R'):
        return (pos_tag[0], wordnet.ADV)
    else:
        return (pos_tag[0], wordnet.NOUN)

tokenizer = nltk.tokenize.punkt.PunktWordTokenizer()
lemmatizer = nltk.stem.wordnet.WordNetLemmatizer()
def is_ci_partial_noun_set_token_stopword_lemma_match(a, b):
    """Check if a and b are matches."""
    pos_a = map(get_wordnet_pos, nltk.pos_tag(tokenizer.tokenize(a)))
    pos_b = map(get_wordnet_pos, nltk.pos_tag(tokenizer.tokenize(b)))
    lemmae_a = [lemmatizer.lemmatize(token.lower().strip(string.punctuation), pos) for token, pos in pos_a \
                    if pos == wordnet.NOUN and token.lower().strip(string.punctuation) not in stopwords]
    lemmae_b = [lemmatizer.lemmatize(token.lower().strip(string.punctuation), pos) for token, pos in pos_b \
                    if pos == wordnet.NOUN and token.lower().strip(string.punctuation) not in stopwords]

    # Calculate Jaccard similarity
    ratio = len(set(lemmae_a).intersection(lemmae_b)) / float(len(set(lemmae_a).union(lemmae_b)))
    return (ratio > 0.66)

for sentence in sentences:
   print(is_ci_partial_noun_set_token_stopword_lemma_match(target_sentence, sentence), sentence)