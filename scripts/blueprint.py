import cv2
import argparse
import numpy as np

def create_blueprint(image_path, output_path):
    # Cargar la imagen de entrada
    image = cv2.imread(image_path)

    if image is None:
        print(f"No se pudo cargar la imagen {image_path}")
        return

    # Convertir la imagen a escala de grises
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Aplicar umbralización para obtener los trazos en blanco
    _, binary_image = cv2.threshold(grayscale_image, 100, 230, cv2.THRESH_BINARY)

    # Invertir los colores para que los trazos sean blancos y el fondo azul
    inverted_image = cv2.bitwise_not(binary_image)

    # Combinar el fondo azul con las líneas blancas
    blueprint_image = cv2.merge([inverted_image, inverted_image, inverted_image])
    # Crear un fondo azul
    blue_background = np.zeros_like(blueprint_image)
    blue_background[:] = (255, 0, 0)  # Código de color azul en formato BGR

    blueprint_image[blueprint_image == 0] = 255

    # Guardar la imagen de salida
    cv2.imwrite(output_path, blueprint_image)

def main():
    parser = argparse.ArgumentParser(description="Generador de planos *blueprint*")
    parser.add_argument("input_image", help="Ruta de la imagen de entrada")
    parser.add_argument("output_image", help="Ruta de la imagen de salida")
    args = parser.parse_args()

    create_blueprint(args.input_image, args.output_image)

if __name__ == "__main__":
    main()
