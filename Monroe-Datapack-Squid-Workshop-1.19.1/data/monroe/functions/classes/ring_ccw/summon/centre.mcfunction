summon minecraft:armor_stand ~ ~ ~ {CustomName:'"ring_ccw_centre"', CustomNameVisible:1,NoGravity:1,Marker:1,Tags:["ring_ccw_centre"]}

# refresh the helper entities
kill @e[type=minecraft:area_effect_cloud,tag=ring_ccw_holder]
kill @e[type=minecraft:area_effect_cloud,tag=ring_ccw_centre_2]
execute as @e[tag=ring_ccw_centre] at @s run summon minecraft:area_effect_cloud ~ ~ ~ {Duration:999999,Tags:["ring_ccw_holder"]}
execute as @e[tag=ring_ccw_centre] at @s run summon minecraft:area_effect_cloud ~ ~ ~ {Duration:999999,Tags:["ring_ccw_centre_2"]}