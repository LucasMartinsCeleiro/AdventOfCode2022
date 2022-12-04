backpack = "F:\Python\PROJECT\AdventOfCode2022\Day3\input.txt"
totalvalue = 0
cpt = 0
group = []

with open(backpack) as file :
    
    for line in file :
        group.append(line.strip())
        cpt +=1
        #When 3 string add points
        if cpt % 3 == 0:
            #isolating the common char
            group = [set(line) for line in group]
            commonCharGroup = set.intersection(*group)
            #Totalpoint calculus
            for element in commonCharGroup :
                #Check if the character is upper or lower case
                if element.isupper() :
                    totalvalue += ord(element)-38
                elif element.islower():
                    totalvalue += ord(element)-96
            #Clear the group for the next iteration
            group.clear()
                
    #Print output
    print(totalvalue)


