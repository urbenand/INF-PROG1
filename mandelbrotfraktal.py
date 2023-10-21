import numpy as np
import matplotlib.pyplot as plt

# Funktion zur Berechnung der Mandelbrot-Menge
def mandelbrot(c, max_iterations):
   z = 0
   n = 0
   while abs(z) <= 2 and n < max_iterations:
       z = z*z + c
       n += 1
   return n

# Einstellungen für das Fraktal
width, height = 200, 200
x_min, x_max = -3.0, 1.0
y_min, y_max = -2.0, 2.0
max_iterations = 256

# Erzeuge leeres Bild
img = np.empty((width, height))

# Iteriere über jedes Pixel
for x in range(width):
   for y in range(height):
       # Übersetze Pixelkoordinaten in die komplexe Ebene
       real = x * (x_max - x_min) / (width - 1) + x_min
       imag = y * (y_max - y_min) / (height - 1) + y_min
       c = complex(real, imag)

       # Berechne die Farbe basierend auf den Iterationen
       color = mandelbrot(c, max_iterations)

       # Weise die Farbe dem Pixel zu
       img[x, y] = color

# Darstelle das Mandelbrot-Fraktal
plt.imshow(img, extent=(x_min, x_max, y_min, y_max))
plt.show()