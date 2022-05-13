from rc_car_interface import RC_Car_Interface
from tf_learn import DNN_Driver
import numpy as np
import time
import cv2



class SelfDriving:

    def __init__(self):
        self.rc_car_cntl = RC_Car_Interface()
        self.dnn_driver = DNN_Driver()
        self.rc_car_cntl.set_speed(0,0)
        #self.rc_car_cntl.set_right_speed(0)
        
        self.velocity = 0
        self.direction = 0
        self.dnn_driver.tf_learn_2()
    
    def rc_car_control(self, direction):
        #calculate left and right wheel speed with direction
            
        if direction == 1.0:
            left_speed = 255
            right_speed = 80
        elif direction == 0.8:
            left_speed = 240
            right_speed = 90
        elif direction ==0.3:
            left_speed = 200
            right_speed = 190
        elif direction == 0.0:
            left_speed = 200
            right_speed = 200
        elif direction == -0.3:
            left_speed = 180
            right_speed = 220
        elif direction == -0.8:
            left_speed =90
            right_speed = 240
        elif direction == -1.0:
            left_speed = 80
            right_speed = 255
                
        self.rc_car_cntl.set_speed(right_speed,left_speed)
    def drive(self):
        
        print("start start")
        
        while True:
            
            print("self dirve start")
            
            img = self.rc_car_cntl.get_image_from_camera()
            
            img = np.reshape(img,img.shape[0]**2)
            
            direction = self.dnn_driver.predict_direction_2(img)
            
            print("predicted_direction success")
            print("predicted direction :{0} ".format(direction))
            
            self.rc_car_control(direction)
            
            #cv2.imshow("target", cv2.resize(img,(280,280)))
#cv2.waitKey(0)
            time.sleep(0.2)
            
            self.rc_car_cntl.set_speed(0,0)
            time.sleep(0.2)
            
            
        self.rc_car_cntl.stop()
        cv2.destroyAllWindows()
                                

        


SelfDriving().drive()
