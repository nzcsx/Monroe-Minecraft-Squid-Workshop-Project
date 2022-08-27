# ###############################
# Configure the spiral arms here 

# Number of arms
num_arm = 6

# Starting radius from the center
rad_init = 6

# The angle in between two adjacent blocks in one arm
ang_res = 0.5

# Total amount of blocks in the arm width = 2 * half_num_blocks + 1
half_num_blks = 16

# Colours across the arms
colours = ['orange', 'light_blue', 'pink', 'yellow', 'red', 'lime', 'magenta', 'cyan','white']

# Speed of extension
rad_speed = 0.1
tan_speed = 0.1
#
# ################################



import math
import os.path
import numpy as np



# summon/traveller.mcfunction
path = os.path.join('Monroe-Datapack-Squid-Workshop-1.19.1','data','monroe','functions','classes','spiral','summon','traveller.mcfunction')
n = open(path, "w+")

result = ""

for arm_idx in range(0, \
                     num_arm, \
                     1):
    angle = 90 + 360 / num_arm * arm_idx
    for d_angle in np.arange(0 - half_num_blks * ang_res, \
                             half_num_blks * ang_res + ang_res, \
                             ang_res):
        result += """execute at @e[tag=spiral_center] run summon minecraft:armor_stand ~{} ~{} ~ {{CustomName:'"spiral_traveller"',CustomNameVisible:0,NoGravity:1,Marker:1,Invisible:1,Tags:["spiral_traveller","colour_{}"],Passengers:[{{"id":"minecraft:falling_block",BlockState:{{Name:"minecraft:{}_concrete"}},NoGravity:1b,Time:-2147483648,DropItem:0b,HurtEntities:0b,Tags:["spiral_block"]}}]}}\n""" \
            .format(  f'{round(math.cos(  float(angle + d_angle) * math.pi / 180  ) * rad_init, 4):.4f}'  , \
                      f'{round(math.sin(  float(angle + d_angle) * math.pi / 180  ) * rad_init, 4):.4f}'  , \
                      arm_idx % len(colours)                                                              , \
                      colours[ arm_idx % len(colours) ]                                                   )
    result += "\n"

n.write(result)
n.close()



# travel/
# # location_low
path = os.path.join('Monroe-Datapack-Squid-Workshop-1.19.1','data','monroe','functions','classes','spiral','travel','location_low.mcfunction')
n = open(path, "w+")
result = ""
result += "# setblock\n"
for arm_idx in range(0, \
                     num_arm, \
                     1):
    result += """execute at @s[tag=colour_{}] facing entity @e[tag=spiral_center] feet positioned ~ ~0.5 ~ run setblock ~-0.5 ~0.5 ~ {}_wool\n""" \
        .format(  arm_idx % len(colours)             , \
                  colours[ arm_idx % len(colours) ]  )
result += "\n"
result += "# move\n"
result += """execute at @s facing entity @e[tag=spiral_center] feet run tp @s ~{} ~{} ~ 90 -90\n""" \
    .format(  tan_speed      , \
              0 - rad_speed  )
n.write(result)
n.close()

# # location_neg
path = os.path.join('Monroe-Datapack-Squid-Workshop-1.19.1','data','monroe','functions','classes','spiral','travel','location_neg.mcfunction')
n = open(path, "w+")
result = ""
result += "# setblock\n"
for arm_idx in range(0, \
                     num_arm, \
                     1):
    result += """execute at @s[tag=colour_{}] facing entity @e[tag=spiral_center] feet positioned ~ ~0.5 ~ run setblock ^ ^0.5 ^0.5 {}_wool\n""" \
        .format(  arm_idx % len(colours)             , \
                  colours[ arm_idx % len(colours) ]  )
result += "\n"
result += "# move\n"
result += """execute at @s facing entity @e[tag=spiral_center] feet run tp @s ^ ^{} ^{} ~ ~\n""" \
    .format(  0 - tan_speed  , \
              0 - rad_speed  )
n.write(result)
n.close()

# # location_pos
path = os.path.join('Monroe-Datapack-Squid-Workshop-1.19.1','data','monroe','functions','classes','spiral','travel','location_pos.mcfunction')
n = open(path, "w+")
result = ""
result += "# setblock\n"
for arm_idx in range(0, \
                     num_arm, \
                     1):
    result += """execute at @s[tag=colour_{}] facing entity @e[tag=spiral_center] feet positioned ~ ~0.5 ~ run setblock ^ ^-0.5 ^0.5 {}_wool\n""" \
        .format(  arm_idx % len(colours)             , \
                  colours[ arm_idx % len(colours) ]  )
result += "\n"
result += "# move\n"
result += """execute at @s facing entity @e[tag=spiral_center] feet run tp @s ^ ^{} ^{} ~ ~\n""" \
    .format(  tan_speed      , \
              0 - rad_speed  )
n.write(result)
n.close()

# # location_upp
path = os.path.join('Monroe-Datapack-Squid-Workshop-1.19.1','data','monroe','functions','classes','spiral','travel','location_upp.mcfunction')
n = open(path, "w+")
result = ""
result += "# setblock\n"
for arm_idx in range(0, \
                     num_arm, \
                     1):
    result += """execute at @s[tag=colour_{}] facing entity @e[tag=spiral_center] feet positioned ~ ~0.5 ~ run setblock ~0.5 ~-0.5 ~ {}_wool\n""" \
        .format(  arm_idx % len(colours)             , \
                  colours[ arm_idx % len(colours) ]  )
result += "\n"
result += "# move\n"
result += """execute at @s facing entity @e[tag=spiral_center] feet run tp @s ~{} ~{} ~ -90 90\n""" \
    .format(  0 - tan_speed  , \
              rad_speed      )
n.write(result)
n.close()



# done
print('Spiral: done!')
