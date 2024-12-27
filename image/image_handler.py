from PIL import Image
import os

class ImageHandler:
    def __init__(self, filepath):
        self.filepath = filepath
        self.image = Image.open(filepath)

    def resize_image(self, size=(300, 300)):
        self.image = self.image.resize(size)

    def set_image(self, image):
        self.image = image

    def save_image(self, save_path):
        self.image.save(save_path)
        print(f"Изображение сохранено как {save_path}")

    def get_image(self):
        return self.image