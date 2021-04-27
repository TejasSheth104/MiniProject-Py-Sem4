from tkinter import *
from tkinter.messagebox import *
from TicTacToe import chance,win_con,draw_grid

counter=0
keypress_count={1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}        # dictionary to keep tab of all filled Blocks.
player1,player2=list(),list()                               # keep tab of each players entry.
terminate=False
p_val=""

# to avoid user from manipulating the values once clicked on the button.
def limit_keypress(keypress_count,box_key):

# if the respective value of dictionary is 0, then its changed to 1 & hence cant be used again.
    if keypress_count[box_key]==0:
        keypress_count[box_key]=1
        return True

    else:
        return False

def key_press(frame_main,box_num,place_value,button_play1,button_play2,name_val1,name_val2,back_main,start_button):

    global counter,keypress_count,player1,player2,terminate,p_val

    # start_button.config(state=DISABLED)

# if value of dictionary is 1 already(returning Value FALSE.), no change takes place.
    if limit_keypress(keypress_count,box_num):
        p_val,counter=chance.chance(player1,player2,box_num,button_play1,button_play2)
        place_value.set(p_val)

        back_main.config(state=DISABLED)

# sets the value (X/O) at respective position.        
        if win_con.win_cond(terminate,player1,player2,counter,keypress_count,name_val1,name_val2):
#             msg=askquestion(title="TRY AGAIN", message="WANT TO PLAY AGAIN?")

# # reset every parameter, and call the Grid Function to restart.
#             if msg=='yes':
            terminate=False
            counter=0
            p_val=""
            player1,player2=list(),list()
            keypress_count={1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
#                 draw_grid.draw_grid(frame_player,button_play1,button_play2,name_val1,name_val2,back_main,start_button)

# # thank you message and exit.
#             elif msg=='no':
#                 showinfo("EXIT","THANK YOU. !!!")
#                 
            Frame.tkraise(frame_main)
