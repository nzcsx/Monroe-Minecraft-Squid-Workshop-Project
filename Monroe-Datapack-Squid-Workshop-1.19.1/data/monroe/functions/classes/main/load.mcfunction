function monroe:classes/main/clean

########################################
# Create global objective
scoreboard objectives add monroe dummy

scoreboard players set x_centre_spiral monroe 0
scoreboard players set y_centre_spiral monroe 0
scoreboard players set z_centre_spiral monroe 0

scoreboard players set x_centre_ring_ccw monroe 0
scoreboard players set y_centre_ring_ccw monroe 0
scoreboard players set z_centre_ring_ccw monroe 0

scoreboard players set x_traveller monroe 0
scoreboard players set y_traveller monroe 0

scoreboard players set x_holder monroe 0
scoreboard players set y_holder monroe 0

scoreboard players set tick monroe 0

########################################
# Loading message
tellraw @a {"text":"[Server]: Monroe-Datapack from Squid-Workshop Loaded","italic":true,"color":"gray"}