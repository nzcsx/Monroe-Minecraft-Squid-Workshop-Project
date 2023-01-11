
# move
tp @s ~0 ~-0.3 ~ 0 0

# re-adjust z coordinate
execute store result entity @s Pos[2] double 0.0001 run scoreboard players get z_centre_spiral monroe