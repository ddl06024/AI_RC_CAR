import numpy as np
import cv2
import serial
import time
from picamera.array import PiRGBArray
from picamera import PiCamera
class RC_Car_Interface():
    def __init__(self):
        self.left_wheel = 0
        self.right_wheel = 0
        self.camera = PiCamera()
        self.camera.resolution = (320,320)         # set camera resolution to (320, 320)
        self.camera.color_effects = (128,128)      # set camera to black and white
    def finish_iteration(self):
        print('finish iteration')
    def set_speed(self, r_speed, l_speed):           
        cmd1 = ("R%d" % r_speed).encode('ascii')
        cmd2 = ("L%d\n" % l_speed).encode('ascii')
        cmd = cmd1 + cmd2
        for i in range(2):
            print("My cmd is %s" % cmd)
            ser.write(cmd)
        # For debugging, read cmd from arduino
            read_serial= ser.readline()
        #print("rignt cmd debug :{0}".format(read_serial.dtype))
            print(read_serial)    
        #time.sleep(2)          
    def get_image_from_camera(self):  
        print("get image start")
        img = np.empty((320, 320, 3), dtype=np.uint8)
        self.camera.capture(img, 'bgr',use_video_port = True) 
        print("capture success")
        cv2.imshow('disp',np.array(cv2.resize(img,(280,280))))  
        img = img[:,:,0]           # 3 dimensions have the same value because camera is set to black and white
                                   # remove two dimension data
        # print(img)
        threshold = int(np.mean(img))*0.5
        # print(threshold)
        # Invert black and white with threshold
        ret, img2 = cv2.threshold(img.astype(np.uint8), threshold, 255, cv2.THRESH_BINARY_INV)
        img2 = cv2.resize(img2,(16,16), interpolation=cv2.INTER_AREA )

        # cv2.imshow("Image", img2)
        #        cv2.waitKey(0)
        return img2

    def stop(self):     # robot stop
        print('stop')
