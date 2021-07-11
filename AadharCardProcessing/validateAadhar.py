import cv2

import AadharCardProcessing
import re

from AadharCardProcessing.codeReader import readingQR


def is_aadhar_card(text):
    res = text.split()
    gIndex = 0
    gender = ""
    # print("all data: ",res)
    if 'Government of India' in text:
        print("Aadhar card is valid and the details are below:")
        for l in res:
            if 'DOB' in l:
                index = res.index(l)
            if l == "MALE" or l == "FEMALE":
                gIndex = res.index(l)
                gender = res[gIndex]
        name = ''
        if res[index - 4].isalpha():
            name = res[index - 4] + " " + res[index - 3] + " " + res[index - 2]
    else:
        name = res[0] + " " + res[1]
    if len(name) > 1:
        print("Name:  " + name)
    else:
        print("Name not read")
    # dob_index = res.index()
    date = res[index + 1]
    print("DOB: ", date)
    aadhar_number = ''
    for word in res:
        if len(word) == 4 and word.isdigit():
            aadhar_number = aadhar_number + word
            # print("Aadhar Building: ", aadhar_number)
            if len(aadhar_number) == 12:
                break
    print("Aadhar number is: " + aadhar_number)
    print("Gender: ", gender)
    # qrImg = cv2.imread('QRFullDetect.jpg')
    tempparam = "temp"
    df, d = readingQR.readBarcodeQRcode(tempparam)
    # print("Data: ",df)
    # print("Label: ",d)
    if aadhar_number == df[d.index("uid")] and name == df[d.index("name")]:
        print("Data match")
        return 1
    else:
        print("Data mismatch.")
        return 0
