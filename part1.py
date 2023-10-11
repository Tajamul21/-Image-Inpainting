import cv2
import numpy as np
import skimage
from skimage import metrics


# drawing = False  # true if mouse is pressed
# mode = True  # if True, draw rectangle. Press 'm' to toggle to curve
#
#
# # mouse callback function
# def begueradj_draw(event, former_x, former_y, flags, param):
#     global current_former_x, current_former_y, drawing, mode
#
#     if event == cv2.EVENT_LBUTTONDOWN:
#         drawing = True
#         current_former_x, current_former_y = former_x, former_y
#
#     elif event == cv2.EVENT_MOUSEMOVE:
#         if drawing == True:
#             if mode == True:
#                 cv2.line(im, (current_former_x, current_former_y), (former_x, former_y), (0, 0, 0), 8)
#                 current_former_x = former_x
#                 current_former_y = former_y
#                 # print former_x,former_y
#     elif event == cv2.EVENT_LBUTTONUP:
#         drawing = False
#         if mode == True:
#             cv2.line(im, (current_former_x, current_former_y), (former_x, former_y), (0, 0, 0), 8)
#             current_former_x = former_x
#             current_former_y = former_y
#     return former_x, former_y
#
#
# # im = cv2.imread("S:\IIT DELHI (MSR)\\1st_Semester\COL783 -Digital Image Analysis\Assignements\Assignment3\input0.png")
# # cv2.namedWindow("Bill BEGUERADJ OpenCV")
# # cv2.setMouseCallback('Bill BEGUERADJ OpenCV',begueradj_draw)
# # cv2.imshow('Bill BEGUERADJ OpenCV',im)
# # while(1):
# #     cv2.imshow('Bill BEGUERADJ OpenCV',im)
# #     k=cv2.waitKey(1)
# #     if k==0.01:
# #         break
# #
# # cv2.destroyAllWindows()
# # #
# img = cv2.imread(
#     "S:\IIT DELHI (MSR)\\1st_Semester\COL783 -Digital Image Analysis\Assignements\Assignment3\input0.png")
# cv2.imshow("img", img)
#
# roi = cv2.imread("S:\IIT DELHI (MSR)\\1st_Semester\COL783 -Digital Image Analysis\Assignements\Assignment3\\ROI.png")
#
# a = 0.073235
# b = 0.176765
# c = 0.125
# kernel1 = np.array([[a, b, a],
#                         [b, 0, b],
#                         [a, b, a]])
# kernel2 = np.array([[c, c, c],
#                     [c, 0, c],
#                     [c, c, c]])
#
# def image_impainting(img, roi, kernel):
#     (B, G, R) = cv2.split(img)
#     (Br, Gr, Rr) = cv2.split(roi)
#     img = B
#     roi = Br
#     # cv2.imshow("B", B)
#     # cv2.imshow("roi", roi)
#     img_roi = img - roi
#     image_roi = img - roi
#     # cv2.imshow("image_roi", image_roi)
#     for i in range(image_roi.shape[0]):
#         for j in range(image_roi.shape[1]):
#             if image_roi[i][j].all() != 0:
#                 image_roi[i][j] = 255
#     # cv2.imshow("rois", roi)
#     # cv2.imshow("image_roi", image_roi)
#
#
#
#
#     # print("check")
#     for i in range(10000):
#         identity = cv2.filter2D(src=img, ddepth=-1, kernel=kernel)
#         conv_image = cv2.bitwise_and(identity, image_roi, mask=None)
#         final1 = roi + conv_image
#         img = final1
#
#
#     img = G
#     roi = Gr
#     img_roi = img - roi
#     image_roi = img - roi
#     # cv2.imshow("image_roi", image_roi)
#     for i in range(image_roi.shape[0]):
#         for j in range(image_roi.shape[1]):
#             if image_roi[i][j].all() != 0:
#                 image_roi[i][j] = 255
#     # cv2.imshow("rois", roi)
#     # cv2.imshow("image_roi", image_roi)
#
#
#
#
#     for i in range(10000):
#         identity = cv2.filter2D(src=img, ddepth=-1, kernel=kernel)
#         conv_image = cv2.bitwise_and(identity, image_roi, mask=None)
#         final2 = roi + conv_image
#         img =final2
#
#     # print("check")
#     img = R
#     roi = Rr
#     img_roi = img - roi
#     image_roi = img - roi
#     # cv2.imshow("image_roi", image_roi)
#     for i in range(image_roi.shape[0]):
#         for j in range(image_roi.shape[1]):
#             if image_roi[i][j].all() != 0:
#                 image_roi[i][j] = 255
#     # cv2.imshow("rois", roi)
#     # cv2.imshow("image_roi", image_roi)
#     #
#
#
#
#
#     for i in range(10000):
#         identity = cv2.filter2D(src=img, ddepth=-1, kernel=kernel)
#         conv_image = cv2.bitwise_and(identity, image_roi, mask=None)
#         final3 = roi + conv_image
#         img = final3
#
#
#     # print("check")
#     # final_image = identity
#     # print("check")
#     # cv2.imwrite("check.png", identity)
#     # print("check")
#     # cv2.imshow('Identity', identity)
#     #
#     #
#     # cv2.imwrite("try.jpg", conv_image)
#     #
#     x = cv2.merge([final1, final2, final3])
#     # print(x.shape)
#     # cv2.imwrite("final.png", final)
#     # cv2.imshow("final", x)
#
#     return x
#
#
# result = image_impainting(img, roi, kernel1)
# result2 = image_impainting(result, roi, kernel2)
#
#
#
# cv2.imshow("final11", result)
# cv2.imshow("final2", result2)
#
#
# a=skimage.metrics.mean_squared_error(img, result)
# b=skimage.metrics.mean_squared_error(img, result2)
# print(a, b)
# cv2.waitKey(0)

