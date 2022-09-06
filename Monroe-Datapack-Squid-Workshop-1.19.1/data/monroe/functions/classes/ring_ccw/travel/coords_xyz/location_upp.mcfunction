
# move coordinates
execute at @s facing entity @e[type=marker,limit=1,tag=ring_ccw_centre_2] feet positioned ^ ^-1.5 ^-0.05 facing entity @e[type=marker,limit=1,tag=ring_ccw_centre_2] feet run tp @s ~ ~ ~ 0 ~

# move poses
execute at @s facing entity @e[type=marker,limit=1,tag=ring_ccw_centre_2] feet run function monroe:classes/ring_ccw/travel/coords_rot/check_location

# re-adjust z coordinate
data modify entity @s Pos[2] set from entity @e[type=marker,tag=ring_ccw_centre_2,limit=1] Pos[2]