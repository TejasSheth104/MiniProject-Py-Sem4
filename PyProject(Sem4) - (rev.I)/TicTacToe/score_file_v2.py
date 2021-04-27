from tkinter import *

def score_save(player_name,final_score):
    try:
        fh=open('score.txt','a')
        fh.write(player_name+" : "+str(final_score)+"\n")
        fh.close()
    except FileNotFoundError:
        print("File Not Found")

def get_scores():
# removed the argument above for testing

# using scrollbar?!

    # ls_content=list()
    # try:
    #     fh=open('score.txt','r')
    #     contents=fh.readlines()
    #     for value in contents:
    #         ls_content.append(str(value).strip("\n"))
    #     print(ls_content)

    #     scrollbar = Scrollbar(frame_score)
    #     scrollbar.pack(side=RIGHT,fill=Y)

    #     mylist=Listbox(frame_score,yscrollcommand=scrollbar.set )
    #     for line in range(len(ls_content)):
    #        mylist.insert(END,ls_content[line])

    #     mylist.place()
    #     scrollbar.config(command=mylist.yview )
    # except FileNotFoundError:
    #     print("File Not Found")


# below is a working SCOREBORAD, max at 4 entries.
    ls_content=list()
    new_list = []
    sorted_list = []
    largest_num = -100000000000
    iteration_num = 1
    
    try:
        fh=open('score.txt','r')
        contents=fh.readlines()
        for value in contents:
            ls_content.append(str(value).strip("\n"))
        for x in ls_content:
            new_list.append(x.split(" : "))
        length = len(new_list)
        while(iteration_num <= length):
            for y in new_list:
                if(largest_num < int(y[1])):
                    largest_name = y[0]
                    largest_num = int(y[1])
            # index = 0
            # sorted_list.insert(index, [largest_name, largest_num])
            curr_to_update = [largest_name, str(largest_num)]
            sorted_list.append(curr_to_update)
            largest_num = -100000000000
            iteration_num += 1
            # index += 1
            if(len(new_list) == 1):
                break
            new_list.remove(curr_to_update)
        print(sorted_list)

        # for x in sorted_list:
        # sorted_list.append(" : ".join(x))
        # sorted_list.remove(x)
        
        sorted_list=list(map(" : ".join,sorted_list))
        print("\n\n\n\nop - ", sorted_list)



    # load scores into Lables.
        # const_txt="PLAYER NAME" + " | " + "SCORE"
        # txt_label=Label(frame_score,text=const_txt,bg='black',fg='red',bd=1,relief="sunken",font=('arial',20,'bold'),width=19,height=2)
        # txt_label.grid(row=2,columnspan=4)

        # row_no=3
        # for x in range(len(ls_content)):
        #     display_label=Label(frame_score,text=ls_content[x],fg='red',bd=1,relief="sunken",font=('arial',20,'bold'),width=19,height=2)
        #     display_label.grid(row=row_no,columnspan=4)
        #     row_no+=1

        fh.close()
    except FileNotFoundError:
        print("File Not Found")

get_scores()