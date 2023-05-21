"""
Sentence: iterate over words using a generator function
"""

# tag::SENTENCE_GEN[]
import re
import reprlib

RE_WORD = re.compile(r'\w+')


class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return f'Sentence({reprlib.repr(self.text)})'

    def __iter__(self):
        yield from self.words
        # <3>

# done! <4>

# end::SENTENCE_GEN[]
