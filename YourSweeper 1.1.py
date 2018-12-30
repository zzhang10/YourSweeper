


#⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊#
#      __   __               ____                                            #
#      \ \ / /__  _   _ _ __/ ___|_      _____  ___ _ __   ___ _ __          #
#       \ V / _ \| | | | '__\___ \ \ /\ / / _ \/ _ \ '_ \ / _ \ '__|         #
#        | | (_) | |_| | |   ___) \ V  V /  __/  __/ |_) |  __/ |            #
#        |_|\___/ \__,_|_|  |____/ \_/\_/ \___|\___| .__/ \___|_|              #
#                                                  |_|                       #
#                                                                            #
#                              By Zack Zhang                                 #
#                                                                              #  
#⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊#




#⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊#
#                        IMPORTANT DISCLAIMER:                                       #
#⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊#

#The graphics are optimized for font 13. You might need to switch between the
# fonts Courier and Courier New to make the computer recognize some of the
# Unicode symbols used in game graphics.

#Using other programs to run the game (like Jupyter and CMD) may
# result in distorted graphics or unrecognizable characters that can
# significantly affect gameplay.


#⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊#
#                               GRAPHICS                                       #
#⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊#

#Feel free to replace them with your own symbols to customize the game.

#Some circled letters:
#ⒶⒷⒸⒹⒺⒻⒼⒽⒾⒿⓀⓁⓂⓃⓄⓅⓆⓇⓈⓉⓊⓋⓌⓍⓎⓏ

#Numbers to indicate the columns:
column_indicators="①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳㉑㉒㉓㉔㉕㉖㉗㉘㉙㉚㉛㉜㉝\
㉞㉟㊱㊲㊳㊴㊵㊶㊷㊸㊹㊺㊻㊼㊽㊾㊿"

#⬛: Unscouted minefield

unscouted="⬛"

#⬜: Scouted minefield: nothing around
zero="⬜"

#❶: Scouted minefield: 1 mine in the 8 blocks around
one="❶"

#❷: Scouted minefield: 2 mines in the 8 blocks around
two="❷"

#❸: Scouted minefield: 3 mines in the 8 blocks around
three="❸"

#❹: Scouted minefield: 4 mines in the 8 blocks around
four="❹"

#❺: Scouted minefield: 5 mines in the 8 blocks around
five="❺"

#❻: Scouted minefield: 6 mines in the 8 blocks around
six="❻"

#❼: Scouted minefield: 7 mines in the 8 blocks around
seven="❼"

#❽: Scouted minefield: 8 mines in the 8 blocks around
eight="❽"

#〶: Player marker: "I think there's a mine here."
mine_marker="〶"

#✪: Computer display: "There is a mine here."
mine="✪"

#⛒: Computer display: "You thought there's a mine here, but actually not."
false_alarm="⛒"

#Graphics setup at the beginning of the game:
graphic_setup_prompt="""IMPORTANT GRAPHICS SETUP:

①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳㉑㉒㉓㉔㉕㉖㉗㉘㉙㉚㉛㉜㉝㉞㉟㊱㊲㊳㊴㊵
⬛⬜⬛⬜⬛⬜⬛⬜⬛⬜⬛⬜⬛⬜⬛⬜⬛⬜⬛⬜⬛⬜⬛⬜⬛⬜⬛⬜⬛⬜⬛⬜⬛⬜⬛⬜⬛⬜⬛⬜

If you do not see a line of numbers in circles, followed by a line
of black and white squares, then your graphics may not be optimized
for the game. Make sure you are running the game in Python IDE and
not CMD.

If the lines you see are not equally as long, adjust the IDE fonts
between Courier and Courier New until the graphic updates so that
the two lines are equally as long. You may also need to change the
graphics and screen resolution (1.5 : 1 resolution should be fine)

"""

#⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊#
#                           TECHNICAL CONFIGS                                    #
#⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊#

#Maximum number of rows,increasing this may result in graphic distortions:
row_number_max=30

