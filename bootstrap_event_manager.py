# ###############################
# Configure the event here 

#
# ################################



import math
import os.path
import numpy as np
import shutil



# Make dir structure
path = os.path.join('Monroe-Datapack-Squid-Workshop-1.19.1','data','monroe','functions','classes','circle')
if os.path.isdir(path):
    shutil.rmtree(path)

os.mkdir(os.path.join(path))
os.mkdir(os.path.join(path,'summon'))
os.mkdir(os.path.join(path,'travel'))
