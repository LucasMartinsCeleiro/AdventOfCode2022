signal_input = "F:\\Python\\PROJECT\\AdventOfCode2022\\Day6\\input.txt"

with open(signal_input, "r") as file :
    for char in file :
    
        def isolate_14(list):
            i=0
            output =[]

            while i < len(list) :
                output.append(list[i:i+14])
                i+=1
            return output
        
        def check_similar_char(list):
            cpt =0
            for group in list:
                cpt+=1
                if len(set(group)) == len(group):
                    print("SYSTEM DETECTED AT : ") 
                    print(cpt+13)
                    break
                
                
                
            
        groups = []
        groups = isolate_14(char)
        print(groups)
        check_similar_char(groups)
            
