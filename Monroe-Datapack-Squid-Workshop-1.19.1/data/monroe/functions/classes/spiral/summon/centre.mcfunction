summon armor_stand ~ ~ ~ {CustomName:'"spiral_centre"', CustomNameVisible:1,NoGravity:1,Marker:1,Tags:["spiral_centre"]}

# refresh the helper entities
kill @e[type=minecraft:marker,tag=spiral_centre_2]
execute as @e[tag=spiral_centre] at @s run summon minecraft:marker ~ ~ ~ {Tags:["spiral_centre_2"]}