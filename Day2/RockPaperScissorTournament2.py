strategy = "F:\Python\PROJECT\AdventOfCode2022\Day2\input.txt"
# A X = rock
# B Y = paper
# C Z = scissor

totalPoint = 0
victoire = 6
egalite = 3
defaite = 0
rock = 1
paper = 2
scissors = 3

with open(strategy, mode='r', newline='\n') as file :
    for line in file :
        if line[2] == 'X':
            match line[0] :
                case ('A') :
                    totalPoint += defaite + scissors
                case ('B') :
                    totalPoint += defaite + rock
                case ('C') :
                    totalPoint += defaite + paper
        if line[2] == 'Y':
            match line[0] :
                case ('A') :
                    totalPoint += egalite + rock
                case ('B') :
                    totalPoint += egalite + paper
                case ('C') :
                    totalPoint += egalite + scissors
        if line[2] == 'Z':
            match line[0] :
                case ('A') :
                    totalPoint += victoire + paper
                case ('B') :
                    totalPoint += victoire + scissors
                case ('C') :
                    totalPoint += victoire + rock
    print(totalPoint)   
    print(line)    
    