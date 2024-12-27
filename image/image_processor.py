from PIL import ImageFilter, ImageDraw, ImageFont

class ImageProcessor:
    def __init__(self, image):
        self.image = image

    def apply_blur(self):
        self.image = self.image.filter(ImageFilter.BLUR)

    def add_text(self, text, position, font_path="arial.ttf"):
        draw = ImageDraw.Draw(self.image)
        font = ImageFont.truetype(font_path, 20)
        text_bbox = draw.textbbox((0, 0), text, font=font)
        position = (self.image.width - text_bbox[2] - 10, self.image.height - text_bbox[3] - 10)
        draw.text(position, text, (255, 255, 255), font=font)

    def get_image(self):
        return self.image