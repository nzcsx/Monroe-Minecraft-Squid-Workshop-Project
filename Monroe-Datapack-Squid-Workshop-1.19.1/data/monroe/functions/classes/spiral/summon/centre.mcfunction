summon armor_stand ~ ~ ~ {CustomName:'"spiral_centre"', CustomNameVisible:1,NoGravity:1,Marker:1,Tags:["spiral_centre"]}

# refresh the helper entities
kill @e[type=minecraft:area_effect_cloud,tag=spiral_centre_2]
execute as @e[tag=spiral_centre] at @s run summon minecraft:area_effect_cloud ~ ~ ~ {Duration:999999,Tags:["spiral_centre_2"]}