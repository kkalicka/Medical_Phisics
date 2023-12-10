import os
import cv2 as cv
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# dir path of analyze photo
folder_path = r"C:\\Users\\Kasia\\OV_notebooks\\openvino_env\\Scripts\\openvino_notebooks\\notebooks\\000-erytrocyty\\data\\rav"


def draw_histogram(image, channel, title):
    # Calculate histogram for 256 canals
    hist = cv.calcHist([image], [channel], None, [256], [0, 256])

    # draw histogram with settings below
    plt.plot(hist, color='gray')
    plt.title(title)
    plt.xlabel('Wartość piksela')
    plt.ylabel('Ilość pikseli')
    plt.xlim([0, 256])
    plt.show()

# name of analyze photo
source_file = "photo_01.png"
# path of analyze photo
img_path = os.path.join(folder_path, source_file)

# load image in color
img = cv.imread(img_path, cv.IMREAD_COLOR)

assert img is not None, "file could not be read, check with os.path.exists()"

# convert image to grey scale
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Draw histogram in gray scale for canals 0-255
draw_histogram(gray_img, 0, 'Histogram dla kanału 0')