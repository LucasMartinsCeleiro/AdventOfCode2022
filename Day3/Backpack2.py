backpack = "F:\Python\PROJECT\AdventOfCode2022\Day3\input.txt"
totalvalue = 0
group = []
cpt = 0

#cut the string in two egal size
with open(backpack) as file :
    
    for line in file :
        while cpt != 3:
            group.append(line)
            for char in line :
                if char == '\n':
                    cpt +=1
                    print(cpt)
  
    cpt = 0
    commonCharGroup = set.intersection(*map(set,group))
    if commonCharGroup.isupper () :
        totalvalue += ord(commonCharGroup)-38
    else :
        totalvalue += ord(commonCharGroup)-96
              
    #Print output
    print(totalvalue)
