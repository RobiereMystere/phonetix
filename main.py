from WordAnalyser import WordAnalyser
from distances import levenshtein, hamming

if __name__ == '__main__':
    wa = WordAnalyser()

    mystery_word = wa.pick_word(5)

    # print(mystery_word)
    mystery_word_orth = mystery_word[1]
    mystery_word_phon = mystery_word[2]
    guess = ""
    while guess != mystery_word_orth:
        guess = input()
        if guess == "-abandon!":
            print(mystery_word)
            break
        word_line = wa.find_word(guess)
        print(word_line)
        if len(word_line) > 0:
            guess_line = word_line[0]
            guess_phon = guess_line[2]

            print(levenshtein(mystery_word_phon, guess_phon))
        else:
            print("je ne connais pas le mot", guess)
            print(levenshtein(mystery_word_phon, ""))
    print('well done !')
