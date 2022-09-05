
# move coordinates
execute at @s facing entity @e[tag=ring_ccw_centre] feet positioned ^ ^-1.5 ^0.05 facing entity @e[tag=ring_ccw_centre] feet run tp @s ~ ~ ~ 0 ~

# move poses
execute at @s facing entity @e[tag=ring_ccw_centre] feet positioned ^ ^-1.5 ^0.05 run function monroe:classes/ring_ccw/travel/coords_rot/check_location

# re-adjust z coordinate
data modify entity @s Pos[2] set from entity @e[tag=ring_ccw_centre,limit=1] Pos[2]