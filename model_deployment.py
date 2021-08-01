#!/usr/bin/env python
# coding: utf-8

# In[4]:


from tensorflow.keras.models import load_model
classifier = load_model('C:/Users/Aravinda Raman J/Desktop/project/mask_det.h5')

#Function to label the captured image
def getLabels(result):
    classlabels = {0 : 'No Mask',
                   1 : 'Mask'}
    try:
        res = int(result)
        return classlabels[res]
    except:
        return 'Error'



#Use OpenCV to identify the different object
import cv2
cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()
    frame = cv2.flip(frame,1)

    #region of intrest
    roi = frame[100:400 , 220:520]
    cv2.imshow('roi',roi)
    roi = cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)
    roi = cv2.resize(roi,(150,150))


    copy = frame.copy()
    cv2.rectangle(copy,(220,100),(520,400),(255,0,255),5)

    roi = roi.reshape(1,150,150,1)
    roi = roi/255

    result = (classifier.predict(roi) > 0.7).astype("int32")

    cv2.putText(copy,getLabels(result),(150,100),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
    cv2.imshow('frame',copy)
    print(result)

    if cv2.waitKey(1) == 13:
        break

cap.release()
cv2.destroyAllWindows()
    


# In[ ]:




