from pprint import pprint

frequency = {"a": 8.12,
             "b": 1.49,
             "c": 2.71,
             "d": 4.32,
             "e": 12.02,
             "f": 2.30,
             "g": 2.03,
             "h": 5.92,
             "i": 7.31,
             "j": 0.10,
             "k": 0.69,
             "l": 3.98,
             "m": 2.61,
             "n": 6.95,
             "o": 7.68,
             "p": 1.82,
             "q": 0.11,
             "r": 6.02,
             "s": 6.28,
             "t": 9.10,
             "u": 2.88,
             "v": 1.11,
             "w": 2.09,
             "x": 0.17,
             "y": 2.11,
             "z": 0.07,
             }


def consistent(f, w, slots):
    lowerLetters = ''.join([c for c in f if c.islower()])
    for i in range(5):
        if f[i].isupper() and f[i] != w[i].upper():
            return False
        if w[i] not in slots[i]:
            return False
    for c in lowerLetters:
        if c in w:
            w = w.replace(c, ' ')
        else:
            return False
    return True


def wordScore(word):
    return sum([frequency[c] for c in set(word)])


if __name__ == '__main__':
    with open('word-list.txt') as file:
        words = file.read().split('\n')
        while True:
            print("New Game!")
            slots = ['abcdefghijklmnopqrstuvwxyz',
                     'abcdefghijklmnopqrstuvwxyz',
                     'abcdefghijklmnopqrstuvwxyz',
                     'abcdefghijklmnopqrstuvwxyz',
                     'abcdefghijklmnopqrstuvwxyz']
            while True:
                guess = input('Enter Guess: ').lower()
                if not guess:
                    break
                feedback = input('Enter Feedback: ')
                if not feedback:
                    break

                for i in range(len(guess)):
                    if feedback[i].isupper():
                        slots[i] = ''.join([c if c == feedback[i].lower() else '.' for c in slots[i]])
                    elif feedback[i].islower():
                        slots[i] = slots[i].replace(guess[i], '.')
                    elif feedback[i] == '.' and guess[i] not in feedback.lower():
                        for j in range(len(slots)):
                            slots[j] = slots[j].replace(guess[i], '.')

                legalWords = dict()
                for word in words:
                    if consistent(feedback, word, slots):
                        legalWords[word] = wordScore(word)

                sortedLegalWords = sorted(legalWords, key=legalWords.get, reverse=True)[:5]

                print("Top Guesses:")
                for i in range(min(len(sortedLegalWords), 5)):
                    print(f"{i + 1}. {sortedLegalWords[i]} ({round(legalWords[sortedLegalWords[i]], 2)})")

