tp @e[type=area_effect_cloud,limit=1,tag=ring_ccw_holder] ~ ~ ~
execute store result score x_holder monroe run data get entity @e[type=area_effect_cloud,tag=ring_ccw_holder,limit=1] Pos[0] 10000
execute store result score y_holder monroe run data get entity @e[type=area_effect_cloud,tag=ring_ccw_holder,limit=1] Pos[1] 10000

# x_holder <  x_centre
execute if score x_holder monroe < x_centre monroe run function monroe:classes/ring_ccw/travel/coords_rot/location_neg
# x_holder == x_centre &&  y_holder >  y_centre
execute if score x_holder monroe = x_centre monroe if score y_holder monroe > y_centre monroe run function monroe:classes/ring_ccw/travel/coords_rot/location_upp
# x_holder >  x_centre
execute if score x_holder monroe > x_centre monroe run function monroe:classes/ring_ccw/travel/coords_rot/location_pos
# x_holder == x_centre && y_holder <  y_centre
execute if score x_holder monroe = x_centre monroe if score y_holder monroe < y_centre monroe run function monroe:classes/ring_ccw/travel/coords_rot/location_low