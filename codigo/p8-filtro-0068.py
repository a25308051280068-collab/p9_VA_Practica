# Ejemplo 3
# Numero de lista 24

import cv2

print("Christian Garcia Jimenez Nc = 0068")

# Cargar imagen
imagen = cv2.imread("canguro.jpg")

# Comprobar que la imagen se cargó correctamente
if imagen is None:
    print("Error: no se pudo cargar la imagen canguro.jpg")
    exit()

# Convertir a escala de grises
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Convertir a imagen binaria
_, binaria = cv2.threshold(
    gris,
    127,
    255,
    cv2.THRESH_BINARY
)

# Detectar contornos
contornos, jerarquia = cv2.findContours(
    binaria,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

# Dibujar los contornos
resultado = imagen.copy()

cv2.drawContours(
    resultado,
    contornos,
    -1,
    (0, 255, 0),
    2
)

# Mostrar resultados
cv2.imshow("Imagen original", imagen)
cv2.imshow("Imagen binaria Nc=0068", binaria)
cv2.imshow("Contornos detectados Nc=0068", resultado)

# Guardar resultado
cv2.imwrite("canguro.jpg", resultado)

print("Cantidad de contornos encontrados:", len(contornos))
print("Imagen guardada como canguro.jpg")

# Esperar
cv2.waitKey(0)

# Cerrar ventanas
cv2.destroyAllWindows()

print("Christian Garcia Jimenez Nc = 0068")


