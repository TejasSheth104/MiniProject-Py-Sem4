from tkinter import *
import fileinput

def score_save(player_name,score):
    fh=open('score.py','a')
    fh.close()

    normal_write=True
    fh=open("score.txt","r")
    lines=fh.readlines()
    for line in lines:
    
        temp_v1=line.strip("\n").split(" : ")
    
        if player_name.title()==temp_v1[0].title():
            final_score=score+int(temp_v1[1])
            normal_write=False
            break
    
    fh.close()

    with fileinput.FileInput("score.txt",inplace=True) as f:                # ,backup=".bak" - 3rd parameter

        for line in f:

            if str(player_name).upper() in str(line).upper():
                print(str(player_name).upper()+" : "+str(final_score), end="\n")

            else:
                print(line,end="")

    if normal_write:
        fh3=open('score.txt','a')
        fh3.write(player_name.upper()+" : "+str(score)+"\n")
        fh3.close()

def get_scores(frame_score):

    fh=open('score.py','a')
    fh.close()
    
# A working SCOREBORAD. max 10 entries- sorted 
    ls_content,new_list,sorted_list=list(),list(),list()
    largest_num=-1
    iter_count=1

    try:
        fh=open('score.txt','r')

        contents=fh.readlines()
        
        for value in contents:
            ls_content.append(str(value).strip("\n"))
        
        for x in ls_content:
            new_list.append(x.split(" : "))
        
        length_list = len(new_list)
        
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

            display_label=Label(frame_score,text=str(sorted_list[x]),fg='black',bd=1,relief="sunken",font=('arial',20,'bold'),width=19,height=1)
            display_label.grid(row=row_no,columnspan=4)
            row_no+=1

        fh.close()

    except FileNotFoundError:
        print("File Not Found")
