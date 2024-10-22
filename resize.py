import os
from PIL import Image

# Rutas de origen y destino
input_folder = "C:/Users/renjo/OneDrive - Universidad de los andes/PROYECTOS/2024/ACT/COP16/Paz Ambiental y Territorial/Paz-Ambiental-y-Territorial/assets/Selección/3 -"
output_folder = "C:/Users/renjo/OneDrive - Universidad de los andes/PROYECTOS/2024/ACT/COP16/Paz Ambiental y Territorial/Paz-Ambiental-y-Territorial/assets/Espacio3"

# Tamaño máximo: 720px de ancho (ajusta la altura automáticamente)
max_width = 720

# Asegúrate de que la carpeta de destino exista
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Iterar sobre los archivos en la carpeta de origen
for idx, filename in enumerate(os.listdir(input_folder), start=1):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)

        # Calcular nuevo tamaño manteniendo la relación de aspecto
        width_percent = (max_width / float(img.size[0]))
        new_height = int((float(img.size[1]) * float(width_percent)))
        img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)

        # Guardar la imagen redimensionada
        output_path = os.path.join(output_folder, f'{idx}.jpg')  # Renombrar secuencialmente
        img.save(output_path, 'JPEG')

        print(f'{filename} redimensionada y guardada como {idx}.jpg')

print('Proceso completo.')