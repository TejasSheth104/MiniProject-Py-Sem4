from tkinter import *
from tkinter.messagebox import *
from TicTacToe import chance,win_con,draw_grid

# counter=0
# keypress_count={1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}        # dictionary to keep tab of all filled Blocks.
# player1,player2=list(),list()                               # keep tab of each players entry.
# terminate=False
# p_val=""

terminate_user,terminate_comp=False,False
counter_user,counter_comp=0,0
p_val_user,p_val_comp="",""
player1,player2=list(),list()
player,computer=list(),list()
keypress_count_user,keypress_count_comp={1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0},{1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}

# to avoid user from manipulating the values once clicked on the button.
def limit_keypress_user(keypress_count,box_key):

# if the respective value of dictionary is 0, then its changed to 1 & hence cant be used again.
    if keypress_count_user[box_key]==0:
        keypress_count_user[box_key]=1
        return True

    else:
        return False

def key_press_user(window,box_num,place_value,button_play1,button_play2):

    global counter_user,keypress_count_user,player1,player2,terminate_user,p_val_user

# if value of dictionary is 1 already(returning Value FALSE.), no change takes place.
    if limit_keypress_user(keypress_count_user,box_num):
        p_val_user,counter_user=chance.chance_user(player1,player2,box_num,button_play1,button_play2,counter_user)
        place_value.set(p_val_user)

# sets the value (X/O) at respective position.        
        if win_con.win_cond(terminate_user,player1,player2,counter_user):
            msg=askquestion(title="TRY AGAIN", message="WANT TO PLAY AGAIN?")

# reset every parameter, and call the Grid Function to restart.
            if msg=='yes':
                terminate_user=False
                counter_user=0
                p_val_user=""
                player1,player2=list(),list()
                keypress_count_user={1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
                draw_grid.draw_grid_user(window,button_play1,button_play2)

# thank you message and exit.
            elif msg=='no':
                showinfo("EXIT","THANK YOU. !!!")
                Frame.destroy(window)


def limit_keypress_comp(keypress_count,box_key):

# if the respective value of dictionary is 0, then its changed to 1 & hence cant be used again.
    if keypress_count[box_key]==0:
        keypress_count[box_key]=1
        return True

    else:
        return False

def key_press_comp(window,box_num,place_value,button_play1,button_play2):

    global counter_comp,keypress_count_comp,player,computer,terminate_comp,p_val_comp

    if chance.who_plays()=='X':
# if value of dictionary is 1 already(returning Value FALSE.), no change takes place.
        if limit_keypress_comp(keypress_count_comp,box_num):
            p_val_comp,counter_comp=chance.chance_comp(player,computer,box_num,button_play1,button_play2,counter_comp)
            place_value.set(p_val_comp)

# sets the value (X/O) at respective position.        
            if win_con.win_cond(terminate_comp,player,computer,counter_comp):
                msg=askquestion(title="TRY AGAIN", message="WANT TO PLAY AGAIN?")

# reset every parameter, and call the Grid Function to restart.
                if msg=='yes':
                    terminate_comp=False
                    counter_comp=0
                    p_val_comp=""
                    player,computer=list(),list()
                    keypress_count_comp={1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
                    draw_grid.draw_grid_comp(window,button_play1,button_play2)

# thank you message and exit.
                elif msg=='no':
                    showinfo("EXIT","THANK YOU. !!!")
                    Frame.destroy(window)

    elif chance.who_plays()=='O':
        print("Comp chance shld sleect a block randomly")
        p_val_comp,counter=chance.chance_comp(player,computer,box_num,button_play1,button_play2)

def key_press_rand(window,box_num,place_value,button_play1,button_play2):
    pass