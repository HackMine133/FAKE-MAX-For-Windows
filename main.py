import tkinter as tk
from PIL import Image, ImageTk
import math
import webbrowser  # для открытия ссылки
import sys
import os

def resource_path(relative_path):
    """Получает абсолютный путь к ресурсу для работы с PyInstaller"""
    try:
        # PyInstaller создает временную папку в _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class MaxApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MAX")

        # Фиксированное окно
        self.root.geometry("900x600")
        self.root.resizable(False, False)

        # Устанавливаем иконку приложения
        try:
            icon_path = resource_path("maxlogo.png")
            icon_img = Image.open(icon_path)
            self.icon = ImageTk.PhotoImage(icon_img)
            self.root.iconphoto(False, self.icon)
        except Exception as e:
            print(f"Ошибка загрузки иконки: {e}")

        # Загружаем фон
        try:
            bg_path = resource_path("background.jpg")
            bg_img = Image.open(bg_path)
            bg_img = bg_img.resize((900, 600), Image.LANCZOS)
            self.bg = ImageTk.PhotoImage(bg_img)
        except Exception as e:
            print(f"Ошибка загрузки фона: {e}")
            # Создаем черный фон если изображение не загрузилось
            self.bg = None

        # Canvas
        self.canvas = tk.Canvas(self.root, width=900, height=600, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        # Фон
        if self.bg:
            self.canvas.create_image(0, 0, image=self.bg, anchor="nw")
        else:
            self.canvas.configure(bg="black")

        # Логотип
        try:
            logo_path = resource_path("maxlogo.png")
            logo_img = Image.open(logo_path)
            logo_img = logo_img.resize((180, 180), Image.LANCZOS)
            self.logo = ImageTk.PhotoImage(logo_img)
            self.logo_id = self.canvas.create_image(250, 200, image=self.logo)
        except Exception as e:
            print(f"Ошибка загрузки логотипа: {e}")
            self.logo_id = None

        # Текст MAX
        self.canvas.create_text(
            400, 200,
            text="MAX",
            font=("Arial Black", 90, "bold"),
            fill="white",
            anchor="w"
        )

        # Сообщение
        self.canvas.create_text(
            450, 420,
            text="Временно не работает.",
            font=("Arial", 28),
            fill="#CCCCCC"
        )

        # Текст "Обратитесь в поддержку"
        self.support_text = self.canvas.create_text(
            450, 560,
            text="Обратитесь в поддержку",
            font=("Arial", 10, "underline"),
            fill="gray",
            activefill="white"  # цвет при наведении
        )

        # Привязываем клик по тексту
        self.canvas.tag_bind(self.support_text, "<Button-1>", lambda e: webbrowser.open("https://help.max.ru/"))

        # Текст с символом регистрации ®
        self.canvas.create_text(
            450, 580,
            text="MAX © 2025",
            font=("Arial", 10),
            fill="gray"
        )

        # Параметры анимации
        self.angle = 0.1
        self.amplitude = 1
        self.speed = 0.1

        if self.logo_id is not None:
            self.animate_logo()

    def animate_logo(self):
        """Плавное синусоидальное движение"""
        if self.logo_id is not None:
            offset = math.sin(self.angle) * self.amplitude
            self.canvas.coords(self.logo_id, 250, 200 + offset)
            self.angle += self.speed
            self.root.after(20, self.animate_logo)


if __name__ == "__main__":
    root = tk.Tk()
    app = MaxApp(root)
    root.mainloop()