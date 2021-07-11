from GUI.User.registerCredentials import FirstForm
from GUI.User.registerDetails import SecondForm
from GUI.User.uploadAadhaar import ThirdForm
from AadharCardProcessing.codeReader import readingQR
from AadharCardProcessing.textExtraction import TextExtraction
from AadharCardProcessing.faceExtract import FaceExtraction
from FaceRecognition.processingModel import RecognizeFace
from GUI.User.uploadDP import ForthForm
from GUI.User.uploadSignature import FifthForm



testparam = "demo"

FirstForm.credentialsForm(testparam)
SecondForm.detailsForm(testparam)
ThirdForm.uploadAadhaarForm(testparam)
readingQR.readBarcodeQRcode(testparam)
TextExtraction.extract_text(testparam)
FaceExtraction.face_extraction(testparam)
RecognizeFace.face_recognize(testparam)
ForthForm.uploadDPForm(testparam)
FifthForm.uploadSignatureForm(testparam)
