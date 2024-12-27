import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import ImageTk, Image, ImageFont
from image.handler import ImageHandler
from image.processor import ImageProcessor

class ImageApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Редактор Изображений")

        self.image_label = tk.Label(root)
        self.image_label.pack()

        self.button_frame = tk.Frame(root)
        self.button_frame.pack()

        self.load_button = tk.Button(self.button_frame, text="Загрузить изображение", command=self.load_image)
        self.load_button.grid(row=0, column=0)

        self.resize_button = tk.Button(self.button_frame, text="Изменить размер", command=self.resize_image)
        self.resize_button.grid(row=0, column=1)

        self.blur_button = tk.Button(self.button_frame, text="Применить размытие", command=self.apply_blur)
        self.blur_button.grid(row=0, column=2)

        self.text_button = tk.Button(self.button_frame, text="Добавить текст", command=self.add_text)
        self.text_button.grid(row=0, column=3)

        self.save_button = tk.Button(self.button_frame, text="Сохранить изображение", command=self.save_image)
        self.save_button.grid(row=0, column=4)

        self.handler = None
        self.processor = None

    def load_image(self):
        try:
            file_path = filedialog.askopenfilename(title="Выберите изображение", 
                                                   filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp *.gif")])
            if file_path:
                self.handler = ImageHandler(file_path)
                self.processor = ImageProcessor(self.handler.get_image())
                self.show_image(self.handler.get_image())
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось загрузить изображение: {e}")

    def resize_image(self):
        if self.handler:
            self.handler.resize_image((300, 300))
            self.processor = ImageProcessor(self.handler.get_image())
            self.show_image(self.handler.get_image())

    def apply_blur(self):
        if self.processor:
            self.processor.apply_blur()
            self.handler.set_image(self.processor.get_image())
            self.show_image(self.processor.get_image())

    def add_text(self):
        if self.processor:
            self.processor.add_text("Вариант 1", (0, 0), font_path="arial.ttf")
            self.handler.set_image(self.processor.get_image())
            self.show_image(self.processor.get_image())

    def save_image(self):
        if self.handler:
            save_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                     filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
            if save_path:
                self.handler.save_image(save_path)

    def show_image(self, img):
        img_tk = ImageTk.PhotoImage(img)
        self.image_label.config(image=img_tk)
        self.image_label.image = img_tk

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageApp(root)
    root.mainloop()
