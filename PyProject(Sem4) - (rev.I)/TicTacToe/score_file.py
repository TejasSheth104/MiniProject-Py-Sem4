from tkinter import *

def score_save(player_name,final_score):
    try:
        fh=open('score.txt','a')
        fh.write(player_name+" : "+str(final_score)+"\n")
        fh.close()
    except FileNotFoundError:
        print("File Not Found")

def get_scores(frame_score):
# below is a working SCOREBORAD, max at 4 entries.
    ls_content,new_list,sorted_list=list(),list(),list()
    largest_num=-1
    iter_count=1

    try:
        fh=open('score.txt','r')

        contents=fh.readlines()
        for value in contents:
            ls_content.append(str(value).strip("\n"))
        # print(ls_content)

        for x in ls_content:
            new_list.append(x.split(" : "))
        length_list = len(new_list)
        # print(length_list)

        while(iter_count <= length_list):
            for y in new_list:
                if(largest_num < int(y[1])):
                    largest_name = y[0]
                    largest_num = int(y[1])
            temp_element = [largest_name, str(largest_num)]
            sorted_list.append(temp_element)
            largest_num=-1
            iter_count+=1
            if(len(new_list)==1):
                break
            new_list.remove(temp_element)
        
        # print(sorted_list)
        # rejoined the contents that were split using ":".join()
        sorted_list=list(map(" : ".join,sorted_list))

    # load scores into Lables.
        const_txt="PLAYER NAME" + " | " + "SCORE"
        txt_label=Label(frame_score,text=const_txt,bg='black',fg='red',bd=1,relief="sunken",font=('arial',20,'bold'),width=19,height=2)
        txt_label.grid(row=2,columnspan=4)

        row_no=3
        if length_list>10:
            length_list=10
        for x in range(length_list):
            display_label=Label(frame_score,text=str(sorted_list[x]),fg='red',bd=1,relief="sunken",font=('arial',20,'bold'),width=19,height=1)
            display_label.grid(row=row_no,columnspan=4)
            row_no+=1

        fh.close()
    except FileNotFoundError:
        print("File Not Found")


'''
# 1. disable START button (need to work on this)
# 2. scoreboard is tooo bad, change it.
3. scoring method.
    3 moves = 5 pts
    4 moves = 3 pts
    5 moves = 1 pt
# 4. remove, replay option
# 5. remove Thank You mbox
X# 6. implement scrollbar (if possible)
7. check file for same names!!!
# 8. validate name! in tic_tac_toe.py
9.

'''