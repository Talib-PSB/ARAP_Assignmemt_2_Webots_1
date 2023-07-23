""" ARAP Webots main file """
import robot

def main():
    red = 0
    green = 0
    blue = 0
    range = 0.0
    robot1 = robot.ARAP()
    robot1.init_devices()

    redish = False
    greenish = False
    blueish = False
    water = False
    food = False
    summary = []
    while True:
        robot1.reset_actuator_values()
        range = robot1.get_sensor_input()
        robot1.blink_leds()
        red, green, blue = robot1.get_camera_image(5)

        # Printing only once and pushing string in list data structure              
        if not redish:
            if red > 140 < 160:                     
               summary.append('i see red')
               print("Summary :", summary)
               redish = True
                           
        if not greenish: 
            if green > 140 <= 160:
               summary.append('I see green') 
               print("Summary :",summary)
               greenish = True
               
        if not blueish:       
            if blue > 140 <= 160:
               summary.append('I see blue') 
               print("Summary :",summary) 
               blueish = True
               
        if not water:       
            if blue > 90 <= 110:
               summary.append('I found water') 
               print("Summary :",summary) 
               water = True
               
        if not food:       
            if green > 90 <= 110:
               summary.append('I found food') 
               print("Summary :",summary) 
               food = True      
        
        if robot1.front_obstacles_detected():
            robot1.move_backward()
            robot1.turn_left()
        else:
            robot1.run_braitenberg()
        robot1.set_actuators()
        robot1.step()

if __name__ == "__main__":
    main()
