summon marker ~ ~ ~ {Tags:["ring_cw_centre"]}
execute store result score x_centre_ring_cw monroe run data get entity @e[type=marker,tag=ring_cw_centre,limit=1] Pos[0] 10000
execute store result score y_centre_ring_cw monroe run data get entity @e[type=marker,tag=ring_cw_centre,limit=1] Pos[1] 10000
execute store result score z_centre_ring_cw monroe run data get entity @e[type=marker,tag=ring_cw_centre,limit=1] Pos[2] 10000

