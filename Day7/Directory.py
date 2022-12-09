directory_input = "F:\\Python\\PROJECT\\AdventOfCode2022\\Day7\\input.txt"

def change_directory(commandcd):
    match commandcd:
        case "x":
            print("")
        case "..":
            print("")
        case "/" :
            print("")
    
    
def list(commandls):
    match commandls :
        case " ":
            print(" ")
    print(" ")


with open(directory_input) as file :
    for line in file : 
        print(line)