from msilib.schema import Directory
import os
from time import time

# Using readlines()
file1 = open('edge combine results 2024.txt', 'r')
file2 = open('edge all pro.txt', 'r')

Lines = file1.readlines()
average_allpro = file2.readlines()
  
count = 0
Combine_results = []
allpro_combine = []


# Strips the newline character
for line in Lines:
    Combine_results.append(line)

for line2 in average_allpro:
    allpro_combine.append(line2)
    

average_for_allpro = []
Combine_line = []
player_comparison = []
ideal_traits = []
#Combine_line = Combine_results[2].split('\t')
#print(Combine_results)

average_for_allpro = allpro_combine[11].split('\t')
#print(average_for_allpro[1])
for player in Combine_results:
    Combine_line = player.rstrip('\n').split('\t')
    #print(Combine_line)
    print(Combine_line)
    if (Combine_line[0] == 'Name' ):
        continue
    
    initial_height = Combine_line[5].split('-')
    #print(len(initial_height))
    feet = int(initial_height[0])
    inches = int(initial_height[1])
    height = float(feet*12 + inches)
    
    #height = round(int(Combine_line[4]), -1) 
    #print(height)
    arm_length = float(Combine_line[6]) / 100
    
    #if Combine_line[14] == '--':
    #    broad_jump = 10.03
    #else:
        #r = Combine_line[13] %
    #    broad_jump = (float(Combine_line[14])) /100
    
    #if Combine_line[9] == '--':
    #    yd_dash = 4.463333333
    #else:
        #r = Combine_line[13] %
    #    yd_dash = float(Combine_line[9]) 
    
    #if Combine_line[13] == '--':
    #    vert = 37.16666667
    #else:
        #r = Combine_line[13] %
    #    vert = float(Combine_line[13]) 
    
    #hand = float(Combine_line[5]) / 100
    
    
    int_avg1 = float(average_for_allpro[1])
    int_avg2 = float(average_for_allpro[2])
    float_avg3 = float(average_for_allpro[3])
    float_avg4 = float(average_for_allpro[4])
    float_avg5 = float(average_for_allpro[5])
    float_avg6 = float(average_for_allpro[6])
    float_avg7 = 10.03
    
    weight = int(Combine_line[6])
    #print(int_avg1)
    #print(type(height))
    #print()
    #print(float_avg5)
    #print(yd_dash)
    if((int_avg1 -1 <= height <= int_avg1+2)
       and ((int_avg2 -5.00)  <= weight <= (int_avg2+10.00))
       #and ((float_avg3 -2) <= arm_length <= (float_avg3 + 5))
       #and ((float_avg4 - 1.0) <= hand <= (float_avg4+2.0))
       #and ((float_avg5 - 1) <= yd_dash <= (float_avg5+.05))
       #and ((float_avg6 - 1.0) <= vert <= (float_avg6+10.0))
       #and ((float_avg7 - .5) <= broad_jump <= (float_avg7+1.0))
       ):
        player_comparison.append(player)
        
    

for i in player_comparison:
    print(i)

#print(len(player_comparison))

with open('edge_results2024.txt', 'w') as f:
    for line in player_comparison:
        f.write(f"{line}\n")
#print(len(player_comparison))





    
