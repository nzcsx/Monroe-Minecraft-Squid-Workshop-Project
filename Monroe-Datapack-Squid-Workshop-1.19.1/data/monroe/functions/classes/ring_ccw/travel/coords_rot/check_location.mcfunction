execute store result score x_holder monroe run data get entity @s Pos[0] 10000
execute store result score y_holder monroe run data get entity @s Pos[1] 10000
# x_holder <  x_centre
execute if score x_holder monroe < x_centre_ring_ccw monroe run function monroe:classes/ring_ccw/travel/coords_rot/location_neg
# x_holder == x_centre &&  y_holder >  y_centre
execute if score x_holder monroe = x_centre_ring_ccw monroe if score y_holder monroe > y_centre_ring_ccw monroe run function monroe:classes/ring_ccw/travel/coords_rot/location_upp
# x_holder >  x_centre
execute if score x_holder monroe > x_centre_ring_ccw monroe run function monroe:classes/ring_ccw/travel/coords_rot/location_pos
# x_holder == x_centre && y_holder <  y_centre
execute if score x_holder monroe = x_centre_ring_ccw monroe if score y_holder monroe < y_centre_ring_ccw monroe run function monroe:classes/ring_ccw/travel/coords_rot/location_low