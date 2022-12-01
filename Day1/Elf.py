somme=0
max = 0
second = 0
third = 0
while somme!=-1:
    try:
        while True :
            somme += int(input())
    except :
        if somme > max :
            max = somme
        if somme > second and somme < max :
            second = somme
        if somme > third and somme < second :
            third = somme
        somme = 0
    print ("max : "+str(max))
    print ("second max : "+str(second))
    print ("third max : "+str(third))
    print ("total last 3 : "+str(max + second + third))
    
        
    