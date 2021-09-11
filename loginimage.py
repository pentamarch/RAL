import cv2
import numpy as np
import csv 

username = input("Enter username : ")

flag=0
with open('credentials.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
  
    for row in csv_reader:
      
        if(username == row[0] ):
            print(f'username found {row[0]}')
            flag=1
            break
       
    if(flag == 0):
        print("Incorrect username")

    else:
        print("Press space to capture image and escape after capturing")
        cam = cv2.VideoCapture(0)

        cv2.namedWindow("Python webcam screenshot app")

        img_count = 0

        while True:
            ret,frame = cam.read()

            if not ret:
                print("failed to grab frame")
                break

            cv2.imshow("test",frame)

            k = cv2.waitKey(1)

            if k%256 == 27:
                print("Escape hit, closing the app")
                break

            elif k%256 == 32:
                img_name = "opencv_frame_{}.png".format(img_count)
                cv2.imwrite(img_name, frame)
                print("Screenshot taken")
                img_count+=1

        cam.release()

        cv2.destroyAllWindows()
        img1 = cv2.imread("/home/admin1/ral/opencv_frame_0.png")
        img2 = cv2.imread("/home/admin1/ral/{username}.png")

        


