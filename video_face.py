import cv2

video = cv2.VideoCapture(0, cv2.CAP_DSHOW)
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
# smile_cascade = cv2.CascadeClassifier("smile_cascade.xml")


a = 0

while True:
    a = a+1
    check ,frame = video.read()
    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.05, minNeighbors=5)
    # smile = smile_cascade.detectMultiScale(gray_img, scaleFactor=1.05, minNeighbors=5)

    for x,y,w,h in faces:
        gray_img = cv2.rectangle(gray_img, (x,y), (x+w,y+h), (50,255,255),3)  
        gray_img_Re = cv2.resize(gray_img, (int(gray_img.shape[1]/2), int(gray_img.shape[0]/2)))

    # for a,b,c,d in smile:
    #     gray_img_Re = cv2.rectangle(gray_img_Re,(a,b),(a+c, b+d),(50,50,200),1)

    cv2.imshow("Video",gray_img) 

    key = cv2.waitKey(1)

    if key == ord('q'):
        break

print(a)
video.release()

cv2.destroyAllWindows()


