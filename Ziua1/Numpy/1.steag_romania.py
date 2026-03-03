import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def create_romanian_flag(height=900, width=1500):
    """
    Creează steagul României ca array NumPy.
    height și width pot fi modificate ulterior.
    """

    # Creăm o imagine goală (RGB)
    flag = np.zeros((height, width, 3), dtype=np.uint8)

    # Calculăm lățimea fiecărei benzi
    stripe_width = width // 3

    # Culori RGB oficiale aproximative
    blue = [0, 43, 127]
    yellow = [252, 209, 22]
    red = [206, 17, 38]

    # Banda albastră (stânga)
    flag[:, 0:stripe_width] = blue

    # Banda galbenă (mijloc)
    flag[:, stripe_width:2*stripe_width] = yellow

    # Banda roșie (dreapta)
    flag[:, 2*stripe_width:width] = red

    return flag


# Exemplu de utilizare
height = 1000   # poți modifica
width = 1800    # poți modifica

romanian_flag = create_romanian_flag(height, width)

# plt.figure(figsize=(12, 7))
# plt.imshow(romanian_flag)
# plt.axis("off")
# plt.title("Steagul României")
# plt.show()

image = Image.fromarray(romanian_flag)
image.save("steag_romania.png")