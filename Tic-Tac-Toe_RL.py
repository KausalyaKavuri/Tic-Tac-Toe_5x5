import numpy as np
import random
#The spot holders are for the grid in tic tac toe
#Top left is 0 (0,0), (0,1) is 1, (0,2) is 2, (1,1) is 5 and so on
spot_placeholders = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

class Player():
    def __init__(self, name, start = False):
        self.values = {0:0}
        self.name = name
        self.turn = start
        self.epsilon = 1
        
        
def get_action(player1, player2):
    global spot_placeholders
    
    """to find out which players turn it is, and set thier marker and epsilon."""
    if player1.turn == True:
        marker = 1
        epsilon = player1.epsilon
    else:
        marker = 2
        epsilon = player2.epsilon
    
    players = [player1,player2]
    possible_next_states = {}
    top_value = -1
    
    """loop through every spot and, if it's empty, record the state that
    would come from the player moving in that spot"""    
    for i in range(len(spot_placeholders)):
        if spot_placeholders[i] == 0:
            copy = np.copy(spot_placeholders)
            copy[i] = marker
            s_p = state_to_num(copy)
            possible_next_states[i] = s_p
    
    """Epsilon greedy"""
    if np.random.rand() < epsilon:
        if players[marker-1].epsilon > .05:
            players[marker-1].epsilon -= .001
        return random.sample(possible_next_states.keys(),1)[0]
    
    else:
        i = 0
        for state in possible_next_states.values():
            try:
                """if the current players value for this state is higher than the 
                top recorded value, set the top value to the value of this state 
                and set action = the spot that will lead to this state"""
                if players[marker-1].values[state] > top_value:
                    top_value = players[marker-1].values[state]
                    action = list(possible_next_states.keys())[i]
            except:
                pass
            i +=1
            
        if players[marker-1].epsilon > .05:
            players[marker-1].epsilon -= .001
        
        """if there was no action set, return a random action"""
        try:
            return action
        except:
            return random.sample(possible_next_states.keys(),1)[0]

def state_to_num(state):
    N = state[0]+5*state[1] + 25*state[2]+125*state[3]+625*state[4]+3125*state[5]+15625*state[6]+78125*state[7]+390625*state[8]+1953125*state[9] + 9765625*state[10]+48828125*state[11]+244140625*state[12]+1220703125*state[13]+6103515625*state[14]+30517578125*state[15]+152587890625*state[16]+762939453125*state[17]+3814697265625*state[18]+19073486328125*state[19]+95367431640625*state[20]+476837158203125*state[21]+2384185791015625*state[22]+11920928955078125*state[23]+59604644775390625*state[24]
    return N

