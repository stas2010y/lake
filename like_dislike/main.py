import tkinter
from PIL import ImageTk, Image
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def like():
    global total_like, likes_label, current_image_index, imege_filenames
    total_like += 1
    likes_label.config(text=f'лайков: {total_like}')
    current_image_index = (current_image_index + 1) % len(imege_filenames)
    update_image

def dislike():
    global total_dislike, dislikes_label, current_image_index, imege_filenames
    total_dislike += 1
    dislikes_label.config(text=f'Дизлайков: {total_dislike}')
    current_image_index = (current_image_index + 1) % len(imege_filenames)
    update_image()


def update_image():
    global imege_label
    # Путь к конкрутному избражению
    imege_path = os.path.join(imege_directory, imege_filenames[current_image_index])

    # Маштабирование полученного избражения и отображение
    image = Image.open(imege_path)
    image = image.resize((300, 200), Image.LANCZOS)
    photo = ImageTk.PhotoImage(image)

    imege_label.config(image=photo)
    imege_label.image = photo


total_like = 0
total_dislike = 0
current_image_index = 0  # Инндекc пути к фотогра

root = tkinter.Tk()
root.title('лайк-дизлайк')
root.geometry('400x450')
root.resizable(False, False)

imege_directory = os.path.join(BASE_DIR, 'images')  # Абсолютный путь к папке с изображении
imege_filenames = sorted(os.listdir(imege_directory))  # Список с изображения



like_image = Image.open(os.path.join(BASE_DIR, 'like.png'))
dislike_image = Image.open(os.path.join(BASE_DIR, 'dislike.png'))
like_image = like_image.resize((100, 100), Image.LANCZOS)
dislike_image = dislike_image.resize((100, 100), Image.LANCZOS)

like_image = ImageTk.PhotoImage(like_image)
dislike_image = ImageTk.PhotoImage(dislike_image)

buttons_frame = tkinter.Frame(root)
buttons_frame.pack(pady=20)

# Путь к конкрутному избражению
imege_path = os.path.join(imege_directory, imege_filenames[current_image_index])

# Маштабирование полученного избражения и отображение

image = Image.open(imege_path)
image = image.resize((300, 200), Image.LANCZOS)
photo = ImageTk.PhotoImage(image)

imege_label = tkinter.Label(root, image=photo)
imege_label.pack(pady=10)

# Создаем и размещаем кнопку лайк
like_button = tkinter.Button(buttons_frame, image=like_image, bd=0, font=('Arial', 18
                                                                          ), command=like)
like_button.pack(side=tkinter.LEFT, padx=10)

# Создаем и размещаем кнопку дизлайк
dislike_button = tkinter.Button(buttons_frame, image=dislike_image, bd=0, font=('Arial', 18), command=dislike)
dislike_button.pack(side=tkinter.RIGHT, padx=10)

#  Создаем контейнер  для кол-ва лайков
likes_label = tkinter.Label(root, text='лайков: 0')
likes_label.pack()

#  Создаем контейнер  для кол-ва лайков
dislikes_label = tkinter.Label(root, text='дизлайков: 0')
dislikes_label.pack()
# Включается программа
root.mainloop()
