import cv2

class FaceExtraction:
    def face_extraction(self):
        # img = cv2.imread("D:\\SPIT\\Semester 4\\Mini Project\\Wroking Module\\VerifyMe\\AadharCardProcessing\\Asset\\aadharCard.png")
        img = cv2.imread("D:\\SPIT\\Semester 4\\Mini Project\\Wroking Module\\VerifyMe\\MiddleTier\\aadharCard.png")
        # cv2.imshow(img)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        face_cascade = cv2.CascadeClassifier('D:\\SPIT\\Semester 4\\Mini Project\\Wroking Module\\VerifyMe\\AadharCardProcessing\\Asset\\haarcascade_frontalface_alt.xml')
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
            faces = img[y:y + h, x:x + w]
            cv2.imshow("face", faces)
            cv2.imwrite('D:\\SPIT\\Semester 4\\Mini Project\\Wroking Module\\VerifyMe\\AadharCardProcessing\\Asset\\face.jpg', faces)
        cv2.imwrite('D:\\SPIT\\Semester 4\\Mini Project\\Wroking Module\\VerifyMe\\AadharCardProcessing\\Asset\\detcted.jpg', img)
        cv2.imshow('img', img)
        cv2.waitKey()