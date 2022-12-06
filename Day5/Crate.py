crates_file = "F:\Python\PROJECT\AdventOfCode2022\Day5\init.txt"
input_file = "F:\Python\PROJECT\AdventOfCode2022\Day5\input.txt"

boxes_matrix = []
yD = 8

with open(crates_file, "r") as file:

    for line in file:
        if(yD>0) :
            boxes_matrix.append(line)
            yD = yD-1
            #print(len(boxes_matrix[-1]))
        
    
    boxes_matrix.reverse()

stack_list = [[] for _ in range(9)]

for line in boxes_matrix:

    counter = 0
    spacecounter = 1

    for char in line:

        if char.isalpha():
            stack_list[counter].append(char)
            counter += 1
            spacecounter = 1

        if (char == " "):
            spacecounter += 1

        if(spacecounter == 5):
            counter += 1
            spacecounter = 1

print(stack_list)

#from the code of eloworld-star
with open(input_file) as file:
    for line in file:
        chunk=line.split()
        nbrMove = int(chunk[1])
        fromCol = int(chunk[3])
        toCol = int(chunk[5])
        tabFrom = stack_list[fromCol-1]
        tabTo = stack_list[toCol-1]

        print(nbrMove)
        print("-")
        print(fromCol)
        print(tabFrom)
        print("-")
        print(toCol)
        print(tabTo)
        print("-")


        lenght=len(tabFrom)
        partToMove = tabFrom[lenght-nbrMove:lenght]
        i=0
        while i<nbrMove:
            tabFrom.pop(lenght-nbrMove)
            i+=1
            
        #enlever le # a la ligne suivante pour la partie A
        #partToMove.reverse()
        for element in partToMove:
            tabTo.append(element)

        print("partToMove")
        print(partToMove)
        print("new tab "+str(toCol))
        print(tabTo)
        print("new tab"+str(fromCol))
        print(tabFrom)
        print("======================================")
        print(stack_list)
            
        
            
        

    

    


