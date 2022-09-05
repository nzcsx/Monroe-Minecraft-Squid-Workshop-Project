execute store result score x_traveller monroe run data get entity @s Pos[0] 10000
execute store result score y_traveller monroe run data get entity @s Pos[1] 10000

# x_traveller <  x_centre
execute if score x_traveller monroe < x_centre monroe run function monroe:classes/ring_ccw/travel/coords_xyz/location_neg
# x_traveller == x_centre &&  y_travaller >  y_centre
execute if score x_traveller monroe = x_centre monroe if score y_traveller monroe > y_centre monroe run function monroe:classes/ring_ccw/travel/coords_xyz/location_upp
# x_traveller >  x_centre
execute if score x_traveller monroe > x_centre monroe run function monroe:classes/ring_ccw/travel/coords_xyz/location_pos
# x_traveller == x_centre && y_travaller <  y_centre
execute if score x_traveller monroe = x_centre monroe if score y_traveller monroe < y_centre monroe run function monroe:classes/ring_ccw/travel/coords_xyz/location_low