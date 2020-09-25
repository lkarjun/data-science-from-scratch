from typing import NamedTuple, List, Set, Tuple, Dict, Iterable
import re
import math
from collections import defaultdict


def tokenize(text: str) -> Set[str]:
    useless_words: List = ['to', 'for', 'is', 'was',
                           'the', 'this', 'ie', 'if',
                           'i', 'am'
                           ]
    texts = text.lower()  # convert to lowercase
    all_words = re.findall(r"\w+", texts)  # extract the words
    all_words = [words
                 for words in all_words
                 if words not in useless_words]
    return set(all_words)


# assert tokenize("Data Science is science") == {"data", "science"}


class Message(NamedTuple):
    text: str
    is_spam: bool


class NaiveBayesClassifier:

    def __init__(self, k: float = 0.5) -> None:
        self.k = k  # smoothing factor
        self.tokens: Set[str] = set()
        self.tokens_spam_counts: Dict[str, int] = defaultdict(int)
        self.tokens_ham_counts: Dict[str, int] = defaultdict(int)
        self.spam_messages = self.ham_messages = 0

    def train(self, messages: Iterable[Message]) -> None:
        for message in messages:
            # Increment message counts
            if message.is_spam:
                self.spam_messages += 1
            else:
                self.ham_messages += 1
            # increment word counts
            for token in tokenize(message.text):
                self.tokens.add(token)
                if message.is_spam:
                    self.tokens_spam_counts[token] += 1
                else:
                    self.tokens_ham_counts[token] += 1

    def _probabilities(self, token: str) -> Tuple[float, float]:
        '''returns P(token | spam) and P(token | ham)'''
        spam = self.tokens_spam_counts[token]
        ham = self.tokens_ham_counts[token]

        p_token_spam = (spam + self.k) / (self.spam_messages + 2 * self.k)
        p_token_ham = (ham + self.k) / (self.ham_messages + 2 * self.k)

        return p_token_spam, p_token_ham

    def predict(self, text: str) -> float:
        text_tokens = tokenize(text)
        log_prob_if_spam = log_prob_if_ham = 0.0

        # Iterate through each word in our vocabulary
        for token in self.tokens:
            prob_if_spam, prob_if_ham = self._probabilities(token)

            # If *token* appears in the message,
            # add the log probabilty of seeing it.
            if token in text_tokens:
                log_prob_if_spam += math.log(prob_if_spam)
                log_prob_if_ham += math.log(prob_if_ham)

            # Otherwise add the log probability of _not_ seeing it,
            # which is log(1 - probability of seeing it)

            else:
                log_prob_if_spam += math.log(1.0 - prob_if_spam)
                log_prob_if_ham += math.log(1.0 - prob_if_ham)

        prob_if_spam = math.exp(log_prob_if_spam)
        prob_if_ham = math.exp(log_prob_if_ham)
        return prob_if_spam/(prob_if_spam + prob_if_ham)
