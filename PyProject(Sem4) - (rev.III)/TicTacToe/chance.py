from tkinter import *

# counter_comp,counter_user=0,0

def chance_user(player1,player2,box_num,button_play1,button_play2,counter_user):

    # global counter_user
    # print(counter_user)
# iterate over 1 to 9, to Toggle Button and Check for Players Chance
    for box_num_value in range(1,10):
    
        if box_num==box_num_value:
    
            if counter_user%2==0:
                counter_user+=1
                player1.append(box_num)
                button_play1.config(state=DISABLED)         # disable button 1
                button_play2.config(state=ACTIVE)           # enable button 2
                return 'X',counter_user

            elif counter_user%2!=0:
                counter_user+=1
                player2.append(box_num)
                button_play2.config(state=DISABLED)         # disable button 2
                button_play1.config(state=ACTIVE)           # enable button 1
                return 'O',counter_user

# def chance_comp(player1,player2,box_num,button_play1,button_play2,counter_comp):
    
#     # global counter_comp

# # iterate over 1 to 9, to Toggle Button and Check for Players Chance
#     for box_num_value in range(1,10):
    
#         if box_num==box_num_value:
    
#             if counter_comp%2==0:
#                 counter_comp+=1
#                 player1.append(box_num)
#                 button_play1.config(state=DISABLED)         # disable button 1
#                 button_play2.config(state=ACTIVE)           # enable button 2
#                 return 'X',counter_comp

#             elif counter_comp%2!=0:
#                 counter_comp+=1
#                 player2.append(box_num)
#                 button_play2.config(state=DISABLED)         # disable button 2
#                 button_play1.config(state=ACTIVE)           # enable button 1
#                 return 'O',counter_comp

# def who_plays(counter_comp):
#     if counter_comp%2==0:
#         return 'X'
#     elif counter_comp%2!=0:
#         return 'O'
