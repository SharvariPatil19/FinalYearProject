import cv2
import tkinter as tk


cap = cv2.VideoCapture(0)
            
while(True): 
                # Capture frame-by-frame
                
                ret, frame = cap.read()
                
                # Display the resulting frame
                
                cv2.imshow('Preview',frame)
                
                #Waits for a user input to quit the application
                
                if cv2.waitKey(1) & 0xFF == ord('q'):
                
                    break
