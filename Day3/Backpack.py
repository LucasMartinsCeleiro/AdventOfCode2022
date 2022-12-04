backpack = "F:\Python\PROJECT\AdventOfCode2022\Day3\input.txt"
totalvalue = 0

#cut the string in two egal size
with open(backpack, mode='r', newline='\n') as file :
    for line in file :
        #Cut the String in two egal part
        l = len(line)
        half1 = slice(0,l//2)
        half2 = slice(l//2,l)

        print(line[half1], line[half2])
        
        #Find the common char
        a= ''.join((set(line[half1]).intersection(line[half2])))
        for i in a:
            commonChar = i
        
            #Set the score
            if commonChar.isupper() == 'False' :
                totalvalue += ord(commonChar)-96   
            else :
                totalvalue += ord(commonChar)-64  
              
    #Print output
    print(totalvalue)    
