import time
import random

i = 0
position = 12
space_before_wall = 10
break_inner_while = 1

print(" "*(space_before_wall) +" "*10  + "START")
print(" "*(space_before_wall) + str(i)+ "|" + " "*(position-1) + "*" + " "*(23-position) + "|" + str(position-12))

"when * is on 0 index or 23 index loop should finish"
while(position > 1  and position < 23):
    
    time.sleep(0.03)
    i += 1
    # making first line not moving
    if(10**break_inner_while == i) : 
        space_before_wall -= 1 
        break_inner_while += 1
        
    position = position + random.choice([1, -1])
    print(" "*space_before_wall + str(i)+ "|" + " "*(position-1) + "*" + " "*(23-position) + "|" + str(position-12))



