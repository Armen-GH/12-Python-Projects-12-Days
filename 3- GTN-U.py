import random

def pc_guess(x):
    low = 1
    high = x

    feedback = ''
    
    while feedback != 'c':
        if high != low:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'Is {guess} too high (H), too low (L) or correct (H)'.lower())
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    
    print(f'Finally! Your computer guessed {guess} correctly')
    
pc_guess(10)
