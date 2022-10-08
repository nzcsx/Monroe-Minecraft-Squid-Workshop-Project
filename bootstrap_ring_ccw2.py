# ###############################
# Configure the ring_ccw2 arms here 

# Number of arms
num_arm = 20

# Starting radius from the centre
rad_init = 7.2

# The angle in between two adjacent blocks in one arm
ang_res = 3.3

# Total amount of blocks in the arm width = 2 * half_num_blocks + 1
half_num_blks = 2

# Colours across the arms
colours = ['orange', 'light_blue', 'pink', 'yellow', 'red', 'lime', 'magenta', 'cyan','white']

# Speed of extension
rad_speed = -0.005
tan_speed = 0.27
#
# ################################



import math
import os.path
import numpy as np
import shutil



# Make dir structure
path = os.path.join('Monroe-Datapack-Squid-Workshop-1.19.1','data','monroe','functions','classes','ring_ccw2')
if os.path.isdir(path):
    shutil.rmtree(path)

os.mkdir(os.path.join(path))
os.mkdir(os.path.join(path,'summon'))
os.mkdir(os.path.join(path,'travel'))
os.mkdir(os.path.join(path,'travel','coords'))
os.mkdir(os.path.join(path,'travel','poses'))



# summon/
# # centre
path = os.path.join('Monroe-Datapack-Squid-Workshop-1.19.1','data','monroe','functions','classes','ring_ccw2','summon','centre.mcfunction')
n = open(path, "w+")

result = "summon marker ~ ~ ~ {Tags:[\"ring_ccw2_centre\"]}\n"
result += "execute store result score x_centre_ring_ccw2 monroe run data get entity @e[type=marker,tag=ring_ccw2_centre,limit=1] Pos[0] 10000\n"
result += "execute store result score y_centre_ring_ccw2 monroe run data get entity @e[type=marker,tag=ring_ccw2_centre,limit=1] Pos[1] 10000\n"
result += "execute store result score z_centre_ring_ccw2 monroe run data get entity @e[type=marker,tag=ring_ccw2_centre,limit=1] Pos[2] 10000\n\n"

n.write(result)
n.close()

# # travellers
path = os.path.join('Monroe-Datapack-Squid-Workshop-1.19.1','data','monroe','functions','classes','ring_ccw2','summon','travellers.mcfunction')
n = open(path, "w+")
result = ""

for arm_idx in range(0, \
                     num_arm, \
                     1):
    angle = 90 + 360 / num_arm * arm_idx
    for d_angle in np.arange(0 - half_num_blks * ang_res, \
                             half_num_blks * ang_res + ang_res, \
                             ang_res):
        result += """execute at @e[type=marker,tag=ring_ccw2_centre,limit=1] run summon minecraft:armor_stand ~{} ~{} ~ {{CustomName:'"ring_ccw2_traveller"',CustomNameVisible:0,NoGravity:1,Marker:1,Invisible:1,Tags:["ring_ccw2_traveller","colour_{}"],ArmorItems:[{{}},{{}},{{}},{{id:"{}_concrete",Count:1b}}],Pose:{{Head:[90f,0f,0f]}}}}\n""" \
            .format(  f'{round(math.cos(  float(angle + d_angle) * math.pi / 180  ) * rad_init, 4):.4f}'  , \
                      f'{round(math.sin(  float(angle + d_angle) * math.pi / 180  ) * rad_init, 4):.4f}'  , \
                      arm_idx % len(colours)                                                              , \
                      colours[ arm_idx % len(colours) ]                                                   )
    result += "\n"

n.write(result)
n.close()



# travel/
# # tick
path = os.path.join('Monroe-Datapack-Squid-Workshop-1.19.1','data','monroe','functions','classes','ring_ccw2','travel','tick.mcfunction')
n = open(path, "w+")

result = "# travel\n"
result += "execute as @e[tag=ring_ccw2_traveller] at @s facing entity @e[type=marker,tag=ring_ccw2_centre,limit=1] feet run function monroe:classes/ring_ccw2/travel/coords/check_location"

n.write(result)
n.close()



