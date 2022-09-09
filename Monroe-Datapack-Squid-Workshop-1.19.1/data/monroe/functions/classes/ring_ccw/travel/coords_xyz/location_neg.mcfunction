
# move coordinates
execute at @s facing entity @e[type=marker,tag=ring_ccw_centre,limit=1] feet positioned ^ ^-1.5 ^0.05 facing entity @e[type=marker,tag=ring_ccw_centre,limit=1] feet run tp @s ~ ~ ~ 0 ~

# move poses
execute at @s facing entity @e[type=marker,tag=ring_ccw_centre,limit=1] feet positioned ^ ^-1.5 ^0.05 run function monroe:classes/ring_ccw/travel/coords_rot/check_location

# re-adjust z coordinate
execute store result entity @s Pos[2] double 0.0001 run scoreboard players get z_centre_ring_ccw monroe