execute store result score x_travaller monroe run data get entity @s Pos[0] 1000
execute store result score y_travaller monroe run data get entity @s Pos[1] 1000

# x_travaller < x_centre
execute if score x_travaller monroe < x_centre monroe run function monroe:classes/spiral/travel/location_neg
# x_travaller = x_centre && 
# y_travaller > y_centre
execute if score x_travaller monroe = x_centre monroe if score y_traveller monroe > y_centre monroe run function monroe:classes/spiral/travel/location_upp

# x_travaller > x_centre
execute if score x_travaller monroe > x_centre monroe run function monroe:classes/spiral/travel/location_pos
# x_travaller = x_centre && 
# y_travaller < y_centre
execute if score x_travaller monroe = x_centre monroe if score y_traveller monroe < y_centre monroe run function monroe:classes/spiral/travel/location_low