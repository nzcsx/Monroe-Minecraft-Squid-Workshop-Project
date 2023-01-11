# setblock for any distance
execute as @e[tag=circle2_traveller] at @s positioned ~ ~0.5 ~ facing entity @e[type=marker,tag=circle2_centre,limit=1] feet run function monroe:classes/circle2/travel/location_any
# fill for 50 meters away
execute at @e[type=marker,tag=circle2_centre,limit=1] as @e[tag=circle2_traveller,distance=50..] at @s positioned ~ ~0.5 ~ facing entity @e[type=marker,tag=circle2_centre,limit=1] feet run function monroe:classes/circle2/travel/location_further

# move
execute as @e[tag=circle2_traveller] at @s facing entity @e[type=marker,tag=circle2_centre,limit=1] feet run tp @s ^ ^ ^-0.17 ~ ~ 
