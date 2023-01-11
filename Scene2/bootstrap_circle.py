# ###############################
# Configure the circle here 

# Number of arms
num_arm = 6

# Starting radius from the centre
rad_init = 7

# The angle in between two adjacent blocks in one arm
ang_res = 1

# Total amount of blocks in the arm width = 2 * half_num_blocks + 1
half_num_blks = 25

# Colours across the arms
colours = ['magenta', 'magenta', 'magenta', 'magenta', 'magenta', 'magenta', 'magenta' ]

# Speed of extension
rad_speed = 0.17

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

os.makedirs(os.path.join(path))
os.mkdir(os.path.join(path,'summon'))
os.mkdir(os.path.join(path,'travel'))



# summon/
# # centre
path = os.path.join('Monroe-Datapack-Squid-Workshop-1.19.1','data','monroe','functions','classes','circle','summon','centre.mcfunction')
n = open(path, "w+")

result = "summon marker ~ ~ ~ {Tags:[\"circle_centre\"]}"

n.write(result)
n.close()

# # travellers
path = os.path.join('Monroe-Datapack-Squid-Workshop-1.19.1','data','monroe','functions','classes','circle','summon','travellers.mcfunction')
n = open(path, "w+")
result = ""

for arm_idx in range(0, \
                     num_arm, \
                     1):
    angle = 90 + 360 / num_arm * arm_idx
    for d_angle in np.arange(0 - half_num_blks * ang_res, \
                             half_num_blks * ang_res + ang_res, \
                             ang_res):
        result += """execute at @e[type=marker,tag=circle_centre,limit=1] run summon armor_stand ~{} ~{} ~ {{CustomName:'"circle_traveller"',CustomNameVisible:0,NoGravity:1,Marker:1,Invisible:1,Tags:["circle_traveller","colour_{}"],Passengers:[{{"id":"falling_block",BlockState:{{Name:"{}_concrete",Properties:{{east:"true",west:"true"}}}},NoGravity:1b,Time:-2147483648,DropItem:0b,HurtEntities:0b,Tags:["circle_block"]}}]}}\n""" \
            .format(  f'{round(math.cos(  float(angle + d_angle) * math.pi / 180  ) * rad_init, 4):.4f}'  , \
                      f'{round(math.sin(  float(angle + d_angle) * math.pi / 180  ) * rad_init, 4):.4f}'  , \
                      arm_idx % len(colours)                                                              , \
                      colours[ arm_idx % len(colours) ]                                                   )
    result += "\n"

n.write(result)
n.close()


# travel/
# # tick.mcfunction
path = os.path.join('Monroe-Datapack-Squid-Workshop-1.19.1','data','monroe','functions','classes','circle','travel','tick.mcfunction')
n = open(path, "w+")
result = ""

result += "# setblock for any distance\n"
result += "execute as @e[tag=circle_traveller] at @s positioned ~ ~0.5 ~ facing entity @e[type=marker,tag=circle_centre,limit=1] feet run function monroe:classes/circle/travel/location_any"

result += "\n# fill for 50 meters away\n"
result += "execute at @e[type=marker,tag=circle_centre,limit=1] as @e[tag=circle_traveller,distance=50..] at @s positioned ~ ~0.5 ~ facing entity @e[type=marker,tag=circle_centre,limit=1] feet run function monroe:classes/circle/travel/location_further\n"

result += "\n# move\n"
result += """execute as @e[tag=circle_traveller] at @s facing entity @e[type=marker,tag=circle_centre,limit=1] feet positioned ^ ^ ^{} facing entity @e[type=marker,tag=circle_centre,limit=1] feet run function monroe:classes/circle/travel/move \n""" \
    .format(  0 - rad_speed  )

n.write(result)
n.close()

# # move.mcfunction
path = os.path.join('Monroe-Datapack-Squid-Workshop-1.19.1','data','monroe','functions','classes','circle','travel','move.mcfunction')
n = open(path, "w+")

result = "# move\n"
result += "tp @s ~ ~ ~ ~ ~ \n\n"

result += "# adjust rotation\n"
result += "execute as @s[y_rotation=0] run tp @s ~ ~ ~ 90 ~\n"
result += "execute as @s[y_rotation=180] run tp @s ~ ~ ~ 90 ~\n"

n.write(result)
n.close()

# # location_any.mcfunction
path = os.path.join('Monroe-Datapack-Squid-Workshop-1.19.1','data','monroe','functions','classes','circle','travel','location_any.mcfunction')
n = open(path, "w+")

result = "# setblock for any distance\n"
for arm_idx in range(0, \
                     len(colours), \
                     1):
    result += """execute as @s[tag=colour_{}] run setblock ^ ^ ^0.2 {}_wool keep\n""" \
        .format(  arm_idx % len(colours)             , \
                  colours[ arm_idx % len(colours) ]  )

n.write(result)
n.close()

# # location_further.mcfunction
path = os.path.join('Monroe-Datapack-Squid-Workshop-1.19.1','data','monroe','functions','classes','circle','travel','location_further.mcfunction')
n = open(path, "w+")

result = "# fill for 50 meters away\n"
for arm_idx in range(0, \
                     len(colours), \
                     1):
    result += """execute as @s[tag=colour_{}] run fill ^ ^ ^0.2 ^ ^-0.6 ^0.2 {}_wool keep\n""" \
        .format(  arm_idx % len(colours)             , \
                  colours[ arm_idx % len(colours) ]  )    

n.write(result)
n.close()

# done
print('Circle: done!')
