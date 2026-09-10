from random import randint

HAND_SIZE = 10
LETTER_POOL = {
    'A': 9, 
    'B': 2, 
    'C': 2, 
    'D': 4, 
    'E': 12, 
    'F': 2, 
    'G': 3, 
    'H': 2, 
    'I': 9, 
    'J': 1, 
    'K': 1, 
    'L': 4, 
    'M': 2, 
    'N': 6, 
    'O': 8, 
    'P': 2, 
    'Q': 1, 
    'R': 6, 
    'S': 4, 
    'T': 6, 
    'U': 4, 
    'V': 2, 
    'W': 2, 
    'X': 1, 
    'Y': 2, 
    'Z': 1
}

SCORE_CHART = {
    "A": 1, "E": 1, "I": 1, "O": 1, "U": 1,
    "L": 1, "N": 1, "R": 1, "S": 1, "T": 1,
    "D": 2, "G": 2,
    "B": 3, "C": 3, "M": 3, "P": 3,
    "F": 4, "H": 4, "V": 4, "W": 4, "Y": 4,
    "K": 5,
    "J": 8, "X": 8,
    "Q": 10, "Z": 10
}


def draw_letters():
    letter_pool = LETTER_POOL.copy()

    # create list of all letters that have quantity more than 0
    available_letters = [
        letter for letter, quantity in letter_pool.items()
        if quantity > 0
    ]

    hand = []

   # loop until we have 10 letters in hand
    while len(hand) < HAND_SIZE:
        index = randint(0, len(available_letters) - 1)
        letter = available_letters[index]

        hand.append(letter)
        letter_pool[letter] -= 1

        # remove letter from available_letters if quality is 0
        if letter_pool[letter] == 0:
            available_letters.pop(index)

    return hand

def uses_available_letters(word, letter_bank):
    # Create a map to store each letter and its count
    letter_bank_map = {}

    for letter in letter_bank:
        letter_bank_map[letter] = letter_bank_map.get(letter, 0) + 1

    # Check whether the word uses available letters
    for letter in word.upper():
        count = letter_bank_map.get(letter, 0)

        if count == 0:
            return False

        letter_bank_map[letter] = count - 1

    return True

def score_word(word):
    score = 0

    for letter in word.upper():
        score += SCORE_CHART.get(letter, 0)

    if len(word) >= 7:
        score += 8

    return score

def get_highest_word_score(word_list):
    best_word = ('', 0)

    for word in word_list:
        score = score_word(word)

        if score > best_word[1]:
            best_word = (word, score)

        elif score == best_word[1]:
            if len(best_word[0]) == 10:
                continue

            if len(word) == 10 or len(word) < len(best_word[0]):
                best_word = (word, score)

    return best_word