# tic-tac-toe GUI

from tkinter import *
from tkinter.messagebox import *
from itertools import permutations

window=Tk()
p_val=""
counter=0
terminate=False
player1,player2=list(),list()
keypress_count={1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}

def draw_grid(window):
    place_value1, place_value2, place_value3=StringVar(), StringVar(), StringVar()
    place_value4, place_value5, place_value6=StringVar(), StringVar(), StringVar()
    place_value7, place_value8, place_value9=StringVar(), StringVar(), StringVar()

    grid_but1=Button(window, textvariable=place_value1, width=10,height=4, command=lambda: key_press(1,"",place_value1))
    grid_but1.grid(row=5,column=1)
    grid_but2=Button(window, textvariable=place_value2, width=10,height=4, command=lambda: key_press(2,"",place_value2))
    grid_but2.grid(row=5,column=2)
    grid_but3=Button(window, textvariable=place_value3, width=10,height=4, command=lambda: key_press(3,"",place_value3))
    grid_but3.grid(row=5,column=3)
    grid_but4=Button(window, textvariable=place_value4, width=10,height=4, command=lambda: key_press(4,"",place_value4))
    grid_but4.grid(row=6,column=1)
    grid_but5=Button(window, textvariable=place_value5, width=10,height=4, command=lambda: key_press(5,"",place_value5))
    grid_but5.grid(row=6,column=2)
    grid_but6=Button(window, textvariable=place_value6, width=10,height=4, command=lambda: key_press(6,"",place_value6))
    grid_but6.grid(row=6,column=3)
    grid_but7=Button(window, textvariable=place_value7, width=10,height=4, command=lambda: key_press(7,"",place_value7))
    grid_but7.grid(row=7,column=1)
    grid_but8=Button(window, textvariable=place_value8, width=10,height=4, command=lambda: key_press(8,"",place_value8))
    grid_but8.grid(row=7,column=2)
    grid_but9=Button(window, textvariable=place_value9, width=10,height=4, command=lambda: key_press(9,"",place_value9))
    grid_but9.grid(row=7,column=3)

def win_cond():
    global counter,terminate,player1,player2
    poss_1=permutations([1,2,3])
    poss_2=permutations([4,5,6])
    poss_3=permutations([7,8,9])
    poss_4=permutations([1,4,7])
    poss_5=permutations([2,5,8])
    poss_6=permutations([3,6,9])
    poss_7=permutations([1,5,9])
    poss_8=permutations([3,5,7])
    
    for i in poss_1,poss_2,poss_3,poss_4,poss_5,poss_6,poss_7,poss_8:
        for j in list(i):
            play1=all(poss in player1 for poss in j)
            play2=all(poss in player2 for poss in j)

            if play1:
                showinfo("RESULT - ","Player 1 WINS. !!!")
                terminate=True
                return terminate
            elif play2:
                showinfo("RESULT - ","Player 2 WINS. !!!")
                terminate=True
                return terminate
            temp_var=0
            for value in keypress_count.values():
                if value==1:
                    temp_var=1
                else:
                    temp_var=0
                    break
            if temp_var==1:
                showinfo("RESULT - ","It's a DRAW. !!!")
                terminate=True
                return terminate

def chance(box_num):
    global counter,player1,player2
    for box_num_value in range(1,10):
        if box_num==box_num_value:
            if counter%2==0:
                counter+=1
                player1.append(box_num)
                return 'X'
            else:
                counter+=1
                player2.append(box_num)
                return 'O'

def limit_keypress(box_key):
    global keypress_count
    if keypress_count[box_key]==0:
        keypress_count[box_key]=1
        return True
    else:
        return False

def key_press(box_num,val,place_value):
    global p_val,counter,window,terminate,keypress_count,player1,player2
    if limit_keypress(box_num):
        p_val=chance(box_num)+val
        place_value.set(p_val)
        if win_cond():
            msg=askquestion(title="TRY AGAIN", message="WANT TO PLAY AGAIN?")
            if msg=='yes':
                draw_grid(window)
                terminate=False
                counter=0
                p_val=""
                player1,player2=list(),list()
                keypress_count={1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
            if msg=='no':
                showinfo("EXIT","THANK YOU. !!!")
                window.destroy()

def main_body():
    global window
    window.title("Tic Tac Toe")
    window.geometry("300x400")

    lab_def=Label(window, text="\nPlayer1 = X\nPlayer2 = O\n", width=40,height=2)
    lab_def.grid(row=2, columnspan=4)

    draw_grid(window)

    quit_button=Button(window, text="EXIT", command=window.destroy, width=20,height=1)
    quit_button.grid(row=10, columnspan=4)

    window.mainloop()

if __name__ == '__main__':
    main_body()
