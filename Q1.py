
import cv2
import numpy as np



img = cv2.imread(
    "S:\IIT DELHI (MSR)\\1st_Semester\COL783 -Digital Image Analysis\Assignements\Assignment3\COL783_Test_Dataset\COL783_Test_Dataset\Distorted\line_Image_0000.png")

roi = cv2.imread(
    "S:\IIT DELHI (MSR)\\1st_Semester\COL783 -Digital Image Analysis\Assignements\Assignment3\COL783_Test_Dataset\COL783_Test_Dataset\Masks\line_Image_0000.png")
cv2.imshow("omg", img)
cv2.imshow("df", roi)
invert = cv2.bitwise_not(roi)

im = invert
cv2.imshow("invert", im)
for i in range(invert.shape[0]-2):
    for j in range(invert.shape[1]-2):
         if im[i][j].all() == 0 :
            print("hi")
            img[i+1][j] = 0
            img[i -1][j] = 0
            img[i][j+1] = 0
            img[i][j-1] = 0
            img[i + 1][j+1] = 0
            img[i-1][j + 1] = 0
            img[i + 1][j-1] = 0
            img[i-1][j - 1] = 0
            img[i + 2][j] = 0
            img[i][j + 2] = 0
            img[i - 2][j] = 0
            img[i][j - 2] = 0
            img[i + 2][j + 2] = 0
            img[i - 2][j + 2] = 0
            img[i + 2][j - 2] = 0
            img[i - 2][j - 2] = 0

cv2.imshow("invert", img)
# roi= cv2.bitwise_and(img, im, mask=None)
# cv2.imshow("dfs", roi)
# image_roi = roi
# for i in range(roi.shape[0]):
#     for j in range(roi.shape[1]):
#          if roi[i][j] != 0:
#              image_roi[i][j] = 255
#
# cv2.imshow("white_roi", roi)
#
# a= 0.073235
# b =0.176765
# c = 0.125
# kernel1 = np.array([[a, b, a],
#                     [b, 0, b],
#                     [a, b, a]])
# kernel2 = np.array([[c, c, c],
#                     [c, 0, c],
#                     [c, c, c]])
#
# for i in range(50):
#     identity = cv2.filter2D(src=img, ddepth=-1, kernel=kernel1)
#     conv_image = cv2.bitwise_and(identity, image_roi, mask=None)
#     final = roi + conv_image
#     img = final
#
# cv2.imshow("final", final)
# #
#
#
#






cv2.waitKey(0)


