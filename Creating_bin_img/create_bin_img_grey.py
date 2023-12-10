import os
import cv2 as cv
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# dir path of analyze photo
folder_path = r"C:\\Users\\Kasia\\OV_notebooks\\openvino_env\\Scripts\\openvino_notebooks\\notebooks\\000-erytrocyty\\data\\rav"
source_file = "photo_01.png"
img_path = os.path.join(folder_path, source_file)

# chceck if path exist
assert os.path.exists(img_path), "File could not be read, check with os.path.exists()"

# load image in color
img = cv.imread(img_path, cv.IMREAD_COLOR)

# chceck if loaded file exist
assert img is not None, "File could not be read, check if type of image is correct"

# devide image to color channels
b, g, r = cv.split(img)

# # set treshold range
# 195, 146, 208, 196, 170, 217 -> samples of color of an erythrocyte (RGB scale)
range_grey = [130, 200] 

def invert_colors(image):
    return cv.bitwise_not(image)

# Module for update after changing treshold range by slider
def update(val):
    range_grey[0] = grey_slider_min.val
    range_grey[1] = grey_slider_max.val
    
    # devide input picture to objects that has information how color value
    # information is in a pixel
    _, thresh_r = cv.threshold(r, *range_grey, cv.THRESH_BINARY)
    _, thresh_g = cv.threshold(g, *range_grey, cv.THRESH_BINARY)
    _, thresh_b = cv.threshold(b, *range_grey, cv.THRESH_BINARY)
    
    # Connect created binary images
    binary_image = cv.bitwise_and(thresh_r, cv.bitwise_and(thresh_g, thresh_b))
    
    # Conversion to black-white picture
    binary_image[binary_image > 0] = 255
    
    # color inversion -> if black with white needs to be switch, uncomment
    # binary_image = invert_colors(binary_image)
    
    # create binary picture
    binary_image_gray = cv.cvtColor(binary_image, cv.COLOR_GRAY2BGR)
    ax.imshow(cv.cvtColor(binary_image_gray, cv.COLOR_BGR2RGB))
    fig.canvas.draw_idle()

# Creating array with interactive sliders
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.3)

# settings for mininal grey slider
grey_slider_min_ax = plt.axes([0.2, 0.1, 0.65, 0.03], facecolor='lightgoldenrodyellow')
grey_slider_min = Slider(grey_slider_min_ax, 'grey Min', 0, 255, valinit=range_grey[0], valstep=1)

# settings for maximum grey slider
grey_slider_max_ax = plt.axes([0.2, 0.05, 0.65, 0.03], facecolor='lightgoldenrodyellow')
grey_slider_max = Slider(grey_slider_max_ax, 'grey Max', 0, 255, valinit=range_grey[1], valstep=1)

# first trigger of update function, to make picture with set range
update(None)

# Connect slider to update module
grey_slider_min.on_changed(update)
grey_slider_max.on_changed(update)

# print binary picture with settings
plt.xticks([]), plt.yticks([])
plt.show()

"""
old, not working version:
import os
import cv2 as cv
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# dir path of analyze photo
folder_path = r"C:\\Users\\Kasia\\OV_notebooks\\openvino_env\\Scripts\\openvino_notebooks\\notebooks\\000-erytrocyty\\data\\rav"
# set treshold range
range_grey = [150, 255]

# name of analyze photo
source_file = "photo_06.png"
# path of analyze photo
img_path = os.path.join(folder_path, source_file)

# load image in color
img = cv.imread(img_path, cv.IMREAD_COLOR)

# chceck if loaded file exist
assert img is not None, "file could not be read, check with os.path.exists()"

# convert image to grey scale
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, thresh1 = cv.threshold(img, *range_grey, cv.THRESH_BINARY)

def invert_colors(image):
    return cv.bitwise_not(image)

# Module for update after changing treshold range by slider
def update(val):
    range_grey[0] = grey_slider_min.val
    range_grey[1] = grey_slider_max.val
    
    # Konwersja na obraz czarno-biały -> niepotrzebne???!!!
    # gray_img[gray_img > 0] = 255
    
    # create binary picture
    ret, thresh1 = cv.threshold(img, *range_grey, cv.THRESH_BINARY)
    fig.canvas.draw_idle()

# Creating array with interactive sliders
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.3)

# settings for mininal grey slider
grey_slider_min_ax = plt.axes([0.2, 0.1, 0.65, 0.03], facecolor='lightgoldenrodyellow')
grey_slider_min = Slider(grey_slider_min_ax, 'grey Min', 0, 255, valinit=range_grey[0], valstep=1)

# settings for mininal grey slider
grey_slider_max_ax = plt.axes([0.2, 0.05, 0.65, 0.03], facecolor='lightgoldenrodyellow')
grey_slider_max = Slider(grey_slider_max_ax, 'grey Max', 0, 255, valinit=range_grey[1], valstep=1)

# first trigger of update function, to make picture with set range
# update(None)

# Connect slider to update module
grey_slider_min.on_changed(update)
grey_slider_max.on_changed(update)

# print binary picture with settings
plt.imshow(thresh1, 'gray', vmin=0, vmax=255)
plt.xticks([]), plt.yticks([])
plt.show()"""