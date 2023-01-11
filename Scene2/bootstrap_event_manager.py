# ###############################
# Configure the event here 

circle_centre = "0.5 23.5 -21.5"
circle2_centre =  "0.5 23.5 -19.5"
spiral_center = "0.5 30.5 -18.5"

circle_delay = 20
circle2_delay = 0
spiral_delay = 280
spiral_stop  = 90 + spiral_delay

#
# ################################



import math
import os.path
import numpy as np
import shutil



# Make dir structure
path = os.path.join('Monroe-Datapack-Squid-Workshop-1.19.1','data','app','functions','monroe_event_manager')
if os.path.isdir(path):
    shutil.rmtree(path)
os.makedirs(path)



# summon
path = os.path.join('Monroe-Datapack-Squid-Workshop-1.19.1','data','app','functions','monroe_event_manager','summon.mcfunction')
n = open(path, "w+")
result = ""

result += """execute positioned {} run function monroe:classes/circle/summon/centre\n""" \
    .format(circle_centre)
result += "function monroe:classes/circle/summon/travellers\n"

result += """execute positioned {} run function monroe:classes/circle2/summon/centre\n""" \
    .format(circle2_centre)
result += "function monroe:classes/circle2/summon/travellers\n"

result += """execute positioned {} run function monroe:classes/spiral/summon/centre\n""" \
    .format(spiral_center)
result += "function monroe:classes/spiral/summon/travellers\n"

n.write(result)
n.close()



# tick
path = os.path.join('Monroe-Datapack-Squid-Workshop-1.19.1','data','app','functions','monroe_event_manager','tick.mcfunction')
n = open(path, "w+")
result = ""

if (circle_delay):
    result += """execute if score tick monroe matches {}.. run function monroe:classes/circle/travel/tick\n"""\
        .format(circle_delay)
else:
    result += "function monroe:classes/circle/travel/tick\n"

if (circle2_delay):
    result += """execute if score tick monroe matches {}.. run function monroe:classes/circle2/travel/tick\n"""\
        .format(circle2_delay) 
else:
    result += "function monroe:classes/circle2/travel/tick\n"
    
if (spiral_delay):
    result += """execute if score tick monroe matches {}..{} run function monroe:classes/spiral/travel/tick\n"""\
        .format(spiral_delay,
                spiral_stop)
else:
    result += "function monroe:classes/spiral/travel/tick\n"

result += "scoreboard players add tick monroe 1"

n.write(result)
n.close()



# reload
path = os.path.join('Monroe-Datapack-Squid-Workshop-1.19.1','data','app','functions','monroe_event_manager','reload.mcfunction')
n = open(path, "w+")

result = "function monroe:classes/main/load"

n.write(result)
n.close()



# done
print('Event_manager: done!')