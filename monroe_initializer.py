import math
import os.path
import numpy as np

path=os.path.join('Monroe-Datapack-Squid-Workshop-1.19.1','data','monroe','functions','classes','spiral','summon','traveller.mcfunction')
n = open(path, "w+")

result = ""

for angle in range(90,450,60):
    for d_angle in np.arange(-5,6.25,1.25):
        result += """execute at @e[tag=spiral_center] run summon minecraft:armor_stand ~{} ~{} ~ {{CustomName:'"spiral_traveller"', CustomNameVisible:1,NoGravity:1,Marker:1,Tags:["spiral_traveller"],Passengers:[{{"id":"minecraft:falling_block",BlockState:{{Name:"minecraft:lime_wool"}},NoGravity:1b,Time:-2147483648,DropItem:0b,HurtEntities:0b,Tags:["spiral_block"]}}]}}\n"""\
            .format(  round(math.cos(  float(angle + d_angle) * math.pi / 180  ), 4)  , \
                      round(math.sin(  float(angle + d_angle) * math.pi / 180  ), 4)  )
    result += "\n"

n.write(result)
n.close()