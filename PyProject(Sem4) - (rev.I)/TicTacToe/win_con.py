from tkinter import *
from tkinter.messagebox import *
from itertools import permutations
from TicTacToe import score_file

# check if Dictionary Values are all 1 or not?
def check_draw(keypress_count):
    for value in keypress_count.values():
        if value==0:
            return False
        elif value==1:
            continue
    return True

def win_cond(terminate,player1,player2,counter,keypress_count,name_val1,name_val2):

# generates every Winning Possibility using inbuilt Permutation Function.    
    poss_1=permutations([1,2,3])
    poss_2=permutations([3,5,7])
    poss_3=permutations([1,5,9])
    poss_4=permutations([4,5,6])
    poss_5=permutations([7,8,9])
    poss_6=permutations([1,4,7])
    poss_7=permutations([2,5,8])
    poss_8=permutations([3,6,9])
    
    for i in poss_1,poss_2,poss_3,poss_4,poss_5,poss_6,poss_7,poss_8:
    
        for j in list(i):
            
# check if ANY player has matched with the winning condition.    
            play1=all(poss in player1 for poss in j)
            play2=all(poss in player2 for poss in j)
            # draw=all(poss in player1 for poss in j) or all(poss in player2 for poss in j)
            
            moves_left=9-counter
            final_score=moves_left*5
            
            if play1:
                showinfo("RESULT - ",str(name_val1+" WINS. !!!"))
                terminate=True
                score_file.score_save(name_val1,final_score)
                return terminate
    
            elif play2:
                showinfo("RESULT - ",str(name_val2+" WINS. !!!"))
                terminate=True
                score_file.score_save(name_val2,final_score)
                return terminate

            elif check_draw(keypress_count):
                for i in poss_1,poss_2,poss_3,poss_4,poss_5,poss_6,poss_7,poss_8:
                    for j in list(i):
                        play1=all(poss in player1 for poss in j)
                        play2=all(poss in player2 for poss in j)

                        moves_left=9-counter
                        final_score=moves_left*5
            
                        if play1:
                            msg=showinfo("RESULT - ",str(name_val1+" WINS. !!!"))
                            terminate=True
                            score_file.score_save(name_val1,final_score)
                            return terminate
    
                        elif play2:
                            showinfo("RESULT - ",str(name_val2+" WINS. !!!"))
                            terminate=True
                            score_file.score_save(name_val2,final_score)
                            return terminate

                showinfo("RESULT - ",str(" DRAW "))
                terminate=True
                return terminate
            