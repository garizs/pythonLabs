import os.path

import cv2
import imutils as imutils
import numpy as np
import logging
import logging.config


class FindRectangle:
    def __init__(self, file_path=None):
        self.path = file_path

    def image_find_rectangle(self: str):
        image = cv2.imread(self)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (3, 3), 0)
        edged = cv2.Canny(gray, 10, 250)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
        closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)
        cnts = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        total = 0
        for c in cnts:
            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.02 * peri, True)
            if len(approx) == 4:
                cv2.drawContours(image, [approx], -1, (0, 255, 0), 4)
                total += 1
        cv2.imshow("Image", image)
        cv2.imwrite('result_by_open.jpg', image)
        cv2.waitKey()

    @staticmethod
    def video_find_rectangle():

        def stackImages(scale, img_array):
            rows = len(img_array)
            cols = len(img_array[0])
            rows_available = isinstance(img_array[0], list)
            width = img_array[0][0].shape[1]
            height = img_array[0][0].shape[0]
            if rows_available:
                for x in range(0, rows):
                    for y in range(0, cols):
                        if img_array[x][y].shape[:2] == img_array[0][0].shape[:2]:
                            img_array[x][y] = cv2.resize(img_array[x][y], (0, 0), None, scale, scale)
                        else:
                            img_array[x][y] = cv2.resize(img_array[x][y],
                                                         (img_array[0][0].shape[1], img_array[0][0].shape[0]), None,
                                                         scale, scale)
                        if len(img_array[x][y].shape) == 2:
                            img_array[x][y] = cv2.cvtColor(img_array[x][y],
                                                           cv2.COLOR_GRAY2BGR)
                image_blank = np.zeros((height, width, 3), np.uint8)
                hor = [image_blank] * rows
                hor_con = [image_blank] * rows
                for x in range(0, rows):
                    hor[x] = np.hstack(img_array[x])
                ver = np.vstack(hor)
            else:
                for x in range(0, rows):
                    if img_array[x].shape[:2] == img_array[0].shape[:2]:
                        img_array[x] = cv2.resize(img_array[x], (0, 0), None, scale, scale)
                    else:
                        img_array[x] = cv2.resize(img_array[x], (img_array[0].shape[1], img_array[0].shape[0]), None,
                                                  scale,
                                                  scale)
                    if len(img_array[x].shape) == 2:
                        img_array[x] = cv2.cvtColor(img_array[x], cv2.COLOR_GRAY2BGR)
                hor = np.hstack(img_array)
                ver = hor
            return ver

        def getContours(image, img_cont):
            contours, hierarchy = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
            for cnt in contours:
                area = cv2.contourArea(cnt)
                area_min = cv2.getTrackbarPos("Area", "Parameters")
                if area > area_min:
                    cv2.drawContours(img_cont, cnt, -1, (255, 0, 0), 3)
                    peri = cv2.arcLength(cnt, True)
                    approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
                    x, y, w, h = cv2.boundingRect(approx)
                    cv2.rectangle(img_cont, (x, y), (x + w, y + h), (0, 255, 0), 5)
                    cv2.imwrite("result_by_real_time.jpg", img_cont)

        cap = cv2.VideoCapture(0)
        if cap:
            frame_width = 640
            frame_height = 480
            cap.set(3, frame_width)
            cap.set(4, frame_height)

            def empty(a):
                pass

            cv2.namedWindow("Parameters")
            cv2.resizeWindow("Parameters", 640, 240)
            cv2.createTrackbar("Threshold1", "Parameters", 150, 255, empty)
            cv2.createTrackbar("Threshold2", "Parameters", 255, 255, empty)
            cv2.createTrackbar("Area", "Parameters", 5000, 30000, empty)
            while True:
                success, img = cap.read()
                img_contour = img.copy()

                img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                img_blur = cv2.GaussianBlur(img_gray, (7, 7), 1)

                threshold1 = cv2.getTrackbarPos("Threshold1", "Parameters")
                threshold2 = cv2.getTrackbarPos("Threshold2", "Parameters")
                img_canny = cv2.Canny(img_blur, threshold1, threshold2)
                kernel = np.ones((5, 5))
                img_dil = cv2.dilate(img_canny, kernel, iterations=1)

                getContours(img_dil, img_contour)

                img_blank = np.zeros_like(img)
                img_stack = stackImages(0.8, ([img, img_gray, img_blur],
                                              [img_canny, img_contour, img_blank]))
                cv2.imshow("Stack", img_stack)
                k = cv2.waitKey(33)
                if k == 27:  # Esc key to stop
                    break
            cap.release()
            cv2.destroyAllWindows()
        else:
            logging.error('Камера не найдена!')
