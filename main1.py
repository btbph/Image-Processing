import cv2
import imutils
import numpy as np
import math

img = cv2.imread('./data/Lenna.png', 1)


def find_keypoints(): # добавить сортировку по размеру
    sift = cv2.xfeatures2d.SIFT_create()
    (kp, desc) = sift.detectAndCompute(img, None)
    return kp, desc


def refactor_keypoints(keypoints, image):
    cv2.imshow('keypoints', image)
    img_keypoints = []
    for (i, item) in enumerate(keypoints):
        angle = item.angle
        rows = image.shape[0]
        cols = image.shape[1]
        size = item.size
        rotation_matrix = cv2.getRotationMatrix2D(item.pt, angle, 1.0)
        dst = cv2.warpAffine(image, rotation_matrix, (cols, rows))
        corp = cv2.getRectSubPix(dst, (int(size), int(size)), item.pt)  # возможно другой размер но не суть
        img_keypoints.append(corp)
    return res


res = find_keypoints()
out_img = 0
out_img = cv2.drawKeypoints(img, res[0], out_img, None, 4)
refactor_keypoints(res[0], out_img)
cv2.imwrite('keypointsLenna.jpg', out_img)
cv2.imshow('keypoints', out_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
