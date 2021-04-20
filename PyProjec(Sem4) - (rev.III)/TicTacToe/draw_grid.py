from tkinter import *
from TicTacToe import key_press

def draw_grid_user(frame_pUser,button_play_user1,button_play_user2):
# 9 variables to set Button Value later (X/O)
    place_value_user1, place_value_user2, place_value_user3=StringVar(), StringVar(), StringVar()
    place_value_user4, place_value_user5, place_value_user6=StringVar(), StringVar(), StringVar()
    place_value_user7, place_value_user8, place_value_user9=StringVar(), StringVar(), StringVar()

    grid_but1=Button(frame_pUser, textvariable=place_value_user1, bg="papaya whip", font=('arial',10,'bold'), relief="sunken", bd=10, width=10,height=4, command=lambda: key_press.key_press_user(frame_pUser,1,place_value_user1,button_play_user1,button_play_user2))
    grid_but1.grid(row=5,column=1)
    
    grid_but2=Button(frame_pUser, textvariable=place_value_user2, bg="papaya whip", font=('arial',10,'bold'), relief="sunken", bd=10, width=10,height=4, command=lambda: key_press.key_press_user(frame_pUser,2,place_value_user2,button_play_user1,button_play_user2))
    grid_but2.grid(row=5,column=2)
    
    grid_but3=Button(frame_pUser, textvariable=place_value_user3, bg="papaya whip", font=('arial',10,'bold'), relief="sunken", bd=10, width=10,height=4, command=lambda: key_press.key_press_user(frame_pUser,3,place_value_user3,button_play_user1,button_play_user2))
    grid_but3.grid(row=5,column=3)
    
    grid_but4=Button(frame_pUser, textvariable=place_value_user4, bg="papaya whip", font=('arial',10,'bold'), relief="sunken", bd=10, width=10,height=4, command=lambda: key_press.key_press_user(frame_pUser,4,place_value_user4,button_play_user1,button_play_user2))
    grid_but4.grid(row=6,column=1)
    
    grid_but5=Button(frame_pUser, textvariable=place_value_user5, bg="papaya whip", font=('arial',10,'bold'), relief="sunken", bd=10, width=10,height=4, command=lambda: key_press.key_press_user(frame_pUser,5,place_value_user5,button_play_user1,button_play_user2))
    grid_but5.grid(row=6,column=2)
    
    grid_but6=Button(frame_pUser, textvariable=place_value_user6, bg="papaya whip", font=('arial',10,'bold'), relief="sunken", bd=10, width=10,height=4, command=lambda: key_press.key_press_user(frame_pUser,6,place_value_user6,button_play_user1,button_play_user2))
    grid_but6.grid(row=6,column=3)
    
    grid_but7=Button(frame_pUser, textvariable=place_value_user7, bg="papaya whip", font=('arial',10,'bold'), relief="sunken", bd=10, width=10,height=4, command=lambda: key_press.key_press_user(frame_pUser,7,place_value_user7,button_play_user1,button_play_user2))
    grid_but7.grid(row=7,column=1)
    
    grid_but8=Button(frame_pUser, textvariable=place_value_user8, bg="papaya whip", font=('arial',10,'bold'), relief="sunken", bd=10, width=10,height=4, command=lambda: key_press.key_press_user(frame_pUser,8,place_value_user8,button_play_user1,button_play_user2))
    grid_but8.grid(row=7,column=2)
    
    grid_but9=Button(frame_pUser, textvariable=place_value_user9, bg="papaya whip", font=('arial',10,'bold'), relief="sunken", bd=10, width=10,height=4, command=lambda: key_press.key_press_user(frame_pUser,9,place_value_user9,button_play_user1,button_play_user2))
    grid_but9.grid(row=7,column=3)

def draw_grid_comp(frame_pComp,button_play_comp1,button_play_comp2):
# 9 variables to set Button Value later (X/O)
    place_value_comp1, place_value_comp2, place_value_comp3=StringVar(), StringVar(), StringVar()
    place_value_comp4, place_value_comp5, place_value_comp6=StringVar(), StringVar(), StringVar()
    place_value_comp7, place_value_comp8, place_value_comp9=StringVar(), StringVar(), StringVar()

    grid_but1=Button(frame_pComp, textvariable=place_value_comp1, bg="papaya whip", font=('arial',10,'bold'), relief="sunken", bd=10, width=10,height=4, command=lambda: key_press.key_press_comp(frame_pComp,1,place_value_comp1,button_play_comp1,button_play_comp2))
    grid_but1.grid(row=5,column=1)
    
    grid_but2=Button(frame_pComp, textvariable=place_value_comp2, bg="papaya whip", font=('arial',10,'bold'), relief="sunken", bd=10, width=10,height=4, command=lambda: key_press.key_press_comp(frame_pComp,2,place_value_comp2,button_play_comp1,button_play_comp2))
    grid_but2.grid(row=5,column=2)
    
    grid_but3=Button(frame_pComp, textvariable=place_value_comp3, bg="papaya whip", font=('arial',10,'bold'), relief="sunken", bd=10, width=10,height=4, command=lambda: key_press.key_press_comp(frame_pComp,3,place_value_comp3,button_play_comp1,button_play_comp2))
    grid_but3.grid(row=5,column=3)
    
    grid_but4=Button(frame_pComp, textvariable=place_value_comp4, bg="papaya whip", font=('arial',10,'bold'), relief="sunken", bd=10, width=10,height=4, command=lambda: key_press.key_press_comp(frame_pComp,4,place_value_comp4,button_play_comp1,button_play_comp2))
    grid_but4.grid(row=6,column=1)
    
    grid_but5=Button(frame_pComp, textvariable=place_value_comp5, bg="papaya whip", font=('arial',10,'bold'), relief="sunken", bd=10, width=10,height=4, command=lambda: key_press.key_press_comp(frame_pComp,5,place_value_comp5,button_play_comp1,button_play_comp2))
    grid_but5.grid(row=6,column=2)
    
    grid_but6=Button(frame_pComp, textvariable=place_value_comp6, bg="papaya whip", font=('arial',10,'bold'), relief="sunken", bd=10, width=10,height=4, command=lambda: key_press.key_press_comp(frame_pComp,6,place_value_comp6,button_play_comp1,button_play_comp2))
    grid_but6.grid(row=6,column=3)
    
    grid_but7=Button(frame_pComp, textvariable=place_value_comp7, bg="papaya whip", font=('arial',10,'bold'), relief="sunken", bd=10, width=10,height=4, command=lambda: key_press.key_press_comp(frame_pComp,7,place_value_comp7,button_play_comp1,button_play_comp2))
    grid_but7.grid(row=7,column=1)
    
    grid_but8=Button(frame_pComp, textvariable=place_value_comp8, bg="papaya whip", font=('arial',10,'bold'), relief="sunken", bd=10, width=10,height=4, command=lambda: key_press.key_press_comp(frame_pComp,8,place_value_comp8,button_play_comp1,button_play_comp2))
    grid_but8.grid(row=7,column=2)
    
    grid_but9=Button(frame_pComp, textvariable=place_value_comp9, bg="papaya whip", font=('arial',10,'bold'), relief="sunken", bd=10, width=10,height=4, command=lambda: key_press.key_press_comp(frame_pComp,9,place_value_comp9,button_play_comp1,button_play_comp2))
    grid_but9.grid(row=7,column=3)