# travel/coords/
# # check_location
path = os.path.join('Monroe-Datapack-Squid-Workshop-1.19.1','data','monroe','functions','classes','ring_ccw2','travel','coords','check_location.mcfunction')
n = open(path, "w+")
result = ""

result += "execute store result score x_traveller monroe run data get entity @s Pos[0] 10000\n"
result += "execute store result score y_traveller monroe run data get entity @s Pos[1] 10000\n\n"
result += "# x_traveller <  x_centre\n"
result += "execute if score x_traveller monroe < x_centre_ring_ccw2 monroe run function monroe:classes/ring_ccw2/travel/coords/location_neg\n"
result += "# x_traveller == x_centre &&  y_travaller >  y_centre\n"
result += "execute if score x_traveller monroe = x_centre_ring_ccw2 monroe if score y_traveller monroe > y_centre_ring_ccw2 monroe run function monroe:classes/ring_ccw2/travel/coords/location_upp\n"
result += "# x_traveller >  x_centre\n"
result += "execute if score x_traveller monroe > x_centre_ring_ccw2 monroe run function monroe:classes/ring_ccw2/travel/coords/location_pos\n"
result += "# x_traveller == x_centre && y_travaller <  y_centre\n"
result += "execute if score x_traveller monroe = x_centre_ring_ccw2 monroe if score y_traveller monroe < y_centre_ring_ccw2 monroe run function monroe:classes/ring_ccw2/travel/coords/location_low"

n.write(result)
n.close()

# # location_low
path = os.path.join('Monroe-Datapack-Squid-Workshop-1.19.1','data','monroe','functions','classes','ring_ccw2','travel','coords','location_low.mcfunction')
n = open(path, "w+")
result = ""

result += "# move coordinates\n"
result += """execute positioned ~{} ~{} ~ facing entity @e[type=marker,tag=ring_ccw2_centre,limit=1] feet run tp @s ~ ~ ~ 0 ~\n""" \
    .format(  tan_speed      , \
              0 - rad_speed  )

result += "\n# move poses\n"
result += """execute at @s run function monroe:classes/ring_ccw2/travel/poses/check_location\n""" \
    .format(  tan_speed      , \
              0 - rad_speed  )

result += "\n# re-adjust z coordinate\n"
result += "execute store result entity @s Pos[2] double 0.0001 run scoreboard players get z_centre_ring_ccw2 monroe"

n.write(result)
n.close()

# # location_neg
path = os.path.join('Monroe-Datapack-Squid-Workshop-1.19.1','data','monroe','functions','classes','ring_ccw2','travel','coords','location_neg.mcfunction')
n = open(path, "w+")
result = ""

result += "\n# move coordinates\n"
result += """execute positioned ^ ^{} ^{} facing entity @e[type=marker,tag=ring_ccw2_centre,limit=1] feet run tp @s ~ ~ ~ 0 ~\n""" \
    .format(  0 - tan_speed  , \
              0 - rad_speed  )

result += "\n# move poses\n"
result += """execute at @s run function monroe:classes/ring_ccw2/travel/poses/check_location\n""" \
    .format(  0 - tan_speed  , \
              0 - rad_speed  )

result += "\n# re-adjust z coordinate\n"
result += "execute store result entity @s Pos[2] double 0.0001 run scoreboard players get z_centre_ring_ccw2 monroe"

n.write(result)
n.close()

# # location_pos
path = os.path.join('Monroe-Datapack-Squid-Workshop-1.19.1','data','monroe','functions','classes','ring_ccw2','travel','coords','location_pos.mcfunction')
n = open(path, "w+")
result = ""
    
result += "\n# move coordinates\n"
result += """execute positioned ^ ^{} ^{} facing entity @e[type=marker,tag=ring_ccw2_centre,limit=1] feet run tp @s ~ ~ ~ 0 ~\n""" \
    .format(  tan_speed      , \
              0 - rad_speed  )

result += "\n# move poses\n"
result += """execute at @s run function monroe:classes/ring_ccw2/travel/poses/check_location\n""" \
    .format(  tan_speed      , \
              0 - rad_speed  )

result += "\n# re-adjust z coordinate\n"
result += "execute store result entity @s Pos[2] double 0.0001 run scoreboard players get z_centre_ring_ccw2 monroe"

