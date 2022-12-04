backpack = "F:\Python\PROJECT\AdventOfCode2022\Day3\input.txt"
totalvalue = 0

#cut the string in two egal size
with open(backpack) as file :
    for line in file :
        #Cut the String in two egal part
        lenght = len(line)
        half1 = line[0:lenght//2]
        half2 = line[lenght//2:lenght]

        print(half1,half2)
        
        #Find the common char
        a= ''.join((set(half1).intersection(half2)))
        for commonChar in a:
        
            #Set the score
            if commonChar.isupper() :
                totalvalue += ord(commonChar)-38
            else :
                totalvalue += ord(commonChar)-96
              
    #Print output
    print(totalvalue)    
