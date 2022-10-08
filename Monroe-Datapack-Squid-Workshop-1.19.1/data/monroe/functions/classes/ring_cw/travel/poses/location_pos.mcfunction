execute store result score r_holder monroe run data get entity @s Rotation[1] -10000
scoreboard players remove r_holder monroe 90000
execute store result entity @s Pose.Head[2] float 0.0001 run scoreboard players get r_holder monroe