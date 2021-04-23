
# file open
def score_save(option,player_name,score):
    if option==3:
        try:
            fh=open('score.txt','a')
        # print("Success")

            file_write=(player_name+", "+str(score)+"\n")
            fh.write(file_write)
            fh.close()
        except FileNotFoundError:
            print("File Not Found")

    fh=open('score.txt','r')
    if option==1:
        for line in fh:
            print(line)
    elif option==2:
        pass
    elif option==3:
        for line in fh:
            line=line.split(', ')
            if line[0]==player_name:
                print(line[1])

    fh.close()

    # print("Done")

score_save(3,'raj',15)

'''
can remove draw condition, if storing just scores for winning.
# store 0 for draw.

parameters score_save(option,name_winning_player,score)
option - create bottons, eg. ALL SCORES, TOP 5, CURRENT GAME
        1 = all_scores
        2 = top_5
        3 = current_game
score - 
        WIN -> no. of moves remaining*5

# file store format. 
# ( dictionary? )
{name_Winning_player:score}
# (list? )
name_Winning_player, score
'''