from tkinter import *
from TicTacToe import draw_grid

window=Tk()

def show_frame(frame):
    frame.tkraise()

# def score(input_name1,input_name2,frame_main,frame_score):
#     name_val1=input_name1.get()
#     name_val2=input_name2.get()

#     frame_score.tkraise()
#     ScoreBoard=Label(frame_score,text= "ScoreBoard" ,bg='black', fg='red',bd=1,relief="sunken",font=('arial',20,'bold') ,width=19,height=2)
#     ScoreBoard.grid(row=1,columnspan=4)
#     fh=open('PyProject(Sem4) - (rev.I)\score.txt','r')
#     line=1
#     for line in fh:
#         print(line)
#         label=Label(frame_score,text=line,font=('arial',20,'bold'),width=10,height=2)
#         label.grid(row=1,columnspan=1)
        


    # count = 0
    # for line in fh:
    #     if line != "\n":
    #         count = count + 1
    # #fh.close()
    # print(count)
    # line = fh.readlines()
    # print(line)
    # score_display=Label(frame_score,text=line,font=('arial',20,'bold'),anchor=CENTER ,justify=CENTER ,width=15,height=10)
    # score_display.grid(row=4,column=1)

    # for line in fh.readlinesine:
    #     line = fh.readlines()
    #     score_display=Label(frame_score,textvariable=line,font=('arial',20,'bold'),anchor=CENTER ,justify=CENTER ,width=10,height=2)
    #     score_display.grid(row=4,column=1)
        # line=line+1
        #print(line)

# def score(input_name1,input_name2,frame_main,frame_score):
#     name_val1=input_name1.get()
#     name_val2=input_name2.get()

#     frame_score.tkraise()
#     ScoreBoard=Label(frame_score,text= "ScoreBoard" ,bg='black', fg='red',bd=1,relief="sunken",font=('arial',20,'bold') ,width=19,height=2)
#     ScoreBoard.grid(row=1,columnspan=4)
#     back=Button(frame_score, bg='black', fg='red', text="BACK", command=lambda:show_frame(frame_main), font=('arial',20,'bold') ,width=19,height=1)
#     back.grid(row=90,columnspan=4)

#     fh=open('score.txt','r')   
#     content = fh.readlines()
#     label1=Label(frame_score,text=content[2],font=('arial',20,'bold'),width=10,height=2)
#     label2=Label(frame_score,text=content[1],font=('arial',20,'bold'),width=10,height=2)
#     label3=Label(frame_score,text=content[0],font=('arial',20,'bold'),width=10,height=2)
#     label1.grid(row=4)
#     label2.grid(row=6)
#     label3.grid(row=8)

def submit(input_name1,input_name2,frame_main,frame_player):
    name_val1=input_name1.get()
    name_val2=input_name2.get()

    frame_player.tkraise()
    
#==================Frame Player code
    play_user1=Button(frame_player, text=str(name_val1+" = X "), font=('arial',20,'bold') ,width=19,height=1,relief="sunken")
    play_user1.grid(row=1, columnspan=4,sticky='w')

    play_user2=Button(frame_player, text=str(name_val2+" = O "), font=('arial',20,'bold') ,width=19,height=1,relief="sunken",state=DISABLED)
    play_user2.grid(row=2, columnspan=4,sticky='e')

    back_main=Button(frame_player, bg='black', fg='red', text="BACK", command=lambda:show_frame(frame_main), font=('arial',20,'bold') ,width=19,height=1)
    back_main.grid(row=9,columnspan=4)

# a 3x3 grid to play on.
# passing 2 buttons as parameters to help toggle at every chance.
    draw_grid.draw_grid(frame_player,play_user1,play_user2,name_val1,name_val2,back_main)

def main_body():
    global window
    window.title("Tic Tac Toe")
    window.geometry("333x445")
    window.resizable(height=0,width=0)
   # window.configure(bg="black")
    frame_main=Frame(window)
    frame_player=Frame(window,bg='black')
    frame_detail=Frame(window,bg='black')
    frame_score=Frame(window,bg='black')

    for frame in (frame_main,frame_player,frame_score):
        frame.grid(row=0,column=0,sticky='nsew')

#==================Frame Main code
    # First Row
    welcome_label=Label(frame_main,text= "TIC TAC TOE" ,bg='black', fg='red',bd=1,relief="sunken",font=('arial',20,'bold') ,width=19,height=2)
    welcome_label.grid(row=1,columnspan=4)

    name1=Label(frame_main,text= "Player 1" ,font=('arial',15,'bold') ,width=15,height=5)
    name1.grid(row=2,column=1,sticky='w')
    input_name1=Entry(frame_main,bd="5" ,relief="sunken")
    input_name1.grid(row=2,column=2)

    # Second Row
    name2=Label(frame_main,text= "Player 2" , font=('arial',15,'bold') ,width=15,height=5)
    name2.grid(row=3,column=1,sticky='w')
    input_name2=Entry(frame_main,bd="5" ,relief="sunken")
    input_name2.grid(row=3,column=2)

    start_button=Button(frame_main, bg='black', fg='red', text="START", bd=1,relief="sunken", font=('arial',20,'bold') ,width=19,height=1, command=lambda: submit(input_name1,input_name2,frame_main,frame_player))
    start_button.grid(row=4, columnspan=4)

    scoreboard_button=Button(frame_main,bg='black',fg='red',text="ScoreBoard",bd=1,relief="sunken",font=('arial',20,'bold'),width=19,height=1,command= lambda: score(input_name1,input_name2,frame_main,frame_score) )
    scoreboard_button.grid(row=5,columnspan=4)

# exit button to terminate program immediately
    quit_button=Button(frame_main, bg='black', fg='red', text="EXIT",bd=1, relief="sunken" ,font=('arial',20,'bold'), command=window.destroy ,width=19,height=1)
    quit_button.grid(row=6,columnspan=4)

    show_frame(frame_main)

    window.mainloop()

# starting of the program.
if __name__ == '__main__':
    main_body()
