sections = 'F:\Python\PROJECT\AdventOfCode2022\Day4\input.txt'
cpt = 0
with open(sections) as file :
    for line in file :
        half = line.split(',')
        print(half[0])
        print(half[1])

        # Utilisation de split() pour séparer les deux nombres
        numbers1 = half[0].split("-")
        numbers2 = half[1].split("-")

        # Conversion des nombres en entiers
        start1 = int(numbers1[0])
        end1 = int(numbers1[1])
        
        start2 = int(numbers2[0])
        end2 = int(numbers2[1])

        # Utilisation de range() pour générer une liste de valeurs
        values1 = list(range(start1, end1 + 1))
        values2 = list(range(start2, end2 + 1))

        # Vérification du nombre d'éléments dans les listes
        if len(values1) <= len(values2):
            # Utilisation de in et all() pour vérifier si tous les éléments de list1 sont présents dans list2
            result = any(x in values2 for x in values1)
            if result == True :
                cpt+=1
        else :
            result = any(x in values1 for x in values2)
            if result == True :
                cpt+=1
    print (cpt)