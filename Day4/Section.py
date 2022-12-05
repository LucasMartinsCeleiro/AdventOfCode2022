sections = 'F:\Python\PROJECT\AdventOfCode2022\Day4\input.txt'

with open(sections) as file :
    for line in file :
        half1 = line.split(',')
        print(half1[1])