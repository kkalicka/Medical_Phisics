import os
import cv2 as cv
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

folder_path = r"C:\\Users\\Kasia\\OV_notebooks\\openvino_env\\Scripts\\openvino_notebooks\\notebooks\\000-erytrocyty\\data\\rav"

def invert_colors(image):
    return cv.bitwise_not(image)

# Funkcja do aktualizacji obrazu po zmianie wartości slidera
def update(val): 
    _, thresh_r = cv.threshold(r, *range_red, cv.THRESH_BINARY)
    _, thresh_g = cv.threshold(g, *range_green, cv.THRESH_BINARY)
    _, thresh_b = cv.threshold(b, *range_blue, cv.THRESH_BINARY)
    
    # Połączenie binaryzowanych kanałów
    binary_image = cv.bitwise_and(thresh_r, cv.bitwise_and(thresh_g, thresh_b))
    
    # Konwersja na obraz czarno-biały
    binary_image[binary_image > 0] = 255
    
    # Inwersja kolorów
    # binary_image = invert_colors(binary_image)
    
    # Konwersja na obraz w odcieniach szarości
    binary_image_gray = cv.cvtColor(binary_image, cv.COLOR_GRAY2BGR)
    
    ax.imshow(cv.cvtColor(binary_image_gray, cv.COLOR_BGR2RGB))
    fig.canvas.draw_idle()

# define which number of rav photos would be used to create bin
file_min = 1
file_max = 3
file_names = ["photo_{:02d}.png".format(name) for name in range(file_min, file_max + 1)]
# source_file = "photo_01.png"

for file_name in file_names:

    img_path = os.path.join(folder_path, file_name)

    # Sprawdź, czy plik istnieje
    assert os.path.exists(img_path), "File could not be read, check with os.path.exists()"

    # Wczytaj obraz
    img = cv.imread(img_path, cv.IMREAD_COLOR)

    # Sprawdź, czy obraz został poprawnie wczytany
    assert img is not None, "File could not be read, check with os.path.exists()"

    # Podziel obraz na kanały kolorów
    b, g, r = cv.split(img)

    # Ustaw początkowe zakresy wartości dla progów binaryzacji dla kanałów czerwonego, zielonego i niebieskiego
    # 195, 146, 208, 196, 170, 217 -> samples of color of an erythrocyte
    range_red = [150, 255] 
    range_green = [200, 255]
    range_blue = [130, 230]
    # Binaryzacja kanałów czerwonego, zielonego i niebieskiego na podstawie zakresów wartości
    _, thresh_r = cv.threshold(r, *range_red, cv.THRESH_BINARY)
    _, thresh_g = cv.threshold(g, *range_green, cv.THRESH_BINARY)
    _, thresh_b = cv.threshold(b, *range_blue, cv.THRESH_BINARY)

    # Połączenie binaryzowanych kanałów
    binary_image = cv.bitwise_and(thresh_r, cv.bitwise_and(thresh_g, thresh_b))

    # Konwersja na obraz czarno-biały
    binary_image[binary_image > 0] = 255  # Wszystkie wartości różne od zera ustawiane są na 255

    # Konwersja na obraz w odcieniach szarości
    binary_image = cv.cvtColor(binary_image, cv.COLOR_GRAY2BGR)

    # Tworzenie interaktywnego wykresu z suwakami
    fig, ax = plt.subplots()
    plt.subplots_adjust(bottom=0.3)

    update(None)
    plt.savefig(f"{file_name}_bin.png")
    plt.show()