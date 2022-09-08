# setblock
execute at @s[tag=colour_0] facing entity @e[type=marker,tag=spiral_centre,limit=1] feet positioned ~ ~0.5 ~ run setblock ~0.5 ~-0.5 ~ orange_wool keep
execute at @s[tag=colour_1] facing entity @e[type=marker,tag=spiral_centre,limit=1] feet positioned ~ ~0.5 ~ run setblock ~0.5 ~-0.5 ~ light_blue_wool keep
execute at @s[tag=colour_2] facing entity @e[type=marker,tag=spiral_centre,limit=1] feet positioned ~ ~0.5 ~ run setblock ~0.5 ~-0.5 ~ pink_wool keep
execute at @s[tag=colour_3] facing entity @e[type=marker,tag=spiral_centre,limit=1] feet positioned ~ ~0.5 ~ run setblock ~0.5 ~-0.5 ~ yellow_wool keep
execute at @s[tag=colour_4] facing entity @e[type=marker,tag=spiral_centre,limit=1] feet positioned ~ ~0.5 ~ run setblock ~0.5 ~-0.5 ~ red_wool keep
execute at @s[tag=colour_5] facing entity @e[type=marker,tag=spiral_centre,limit=1] feet positioned ~ ~0.5 ~ run setblock ~0.5 ~-0.5 ~ lime_wool keep

# move
execute at @s facing entity @e[type=marker,tag=spiral_centre,limit=1] feet run tp @s ~-0.1 ~0.1 ~ 0 0

# re-adjust z coordinate
execute store result entity @s Pos[2] double 0.0001 run scoreboard players get z_centre_spiral monroe