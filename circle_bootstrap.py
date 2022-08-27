# ###############################
# Configure the circle here 

# Number of arms
num_arm = 72

# Starting radius from the center
rad_init = 4

# The angle in between two adjacent blocks in one arm
ang_res = 1

# Total amount of blocks in the arm width = 2 * half_num_blocks + 1
half_num_blks = 2

# Colours across the arms
colours = ['orange', 'light_blue', 'pink', 'yellow', 'red', 'lime', 'magenta' ]

# Speed of extension
rad_speed = 0.11

#
# ################################



import math
import os.path
import numpy as np



# summon/traveller.mcfunction
path = os.path.join('Monroe-Datapack-Squid-Workshop-1.19.1','data','monroe','functions','classes','circle','summon','traveller.mcfunction')
n = open(path, "w+")

result = ""

for arm_idx in range(0, \
                     num_arm, \
                     1):
    angle = 90 + 360 / num_arm * arm_idx
    for d_angle in np.arange(0 - half_num_blks * ang_res, \
                             half_num_blks * ang_res + ang_res, \
                             ang_res):
        result += """execute at @e[tag=circle_center] run summon minecraft:armor_stand ~{} ~{} ~ {{CustomName:'"circle_traveller"',CustomNameVisible:0,NoGravity:1,Marker:1,Invisible:1,Tags:["circle_traveller","colour_{}"],Passengers:[{{"id":"minecraft:falling_block",BlockState:{{Name:"minecraft:{}_stained_glass",Properties:{{east:"true",west:"true"}}}},NoGravity:1b,Time:-2147483648,DropItem:0b,HurtEntities:0b,Tags:["circle_block"]}}]}}\n""" \
            .format(  f'{round(math.cos(  float(angle + d_angle) * math.pi / 180  ) * rad_init, 4):.4f}'  , \
                      f'{round(math.sin(  float(angle + d_angle) * math.pi / 180  ) * rad_init, 4):.4f}'  , \
                      arm_idx % len(colours)                                                              , \
                      colours[ arm_idx % len(colours) ]                                                   )
    result += "\n"

n.write(result)
n.close()


# travel/tick.mcfunction
path = os.path.join('Monroe-Datapack-Squid-Workshop-1.19.1','data','monroe','functions','classes','circle','travel','tick.mcfunction')
n = open(path, "w+")

result = ""
result += "# setblock\n"
for arm_idx in range(0, \
                     len(colours), \
                     1):
    result += """execute as @e[tag=circle_traveller,tag=colour_{}] at @s facing entity @e[tag=circle_center] feet positioned ~ ~0.5 ~ run setblock ^ ^ ^0.5 {}_stained_glass_pane[east=true,west=true]\n""" \
        .format(  arm_idx % len(colours)             , \
                  colours[ arm_idx % len(colours) ]  )
result += "\n"
result += "# move\n"
result += """execute as @e[tag=circle_traveller] at @s facing entity @e[tag=circle_center] feet run tp @s ^ ^ ^{} ~ ~ \n""" \
    .format(  0 - rad_speed  )
n.write(result)
n.close()



# done
print('Circle: done!')