n.write(result)
n.close()

# # location_upp
path = os.path.join('Monroe-Datapack-Squid-Workshop-1.19.1','data','monroe','functions','classes','ring_ccw2','travel','coords','location_upp.mcfunction')
n = open(path, "w+")
result = ""

result += "\n# move coordinates\n"
result += """execute positioned ~{} ~{} ~ facing entity @e[type=marker,tag=ring_ccw2_centre,limit=1] feet run tp @s ~ ~ ~ 0 ~\n""" \
    .format(  0 - tan_speed  , \
              rad_speed      )

result += "\n# move poses\n"
result += """execute at @s run function monroe:classes/ring_ccw2/travel/poses/check_location\n""" \
    .format(  0 - tan_speed  , \
              rad_speed      )

result += "\n# re-adjust z coordinate\n"
result += "execute store result entity @s Pos[2] double 0.0001 run scoreboard players get z_centre_ring_ccw2 monroe"

n.write(result)
n.close()



# travel/poses/
# # check_location
path = os.path.join('Monroe-Datapack-Squid-Workshop-1.19.1','data','monroe','functions','classes','ring_ccw2','travel','poses','check_location.mcfunction')
n = open(path, "w+")
result = ""

result += "execute store result score x_holder monroe run data get entity @s Pos[0] 10000\n"
result += "execute store result score y_holder monroe run data get entity @s Pos[1] 10000\n\n"
result += "# x_holder <  x_centre\n"
result += "execute if score x_holder monroe < x_centre_ring_ccw2 monroe run function monroe:classes/ring_ccw2/travel/poses/location_neg\n"
result += "# x_holder == x_centre &&  y_travaller >  y_centre\n"
result += "execute if score x_holder monroe = x_centre_ring_ccw2 monroe if score y_holder monroe > y_centre_ring_ccw2 monroe run function monroe:classes/ring_ccw2/travel/poses/location_upp\n"
result += "# x_holder >  x_centre\n"
result += "execute if score x_holder monroe > x_centre_ring_ccw2 monroe run function monroe:classes/ring_ccw2/travel/poses/location_pos\n"
result += "# x_holder == x_centre && y_travaller <  y_centre\n"
result += "execute if score x_holder monroe = x_centre_ring_ccw2 monroe if score y_holder monroe < y_centre_ring_ccw2 monroe run function monroe:classes/ring_ccw2/travel/poses/location_low"

n.write(result)
n.close()

# # location_low
path = os.path.join('Monroe-Datapack-Squid-Workshop-1.19.1','data','monroe','functions','classes','ring_ccw2','travel','poses','location_low.mcfunction')
n = open(path, "w+")

result = "data modify entity @s Pose.Head[2] set value -90f\n"

n.write(result)
n.close()

# # location_neg
path = os.path.join('Monroe-Datapack-Squid-Workshop-1.19.1','data','monroe','functions','classes','ring_ccw2','travel','poses','location_neg.mcfunction')
n = open(path, "w+")

result =  "execute store result score r_holder monroe run data get entity @s Rotation[1] 10000\n"
result += "scoreboard players add r_holder monroe 90000\n"
result += "execute store result entity @s Pose.Head[2] float 0.0001 run scoreboard players get r_holder monroe"

n.write(result)
n.close()

# # location_pos
path = os.path.join('Monroe-Datapack-Squid-Workshop-1.19.1','data','monroe','functions','classes','ring_ccw2','travel','poses','location_pos.mcfunction')
n = open(path, "w+")

result =  "execute store result score r_holder monroe run data get entity @s Rotation[1] -10000\n"
result += "scoreboard players add r_holder monroe 90000\n"
result += "execute store result entity @s Pose.Head[2] float 0.0001 run scoreboard players get r_holder monroe"

n.write(result)
n.close()

# # location_upp
path = os.path.join('Monroe-Datapack-Squid-Workshop-1.19.1','data','monroe','functions','classes','ring_ccw2','travel','poses','location_upp.mcfunction')
n = open(path, "w+")

result = "data modify entity @s Pose.Head[2] set value 90f\n"

n.write(result)
n.close()



# done
print('ring_ccw2: done!')
