function monroe:classes/main/clean

########################################
# Create globak objective
scoreboard objectives add monroe dummy
scoreboard players set x_traveller monroe 0
scoreboard players set y_traveller monroe 0
scoreboard players set x_holder monroe 0
scoreboard players set y_holder monroe 0
scoreboard players set x_centre monroe 0
scoreboard players set y_centre monroe 0

########################################
# Loading message
tellraw @a {"text":"[Server]: Monroe-Datapack from Squid-Workshop Loaded","italic":true,"color":"gray"}