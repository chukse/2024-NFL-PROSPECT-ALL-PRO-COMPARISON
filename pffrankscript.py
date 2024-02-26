from msilib.schema import Directory
import os
from time import time

# Using readlines()
#file1 = open('pass rush draft.txt', 'r')
file2 = open('edge all pro 2024 pff .txt', 'r')
#file3 = open('draft names.txt', 'r')
path_ = "C:/Users/chuke/Documents/httpd-2.4.57-win64-VS17/edge compare/Data Folder/"
directory = os.fsencode(path_)

#go through folder and create of all files under 12 characters
file_list = []
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    
    filename = str(filename) 
    #print(filename)
        #print(file)
    if len(filename) != 'Null':
        test = path_ + filename
        stripped_line = test.rstrip()
        test = stripped_line
         
        file_list.append(test)
#print(file_list)

#Lines = file1.readlines()
average_allpro = file2.readlines()
#draft_names = file3.readlines() 
count = 0
combine_pffstats = []
allpro_combine = []
names = []


# Strips the newline character
#for line in Lines:
#    combine_pffstats.append(line)
for line2 in average_allpro:
    allpro_combine.append(line2)


average_for_allpro = []
Combine_line = []
player_comparison = []
average_for_allpro = allpro_combine[1].split('\t')
ideal_traits = []
for f in file_list:
    file1 = open(f, 'r')
    Lines = file1.readlines()
    for player in Lines:
        #print(player)
        Combine_line = player.rstrip('\n').split(',')
        #print(Combine_line)
        
        if (Combine_line[0] == 'player' ):
            continue
        
        else:
    


    

            pass_rush_grade = float(Combine_line[8])
    
    #print(true_prgrade)
            if(Combine_line[13]== ''):
                win_rate == float_avg_winr
            else:
                win_rate = float(Combine_line[13])
                
            #print(win_rate)
            #print(win_rate)
            if(Combine_line[16]== ''):
                prp == float_avg_prp
            else:
                prp = float(Combine_line[16])
            
            Total_pressures = float(Combine_line[20])
            
            if(Combine_line[26]== ''):
                tps_win_rate == float_avg_tpswin
            else:
                tps_win_rate = float(Combine_line[26])
                
            if(Combine_line[28]== ''):
                tps_prp == float_avg_tps_prp
            else:    
                tps_prp = float(Combine_line[28])
            
            tps_totpress = float(Combine_line[32])

            #average of all pro pff stats from college
            float_avg_prg = float(average_for_allpro[8])
            print(float_avg_prg)
            float_avg_winr = float(average_for_allpro[13])
            float_avg_prp = float(average_for_allpro[16])   
            float_avg_totpress = float(average_for_allpro[20])
            float_avg_tpswin = float(average_for_allpro[26])
            float_avg_tps_prp = float(average_for_allpro[28])
            float_avg_tps_totpress = float(average_for_allpro[32])
    
    
    
            
    

    

            if((float_avg_prg -4 <= pass_rush_grade <= float_avg_prg +6)
                and ((float_avg_winr -2.00)  <= win_rate <= (float_avg_winr+50.00))
                and ((float_avg_prp -5) <= prp)
                and ((float_avg_totpress -5) <= Total_pressures <= (float_avg_totpress + 300))
                and ((float_avg_tpswin -3) <= tps_win_rate <= (float_avg_tpswin + 300))
                and ((float_avg_tps_prp -3) <= tps_prp <= (float_avg_tps_prp + 300))
                and ((float_avg_tps_totpress -3) <= tps_totpress <= (float_avg_tps_totpress + 300))
                and (Combine_line[2] == 'ED')
                #and (Combine_line[33] == '2023' or Combine_line[33] == '2022' )
                ):
                    player_comparison.append(player)
    
    


#for j in names:
    #for i in player_comparison:
        #named = i.split('\t')
        #if j == named[0]:
            #player_comparison.remove(i)


    #final_results = []
    #for i in player_comparison:
    #    named = i.rstrip('\n').split('\t')
    #    for n in names:
    #        na = n.rstrip('\n')
    #        if named[0] == na:
    #            final_results.append(i)

 







      

with open('pff_stats2024.txt', 'w') as f:
    f.write('player	player_id	position	team_name	player_game_count	batted_passes	declined_penalties	franchise_id	grades_pass_rush_defense	hits	hurries	pass_rush_opp	pass_rush_percent	pass_rush_win_rate	pass_rush_wins	penalties	prp	sacks	snap_counts_pass_play	snap_counts_pass_rush	total_pressures	true_pass_set_batted_passes	true_pass_set_grades_pass_rush_defense	true_pass_set_hits	true_pass_set_hurries	true_pass_set_pass_rush_opp	true_pass_set_pass_rush_percent	true_pass_set_pass_rush_win_rate	true_pass_set_pass_rush_wins	true_pass_set_prp	true_pass_set_sacks	true_pass_set_snap_counts_pass_play	true_pass_set_snap_counts_pass_rush	true_pass_set_total_pressures \n')
    for w in player_comparison:
        f.write(w)
        f.write('\n')





        





