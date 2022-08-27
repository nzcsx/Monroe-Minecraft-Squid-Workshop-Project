# ###############################
# Configure the spiral arms here 

# Number of arms
num_arm = 6

# The angle in between two adjacent blocks in one arm
ang_res = 1

# Total amount of blocks in the arm width = 2 * half_num_blocks + 1
half_num_blks = 10

# Colours across the arms
colours = ['orange', 'light_blue', 'pink', 'yellow', 'red', 'lime', 'magenta', 'cyan','white']

# Speed of summon
summon_speed = 1
#
# ################################



import math
import os.path
import numpy as np



# summon/traveller.mcfunction

path_prefix = os.path.join('Monroe-Summon-Display-Datapack-Squid-Workshop-1.19.1','data','monroe','functions','classes','spiral','summon')

# # traveller.mcfunction
path = os.path.join(path_prefix, """traveller.mcfunction""")
n = open(path, "w+")
result = """schedule function monroe:classes/spiral/summon/traveller_0 {}t""" \
    .format(summon_speed)
n.write(result)
n.close()

# # traveller_{}.mcfunction
blk_cnt = 0;
for arm_idx in range(0, \
                     num_arm, \
                     1):
    angle = 90 + 360 / num_arm * arm_idx
    for d_angle in np.arange(0 - half_num_blks * ang_res, \
                             half_num_blks * ang_res + ang_res, \
                             ang_res):
        path = os.path.join(path_prefix, """traveller_{}.mcfunction""".format(blk_cnt))
        n = open(path, "w+")
        
        result = ""
        result += """execute at @e[tag=spiral_center] run summon minecraft:armor_stand ~{} ~{} ~ {{CustomName:'"spiral_traveller"',CustomNameVisible:0,NoGravity:1,Marker:1,Invisible:0,Tags:["spiral_traveller","colour_{}"],Passengers:[{{"id":"minecraft:falling_block",BlockState:{{Name:"minecraft:{}_concrete"}},NoGravity:1b,Time:-2147483648,DropItem:0b,HurtEntities:0b,Tags:["spiral_block"]}}]}}\n""" \
            .format(  f'{round(math.cos(  float(angle + d_angle) * math.pi / 180  ) * 5, 4):.4f}'  , \
                      f'{round(math.sin(  float(angle + d_angle) * math.pi / 180  ) * 5, 4):.4f}'  , \
                      arm_idx                                                                      , \
                      colours[arm_idx]                                                             )
        result += """schedule function monroe:classes/spiral/summon/traveller_{} {}t""" \
            .format(blk_cnt+1   , \
                    summon_speed)
        
        blk_cnt += 1
        
        n.write(result)
        n.close()

path = os.path.join(path_prefix, """traveller_{}.mcfunction""".format(blk_cnt))
n = open(path, "w+")
result = ""
n.write(result)
n.close()

# done
print('done!')
