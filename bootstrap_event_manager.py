# ###############################
# Configure the event here 

spiral_center = "0.5 23.5 -18.5"
circle_center = "0.5 23.5 -20.5"
ring_ccw_center = "0.5 28.5 90.5"

spiral_delay = 0
circle_delay = 256
ring_ccw_delay = 288

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

result += """execute positioned {} run function monroe:classes/spiral/summon/centre\n""" \
    .format(spiral_center)

result += "function monroe:classes/spiral/summon/travellers\n"

result += """execute positioned {} run function monroe:classes/circle/summon/centre\n""" \
    .format(circle_center)

result += "function monroe:classes/circle/summon/travellers\n"

result += """execute positioned {} run function monroe:classes/ring_ccw/summon/centre\n""" \
    .format(ring_ccw_center)

result += "function monroe:classes/ring_ccw/summon/travellers\n"

n.write(result)
n.close()



# tick
path = os.path.join('Monroe-Datapack-Squid-Workshop-1.19.1','data','app','functions','monroe_event_manager','tick.mcfunction')
n = open(path, "w+")
result = ""

if (spiral_delay):
    result += """execute if score tick monroe matches {}.. function monroe:classes/spiral/travel/tick\n"""\
        .format(spiral_delay)
else:
    result += "function monroe:classes/spiral/travel/tick\n"

if (circle_delay):
    result += """execute if score tick monroe matches {}.. run function monroe:classes/circle/travel/tick\n"""\
        .format(circle_delay) 
else:
    result += "function monroe:classes/circle/travel/tick\n"

if (ring_ccw_delay):
    result += """execute if score tick monroe matches 288.. run function monroe:classes/ring_ccw/travel/tick\n"""\
        .format(ring_ccw_delay) 
else:
    result += "function monroe:classes/ring_ccw/travel/tick\n"

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