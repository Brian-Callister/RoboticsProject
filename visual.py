import os

import cv2
import numpy as np

'''
maybe a model like this would be okay?
-------------
| 0 | 1 | 2 |
-------------
'''
# once it finds the ball this will be set with codes 0 - 8 found above

'''
detecting circles - https://www.pyimagesearch.com/2014/07/21/detecting-circles-images-using-opencv-hough-circles/
                  - https://www.instructables.com/Detecting-Circles-With-OpenCV-and-Python/
                            - his code - https://content.instructables.com/ORIG/FYS/C6X1/IKECQ3CY/FYSC6X1IKECQ3CY.py
            - hough circle Off Doc - https://docs.opencv.org/2.4/modules/imgproc/doc/feature_detection.html
            - param 1 and param 2 explained - https://dsp.stackexchange.com/questions/22648/in-opecv-function-hough-circles-how-does-parameter-1-and-2-affect-circle-detecti
'''


def find_ball(img):
    ballSegment = None

    # -d configure which camera device to use
    # -r Size of foto
    # -S visibility range 1 - 10 if parameter not set or set to 0 foto will be black
    # if path not specified /home/pi is the default
    # EXAMPLE: "fswebcam -d /dev/video0 --no-banner -r 320x240 -S 10 /home/pi/foto.jpg

    dirFoto = "/home/pi/"
    imageName = "camView.jpg"
    commandToTakeFoto = "fswebcam -d /dev/video0 --no-banner -r 320x240 -S 10 " + dirFoto + imageName
    print("openCV version: " + cv2.__version__)

    # dir = "pictures/"
    # current = dir
    # directory = os.listdir(current)
    # imagesWithCircles = 0
    # for im in directory:

    image = cv2.imread(img)

    # resizing maybe use scale?
    scale_percent = 220  # percent of original size
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)
    print("image width (in pixels): " + str(width))
    widthOneSeg = width / 3

    # resize image
    image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
    # image = cv2.resize(image, (224,224), interpolation=cv2.INTER_AREA)
    output = image.copy()

    # display the image width, height, and number of channels
    # (h, w, c) = image.shape[:3]
    # print("width: {} pixels".format(w))
    # print("height: {}  pixels".format(h))
    # print("channels: {}".format(c))

    # converting image to gray color
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # blurring image
    # gray = cv2.GaussianBlur(gray, (3, 3), cv2.BORDER_DEFAULT)
    gray = cv2.blur(gray, (3, 3))

    # show image and wait for keypress
    # cv2.imshow("Image", gray)
    # cv2.waitKey(0)

    # circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 1000, param1=30, param2=65, minRadius=0, maxRadius=0) todo from Shubham Chopra
    # detect circles in the image - doesnt detect tiny ball in ball5.jfif (should be smaller than camera feed finds)
    # circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 2.2, 1000, param1=60, param2=80, minRadius=0, maxRadius=200)
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 2.2, 1000, param1=60, param2=80, minRadius=0, maxRadius=200)
    # ensure at least some circles were found
    if circles is not None and circles[0] is not None and circles[0][0] is not None:
        # convert the (x, y) coordinates and radius of the circles to integers
        circles = np.round(circles[0, :]).astype("int")
        # loop over the (x, y) coordinates and radius of the circles
        for (x, y, r) in circles:
            # draw the circle in the output image, then draw a rectangle
            # corresponding to the center of the circle
            cv2.circle(output, (x, y), r, (0, 255, 0), 4)
            cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
            cv2.line(output, (int(widthOneSeg), 1), (int(widthOneSeg), int(height)), (0, 0, 255), 2)
            cv2.line(output, (int(width - widthOneSeg), 1), (int(width - widthOneSeg), int(height)), (0, 0, 255), 2)

            # todo: do math to place ball in one of the 3 x 3 segments and set ballSegment to code number
            if x < widthOneSeg:
                ballSegment = 0
            elif x >= widthOneSeg and x < width - widthOneSeg:
                ballSegment = 1
            elif x >= width - widthOneSeg:
                ballSegment = 2
        # show the output image
        print("showing image")
        # cv2.imshow("Image", output)
        # cv2.waitKey(0)
        print("Circle Found")
        # imagesWithCircles += 1
        return ballSegment
    else:
        print("found no circles")
        ballSegment = -1
        return ballSegment
    # print(imagesWithCircles)

# load in image here
# img = ""

# can get an image as input to our function TESTING PURPOSES
# find_ball(img)