#Minimum number of rows,increasing this may result in graphic distortions:
row_number_min=10

#Maximum number of columns,increasing this may result in graphic distortions:
column_number_max=50

#Minimum number of columns,increasing this may result in graphic distortions:
column_number_min=10

#Minimum percentage of mines in the field, changing this may result in
# poor gameplay experience:
mine_percentage_min=5

#Maximum percentage of mines in the field, changing this may result in
# poor gameplay experience:
mine_percentage_max=99

#⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊#
#                             TEXT CONFIGS                                     #
#⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊#

#➤Opening:

#The title/GUI graphics:
#Title may be too wide for certain graphic settings/screen resolutions
title_graphics="""
⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊
  __  __                 _____                                      ___   ___
  \ \/ /___  __  _______/ ___/      _____  ___  ____  ___  _____   <  /  <  /
   \  / __ \/ / / / ___/\__ \ | /| / / _ \/ _ \/ __ \/ _ \/ ___/   / /   / / 
   / / /_/ / /_/ / /   ___/ / |/ |/ /  __/  __/ /_/ /  __/ /      / /_  / /
  /_/\____/\__,_/_/   /____/|__/|__/\___/\___/ .___/\___/_/      /_/(_)/_/   
                                            /_/                                     
⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊
"""

#This is the explanation of the general rules:
greeting="""Welcome to YourSweeper!

In this game you are trying to clear a minefield strategically, by using the
indicators the game sends you.

Please configure your game field as prompted.

MAX SIZE: The maximum size is {} columns by {} rows.
MIN SIZE: The minimum size is {} columns by {} rows.
MINE DENSITY: According to your choice,{} to {}% of the minefield
              is covered in mines.
"""

#➤Field configuration:

#This prompts the player to select the size of the field in rows:
opening_row_selection="Please enter the number of ROWS you would like: "

#When player selects a row that is beyond size limit:
opening_row_invalid="Your entry is invalid. You can only have between {} and {} rows."

#This prompts the player to select the size of the field in columns:
opening_column_selection="Please enter the number of COLUMNS you would like: "

#When player selects a column that is beyond size limit:
opening_column_invalid="Your entry is invalid. You can only have between {} and {} columns."

#This prompts the player to select the percentage of mines:
mine_percentage_selection="Please enter the PERCENTAGE of mines you would like in your field: "

#When player selects a mine composition that is beyond percentage limit:
mine_percentage_invalid="Your entry is invalid. You can only have between\
 {} and {} percent of mines."

#Summary of the size of field and difficulty after the player's configuration:
config_announcement="You have chosen a field of {} rows by {} columns,\
 with {}% mines in the field."

#This announces the amount of mines in the field:
mine_announcement="There will be {} mines in the field."

#This tells the player how many flags they have:
flag_count="""
Flags remaining: {}

"""

#This prompts the player to select input modes:
action_selection=\
"""
Enter 1 if you would like to dig into a square,
      2 if you would like to flag a mine, 
      3 if you would like to un-flag a mine, or

      0 if you would like to quit: """

#When the player selects an invalid mode:
action_invalid="Invalid selection. You can only select 0,1,2,or 3"

#➤Digging:

#The prompt when the player is selecting the row of the field to dig into:
dig_row_selection="Please enter the number of the ROW you would like to dig\
 into,or enter 0 to quit digging mode: "

#When player selects a row outside the field to dig into:
dig_row_invalid="Your entry is invalid. You can only dig between rows 1 and {}"

#The prompt when the player is selecting the column of the field to dig into:
dig_column_selection="Please enter the number of the COLUMN you would like to \
dig into, or enter 0 to quit digging mode: "

#When player selects a column outside the field to dig into:
dig_column_invalid="Your entry is invalid. You can only dig between rows 1 and {}"

#When player tries to dig into a square that they haved marked as a mine:
dig_flagged_invalid="You have marked this square as unsafe to dig. Please\
 remove the marker before digging"

#When the player tries to dig into a square that has been explored already:
dig_explored_invalid="You have explored this square already. Please dig\
 somewhere else."

