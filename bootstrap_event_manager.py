# ###############################
# Configure the event here 

spiral_center = "0.5 23.5 -18.5"
#
# ################################



import math
import os.path
import numpy as np
import shutil



# Make dir structure
path = os.path.join('Monroe-Datapack-Squid-Workshop-1.19.1','data','monroe','functions','classes','event_manager')
if os.path.isdir(path):
    shutil.rmtree(path)
os.mkdir(os.path.join(path))

# summon
path = os.path.join('Monroe-Datapack-Squid-Workshop-1.19.1','data','monroe','functions','classes','event_manager','summon.mcfunction')
n = open(path, "w+")
result = ""

result += """execute positioned {} run function monroe:classes/spiral/summon/centre""" \ 
    .format(spiral_center);

result += "function monroe:classes/spiral/summon/traveller";

result += """execute positioned {} run function monroe:classes/ /summon/centre""" \ 
    .format(spiral_center);


n.write(result)
n.close()
