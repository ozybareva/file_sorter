import os
import shutil

from datetime import date
from pathlib import Path
from tkinter import Tk, Frame, Label, Button, Entry


class FileSorter:
    def __init__(self):
        self.path_to_images_tf = None
        self.window = Tk()
        self.frame = Frame(
            self.window,
            padx=10,
            pady=10
        )
        self.path_to_images = Label(
            self.frame,
            text="Введите путь к папке с изображениями"
        )
        self.cal_btn = Button(
            self.frame,
            text='Разложить по папкам',
            command=self.move_images_to_new_dir
        )

    def start_window(self):
        self.window.title('Сортировка изображений')
        self.window.geometry('600x600')

        self.frame.pack(expand=True)
        self.path_to_images.grid(row=3, column=1)

        self.path_to_images_tf = Entry(self.frame)
        self.path_to_images_tf.grid(row=4, column=1, pady=15)

        self.cal_btn.grid(row=5, column=1)

    def move_images_to_new_dir(self):
        path_to_dir = Path(self.path_to_images_tf.get())
        for image in path_to_dir.rglob("*"):
            if os.path.isfile(image):
                try:
                    created_date = date.fromtimestamp(os.path.getmtime(image))
                    created_year = created_date.year
                    new_path_to_dir = f'{path_to_dir}/{created_year}/{created_date}'
                    os.makedirs(new_path_to_dir, exist_ok=True)
                    shutil.move(src=f'{image}', dst=f'{new_path_to_dir}')
                except Exception:
                    break


if __name__ == "__main__":
    file_sorter = FileSorter()
    file_sorter.start_window()
    file_sorter.window.mainloop()
