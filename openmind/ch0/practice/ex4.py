# -*- coding: utf-8 -*-
cars=100 # 车辆数
space_in_a_car=4.0 #每辆车可以运载的人数
drivers=30 #司机人数
passengers=90 #乘客人数
cars_not_driven=cars-drivers #不可发车数量
cars_driven=drivers #发车数量
carpool_capacity=cars_driven*space_in_a_car #总运力
average_passagers_per_car=passengers/cars_driven #平均每辆车搭载乘客数量


print "There are", cars,"cars available."
print "There are only",drivers,"drivers available."
print "There will be",cars_not_driven,"empty cars today."
print "We can transport",carpool_capacity,"people today."
print "We have",passengers,"to carpool today."
print "We need to put about",average_passagers_per_car,"in each car."