def num_to_state(N):
    y = N //(5**24)
    x = (N - y*(5**24)) //(5**23)
    w = (N - y*(5**24) - x*(5**23)) //(5**22)
    v = (N - y*(5**24) - x*(5**23) - w*(5**22)) //(5**21)
    u = (N - y*(5**24) - x*(5**23) - w*(5**22) - v*(5**21)) //(5**20)
    t = (N - y*(5**24) - x*(5**23) - w*(5**22) - v*(5**21) - u*(5**20)) //(5**19)
    s = (N - y*(5**24) - x*(5**23) - w*(5**22) - v*(5**21) - u*(5**20) - t*(5**19)) //(5**18)
    r = (N - y*(5**24) - x*(5**23) - w*(5**22) - v*(5**21) - u*(5**20) - t*(5**19) - s*(5**18)) //(5**17)
    q = (N - y*(5**24) - x*(5**23) - w*(5**22) - v*(5**21) - u*(5**20) - t*(5**19) - s*(5**18) - r*(5**17)) //(5**16)
    p = (N - y*(5**24) - x*(5**23) - w*(5**22) - v*(5**21) - u*(5**20) - t*(5**19) - s*(5**18) - r*(5**17) - q*(5**16)) //(5**15)
    o = (N - y*(5**24) - x*(5**23) - w*(5**22) - v*(5**21) - u*(5**20) - t*(5**19) - s*(5**18) - r*(5**17) - q*(5**16) - p*(5**15)) //(5**14)
    n = (N - y*(5**24) - x*(5**23) - w*(5**22) - v*(5**21) - u*(5**20) - t*(5**19) - s*(5**18) - r*(5**17) - q*(5**16) - p*(5**15) - o*(5**14)) //(5**13)
    m = (N - y*(5**24) - x*(5**23) - w*(5**22) - v*(5**21) - u*(5**20) - t*(5**19) - s*(5**18) - r*(5**17) - q*(5**16) - p*(5**15) - o*(5**14) - n*(5**13)) //(5**12)
    l = (N - y*(5**24) - x*(5**23) - w*(5**22) - v*(5**21) - u*(5**20) - t*(5**19) - s*(5**18) - r*(5**17) - q*(5**16) - p*(5**15) - o*(5**14) - n*(5**13) - m*(5**12)) //(5**11)
    k = (N - y*(5**24) - x*(5**23) - w*(5**22) - v*(5**21) - u*(5**20) - t*(5**19) - s*(5**18) - r*(5**17) - q*(5**16) - p*(5**15) - o*(5**14) - n*(5**13) - m*(5**12) - l*(5**11)) //(5**10)
    j = (N - y*(5**24) - x*(5**23) - w*(5**22) - v*(5**21) - u*(5**20) - t*(5**19) - s*(5**18) - r*(5**17) - q*(5**16) - p*(5**15) - o*(5**14) - n*(5**13) - m*(5**12) - l*(5**11) - k(5**10)) //(5**9)
    i = (N - y*(5**24) - x*(5**23) - w*(5**22) - v*(5**21) - u*(5**20) - t*(5**19) - s*(5**18) - r*(5**17) - q*(5**16) - p*(5**15) - o*(5**14) - n*(5**13) - m*(5**12) - l*(5**11) - k(5**10) - j*(5**9))//(5**8)
    h = (N - y*(5**24) - x*(5**23) - w*(5**22) - v*(5**21) - u*(5**20) - t*(5**19) - s*(5**18) - r*(5**17) - q*(5**16) - p*(5**15) - o*(5**14) - n*(5**13) - m*(5**12) - l*(5**11) - k(5**10) - j*(5**9) - i*(5**8)) //(5**7)
    g = (N - y*(5**24) - x*(5**23) - w*(5**22) - v*(5**21) - u*(5**20) - t*(5**19) - s*(5**18) - r*(5**17) - q*(5**16) - p*(5**15) - o*(5**14) - n*(5**13) - m*(5**12) - l*(5**11) - k(5**10) - j*(5**9) - i*(5**8) - h*(5**7)) // (5**6) 
    f = (N - y*(5**24) - x*(5**23) - w*(5**22) - v*(5**21) - u*(5**20) - t*(5**19) - s*(5**18) - r*(5**17) - q*(5**16) - p*(5**15) - o*(5**14) - n*(5**13) - m*(5**12) - l*(5**11) - k(5**10) - j*(5**9) - i*(5**8) - h*(5**7) - g*(5**6)) // (5**5)
    e = (N - y*(5**24) - x*(5**23) - w*(5**22) - v*(5**21) - u*(5**20) - t*(5**19) - s*(5**18) - r*(5**17) - q*(5**16) - p*(5**15) - o*(5**14) - n*(5**13) - m*(5**12) - l*(5**11) - k(5**10) - j*(5**9) - i*(5**8) - h*(5**7) - g*(5**6) - f(5**5)) // (5**4)
    d = (N - y*(5**24) - x*(5**23) - w*(5**22) - v*(5**21) - u*(5**20) - t*(5**19) - s*(5**18) - r*(5**17) - q*(5**16) - p*(5**15) - o*(5**14) - n*(5**13) - m*(5**12) - l*(5**11) - k(5**10) - j*(5**9) - i*(5**8) - h*(5**7) - g*(5**6) - f(5**5) - e(5**4)) // (5**3)
    c = (N - y*(5**24) - x*(5**23) - w*(5**22) - v*(5**21) - u*(5**20) - t*(5**19) - s*(5**18) - r*(5**17) - q*(5**16) - p*(5**15) - o*(5**14) - n*(5**13) - m*(5**12) - l*(5**11) - k(5**10) - j*(5**9) - i*(5**8) - h*(5**7) - g*(5**6) - f(5**5) - e(5**4) - d(5**3)) // (5**2)
    b = (N - y*(5**24) - x*(5**23) - w*(5**22) - v*(5**21) - u*(5**20) - t*(5**19) - s*(5**18) - r*(5**17) - q*(5**16) - p*(5**15) - o*(5**14) - n*(5**13) - m*(5**12) - l*(5**11) - k(5**10) - j*(5**9) - i*(5**8) - h*(5**7) - g*(5**6) - f(5**5) - e(5**4) - d(5**3) - c(5**2))//(5**1)
    a = (N - y*(5**15) - x*(5**23) - w*(5**22) - v*(5**21) - u*(5**20) - t*(5**19) - s*(5**18) - r*(5**17) - q*(5**16) - p*(5**15) - o*(5**14) - n*(5**13) - m*(5**12) - l*(5**11) - b(5**10) - j*(5**9) - i*(5**8) - h*(5**7) - g*(5**6) - f(5**5) - e(5**5) - d(5**3) - c(5**2)- b(5**2))//(5**0)

    return([a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y])
