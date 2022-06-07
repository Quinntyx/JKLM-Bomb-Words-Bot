# BOMB WORDS BOT
# JKLM.fun
# Credits: Zlare#7771
try:
    from pynput.keyboard import Key, Controller
except ImportError:
    import os
    print("Installing dependencies on first run")
    os.system("pip install pynput")
    from pynput.keyboard import Key, Controller
import time
import random
keyboard = Controller()

flex_mode = False
flex_cap = 12
autosubmit_mode = True
speed = 1

key = {
    True: "ENABLED",
    False: "DISABLED"
}

if __name__ == "__main__":
    print("JKLM Bomb Words Bot by Zlare")
    print(f"Flex: {key[flex_mode]}", end='')
    if flex_mode:
        print(f" Target: {flex_cap}", end='')
    print()
    print(f"AutoSubmit: {key[autosubmit_mode]}")
    print("============================")
    print(f"Speed: {speed}")

with open("../wordlist_full.txt", 'r') as f:
    data = [i.lower() for i in f.read().splitlines()]

with open("extensions.txt", 'r') as f:
    data.extend([i.lower() for i in f.read().splitlines()])

data = list(set(data))


letter_weights = {
    'a': 0.75,
    'b': 1,
    'c': 1,
    'd': 1,
    'e': 0.75,
    'f': 1.3,
    'g': 1,
    'h': 1,
    'i': 0.75,
    'j': 2.3,
    'k': 0,
    'l': 1,
    'm': 1,
    'n': 1,
    'o': 0.8,
    'p': 1,
    'q': 2.5,
    'r': 1,
    's': 1,
    't': 1,
    'u': 1.5,
    'v': 1.8,
    'w': 0,
    'x': 0,
    'y': 0,
    'z': 0,
    '-': 0.25,
    "'": 0.1,

}


class AddSet(set):
    def __iadd__(self, value):
        return self.__add__(value)

    def __add__(self, value):
        return AddSet(self.union(value))


# Create a list to store words that have already been guessed once before, that way you won't hit
# "aah this has been guessed before" issues
# Will also offer 2-3 top choices in case someone has already guessed the best one [TBI]

guessed_words = []
guessed_letters = AddSet()  # every time pick a word, add it with guessed_letters in order to keep track of bonuses


def value(word, is_flex=None, this_guessed_letters=None):
    if is_flex is None:
        is_flex = flex_mode
        # print(f"Defaulting Flex Mode to {is_flex}")
    """Returns the value associated with a word, calculated by its length and guessed_letters."""
    if this_guessed_letters is None:
        this_guessed_letters = guessed_letters
    score = 1
    for letter in list(set(word)):
        if letter in this_guessed_letters:
            continue
        score += letter_weights[letter]

    word_len_cap = 10
    if is_flex:
        word_len_cap = flex_cap

    if len(word) < word_len_cap:
        word_len = word_len_cap
    else:
        word_len = len(word)

    score_mult = 1 / (1.2 ** (word_len - word_len_cap))

    if is_flex:
        score_mult = (1.1 ** (word_len - word_len_cap))
        if word_len < flex_cap:
            score /= 3

    # print(score)
    # print(score_mult)

    return score * (1 + score_mult) / 2


def guess(word):
    global guessed_letters
    global guessed_words
    guessed_letters += word
    guessed_words.append(word)
    if not gold():
        guessed_letters = AddSet()
        print("Gold Letters Exhausted, restarting computation.")


def get_best(dataset, is_flex=None, this_guessed_letters=None):
    max_score = []
    for i in dataset:
        i_val = value(i, is_flex, this_guessed_letters)
        try:
            if max_score[0] < i_val:
                max_score[0] = i_val
                max_score[1] = i
        except IndexError:
            # print("First Word, Adding " + i + " with score", i_val)
            max_score = [i_val, i]
    return max_score


def find_containing(dataset, substr):
    return [i for i in dataset if substr in i and i not in guessed_words]


def gold():
    return [i for i in 'abcdefghijelmnopqrstuv' if i not in guessed_letters]


def clear():
    global guessed_letters
    guessed_letters = AddSet()
    print("Manually cleared bonus")


def flex(val=flex_cap):
    global flex_mode
    global flex_cap
    flex_mode = not flex_mode
    if flex_mode:
        flex_cap = val
        print(f"Flex Enabled, len {flex_cap}")
    else:
        print("Flex Disabled")


def setVar(var, value):
    globals()['var'] = value
    print(f"Set {var} to {globals()['var']}")


def submit(word):
    length = len(word) * 2 / speed + 1
    time.sleep(0.1)
    for i in word:
        keyboard.type(i)
        time.sleep(random.random()/length)
        if random.random() < 0.3:
            time.sleep((random.random() + 2) / length)
    time.sleep(0.05)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)


def search(prompt):
    return get_best(find_containing(data, prompt), False, AddSet())


def autosubmit():
    global autosubmit_mode
    autosubmit_mode = not autosubmit_mode


def tab():
    keyboard.press(Key.alt)
    # time.sleep(0.1)
    keyboard.press(Key.tab)
    # time.sleep(0.2)
    keyboard.release(Key.tab)
    # time.sleep(0.1)
    keyboard.release(Key.alt)


if __name__ == "__main__":
    while True:
        inval = input("prompt >  ")
        if inval.startswith(':'):
            out = eval(inval[1:])
            if out:
                print(out)
            continue
        this_guess = get_best(find_containing(data, inval))
        if not this_guess:
            print("No Answer")
            continue
        print(round(this_guess[0], 3), this_guess[1])
        guess(this_guess[1])

        if autosubmit_mode:
            tab()
            submit(this_guess[1])
            tab()
