from random import choice

def word_list():
    """
    opens file '5_letter_words.txt' and returns it as a list
    """
    with open('5_letter_words.txt', 'r') as words2:
        words = [line.rstrip('\n') for line in words2]
    return words

def random_word(word_list):
    """
    returns a random word from the given list
    """    
    return choice(word_list)

def is_real_word(guess, word_list):
    """
    checks whether guess is in word_list
    """
    return bool(guess in word_list)

def check_guess(guess, answer):
    """
    compares guess and answer and returns score in respect to guess:
    x = letter in place
    o = letter in wrong position
    _ = no such letter in answer
    """
# see the sandbox for another example
    score = []
    to_check = [True]*5
    for i in range(5):
        if guess[i] == answer[i]:
            score.append('x')
            to_check[i] = False
            continue
        for j in range(5):
            if to_check[j] and guess[i] == answer[j]:
                to_check[j] = False
                score.append('o')
                break
        else:
            score.append('_')
    return ''.join(score)
    
def next_guess(word_list):
    """
    returns lowercase input if it is a 5-letter word from the word_list
    """
    while True:
        guess = input('Please enter a guess: ').lower()
        if not(guess.isalpha() and len(guess) == 5):
            print('That\'s not a 5-letter word!')
        elif not is_real_word(guess, word_list):
            print('That\'s not a real word!')
        else:
            return guess


def play():
    """
    game of Wordle based on '5_letter_words.txt' word list
    """
    words = word_list()
    answer = random_word(words)
    for i in range(5):
        guess = next_guess(words)
        score = check_guess(guess, answer)
        print(score)
        if score == 'xxxxx':
            print('You won!')
            return
    print('You lost!')
    print('The word was:', answer)
    return 'You lost!'

play()