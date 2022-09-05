# travel
execute store result score x_centre monroe run data get entity @e[tag=ring_ccw_centre,limit=1] Pos[0] 10000
execute store result score y_centre monroe run data get entity @e[tag=ring_ccw_centre,limit=1] Pos[1] 10000

execute as @e[tag=ring_ccw_traveller] run function monroe:classes/ring_ccw/travel/coords_xyz/check_location