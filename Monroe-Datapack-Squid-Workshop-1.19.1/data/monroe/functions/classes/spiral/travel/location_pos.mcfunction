# setblock
execute if entity @s[tag=colour_0] positioned ~ ~0.5 ~ run setblock ^ ^-0.5 ^0.6 orange_wool keep
execute if entity @s[tag=colour_1] positioned ~ ~0.5 ~ run setblock ^ ^-0.5 ^0.6 light_blue_wool keep
execute if entity @s[tag=colour_2] positioned ~ ~0.5 ~ run setblock ^ ^-0.5 ^0.6 pink_wool keep
execute if entity @s[tag=colour_3] positioned ~ ~0.5 ~ run setblock ^ ^-0.5 ^0.6 yellow_wool keep
execute if entity @s[tag=colour_4] positioned ~ ~0.5 ~ run setblock ^ ^-0.5 ^0.6 red_wool keep
execute if entity @s[tag=colour_5] positioned ~ ~0.5 ~ run setblock ^ ^-0.5 ^0.6 lime_wool keep

# move
tp @s ^ ^0.1 ^-0.1 0 0

# re-adjust z coordinate
execute store result entity @s Pos[2] double 0.0001 run scoreboard players get z_centre_spiral monroe