import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk  # Импортируем модуль Pillow

class FileViewerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Viewer App")
        self.root.geometry("800x600")

        # Загружаем изображения для кнопок
        self.img1 = ImageTk.PhotoImage(Image.open("images/img1.png"))
        self.img2 = ImageTk.PhotoImage(Image.open("images/img2.png"))
        self.img3 = ImageTk.PhotoImage(Image.open("images/img3.png"))
        self.img4 = ImageTk.PhotoImage(Image.open("images/img4.png"))

        # Создание элементов интерфейса
        self.save_button = tk.Button(root, text="Сохранить файл", command=self.save_file, image=self.img1, compound="left")
        self.save_button.pack(side=tk.TOP, padx=10, pady=10)

        self.open_button = tk.Button(root, text="Открыть файл", command=self.open_file, image=self.img2, compound="left")
        self.open_button.pack(side=tk.TOP, padx=10, pady=10)

        self.new_text_area_button = tk.Button(root, text="Очистить", command=self.create_new_text_area, image=self.img4, compound="left")
        self.new_text_area_button.pack(side=tk.TOP, padx=10, pady=10)

        self.exit_button = tk.Button(root, text="Выход", command=root.destroy, image=self.img3, compound="left")
        self.exit_button.pack(side=tk.BOTTOM, pady=10)

        self.text_area = tk.Text(root, wrap=tk.WORD, width=50, height=20)
        self.text_area.pack(side=tk.RIGHT, padx=10, pady=10)

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, 'w', encoding='utf-8') as file:
                file_content = self.text_area.get(1.0, tk.END)
                file.write(file_content)

    def clear_area(self):
        self.text_area.delete(1.0, tk.END)
    
    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, 'r', encoding='utf-8') as file:
                file_content = file.read()
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, file_content)

    def create_new_text_area(self):
        self.text_area.destroy()
        self.text_area = tk.Text(self.root, wrap=tk.WORD, width=50, height=20)
        self.text_area.pack(side=tk.RIGHT, padx=10, pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = FileViewerApp(root)
    root.mainloop()
