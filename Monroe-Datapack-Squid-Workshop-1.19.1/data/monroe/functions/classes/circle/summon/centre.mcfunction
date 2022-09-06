summon armor_stand ~ ~ ~-0.4375 {CustomName:'"circle_centre"', CustomNameVisible:1,NoGravity:1,Marker:1,Tags:["circle_centre"]}

# refresh the helper entities
kill @e[type=minecraft:marker,tag=circle_centre_2]
execute as @e[tag=circle_centre] at @s run summon minecraft:marker ~ ~ ~ {Tags:["circle_centre_2"]}