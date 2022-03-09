row1 = ["⬜️","⬜️","⬜️"]#the white blocks are just emojis that                             were copied and pasted
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]#we created a list that includes all 3 rows i.e. this is                     a nested list
print(f"{row1}\n{row2}\n{row3}")# \n gives a line between each row
position = input("Where do you want to put the treasure? ")

#lets say we input 23
# we also need to convert these to integers
horizontal = int(position[0]) #position 0 is 2 which we assign to horizontal
vertical = int(position[1]) #position 1 is 3 which we assign to vertical


#we get the selected ROW using the VERTICLE
selected_row = map[vertical - 1]#gives colum 2
#then inside the selected_row, we ca get the horizontal tile that was specified
#we get the selected TILE using the horizontal
selected_row[horizontal - 1] = "X" #at the postision of the                                          horizontal - 1
                                   #now we want to change that to                                    "X"