import cv2
import skimage
from skimage import metrics



img = cv2.imread(
    "S:\IIT DELHI (MSR)\\1st_Semester\COL783 -Digital Image Analysis\Assignements\Assignment3\images\input0.png")
cv2.imshow("img", img)

roi = cv2.imread("S:\IIT DELHI (MSR)\\1st_Semester\COL783 -Digital Image Analysis\Assignements\Assignment3\pred\\0_k1.png")


b=skimage.metrics.mean_squared_error(img, roi)
print( b)