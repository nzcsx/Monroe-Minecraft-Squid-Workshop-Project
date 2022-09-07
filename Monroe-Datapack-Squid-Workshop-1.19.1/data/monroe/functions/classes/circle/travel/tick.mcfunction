# setblock for any distance
execute as @e[tag=circle_traveller] at @s positioned ~ ~0.5 ~0.4375 facing entity @e[type=marker,tag=circle_centre,limit=1] feet run function monroe:classes/circle/travel/setblock/check_colours

# fill for 50 meters away
execute at @e[type=marker,tag=circle_centre,limit=1] as @e[tag=circle_traveller,distance=50..] at @s positioned ~ ~0.5 ~0.4375 facing entity @e[type=marker,tag=circle_centre,limit=1] feet run function monroe:classes/circle/travel/location_further 

# move
execute as @e[tag=circle_traveller] at @s facing entity @e[type=marker,tag=circle_centre,limit=1] feet run tp @s ^ ^ ^-0.17 ~ ~ 
