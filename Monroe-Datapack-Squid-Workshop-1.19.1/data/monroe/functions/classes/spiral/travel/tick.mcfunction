# travel
execute store result score x_centre monroe run data get entity @e[type=area_effect_cloud,tag=spiral_centre_2,limit=1] Pos[0] 10000
execute store result score y_centre monroe run data get entity @e[type=area_effect_cloud,tag=spiral_centre_2,limit=1] Pos[1] 10000

execute as @e[tag=spiral_traveller] run function monroe:classes/spiral/travel/check_location