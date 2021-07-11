from tkinter import messagebox, Tk

import AadharCardProcessing.validateAadhar as validate
import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'D:\\SPIT\\Semester 4\\Mini Project\\Wroking Module\\VerifyMe\\Tesseract\\tesseract.exe'

class TextExtraction:
    # Function to extract the text from image as string
    def extract_text(self):
        # image = cv2.imread("D:/SPIT/Semester 4/Mini Project/Wroking Module/VerifyMe/AadharCardProcessing/Asset/aadharCard.png")
        image = cv2.imread(
            "D:\\SPIT\\Semester 4\\Mini Project\\Wroking Module\\VerifyMe\\MiddleTier\\aadharCard.png")
        print("Image reading successful")
        # resize the image
        img = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)
        print("image resizing successful")
        print("dimension: ", img.shape)
        cv2.imshow("Image", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        # convert the image to gray
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # the following command uses the tesseract directory path to get the trained data in the config option
        text = pytesseract.image_to_string(img,config='--tessdata-dir "D:/SPIT/Semester 4/Mini Project/Wroking Module/VerifyMe/Tesseract/tessdata"')
        # print(text)
        match_boolean = validate.is_aadhar_card(text)
        ws = Tk()
        if match_boolean == 1:
            messagebox.showinfo("Success", "Aadhaar Card is not forged. Please wait while we establish your identity.\n"
                                "Please let the window stay active and detect your face and then press \"Esc\" to "
                                "close the window.\n "
                                "Make sure you are in well lit room and no one else is in frame apart from you.")
            ws.destroy()
        else:
            messagebox.showinfo("Failure", "Aadhaar Card is forged. Please retry.")

