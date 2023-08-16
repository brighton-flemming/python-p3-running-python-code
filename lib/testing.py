# Write a program that takes as input the speed of a car e.g 80. If the speed is less than 70, it should print “Ok”. Otherwise, for every 5 km/s above the speed limit (70), it should give the driver one demerit point and print the total number of demerit points.
# For example, if the speed is 80, it should print: “Points: 2”. If the driver gets more than 12 points, the function should print: “License suspended”. 



points = 0
speed_limit = 70
max_speed = 130
points_limit = 12
def check_speed(speed, points):
    if speed < speed_limit :
        return "Points: "+ str(points) +  "  Ok"
    elif speed > speed_limit :
        points= int((speed - speed_limit) // 5)
        return "Points: " + str(points)
    
    elif speed >= max_speed:
        if points > points_limit:
            return "License suspended"
    else:
        return "No points added" 
  

speed= int(input("How fast were you going?  "))
result = check_speed(speed,points)
print( result)


