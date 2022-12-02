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
        match line[0] :
            case ('A') :
                match line[2] :
                    case 'X' :
                        totalPoint += egalite + rock
                    case 'Y' :
                        totalPoint += victoire + paper
                    case 'Z' :
                        totalPoint += defaite + scissors
            case ('B') :
                match line[2] :
                    case 'X' :
                        totalPoint += defaite + rock
                    case 'Y' :
                        totalPoint += egalite + paper
                    case 'Z' :
                        totalPoint += victoire + scissors
            case ('C') :
                match line[2] :
                    case 'X' :
                        totalPoint += victoire + rock
                    case 'Y' :
                        totalPoint += defaite + paper
                    case 'Z' :
                        totalPoint += egalite + scissors
    print(totalPoint)   
    print(line)    
    