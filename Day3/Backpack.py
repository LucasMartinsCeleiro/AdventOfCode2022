backpack = "F:\Python\PROJECT\AdventOfCode2022\Day3\input.txt"
totalvalue = 0

#cut the string in two egal size
with open(backpack, mode='r', newline='\n') as file :
    for line in file :
        #Cut the String in two egal file
        l = len(line)
        half1 = slice(0,l//2)
        half2 = slice(l//2,l)
        print(line[half1], line[half2])
        
        #Find the common char
        a=list(set(half1)&set(half2))
        for i in a:
            commonChar = i
        
        #Set the score
        if commonChar.isupper() == 'False' :
                if 'a':
                    totalvalue += 1
                elif 'b':
                    totalvalue += 2
                elif 'c':
                    totalvalue += 3
                elif 'd':
                    totalvalue += 4
                elif 'e':
                    totalvalue += 5
                elif 'f':
                    totalvalue += 6
                elif 'g':
                    totalvalue += 7
                elif 'h':
                    totalvalue += 8
                elif 'i':
                    totalvalue += 9
                elif 'j':
                    totalvalue += 10
                elif 'k':
                    totalvalue += 11
                elif 'l':
                    totalvalue += 12
                elif 'm':
                    totalvalue += 13
                elif 'n':
                    totalvalue += 14
                elif 'o':
                    totalvalue += 15
                elif 'p':
                    totalvalue += 16
                elif 'q':
                    totalvalue += 17
                elif 'r':
                    totalvalue += 18
                elif 's':
                    totalvalue += 19
                elif 't':
                    totalvalue += 20
                elif 'u':
                    totalvalue += 21
                elif 'v':
                    totalvalue += 22
                elif 'w':
                    totalvalue += 23
                elif 'x':
                    totalvalue += 24
                elif 'y':
                    totalvalue += 25
                elif 'z':
                    totalvalue += 26
        else :
                if 'A':
                    totalvalue += 27
                elif 'B':
                    totalvalue += 28
                elif 'C':
                    totalvalue += 29
                elif 'D':
                    totalvalue += 30
                elif 'E':
                    totalvalue += 31
                elif 'F':
                    totalvalue += 32
                elif 'G':
                    totalvalue += 33
                elif 'H':
                    totalvalue += 34
                elif 'I':
                    totalvalue += 35
                elif 'J':
                    totalvalue += 36
                elif 'K':
                    totalvalue += 37
                elif 'L':
                    totalvalue += 38
                elif 'M':
                    totalvalue += 39
                elif 'N':
                    totalvalue += 40
                elif 'O':
                    totalvalue += 41
                elif 'P':
                    totalvalue += 42
                elif 'Q':
                    totalvalue += 43
                elif 'R':
                    totalvalue += 44
                elif 'S':
                    totalvalue += 45
                elif 'T':
                    totalvalue += 46
                elif 'U':
                    totalvalue += 47
                elif 'V':
                    totalvalue += 48
                elif 'W':
                    totalvalue += 49
                elif 'X':
                    totalvalue += 50
                elif 'Y':
                    totalvalue += 51
                elif 'Z':
                    totalvalue += 52  
    #Print output
    print(totalvalue)    
