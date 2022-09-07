# setblock
execute as @e[tag=circle_traveller,tag=colour_0] at @s facing entity @e[type=marker,tag=circle_centre,limit=1] feet positioned ~ ~0.5 ~0.4375 run setblock ^ ^ ^0.2 orange_stained_glass_pane[east=true,west=true] keep
execute as @e[tag=circle_traveller,tag=colour_1] at @s facing entity @e[type=marker,tag=circle_centre,limit=1] feet positioned ~ ~0.5 ~0.4375 run setblock ^ ^ ^0.2 light_blue_stained_glass_pane[east=true,west=true] keep
execute as @e[tag=circle_traveller,tag=colour_2] at @s facing entity @e[type=marker,tag=circle_centre,limit=1] feet positioned ~ ~0.5 ~0.4375 run setblock ^ ^ ^0.2 pink_stained_glass_pane[east=true,west=true] keep
execute as @e[tag=circle_traveller,tag=colour_3] at @s facing entity @e[type=marker,tag=circle_centre,limit=1] feet positioned ~ ~0.5 ~0.4375 run setblock ^ ^ ^0.2 yellow_stained_glass_pane[east=true,west=true] keep
execute as @e[tag=circle_traveller,tag=colour_4] at @s facing entity @e[type=marker,tag=circle_centre,limit=1] feet positioned ~ ~0.5 ~0.4375 run setblock ^ ^ ^0.2 red_stained_glass_pane[east=true,west=true] keep
execute as @e[tag=circle_traveller,tag=colour_5] at @s facing entity @e[type=marker,tag=circle_centre,limit=1] feet positioned ~ ~0.5 ~0.4375 run setblock ^ ^ ^0.2 lime_stained_glass_pane[east=true,west=true] keep
execute as @e[tag=circle_traveller,tag=colour_6] at @s facing entity @e[type=marker,tag=circle_centre,limit=1] feet positioned ~ ~0.5 ~0.4375 run setblock ^ ^ ^0.2 magenta_stained_glass_pane[east=true,west=true] keep

# fill for 50 meters away
execute at @e[type=marker,tag=circle_centre,limit=1] as @e[tag=circle_traveller,distance=50..] run function monroe:classes/circle/travel/location_further 

# move
execute as @e[tag=circle_traveller] at @s facing entity @e[type=marker,tag=circle_centre,limit=1] feet run tp @s ^ ^ ^-0.17 ~ ~ 