#This announces that you have dug into a mine:
stepped_on_mine_announcement="You have stepped on a mine!"

#When the player quits digging mode:
dig_exit="You will now exit digging mode."

#➤Flagging:

#The prompt when the player is selecting the row of the field to flag:
flag_row_selection="Please enter the number of the row you would like to\
 flag,or enter 0 to quit flagging mode: "

#When player selects a row outside the field to flag on:
flag_row_invalid="Your entry is invalid. You can only flag between \
rows 1 and {}."

#The prompt when the player is selecting the column of the field to flag:
flag_column_selection="Please enter the number of the column you would like\
 to flag,or enter 0 to quit flagging mode: "

#When the player selects a column outside the field to flag on:
flag_column_invalid="Your entry is invalid. You can only flag between rows\
 1 and {}"

#When the player tries to flag but have ran out of flags:
flag_depleted_invalid="You have ran out of flags. You may not flag a mine right now."

#When the player tries to flag a square that has been explored already:
flag_explored_invalid="You have explored/flagged this square already. \
Please choose somewhere else."

#When the player quits flagging mode:
flag_exit="You will now exit flagging mode."


#➤Un-flagging:

#The prompt when the player is selecting the row of the field to unflag:
unflag_row_selection="Please enter the number of the row you would like to\
 unflag,or enter 0 to quit unflagging mode: "

#When the player selects a row outside the field to unflag:
unflag_row_invalid="Your entry is invalid. You can only choose between \
 rows 1 and {}."

#The prompt when the player is selecting the column of the field to unflag:
unflag_column_selection="Please enter the number of the column you would like\
to unflag,or enter 0 to quit unflagging mode: "

#When the player selects a column outside the field to unflag:
unflag_column_invalid="Your entry is invalid. You can only choose between rows\
 1 and {}."

#When the player tries to unflag but have not put down any flags:
unflag_no_flags_put_down_invalid="You have not flagged any mines. You may not unflag a mine right now."

#When the player tries to flag a square that has been explored already:
unflag_not_flagged_invalid="This square does not contain a flag. Please choose somewhere else."

#When the player quits flagging mode:
unflag_exit="You will now exit unflagging mode."

#➤Ending:

#After the player steps on a mine:
lost_message="You lost!"

#After the player explores all the field without stepping on a mine:
win_message="You won!"

#After the player quits the game without finishing it:
quit_message="Quitting game..."

#After the player finishes one game:
play_again_prompt="Would you like to play again? Enter yes or no: "

#If the player does not respond with "yes" or "no" to above prompt:
play_again_invalid="Selection invalid. You may only enter yes or no."



#⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊#
#                               CHEAT MODE                                       #
#⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊#

#Cheat mode:
#Shows coordinates of mines before game. Defaults to False.
cheat_mode=True


#Displays this message when cheat mode is True:
cheat_message="\nCHEAT MODE ACTIVATED! BELOW ARE THE LOCATIONS OF THE MINES.\n"


#⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊#
#                              VVV CODE VVV                                    #
#⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊#

import random

