import random
import copy
from random import shuffle


def game_start():
    number_input = input("Enter the range of word lengths (low,high): ")
    number_input = number_input.strip("()")
    number_range = number_input.split(",")
    global low
    low = int(number_range[0])
    global high
    high = int(number_range[1])
    doc = open("words.txt", 'r')
    content = doc.read()
    global all_words
    all_words = content.splitlines()

    high_word_list = []
    low_word_list = []
    global low_word_list_two
    low_word_list_two = []
    global high_word_list_two
    high_word_list_two = []
    global game_done
    game_done = False
    global game_win
    game_win = 0
    global x
    x = 0
    global yy
    yy = low

    for j in all_words:
        wordLength = len(j)
        if wordLength == high:
            high_word_list.append(j)
    global base_word
    base_word = high_word_list[random.randrange(len(high_word_list))]

    print(base_word)

    for i in all_words:
        wordLength = len(i)
        if wordLength == low:
            low_word_list.append(i)

    for k in high_word_list:
        if check(base_word, k):
            high_word_list_two.append(k)

    for kk in low_word_list:
        if check2(base_word, kk):
            low_word_list_two.append(kk)
    global t
    t = 1
    global low_plus
    low_plus = ""
    global word_dict
    word_dict = {0: low_word_list_two}
    while yy != high - 1:
        yy += 1
        low_plus = ""
        low_plus += str(yy)
        low_plus = []
        for z in all_words:
            if len(z) == yy:
                if check2(base_word, z):
                    low_plus.append(z)
        word_dict[t] = low_plus
        t += 1
    word_dict[t] = high_word_list_two
    global blank_dict
    blank_dict = copy.deepcopy(word_dict)

    for q in blank_dict.keys():
        first_word = ""
        dash = ""
        c = 0
        d = 0
        temp_list = blank_dict[q]
        first_word = temp_list[0]
        dash_loop = len(first_word)
        while d < dash_loop:
            dash += "-"
            d += 1
        while c < len(temp_list):
            blank_dict[q][c] = dash
            game_win += 1
            c += 1
#    print(word_dict)
    for r in blank_dict.values():
        print(r)
    while not game_done:

        word_guess = input("Enter a Guess: ")
        if word_guess == "q":
            for r in word_dict.values():
                print(r)
            game_done = True
            break
        if word_guess == "r":
            for r in word_dict.values():
                print(r)
            game_done = True
            game_start()
        base_word_shuffle = shuffle_word(base_word)
        wrong = True
        for b in word_dict.keys():
            bb = 0
            temp_list_two = word_dict[b]
            while bb < len(temp_list_two):
                if word_dict[b][bb] == word_guess:
                    blank_dict[b][bb] = word_guess
                    print("Correct!")
                    game_win -= 1
                    wrong = False
                bb += 1
        if wrong is True:
            print("Sorry Try Again!")
        print(base_word_shuffle + ":")
        for r in blank_dict.values():
            print(r)
        if game_win == 0:
            print("Congratualtions you won!")
            game_done = True
            game_start()


def shuffle_word(word):
    word = list(word)
    shuffle(word)
    return ''.join(word)


def check(w1, w2):
    if sorted(w1) == sorted(w2):
        return True
    else:
        return False


def check2(ww1, ww2):
    yes = 0
    letters = list(ww1)
    for ii in letters:
        if ii in ww2:
            yes += 1
    if yes >= len(ww2):
        return True
    else:
        return False


game_start()
