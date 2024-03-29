# ###############################
# Configure the spiral arms here 

# Number of arms
num_arm = 6

# Starting radius from the centre
rad_init = 7

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
import shutil



# Make dir structure
path = os.path.join('Monroe-Datapack-Squid-Workshop-1.19.1','data','monroe','functions','classes','spiral')
if os.path.isdir(path):
    shutil.rmtree(path)

os.makedirs(os.path.join(path))
os.mkdir(os.path.join(path,'summon'))
os.mkdir(os.path.join(path,'travel'))



# summon/
# # centre
path = os.path.join('Monroe-Datapack-Squid-Workshop-1.19.1','data','monroe','functions','classes','spiral','summon','centre.mcfunction')
n = open(path, "w+")

result = "summon marker ~ ~ ~ {Tags:[\"spiral_centre\"]}\n"
result += "execute store result score x_centre_spiral monroe run data get entity @e[type=marker,tag=spiral_centre,limit=1] Pos[0] 10000\n"
result += "execute store result score y_centre_spiral monroe run data get entity @e[type=marker,tag=spiral_centre,limit=1] Pos[1] 10000\n"
result += "execute store result score z_centre_spiral monroe run data get entity @e[type=marker,tag=spiral_centre,limit=1] Pos[2] 10000\n\n"

n.write(result)
n.close()

# # travellers
path = os.path.join('Monroe-Datapack-Squid-Workshop-1.19.1','data','monroe','functions','classes','spiral','summon','travellers.mcfunction')
n = open(path, "w+")
result = ""

for arm_idx in range(0, \
                     num_arm, \
                     1):
    angle = 90 + 360 / num_arm * arm_idx
    for d_angle in np.arange(0 - half_num_blks * ang_res, \
                             half_num_blks * ang_res + ang_res, \
                             ang_res):
        result += """execute at @e[type=marker,tag=spiral_centre,limit=1] run summon armor_stand ~{} ~{} ~ {{CustomName:'"spiral_traveller"',CustomNameVisible:0,NoGravity:1,Marker:1,Invisible:1,Tags:["spiral_traveller","colour_{}"],Passengers:[{{"id":"falling_block",BlockState:{{Name:"{}_concrete"}},NoGravity:1b,Time:-2147483648,DropItem:0b,HurtEntities:0b,Tags:["spiral_block"]}}]}}\n""" \
            .format(  f'{round(math.cos(  float(angle + d_angle) * math.pi / 180  ) * rad_init, 4):.4f}'  , \
                      f'{round(math.sin(  float(angle + d_angle) * math.pi / 180  ) * rad_init, 4):.4f}'  , \
                      arm_idx % len(colours)                                                              , \
                      colours[ arm_idx % len(colours) ]                                                   )
    result += "\n"

n.write(result)
n.close()



# travel/
# # tick
path = os.path.join('Monroe-Datapack-Squid-Workshop-1.19.1','data','monroe','functions','classes','spiral','travel','tick.mcfunction')
n = open(path, "w+")

result = "# travel\n"
result += "execute as @e[tag=spiral_traveller] at @s facing entity @e[type=marker,tag=spiral_centre,limit=1] feet run function monroe:classes/spiral/travel/check_location"

n.write(result)
n.close()



# travel/
# # check_location
path = os.path.join('Monroe-Datapack-Squid-Workshop-1.19.1','data','monroe','functions','classes','spiral','travel','check_location.mcfunction')
n = open(path, "w+")
result = ""

result += "execute store result score x_traveller monroe run data get entity @s Pos[0] 10000\n"
result += "execute store result score y_traveller monroe run data get entity @s Pos[1] 10000\n\n"
result += "# x_traveller <  x_centre\n"
result += "execute if score x_traveller monroe < x_centre_spiral monroe run function monroe:classes/spiral/travel/location_neg\n"
result += "# x_traveller == x_centre &&  y_travaller >  y_centre\n"
result += "execute if score x_traveller monroe = x_centre_spiral monroe if score y_traveller monroe > y_centre_spiral monroe run function monroe:classes/spiral/travel/location_upp\n"
result += "# x_traveller >  x_centre\n"
result += "execute if score x_traveller monroe > x_centre_spiral monroe run function monroe:classes/spiral/travel/location_pos\n"
result += "# x_traveller == x_centre && y_travaller <  y_centre\n"
result += "execute if score x_traveller monroe = x_centre_spiral monroe if score y_traveller monroe < y_centre_spiral monroe run function monroe:classes/spiral/travel/location_low"

n.write(result)
n.close()

# # location_low
path = os.path.join('Monroe-Datapack-Squid-Workshop-1.19.1','data','monroe','functions','classes','spiral','travel','location_low.mcfunction')
n = open(path, "w+")
result = ""

result += "# setblock\n"
for arm_idx in range(0, \
                     num_arm, \
                     1):
    result += """execute if entity @s[tag=colour_{}] positioned ~ ~0.5 ~ run setblock ~-0.6 ~0.5 ~ {}_wool keep\n""" \
        .format(  arm_idx % len(colours)             , \
                  colours[ arm_idx % len(colours) ]  )

result += "\n# move\n"
result += """tp @s ~{} ~{} ~ 0 0\n""" \
    .format(  tan_speed      , \
              0 - rad_speed  )

result += "\n# re-adjust z coordinate\n"
result += "execute store result entity @s Pos[2] double 0.0001 run scoreboard players get z_centre_spiral monroe"

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
    result += """execute if entity @s[tag=colour_{}] positioned ~ ~0.5 ~ run setblock ^ ^0.5 ^0.6 {}_wool keep\n""" \
        .format(  arm_idx % len(colours)             , \
                  colours[ arm_idx % len(colours) ]  )

result += "\n# move\n"
result += """tp @s ^ ^{} ^{} 0 0\n""" \
    .format(  0 - tan_speed  , \
              0 - rad_speed  )

result += "\n# re-adjust z coordinate\n"
result += "execute store result entity @s Pos[2] double 0.0001 run scoreboard players get z_centre_spiral monroe"

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
    result += """execute if entity @s[tag=colour_{}] positioned ~ ~0.5 ~ run setblock ^ ^-0.5 ^0.6 {}_wool keep\n""" \
        .format(  arm_idx % len(colours)             , \
                  colours[ arm_idx % len(colours) ]  )
    
result += "\n# move\n"
result += """tp @s ^ ^{} ^{} 0 0\n""" \
    .format(  tan_speed      , \
              0 - rad_speed  )

result += "\n# re-adjust z coordinate\n"
result += "execute store result entity @s Pos[2] double 0.0001 run scoreboard players get z_centre_spiral monroe"

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
    result += """execute if entity @s[tag=colour_{}] positioned ~ ~0.5 ~ run setblock ~0.6 ~-0.5 ~ {}_wool keep\n""" \
        .format(  arm_idx % len(colours)             , \
                  colours[ arm_idx % len(colours) ]  )

result += "\n# move\n"
result += """tp @s ~{} ~{} ~ 0 0\n""" \
    .format(  0 - tan_speed  , \
              rad_speed      )

result += "\n# re-adjust z coordinate\n"
result += "execute store result entity @s Pos[2] double 0.0001 run scoreboard players get z_centre_spiral monroe"

n.write(result)
n.close()



# done
print('Spiral: done!')