def start_game(cheat_mode):

    #is_number checks if the input is a number, to make sure the rest of the code functions correctly:
    def is_number(anything):
        try:
            float(anything)
            return True
        except:
            return False

    #selection prompts the player to select the size of the minefield:
    def selection (prompt,minimum,maximum,error_message):
        selected=False
        while selected==False:
            output=input("{}".format(prompt))
            if is_number (output):
                if float.is_integer(float(output)):
                    if minimum <= int(float(output)) <= maximum:
                        columns_selected=True
                        return output
                    else:
                        print ("{}".format(error_message))
                else:
                    print ("{}".format(error_message))
            else:
                print ("{}".format(error_message))

    #make_field generates the minefield according to the player's selection:
    def make_field(row_number, column_number):
        row_counter=0
        one_field=[]
        top_row=column_indicators
        one_field.append("   "+top_row[0:column_number])
        while row_counter<row_number:
            column_counter=0
            if row_counter<=8:
                local_column=[str(row_counter+1)+"  " ]
            else:
                local_column=[str(row_counter+1)+" " ]
            while column_counter<column_number:
                local_column.append (unscouted)
                column_counter+=1          
            one_field.append(local_column)
            row_counter+=1
        return one_field

    #print_field prints out the minefield in its current state:
    def print_field (field,row_number,column_number):
        main_field=[]
        for row in field:
            for item in row:
                main_field.append(item)
            main_field.append ("\n")
        print ("".join(main_field))

    #lay_mines randomly generates the mines in the field:
    def lay_mines (field):
        mines_laid=0
        target_mines = int(int(rows)*int(columns)*int(mine_percentage)/100)
        print (mine_announcement.format(target_mines))
        while mines_laid < target_mines:
            mine_coords_1=random.randint(1, int(rows))
            mine_coords_2=random.randint(1,int(columns))
            if field [mine_coords_1][mine_coords_2] != mine:
                field [mine_coords_1][mine_coords_2] = mine
                mines_laid += 1
            else:
                pass

    #mines_around checks the mines around a certain grid:
    def mines_around (target_row,target_column,maximum_row,maximum_column):
        mine_count=0
        for sublist in [[-1,0],[1,0],[0,-1],[0,1],[-1,-1],[1,1],[-1,1],[1,-1]]:
            try:
                if minetracker_field[target_row+sublist[0]][target_column+sublist[1]]==mine:
                    mine_count += 1
            except:
                pass
        return mine_count

    #reveal_minefield reveals the mines at the end of the game:
    def reveal_minefield (field, minetracker_field,row_number,column_number):
        for row in minetracker_field:
            counter=0
            while counter<=int(column_number):
                if row[counter]==mine and field [minetracker_field.index(row)][counter]!= mine_marker:
                    field [minetracker_field.index(row)][counter]=mine
                elif row[counter]!=mine and field [minetracker_field.index(row)][counter]== mine_marker:
                    field [minetracker_field.index(row)][counter]=false_alarm
                elif row[counter]==unscouted and field [minetracker_field.index(row)][counter]== unscouted:
                    field [minetracker_field.index(row)][counter]=zero
                else:
                    pass
                counter+=1       

    #explore simulates digging the select square of the minefield:                         
    def explore (target_row,target_column,maximum_row,maximum_column):
        if minetracker_field [target_row][target_column] == mine:
            reveal_minefield(field,minetracker_field,maximum_row,maximum_column)
            print(stepped_on_mine_announcement)
        else:
            mine_count = mines_around(target_row,target_column,maximum_row,maximum_column)
            if mine_count==0:
                field [target_row][target_column]=zero
            elif mine_count==1:
                field [target_row][target_column]=one
            elif mine_count==2:
                field [target_row][target_column]=two
            elif mine_count==3:
                field [target_row][target_column]=three
            elif mine_count==4:
                field [target_row][target_column]=four
            elif mine_count==5:
                field [target_row][target_column]=five
            elif mine_count==6:
                field [target_row][target_column]=six
            elif mine_count==7:
                field [target_row][target_column]=seven
            elif mine_count==8:
                field [target_row][target_column]=eight

    #explore_around expands the exploration around the square, and detect other safe squares:            
    def explore_around (target_row,target_column,maximum_row,maximum_column):
        explore(target_row,target_column,maximum_row,maximum_column)
        if minetracker_field [target_row][target_column]!= mine and\
           mines_around (target_row,target_column,maximum_row,maximum_column)== 0:
            to_explore=[[target_row,target_column]]
            explored=[]
            for item in to_explore:
                if item in explored:
                    to_explore.remove(item)
            while to_explore!=[]:
                explored.append([to_explore[0][0],to_explore[0][1]])
                for sublist in [[-1,0],[1,0],[0,-1],[0,1],[-1,-1],[-1,1],[1,-1],[1,1]]:
                    if maximum_row>=to_explore[0][0]+sublist[0]>=0\
                       and maximum_column>=to_explore[0][1]+sublist[1]>=0\
                       and field [to_explore[0][0]+sublist[0]][to_explore[0][1]+sublist[1]]==unscouted\
                       and minetracker_field [to_explore[0][0]+sublist[0]][to_explore[0][1]+sublist[1]]!= mine\
                       and [to_explore[0][0]+sublist[0],to_explore[0][1]+sublist[1]] not in explored:
                        try:
                            explore(to_explore[0][0]+sublist[0],to_explore[0][1]+sublist[1]\
                                    ,maximum_row,maximum_column)                                               
                        except:
                            pass
                    else:
                        pass
                for sublist in [[-1,0],[1,0],[0,-1],[0,1],[-1,-1],[-1,1],[1,-1],[1,1]]:
                    if maximum_row>=to_explore[0][0]+sublist[0]>=0\
                       and maximum_column>=to_explore[0][1]+sublist[1]>=0\
                       and field [to_explore[0][0]+sublist[0]][to_explore[0][1]+sublist[1]]==zero\
                       and [to_explore[0][0]+sublist[0],to_explore[0][1]+sublist[1]] not in explored:
                        to_explore.append([to_explore[0][0]+sublist[0],to_explore[0][1]+sublist[1]])
                        explored.append([to_explore[0][0]+sublist[0],to_explore[0][1]+sublist[1]])                   
                    else:
                        pass
                del to_explore[0]
            print_field(field,int(rows),int(columns))

    #dig prompts the player to select a square to explore:        
    def dig ():
        finished_digging=False
        while finished_digging==False:
            row_selected1=selection(dig_row_selection,0,int(rows),dig_row_invalid.format(int(rows)))
            if int(row_selected1)==0:
                print(dig_exit)
                break
            column_selected1=selection(dig_column_selection,0,int(columns),\
                                       dig_column_invalid.format(int(columns)))
            if int(column_selected1)==0:
                print(dig_exit)
                break
            elif int(row_selected1)!=0 and int(column_selected1)!=0 and \
               field[int(row_selected1)][int(column_selected1)]==unscouted:
                finished_digging=True
                explore_around (int(row_selected1),int(column_selected1),int(rows),int(columns))
            elif int(row_selected1)!=0 and int(column_selected1)!=0 and \
                 field[int(row_selected1)][int(column_selected1)]==mine_marker:
                print(dig_flagged_invalid)
            else:
                print(dig_explored_invalid)

    #flag_mine prompts the player to flag a possible mine:
    def flag_mine(field):     
        finished_flagging=False
        while finished_flagging==False:
            row_selected2=selection(flag_row_selection,0,int(rows),flag_row_invalid.format(int(rows)))
            if int(row_selected2)==0:
                print(flag_exit)
                return False
                break
            column_selected2=selection(flag_column_selection,0,int(columns),\
                                       flag_column_invalid.format(int(columns)))
            if int(column_selected2)==0:
                print(flag_exit)
                return False
                break
            elif field[int(row_selected2)][int(column_selected2)]==unscouted:
                field[int(row_selected2)][int(column_selected2)]=mine_marker
                finished_flagging=True
                return True
            else:
                print(flag_explored_invalid)

    #unflag_mine prompts the player to remove a mine flag:
    def unflag_mine(field):     
        finished_unflagging=False
        while finished_unflagging==False:
            row_selected3=selection(unflag_row_selection,0,int(rows),unflag_row_invalid.format(int(rows)))
            if int(row_selected3)==0:
                print(unflag_exit)
                return False
                break
            column_selected3=selection(unflag_column_selection,0,int(columns),\
                                       unflag_column_invalid.format(int(columns)))
            if int(column_selected3)==0:
                print(unflag_exit)
                return False
                break
            elif field[int(row_selected3)][int(column_selected3)]==mine_marker:
                field[int(row_selected3)][int(column_selected3)]=unscouted
                finished_flagging=True
                return True
            else:
                print(unflag_not_flagged_invalid)        

    #check_win checks to see if the player has identified all the mines:    
    def check_win ():
        field_explored=True
        for row in field:
            counter=0
            while counter<=int(columns):
                if field[field.index(row)][counter] == unscouted and\
                   minetracker_field [field.index(row)][counter]!=mine:
                    field_explored=False
                elif field[field.index(row)][counter] == mine_marker and\
                     minetracker_field [field.index(row)][counter]!=mine:
                    field_explored=False
                else:
                    pass
                counter+=1
        return field_explored

    #check_lost checks whether the player has stepped on a mine:
    def check_lost():
        blew_up=False
        for row in field:
            for square in row:
                if square==mine:
                    blew_up=True
                else:
                    pass
        return blew_up


    #Game begins:
    print (title_graphics)
    print(greeting.format(column_number_max,row_number_max,column_number_min,row_number_min,\
                                      mine_percentage_min,mine_percentage_max))
    rows=selection(opening_row_selection,row_number_min,row_number_max,\
                   opening_row_invalid.format(row_number_min,row_number_max))
    columns=selection(opening_column_selection,column_number_min,column_number_max,\
                      opening_column_invalid.format(column_number_min,column_number_max))
    mine_percentage=selection(mine_percentage_selection,mine_percentage_min,mine_percentage_max,\
                      mine_percentage_invalid.format(mine_percentage_min,mine_percentage_max))

    print (config_announcement.format (rows,columns,mine_percentage))
    field=make_field(int(rows),int(columns))
    minetracker_field=make_field(int(rows),int(columns))
    lay_mines (minetracker_field)
    if cheat_mode==True:
        print (cheat_message)
        print_field (minetracker_field,int(rows),int(columns))
        cheat_mode=False
    mine_markers = int(int(rows)*int(columns)*int(mine_percentage)/100)  
    print_field (field,int(rows),int(columns))
    print (flag_count.format(mine_markers))
    action_layer_1=False
    while action_layer_1==False:
        if check_lost()==True:
            print (lost_message)
            action_layer_1=True
        elif check_win()==True:
            reveal_minefield (field, minetracker_field,int(rows),int(columns))
            print_field(field,int(rows),int(columns))
            print (win_message)
            action_layer_1=True
        elif check_win()==False and check_lost()==False:    
            action_layer_2=False
            while action_layer_2==False:
                action=input(action_selection)
                if is_number(action)==True and (float(action)).is_integer() and int(action)==0:
                    print (quit_message)
                    action_layer_1=True
                    action_layer_2=True
                    break            
                elif is_number(action)==True and (float(action)).is_integer() and int(action)==1:
                    action_layer_2=True
                    dig()
                    print_field(field,int(rows),int(columns))
                    print (flag_count.format(mine_markers))
                elif is_number(action)==True and (float(action)).is_integer() and int(action)==2:
                    if mine_markers<=0:
                        print (flag_depleted_invalid) 
                    else:
                        action_decided=True
                        if flag_mine(field)==True:
                            mine_markers-=1
                            print_field(field,int(rows),int(columns))
                            print (flag_count.format(mine_markers))
                    action_layer_2=True
                elif is_number(action)==True and (float(action)).is_integer() and int(action)==3:
                    if mine_markers>=(int(rows)*int(columns)*int(mine_percentage)/100):
                        print (unflag_no_flags_put_down_invalid)
                    else:
                        if unflag_mine(field)==True:
                            mine_markers+=1
                            print_field(field,int(rows),int(columns))
                            print (flag_count.format(mine_markers))
                    action_layer_2=True
                else:
                    print(action_invalid)
        else:
            pass

    
#Main sequence of the game:
print(graphic_setup_prompt)
input("After your graphic is set up, enter anything to continue.")
start_game(cheat_mode)               
again=True
while again==True:
    play_again=input(play_again_prompt)
    if play_again.lower()=="no":
        again=False
    elif play_again.lower()=="yes":
        start_game(cheat_mode)
    else:
        print (play_again_invalid)       











