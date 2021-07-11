import cv2
from pyzbar.pyzbar import decode


class readingQR:
    def readBarcodeQRcode(self):
        img = cv2.imread('D:/SPIT/Semester 4/Mini Project/Wroking Module/VerifyMe/AadharCardProcessing/Asset/aadhar_QR.jpg')
        for barcode in decode(img):
            data = barcode.data
            myData = barcode.data.decode('utf-8')
            # print(myData)
        # myData = myData.split()
        # print("List: ", myData)
        d = ["uid", "name", "gender", "yob", "gname", "co", "house", "lm", "loc", "vtc", "po", "dist", "subdist", "state",
             "pc"]
        def stringToList(string):
            l = []
            flag = 0
            for c in string:
                if flag:
                    if c != '"':
                        str += c
                    else:
                        l.append(str)
                        flag = 0
                elif c == '"':
                    str = ''
                    flag = 1
            return l
        df = stringToList(myData)
        del df[0:2]
        print(df)
        # print(df[d.index("name")])
        return df, d