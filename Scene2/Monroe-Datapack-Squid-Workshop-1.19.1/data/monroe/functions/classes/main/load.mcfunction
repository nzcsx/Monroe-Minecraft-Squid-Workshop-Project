function monroe:classes/main/clean

########################################
# Create global objective
scoreboard objectives add monroe dummy

scoreboard players set tick monroe 0

########################################
# Loading message
tellraw @a {"text":"[Server]: Monroe-Datapack from Squid-Workshop Loaded","italic":true,"color":"gray"}