# Winning criteria
def check_for_winner():
    if spot_placeholders[0] == spot_placeholders[1] and spot_placeholders[1] == spot_placeholders[2] and spot_placeholders[2] == spot_placeholders[3] and spot_placeholders[3] == spot_placeholders[4] and spot_placeholders[4]!= 0:
        return True
    if spot_placeholders[0] == spot_placeholders[6] and spot_placeholders[6] == spot_placeholders[12] and spot_placeholders[12] == spot_placeholders[18] and spot_placeholders[18] == spot_placeholders[24] and spot_placeholders[24] != 0:
        return True
    if spot_placeholders[0] == spot_placeholders[5] and spot_placeholders[5] == spot_placeholders[10] and spot_placeholders[10] == spot_placeholders[15] and spot_placeholders[15] == spot_placeholders[20] and spot_placeholders[20] != 0:
        return True
    if spot_placeholders[1] == spot_placeholders[6] and spot_placeholders[6] == spot_placeholders[11] and spot_placeholders[11] == spot_placeholders[16] and spot_placeholders[16] == spot_placeholders[21] and spot_placeholders[21] != 0:
        return True
    if spot_placeholders[2] == spot_placeholders[7] and spot_placeholders[7] == spot_placeholders[12] and spot_placeholders[12] == spot_placeholders[17] and spot_placeholders[17] == spot_placeholders[22] and spot_placeholders[22] != 0:
        return True
    if spot_placeholders[3] == spot_placeholders[8] and spot_placeholders[8] == spot_placeholders[13] and spot_placeholders[13] == spot_placeholders[18] and spot_placeholders[18] == spot_placeholders[23] and spot_placeholders[23] != 0:
        return True
    if spot_placeholders[4] == spot_placeholders[9] and spot_placeholders[9] == spot_placeholders[14] and spot_placeholders[14] == spot_placeholders[19] and spot_placeholders[19] == spot_placeholders[24] and spot_placeholders[24] != 0:
        return True
    if spot_placeholders[5] == spot_placeholders[6] and spot_placeholders[6] == spot_placeholders[7] and spot_placeholders[7] == spot_placeholders[8] and spot_placeholders[8] == spot_placeholders[9] and spot_placeholders[9] != 0:
        return True
    if spot_placeholders[10] == spot_placeholders[11] and spot_placeholders[11] == spot_placeholders[12] and spot_placeholders[12] == spot_placeholders[13] and spot_placeholders[13] == spot_placeholders[14] and spot_placeholders[14] != 0:
        return True
    if spot_placeholders[15] == spot_placeholders[16] and spot_placeholders[16] == spot_placeholders[17] and spot_placeholders[17] == spot_placeholders[18] and spot_placeholders[18] == spot_placeholders[19] and spot_placeholders[19] != 0:
        return True
    if spot_placeholders[20] == spot_placeholders[21] and spot_placeholders[21] == spot_placeholders[22] and spot_placeholders[22] == spot_placeholders[23] and spot_placeholders[23] == spot_placeholders[24] and spot_placeholders[24] != 0:
        return True
    if spot_placeholders[4] == spot_placeholders[8] and spot_placeholders[8] == spot_placeholders[12] and spot_placeholders[12] == spot_placeholders[16] and spot_placeholders[16] == spot_placeholders[20] and spot_placeholders[20] != 0:
        return True
    elif (spot_placeholders[0] != 0 and spot_placeholders[1] != 0 and
          spot_placeholders[2] != 0 and spot_placeholders[3] != 0 and
          spot_placeholders[4] != 0 and spot_placeholders[5] != 0 and
          spot_placeholders[6] != 0 and spot_placeholders[7] != 0 and
          spot_placeholders[8] != 0 and spot_placeholders[9] != 0 and 
          spot_placeholders[10] != 0 and spot_placeholders[11] != 0 and 
          spot_placeholders[12] != 0 and spot_placeholders[13] != 0 and
          spot_placeholders[14] != 0 and spot_placeholders[15] != 0 and 
          spot_placeholders[16] != 0 and spot_placeholders[17] != 0 and
          spot_placeholders[18] != 0 and spot_placeholders[19] != 0 and 
          spot_placeholders[20] != 0 and spot_placeholders[21] != 0 and
          spot_placeholders[22] != 0 and spot_placeholders[23] != 0 and spot_placeholders[24] != 0 ):
        return 'WinWin'
    else:
        return False
    
