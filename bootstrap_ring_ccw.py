# ###############################
# Configure the ring_ccw arms here 

# Number of arms
num_arm = 40

# Starting radius from the centre
rad_init = 6

# The angle in between two adjacent blocks in one arm
ang_res = 1

# Total amount of blocks in the arm width = 2 * half_num_blocks + 1
half_num_blks = 4

# Colours across the arms
colours = ['orange', 'light_blue', 'pink', 'yellow', 'red', 'lime', 'magenta', 'cyan','white']

# Speed of extension
rad_speed = -0.05
tan_speed = 1.5
#
# ################################



import math
import os.path
import numpy as np



# summon/
# # centre
path = os.path.join('Monroe-Datapack-Squid-Workshop-1.19.1','data','monroe','functions','classes','ring_ccw','summon','centre.mcfunction')
n = open(path, "w+")

result = "summon minecraft:armor_stand ~ ~ ~ {CustomName:\'\"ring_ccw_centre\"\', CustomNameVisible:1,NoGravity:1,Marker:1,Tags:[\"ring_ccw_centre\"]}"

n.write(result)
n.close()

# # traveller
path = os.path.join('Monroe-Datapack-Squid-Workshop-1.19.1','data','monroe','functions','classes','ring_ccw','summon','traveller.mcfunction')
n = open(path, "w+")
result = ""

for arm_idx in range(0, \
                     num_arm, \
                     1):
    angle = 90 + 360 / num_arm * arm_idx
    for d_angle in np.arange(0 - half_num_blks * ang_res, \
                             half_num_blks * ang_res + ang_res, \
                             ang_res):
        result += """execute at @e[tag=ring_ccw_centre] run summon minecraft:armor_stand ~{} ~{} ~ {{CustomName:'"ring_ccw_traveller"',CustomNameVisible:0,NoGravity:1,Marker:1,Invisible:1,Tags:["ring_ccw_traveller","colour_{}"],ArmorItems:[{{}},{{}},{{}},{{id:"{}_concrete",Count:1b}}],Pose:{{Head:[90f,0f,0f]}}}}\n""" \
            .format(  f'{round(math.cos(  float(angle + d_angle) * math.pi / 180  ) * rad_init, 4):.4f}'  , \
                      f'{round(math.sin(  float(angle + d_angle) * math.pi / 180  ) * rad_init, 4):.4f}'  , \
                      arm_idx % len(colours)                                                              , \
                      colours[ arm_idx % len(colours) ]                                                   )
    result += "\n"

n.write(result)
n.close()



# travel/
# # tick
path = os.path.join('Monroe-Datapack-Squid-Workshop-1.19.1','data','monroe','functions','classes','ring_ccw','travel','tick.mcfunction')
n = open(path, "w+")

result = "# travel\n"
result += "execute store result score x_centre monroe run data get entity @e[tag=ring_ccw_centre,limit=1] Pos[0] 10000\n"
result += "execute store result score y_centre monroe run data get entity @e[tag=ring_ccw_centre,limit=1] Pos[1] 10000\n\n"
result += "execute as @e[tag=ring_ccw_traveller] run function monroe:classes/ring_ccw/travel/coords_xyz/check_location"

n.write(result)
n.close()



# travel/coords_xyz/
# # check_location
path = os.path.join('Monroe-Datapack-Squid-Workshop-1.19.1','data','monroe','functions','classes','ring_ccw','travel','coords_xyz','check_location.mcfunction')
n = open(path, "w+")
result = ""

result += "execute store result score x_traveller monroe run data get entity @s Pos[0] 10000\n"
result += "execute store result score y_traveller monroe run data get entity @s Pos[1] 10000\n\n"
result += "# x_traveller <  x_centre\n"
result += "execute if score x_traveller monroe < x_centre monroe run function monroe:classes/ring_ccw/travel/coords_xyz/location_neg\n"
result += "# x_traveller == x_centre &&  y_travaller >  y_centre\n"
result += "execute if score x_traveller monroe = x_centre monroe if score y_traveller monroe > y_centre monroe run function monroe:classes/ring_ccw/travel/coords_xyz/location_upp\n"
result += "# x_traveller >  x_centre\n"
result += "execute if score x_traveller monroe > x_centre monroe run function monroe:classes/ring_ccw/travel/coords_xyz/location_pos\n"
result += "# x_traveller == x_centre && y_travaller <  y_centre\n"
result += "execute if score x_traveller monroe = x_centre monroe if score y_traveller monroe < y_centre monroe run function monroe:classes/ring_ccw/travel/coords_xyz/location_low"

