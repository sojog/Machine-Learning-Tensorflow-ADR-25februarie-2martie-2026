import numpy as np
from PIL import Image


def create_sweden_flag(height=900, width=1500):
    """
    Creează steagul Suediei ca array NumPy (RGB).
    Dimensiunea este reglabilă.
    """

    # Imagine goală
    flag = np.zeros((height, width, 3), dtype=np.uint8)

    # Culori aproximative oficiale
    blue = [0, 82, 147]
    yellow = [254, 204, 0]

    # Umplem fundalul cu albastru
    flag[:] = blue

    # Proporții clasice nordice:
    # Crucea verticală este poziționată la aproximativ 5/16 din lățime
    vertical_start = width * 5 // 16
    vertical_width = width // 8

    # Crucea orizontală la mijloc
    horizontal_start = height // 2 - height // 10
    horizontal_height = height // 5

    # Bandă verticală
    flag[:, vertical_start:vertical_start + vertical_width] = yellow

    # Bandă orizontală
    flag[horizontal_start:horizontal_start + horizontal_height, :] = yellow

    return flag


# -------------------------
# 1️⃣ Generare steag
# -------------------------
height = 1000
width = 1600

sweden_flag = create_sweden_flag(height, width)

# -------------------------
# 2️⃣ Salvare imagine
# -------------------------
image = Image.fromarray(sweden_flag)
image.save("steag_suedia.png")

print("Imagine salvată ca steag_suedia.png")


# -------------------------
# 3️⃣ Citire imagine
# -------------------------
loaded_image = Image.open("steag_suedia.png")
loaded_array = np.array(loaded_image)

print("Imagine citită din fișier.")
print("Dimensiune:", loaded_array.shape)