from tkinter import *

counter=0

def chance(player1,player2,box_num,button_play1,button_play2):
    
    global counter
# iterate over 1 to 9, to Toggle Button and Check for Players Chance
    for box_num_value in range(1,10):
    
        if box_num==box_num_value:
    
            if counter%2==0:
                counter+=1
                player1.append(box_num)
                button_play1.config(state=DISABLED)         # disable button 1
                button_play2.config(state=ACTIVE)           # enable button 2
                return 'X',counter

            elif counter%2!=0:
                counter+=1
                player2.append(box_num)
                button_play2.config(state=DISABLED)         # disable button 2
                button_play1.config(state=ACTIVE)           # enable button 1
                return 'O',counter
