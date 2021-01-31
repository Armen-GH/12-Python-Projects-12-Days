import random

def rps():
    user = input('(R) for rock, (P) for paper and (S) for scissors. Pick!').lower()
    pc = random.choice(['r', 'p', 's'])

    if user == pc:
        return 'It is a tie!'
    
    if rules(user, pc):
        return 'That is a win!'
    
    return 'Ops, You lost!'

def rules(player, env):
    if (player == 'p' and env == 'r') or (player == 'r' and env == 's') or (player == 's' and env == 'p'):
        return True 

print(rps())