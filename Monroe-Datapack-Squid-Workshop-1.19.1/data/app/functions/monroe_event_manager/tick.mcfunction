function monroe:classes/spiral/travel/tick
execute if score tick monroe matches 256.. run function monroe:classes/circle/travel/tick
execute if score tick monroe matches 288.. run function monroe:classes/ring_ccw/travel/tick
scoreboard players add tick monroe 1