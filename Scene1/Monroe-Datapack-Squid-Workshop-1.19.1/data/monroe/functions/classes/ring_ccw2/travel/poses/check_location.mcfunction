execute store result score x_holder monroe run data get entity @s Pos[0] 10000
execute store result score y_holder monroe run data get entity @s Pos[1] 10000

# x_holder <  x_centre
execute if score x_holder monroe < x_centre_ring_ccw2 monroe run function monroe:classes/ring_ccw2/travel/poses/location_neg
# x_holder == x_centre &&  y_travaller >  y_centre
execute if score x_holder monroe = x_centre_ring_ccw2 monroe if score y_holder monroe > y_centre_ring_ccw2 monroe run function monroe:classes/ring_ccw2/travel/poses/location_upp
# x_holder >  x_centre
execute if score x_holder monroe > x_centre_ring_ccw2 monroe run function monroe:classes/ring_ccw2/travel/poses/location_pos
# x_holder == x_centre && y_travaller <  y_centre
execute if score x_holder monroe = x_centre_ring_ccw2 monroe if score y_holder monroe < y_centre_ring_ccw2 monroe run function monroe:classes/ring_ccw2/travel/poses/location_low