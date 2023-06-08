#!/usr/bin/python3
def multiple_returns(sentence):
    new_sentence = len(sentence)
    if new_sentence == 0:
        return (new_sentence, None)
    else:
        return (new_sentence, sentence[0])
