#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().system('pip install opencv-python')


# In[ ]:


def makedirectory(directory):
    if not os.path.exists(directory):
        os.mkdir(directory)
        return None
    else:
        pass




import cv2
import os


cap = cv2.VideoCapture(0)


i = 0
image_count=0


while i <= 6:
    state,frame = cap.read()
    frame = cv2.flip(frame,1)


    #ROI
    roi = frame[100:400,220:520]
    #cv2.imshow('roi',roi)


    roi = cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)
    roi = cv2.resize(roi,(75,75))
    cv2.imshow('roi',roi)


    copy = frame.copy()
    cv2.rectangle(copy,(220,100),(520,400),(255,0,0),5)


    if i == 0:
        image_count=0
        cv2.putText(copy,'press a to record 1st object',(50,100),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,0),1)


    if i == 1:
        image_count += 1
        cv2.putText(copy,'Recording 1st Object-Train Dataset with mask',(50,100),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,0),1)
        cv2.putText(copy,str(image_count),(300,400),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,255),1)
        faces = 'C:/Users/Aravinda Raman J/Desktop/project/train/train 1'
        makedirectory(faces)
        cv2.imwrite(faces + str(image_count) + ".jpg", roi)
        
    if i == 2:
        image_count += 1
        cv2.putText(copy,'Recording 1st Object-Test Dataset without mask',(50,100),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,0),1)
        cv2.putText(copy,str(image_count),(300,400),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,255),1)
        faces = 'C:/Users/Aravinda Raman J/Desktop/project/train/train 0'
        makedirectory(faces)
        cv2.imwrite(faces + str(image_count) + ".jpg", roi)


    if i == 3:
        image_count=0
        cv2.putText(copy,'press a to record 2nd object withhout mask',(50,100),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,0),1)


    if i == 4:
        image_count += 1
        cv2.putText(copy,'Recording 2nd Object-Train Dataset with mask',(50,100),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,0),1)
        cv2.putText(copy,str(image_count),(300,400),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,255),1)
        faces = 'C:/Users/Aravinda Raman J/Desktop/project/test/test 1'
        makedirectory(faces)
        cv2.imwrite(faces + str(image_count) + ".jpg", roi)
        
    if i == 5:
        image_count += 1
        cv2.putText(copy,'Recording 2nd Object-Test Dataset without mask',(50,100),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,0),1)
        cv2.putText(copy,str(image_count),(300,400),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,255),1)
        faces = 'C:/Users/Aravinda Raman J/Desktop/project/test/test 0'
        makedirectory(faces)
        cv2.imwrite(faces + str(image_count) + ".jpg", roi)


    if i == 6:
        cv2.putText(copy,"Press a to Exit",(50,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,255),1)
    cv2.imshow('Image',copy)        
    
    if cv2.waitKey(1) == ord('a'):
        image_count=0
        i = i+1
        


cap.release()
cv2.destroyAllWindows()


# In[ ]:




