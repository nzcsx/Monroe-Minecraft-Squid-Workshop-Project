
# move coordinates
execute positioned ^ ^0.25 ^0.005 facing entity @e[type=marker,tag=ring_ccw_centre,limit=1] feet run tp @s ~ ~ ~ 0 ~

# move poses
execute at @s run function monroe:classes/ring_ccw/travel/poses/check_location

# re-adjust z coordinate
execute store result entity @s Pos[2] double 0.0001 run scoreboard players get z_centre_ring_ccw monroe