# # import cv2

# # video_capture = cv2.VideoCapture(1)
# # while True :
# #     ret , video_data = video_capture.read()
# #     cv2.imshow("video_live" , video_data)
# #     if cv2.waitKey(10) == ord("a"):
# #         break
# #     video_capture.release()



# import cv2
# face_cap = cv2.CascadeClassifier("data/haarcascades/haarcascade_frontalface_default.xml")

# video_capture = cv2.VideoCapture(0)

# while True:
#     ret, video_data = video_capture.read()
#     col = cv2.cvtColor(video_data, cv2.COLOR_BGR2GRAY)
#     faces = face_cap.detectMultiScale(
#         col,
#         scaleFactor= 1.1,
#         minNeighbors=5,
#         minSize=(30, 30),
#         flags= cv2.CASCADE_SCALE_IMAGE
#     )
#     for (x,y,w,h) in faces:
#         cv2.rectangle(video_data, (x,y) , (x+w,y+h), (0,255,0) , 2)

    
#     # Check if frame was read successfully
#     if not ret or video_data is None:
#         print("Failed to grab frame")
#         break
    
#     cv2.imshow("video_live", video_data)
    
#     if cv2.waitKey(10) == ord("a"):
#         break

# video_capture.release()
# cv2.destroyAllWindows()




import cv2

# Fix the path to the Haar Cascade file
face_cap = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

video_capture = cv2.VideoCapture(0)

while True:
    ret, video_data = video_capture.read()
    
    # Check if frame was read successfully
    if not ret or video_data is None:
        print("Failed to grab frame")
        break
    
    col = cv2.cvtColor(video_data, cv2.COLOR_BGR2GRAY)
    
    # Fix: Pass col directly, not as a tuple
    faces = face_cap.detectMultiScale(
        col,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    
    for (x, y, w, h) in faces:
        cv2.rectangle(video_data, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    cv2.imshow("video_live", video_data)
    
    if cv2.waitKey(10) == ord("a"):
        break

video_capture.release()
cv2.destroyAllWindows()