def play_game(player1,player2):
    global spot_placeholders 
    state_history = []
    if np.random.rand() >= .5:
        player1.turn = True
    player2.turn = not player1.turn
    
    while True:
        #Human starts the game
        if player1.turn == True:
            a = get_action(player1,player2)
            spot_placeholders[a] = 1
            state_history.append(state_to_num(spot_placeholders))
            
            if check_for_winner() == True:
                spot_placeholders = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                update_values(player1,state_history,True)
                update_values(player2,state_history)
                break
        # AI starts the game    
        if player2.turn == True:
            a = get_action(player1,player2)
            spot_placeholders[a] = 2
            state_history.append(state_to_num(spot_placeholders))
            
            if check_for_winner() == True:
                spot_placeholders = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                update_values(player2,state_history,True)
                update_values(player1,state_history)
                
                break
            
        if check_for_winner() == 'WinWin':
            spot_placeholders = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            update_values(player1,state_history)
            update_values(player2,state_history)
            break
        
        player1.turn = not player1.turn
        player2.turn = not player2.turn
      
def update_values(player,state_history,winner=False):
    player.values[state_history[-1]] = -1
    if winner == True:
        player.values[state_history[-1]] = 1
    
    for state in state_history:
        if state not in player.values:
            player.values[state] = 0
    
    for i in range(len(state_history)-1,0,-1):
        player.values[state_history[i-1]] += .1*(player.values[state_history[i]] - player.values[state_history[i-1]])

      
        

p1 = Player('Computer 1', True) 
p2 = Player('Computer 2')   

for i in range(100000):
    play_game(p1,p2)
    if i % 10000 == 0:
        if i%20000==0:
            print("Loading Game...")
        else:
            print("Please wait")
        #print(i)



def print_board():
    board = []
    for spot in spot_placeholders:
        if spot == 0:
            board.append('_')
        if spot == 1:
            board.append('X')
        if spot == 2:
            board.append('O')
    print(board[0],board[1],board[2],board[3],board[4])
    print(board[5],board[6],board[7],board[8],board[9])
    print(board[10],board[11],board[12],board[13],board[14])
    print(board[15],board[16],board[17],board[18],board[19])
    print(board[20],board[21],board[22],board[23],board[24])
    
def test(computer):
    global spot_placeholders
    
    p1.turn = True
    p2.turn = False
    p1.epsilon = 0
    p2.epsilon = 0
    
    while True:
        if computer.turn == True:
            a = get_action(p1,p2)
            spot_placeholders[a] = 1
            
            if check_for_winner() == True:
                print('\nYou Lose!\n')
                print_board()
                spot_placeholders = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                break
        else:
            print_board()
            while True:
                action = int(input('Your turn to play?\n \nMark at: '))
                if spot_placeholders[action] == 0:
                    spot_placeholders[action] = 2
                    break
                else:
                    continue
            if check_for_winner() == True:
                print('\nYou Win!\n')
                spot_placeholders = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                break
        if check_for_winner() == 'WinWin':
            print('\nDraw Game!\n')
            spot_placeholders = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            break
        
        p1.turn = not p1.turn
        p2.turn = not p2.turn

while True:
    place = input('Would you like to play first or second? Input 1 or 2.\n \nInput:')
    if place == '1':
        test(p2)
    else:
        test(p1)