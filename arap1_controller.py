""" ARAP Webots main file """
import robot
import cv2 as cv

#image is shown from a defined folder
# img = cv.imread("G:\PSB_ACADEMY\Modules\Applied Robotics & AI Projects\Talib_Arap_Project2\worlds\dog.png")
# cv.imshow("window",img)
# cv.waitKey(0)

 

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
            if red > 155 and red < 180:                     
               summary.append('i see red')
               print("Summary :", summary)
               redish = True
                           
        if not greenish: 
            if green > 155 and green < 180:
               summary.append('I see green') 
               print("Summary :",summary)
               greenish = True
               
        if not blueish:       
            if blue > 170 and blue < 180:
               summary.append('I see blue') 
               print("Summary :",summary) 
               blueish = True
               
        if not water:       
            if red > 70 and red <80 and green > 120 and green <130 and blue > 160 and blue < 165 :
               summary.append('I found water') 
               print("Summary :",summary) 
               water = True
               
        if not food:       
            if red > 85 and red < 90 and green > 140 and green < 145 and blue > 120 and blue < 130:
               summary.append('I found food') 
               print("Summary :",summary) 
               food = True
        
        #if see truck take picture       
        if red > 130 <140 and green > 130 < 140 and blue > 130 < 140 :
            robot1.save_picture() 
        #if see dog take picture    
        if red >135 < 140 and green >130<135 and blue > 125<130:       
            robot1.save_picture()
        #if see frog take picture    
        if red >120 < 130 and green >120<130 and blue > 130<140:       
            robot1.save_picture()
                                                 
        if robot1.front_obstacles_detected():
            robot1.move_backward()
            robot1.turn_left()
        else:
            robot1.run_braitenberg()
            robot1.set_actuators()
            robot1.step()

if __name__ == "__main__":
    main()
