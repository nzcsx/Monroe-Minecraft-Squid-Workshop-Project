# refresh the helper entities
kill @e[type=minecraft:marker,tag=ring_ccw_centre]
summon minecraft:marker ~ ~ ~ {Tags:["ring_ccw_centre"]}
execute store result score z_centre monroe run data get entity @e[type=minecraft:marker,tag=ring_ccw_centre,limit=1] Pos[2] 10000