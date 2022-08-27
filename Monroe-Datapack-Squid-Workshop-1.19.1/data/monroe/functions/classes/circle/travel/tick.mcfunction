# setblock
execute as @e[tag=circle_traveller,tag=colour_0] at @s facing entity @e[tag=circle_center] feet positioned ~ ~0.5 ~ run setblock ^ ^ ^0.5 orange_stained_glass_pane[east=true,west=true]
execute as @e[tag=circle_traveller,tag=colour_1] at @s facing entity @e[tag=circle_center] feet positioned ~ ~0.5 ~ run setblock ^ ^ ^0.5 light_blue_stained_glass_pane[east=true,west=true]
execute as @e[tag=circle_traveller,tag=colour_2] at @s facing entity @e[tag=circle_center] feet positioned ~ ~0.5 ~ run setblock ^ ^ ^0.5 pink_stained_glass_pane[east=true,west=true]
execute as @e[tag=circle_traveller,tag=colour_3] at @s facing entity @e[tag=circle_center] feet positioned ~ ~0.5 ~ run setblock ^ ^ ^0.5 yellow_stained_glass_pane[east=true,west=true]
execute as @e[tag=circle_traveller,tag=colour_4] at @s facing entity @e[tag=circle_center] feet positioned ~ ~0.5 ~ run setblock ^ ^ ^0.5 red_stained_glass_pane[east=true,west=true]
execute as @e[tag=circle_traveller,tag=colour_5] at @s facing entity @e[tag=circle_center] feet positioned ~ ~0.5 ~ run setblock ^ ^ ^0.5 lime_stained_glass_pane[east=true,west=true]
execute as @e[tag=circle_traveller,tag=colour_6] at @s facing entity @e[tag=circle_center] feet positioned ~ ~0.5 ~ run setblock ^ ^ ^0.5 magenta_stained_glass_pane[east=true,west=true]

# move
execute as @e[tag=circle_traveller] at @s facing entity @e[tag=circle_center] feet run tp @s ^ ^ ^-0.11 ~ ~ 
