from tkinter import *
from TicTacToe import draw_grid

window=Tk()

def show_frame(frame):
    frame.tkraise()

def submit(input_name1,input_name2,frame_main,frame_pUser):
    name_val1=input_name1.get()
    name_val2=input_name2.get()

    frame_main.tkraise()
#==================Frame User code
    button_play_user1=Button(frame_pUser, text=str(name_val1+"'X'"), font=('arial',10,'bold') ,width=18,height=1)
    button_play_user1.grid(row=3, columnspan=4,sticky='w')

    button_play_user2=Button(frame_pUser, text=str(name_val2+"'O'"), font=('arial',10,'bold') ,width=18,height=1,state=DISABLED)
    button_play_user2.grid(row=3, columnspan=4,sticky='e')

    draw_grid.draw_grid_user(frame_pUser,button_play_user1,button_play_user2)

    exit_user=Button(frame_pUser, bg='black', fg='red', text="BACK", command=lambda:show_frame(frame_main), font=('arial',10,'bold') ,width=18,height=1)
    exit_user.grid(row=8,columnspan=4,sticky='nsew')

def main_body():
    global window
    window.title("Tic Tac Toe")
    window.geometry("340x400")

    terminate_user,terminate_comp=False,False
    counter_user,counter_comp=0,0
    p_val_user,p_val_comp="",""
    player1,player2=list(),list()
    player,computer=list(),list()
    keypress_count_user,keypress_count_comp={1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0},{1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}

    frame_detail=Frame(window)
    frame_main=Frame(window)
    frame_pComp=Frame(window)
    frame_pUser=Frame(window)

    for frame in (frame_detail,frame_main,frame_pComp,frame_pUser):
        frame.grid(row=0,column=0,sticky='nsew')

#==================Name Frame
    # First Row
    name1=Label(frame_detail,text= "Player Name")
    name1.grid(row=1,column=2,sticky='w')
    input_name1=Entry(frame_detail)
    input_name1.grid(row=1,column=3)

    # Second Row
    name2=Label(frame_detail,text= "Player Name")
    name2.grid(row=2,column=2,sticky='w')
    input_name2=Entry(frame_detail)
    input_name2.grid(row=2,column=3)

    opt_user=Button(frame_detail, text="SUBMIT", font=('arial',10,'bold') ,width=18,height=1, command=lambda: submit(input_name1,input_name2,frame_main,frame_pUser))
    opt_user.grid(row=3, columnspan=4,sticky='nsew')
#==================Frame Main code
    
    opt_user=Button(frame_main, text="User v User", font=('arial',10,'bold') ,width=18,height=1, command=lambda:show_frame(frame_pUser))
    opt_user.grid(row=1, columnspan=4,sticky='w')

    opt_comp=Button(frame_main, text="User v Comp", font=('arial',10,'bold') ,width=18,height=1, command=lambda:show_frame(frame_pComp))
    opt_comp.grid(row=2, columnspan=4,sticky='e')

# a 3x3 grid to play on.
# passing button1 and button2 as parameters to help toggle at every chance.
    # draw_grid.draw_grid(frame_main,button_play1,button_play2)

    reset_button=Button(frame_main, bg='black', fg='red', text="RESET", command=main_body, font=('arial',10,'bold') ,width=18,height=1)
    reset_button.grid(row=8,columnspan=4,sticky='w')

# exit button to terminate program immediately
    quit_button=Button(frame_main, bg='black', fg='red', text="EXIT", command=window.destroy, font=('arial',10,'bold') ,width=18,height=1)
    quit_button.grid(row=9,columnspan=4,sticky='e')

#==================Frame Comp code
    # Highlighted Button, implies that players turn to play.
    button_play_comp1=Button(frame_pComp, text="Player: 'X'", font=('arial',10,'bold') ,width=18,height=1)
    button_play_comp1.grid(row=3, columnspan=4,sticky='w')

    button_play_comp2=Button(frame_pComp, text="Computer: 'O'", font=('arial',10,'bold') ,width=18,height=1,state=DISABLED)
    button_play_comp2.grid(row=3, columnspan=4,sticky='e')
    
    draw_grid.draw_grid_comp(frame_pComp,button_play_comp1,button_play_comp2)

    exit_comp=Button(frame_pComp, bg='black', fg='red', text="BACK", command=lambda:show_frame(frame_main), font=('arial',10,'bold') ,width=18,height=1)
    exit_comp.grid(row=8,columnspan=4,sticky='nsew')

    show_frame(frame_detail)

    window.mainloop()

# starting of the program.
if __name__ == '__main__':
    main_body()