n.write(result)
n.close()

# # location_low
path = os.path.join('Monroe-Datapack-Squid-Workshop-1.19.1','data','monroe','functions','classes','ring_ccw','travel','coords_xyz','location_low.mcfunction')
n = open(path, "w+")
result = ""

result += "# move coordinates\n"
result += """execute at @s facing entity @e[tag=ring_ccw_centre] feet positioned ^ ^{} ^{} facing entity @e[tag=ring_ccw_centre] feet run tp @s ~ ~ ~ 0 ~\n""" \
    .format(  tan_speed      , \
              0 - rad_speed  )

result += "\n# move poses\n"
result += """execute at @s facing entity @e[tag=ring_ccw_centre] feet positioned ^ ^{} ^{} run function monroe:classes/ring_ccw/travel/coords_rot/check_location\n""" \
    .format(  tan_speed      , \
              0 - rad_speed  )

result += "\n# re-adjust z coordinate\n"
result += "data modify entity @s Pos[2] set from entity @e[tag=ring_ccw_centre,limit=1] Pos[2]"

n.write(result)
n.close()

# # location_neg
path = os.path.join('Monroe-Datapack-Squid-Workshop-1.19.1','data','monroe','functions','classes','ring_ccw','travel','coords_xyz','location_neg.mcfunction')
n = open(path, "w+")
result = ""

result += "\n# move coordinates\n"
result += """execute at @s facing entity @e[tag=ring_ccw_centre] feet positioned ^ ^{} ^{} facing entity @e[tag=ring_ccw_centre] feet run tp @s ~ ~ ~ 0 ~\n""" \
    .format(  0 - tan_speed  , \
              0 - rad_speed  )

result += "\n# move poses\n"
result += """execute at @s facing entity @e[tag=ring_ccw_centre] feet positioned ^ ^{} ^{} run function monroe:classes/ring_ccw/travel/coords_rot/check_location\n""" \
    .format(  0 - tan_speed  , \
              0 - rad_speed  )

result += "\n# re-adjust z coordinate\n"
result += "data modify entity @s Pos[2] set from entity @e[tag=ring_ccw_centre,limit=1] Pos[2]"

n.write(result)
n.close()

# # location_pos
path = os.path.join('Monroe-Datapack-Squid-Workshop-1.19.1','data','monroe','functions','classes','ring_ccw','travel','coords_xyz','location_pos.mcfunction')
n = open(path, "w+")
result = ""
    
result += "\n# move coordinates\n"
result += """execute at @s facing entity @e[tag=ring_ccw_centre] feet positioned ^ ^{} ^{} facing entity @e[tag=ring_ccw_centre] feet run tp @s ~ ~ ~ 0 ~\n""" \
    .format(  tan_speed      , \
              0 - rad_speed  )

result += "\n# move poses\n"
result += """execute at @s facing entity @e[tag=ring_ccw_centre] feet positioned ^ ^{} ^{} run function monroe:classes/ring_ccw/travel/coords_rot/check_location\n""" \
    .format(  tan_speed      , \
              0 - rad_speed  )

result += "\n# re-adjust z coordinate\n"
result += "data modify entity @s Pos[2] set from entity @e[tag=ring_ccw_centre,limit=1] Pos[2]"

n.write(result)
n.close()

# # location_upp
path = os.path.join('Monroe-Datapack-Squid-Workshop-1.19.1','data','monroe','functions','classes','ring_ccw','travel','coords_xyz','location_upp.mcfunction')
n = open(path, "w+")
result = ""

