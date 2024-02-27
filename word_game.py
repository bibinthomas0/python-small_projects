import random

words = [
    "earth",
    "jupiter",
    "venus",
    "mars",
    "pluto",
    "moon",
    "sun",
    "mercury",
    "neptune",
]
game = True

while game == True:
    choosen_word = random.choice(words)
    display_word = ["_" for _ in choosen_word]

    health = 5
    print(display_word)

    while health > 0:
        char = input("\nGuess the words\n").lower()
        if char in choosen_word:
            for i in range(len(choosen_word)):
                if char == choosen_word[i]:
                    display_word[i] = char
            print(display_word)
            if list(choosen_word) == display_word:
                print(f"\n\nyou got it. The answer is {choosen_word} ")
                break
        else:
            health -= 1
            print(f"\nNot in this 😹, Remaining health is {health}")

    if health == 0:
        reset = input("\nNo luck, Wanna try again?(y/n)\n").lower()
        if reset == "n":
            game = False
            print("\nSee you later👋\n")
    else:
        reset = input("Good job!, Wanna try again?(y/n)\n").lower()
        if reset == "n":
            game = False
            print("\nSee you later👋\n")
