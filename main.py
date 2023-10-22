import random
import time

words = ["accommodate", "bureaucracy", "cappuccino", "daiquiri", "embarrass", "floccinaucinihilipilification", "gobbledygook", "haphazard", "idiosyncrasy", "juxtaposition", "kleptomania", "liaison", "mnemonic", "onomatopoeia", "pseudopseudohypoparathyroidism", "quizzaciously", "rhythm", "schizophrenia", "tchotchke", "unquestionable", "vichyssoise", "weltschmerz", "xerophthalmia", "yoicks", "zeitgeist"]

while True:
    random_sentence = ' '.join(random.choices(words, k=15))

    print("Type the following sentence:")
    print(random_sentence)

    input("Press Enter to start...")

    start_time = time.time()

    user_input = input("Type the sentence: ")

    end_time = time.time()

    time_taken = end_time - start_time
    characters_typed = len(user_input)
    words_per_minute = (characters_typed / 5) / (time_taken / 60)

    if user_input == random_sentence:
        print("You typed the sentence correctly!")
        print(f"Time taken: {time_taken:.2f} seconds")
        print(f"Typing Speed: {words_per_minute:.2f} words per minute")
    else:
        print("The entered sentence does not match the original sentence. Please try again.")
