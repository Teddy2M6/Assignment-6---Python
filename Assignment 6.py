x = int(input("Enter a number: "))

D = [1]

for i in range(x-1):
    y = D[i] + 2
    D.append(y)

counter = 0 
elem = 4 / D[0]

for j in range(len(D)):
    if (j != len(D)-1):
        z = 4/D[j+1]
        if (counter%2 == 0):    
            elem = elem - z
            counter += 1
        else:
            elem = elem + z
            counter += 1

print("The value of pi for ",x," value is ",elem)
            
            

    

        
        



    

