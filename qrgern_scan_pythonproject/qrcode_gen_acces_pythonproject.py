##### # # # ===> https://www.youtube.com/watch?v=rvf2stRRMLo  [ codebasics Hindi ]

import qrcode

img = qrcode.make("Jai Shree Ram जय श्री राम ==> :)")
img.save("jai_shree_ram.jpg")


import cv2

a = cv2.QRCodeDetector()
val, points, straight_qrcoded = a.detectAndDecode(cv2.imread("jai_shree_ram.jpg"))
print(val)
