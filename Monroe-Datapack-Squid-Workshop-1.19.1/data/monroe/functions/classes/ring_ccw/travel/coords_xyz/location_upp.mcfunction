
# move coordinates
execute positioned ^ ^-1.5 ^-0.05 facing entity @e[type=marker,limit=1,tag=ring_ccw_centre] feet run tp @s ~ ~ ~ 0 ~

# move poses
function monroe:classes/ring_ccw/travel/coords_rot/check_location

# re-adjust z coordinate
execute store result entity @s Pos[2] double 0.0001 run scoreboard players get z_centre monroe