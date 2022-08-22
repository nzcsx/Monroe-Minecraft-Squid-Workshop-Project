########################################
# Create globak objective
scoreboard objectives add monroe dummy
scoreboard players set x_travaller monroe 0
scoreboard players set y_travaller monroe 0
scoreboard players set x_centre monroe 0
scoreboard players set y_centre monroe 0

########################################
# Loading message
tellraw @a {"text":"[Server]: Monroe-Datapack from Squid-Workshop Loaded","italic":true,"color":"gray"}