result += "\n# move coordinates\n"
result += """execute at @s facing entity @e[tag=ring_ccw_centre] feet positioned ^ ^{} ^{} facing entity @e[tag=ring_ccw_centre] feet run tp @s ~ ~ ~ 0 ~\n""" \
    .format(  0 - tan_speed  , \
              rad_speed      )

result += "\n# move poses\n"
result += """execute at @s facing entity @e[tag=ring_ccw_centre] feet positioned ^ ^{} ^{} run function monroe:classes/ring_ccw/travel/coords_rot/check_location\n""" \
    .format(  0 - tan_speed  , \
              rad_speed      )

result += "\n# re-adjust z coordinate\n"
result += "data modify entity @s Pos[2] set from entity @e[tag=ring_ccw_centre,limit=1] Pos[2]"

n.write(result)
n.close()



# travel/coords_rot/
# # check_location
path = os.path.join('Monroe-Datapack-Squid-Workshop-1.19.1','data','monroe','functions','classes','ring_ccw','travel','coords_rot','check_location.mcfunction')
n = open(path, "w+")
result = ""

result += "summon minecraft:armor_stand ~ ~ ~ {CustomName:\'\"ring_ccw_holder\"\', CustomNameVisible:0,NoGravity:1,Marker:0,Invisible:1,Tags:[\"ring_ccw_holder\"]}\n"
result += "execute store result score x_holder monroe run data get entity @e[tag=ring_ccw_holder,limit=1] Pos[0] 10000\n"
result += "execute store result score y_holder monroe run data get entity @e[tag=ring_ccw_holder,limit=1] Pos[1] 10000\n"
result += "kill @e[tag=ring_ccw_holder]\n\n"
result += "# x_holder <  x_centre\n"
result += "execute if score x_holder monroe < x_centre monroe run function monroe:classes/ring_ccw/travel/coords_rot/location_neg\n"
result += "# x_holder == x_centre &&  y_holder >  y_centre\n"
result += "execute if score x_holder monroe = x_centre monroe if score y_holder monroe > y_centre monroe run function monroe:classes/ring_ccw/travel/coords_rot/location_upp\n"
result += "# x_holder >  x_centre\n"
result += "execute if score x_holder monroe > x_centre monroe run function monroe:classes/ring_ccw/travel/coords_rot/location_pos\n"
result += "# x_holder == x_centre && y_holder <  y_centre\n"
result += "execute if score x_holder monroe = x_centre monroe if score y_holder monroe < y_centre monroe run function monroe:classes/ring_ccw/travel/coords_rot/location_low"

n.write(result)
n.close()

# # location_low
path = os.path.join('Monroe-Datapack-Squid-Workshop-1.19.1','data','monroe','functions','classes','ring_ccw','travel','coords_rot','location_low.mcfunction')
n = open(path, "w+")

result = "data modify entity @s Pose.Head[2] set value -90f\n"

n.write(result)
n.close()

# # location_neg
path = os.path.join('Monroe-Datapack-Squid-Workshop-1.19.1','data','monroe','functions','classes','ring_ccw','travel','coords_rot','location_neg.mcfunction')
n = open(path, "w+")

result = "execute store result entity @s Pose.Head[2] float 1 run data get entity @s Rotation[1]"

n.write(result)
n.close()

# # location_pos
path = os.path.join('Monroe-Datapack-Squid-Workshop-1.19.1','data','monroe','functions','classes','ring_ccw','travel','coords_rot','location_pos.mcfunction')
n = open(path, "w+")

result = "execute store result entity @s Pose.Head[2] float -1 run data get entity @s Rotation[1]"

n.write(result)
n.close()

# # location_upp
path = os.path.join('Monroe-Datapack-Squid-Workshop-1.19.1','data','monroe','functions','classes','ring_ccw','travel','coords_rot','location_upp.mcfunction')
n = open(path, "w+")

result = "data modify entity @s Pose.Head[2] set value 90f\n"

n.write(result)
n.close()



# done
print('ring_ccw: done!')
