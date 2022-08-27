# setblock
execute at @s[tag=colour_0] facing entity @e[tag=spiral_center] feet positioned ~ ~0.5 ~ run setblock ~0.5 ~-0.5 ~ orange_wool
execute at @s[tag=colour_1] facing entity @e[tag=spiral_center] feet positioned ~ ~0.5 ~ run setblock ~0.5 ~-0.5 ~ light_blue_wool
execute at @s[tag=colour_2] facing entity @e[tag=spiral_center] feet positioned ~ ~0.5 ~ run setblock ~0.5 ~-0.5 ~ pink_wool
execute at @s[tag=colour_3] facing entity @e[tag=spiral_center] feet positioned ~ ~0.5 ~ run setblock ~0.5 ~-0.5 ~ yellow_wool
execute at @s[tag=colour_4] facing entity @e[tag=spiral_center] feet positioned ~ ~0.5 ~ run setblock ~0.5 ~-0.5 ~ red_wool
execute at @s[tag=colour_5] facing entity @e[tag=spiral_center] feet positioned ~ ~0.5 ~ run setblock ~0.5 ~-0.5 ~ lime_wool

# move
execute at @s facing entity @e[tag=spiral_center] feet run tp @s ~-0.1 ~0.1 ~ -90 90
