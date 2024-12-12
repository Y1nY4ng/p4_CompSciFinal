import random
from random import shuffle

word_list = ["ribbon","baseball","dogs","document","fabricated","excessive","mississippi","redundant","zebra","mario"]
word = random.choice(word_list)
answer1 = word
def shuffle_word(word):
    word = list(word)
    shuffle(word)
    return ''.join(word)

def level_1():
    for i in range(5):
        print(shuffle_word(word))
        user_guess = input("Level 1: Try to unshuffle the word! ")
        if user_guess == answer1:
            print("Thats Correct!")
            break
        else:
            print("Wrong, Try Again!")

def level_2():
    for i in range(10):
        word = random.choice(word_list)
        answer2 = word
        print(shuffle_word(word))
        user_guess = input("Level 2: Now do it in one guess! ")
        if user_guess == answer2:
            print("Wow! That's Correct Again!")
            break
        else:
            print("Nope, Reshuffling!")

level_1()
level_2()