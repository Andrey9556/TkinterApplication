import tkinter as tk
from tkinter import filedialog

class FileViewerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Viewer App") #поменять название
        self.root.geometry("800x600") #Если требуется то поменять размер
        #Поменять расположение кнопок
        # Создание элементов интерфейса
#save
        self.save_button = tk.Button(root, text="Сохранить файл", command=self.save_file)
        self.save_button.place(x=20, y=30)
#open
        self.open_button = tk.Button(root, text="Открыть файл", command=self.open_file)
        self.open_button.place(x=20, y=60)
#text area
        self.text_area = tk.Text(root, wrap=tk.WORD, width=50, height=20)
        self.text_area.pack(side=tk.RIGHT, padx=10, pady=10)
#exit button
        self.exit_button = tk.Button(root, text="Выход", command=root.destroy)
        self.exit_button.place(x=100, y=550)
#clear button
        self.exit_button = tk.Button(root, text="Очистить", command=self.clear_text_area)
        self.exit_button.place(x=20, y=550)

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, 'w', encoding='utf-8') as file:
                file_content = self.text_area.get(1.0, tk.END)
                file.write(file_content)
                
    def clear_text_area(self):
        self.text_area.delete(1.0, tk.END)
        
    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, 'r', encoding='utf-8') as file:
                file_content = file.read()
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, file_content)

if __name__ == "__main__":
    root = tk.Tk()
    app = FileViewerApp(root)
    root.mainloop()
