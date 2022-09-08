summon marker ~ ~ ~ {Tags:["spiral_centre"]}
execute store result score x_centre_spiral monroe run data get entity @e[type=marker,tag=spiral_centre,limit=1] Pos[0] 10000
execute store result score y_centre_spiral monroe run data get entity @e[type=marker,tag=spiral_centre,limit=1] Pos[1] 10000
execute store result score z_centre_spiral monroe run data get entity @e[type=marker,tag=spiral_centre,limit=1] Pos[2] 10000

