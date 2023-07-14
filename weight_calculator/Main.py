import tkinter
from PIL import ImageTk, Image


def calculate():
    try:
        height = float(height_entry.get())
        weight = float(weight_entry.get())

        result = weight / (height ** 2)

        result_label.config(text=f'Индекс массы тела: {result:.2f}')
    except ValueError:
        result_label.config(text=f'Данные должны иметь числовой тип')


root = tkinter.Tk()  # Инициализаци окна
root.title('калькулятор веса')
root.geometry('800x600')  # установка размеров окна в писелях

# Загрузка фона
background_image = Image.open('blue-office-stationery-with-copy-space.jpg')
window_width = 800
window_height = 600

# Масштабирование изображения фона под размер окна
background_image = background_image.resize((window_width, window_width), Image.LANCZOS)
root.geometry(f'{window_width}x{window_height}')  # Установка размеров окна в пиксиле
background_photo = ImageTk.PhotoImage(background_image)
background_label = tkinter.Label(root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
root.resizable(False,False)

# Поле для ввода роста

height_label = tkinter.Label(root, text='Рост (м):', font=('Arial', 14), fg='black', bg='white')
height_label.place(relx=0.5, rely=0.4, anchor='center')
height_entry = tkinter.Entry(root, font=('Arial', 14))
height_entry.place(relx=0.5, rely=0.45, anchor="center")

# Поле для ввода веса
weight_label = tkinter.Label(root, text='Вес (кг)', font=("Arial", 14), fg="black", bg='white')
weight_label.place(relx=0.5, rely=0.5, anchor="center")
weight_entry = tkinter.Entry(root, font=('Arial', 14))
weight_entry.place(relx=0.5, rely=0.55, anchor="center")

button = tkinter.Button(root, text='Расчитать', font=('Arial', 14), command=calculate,
                        bg='#4CAF50', activebackground='#45A049', activeforeground='white')
button.place(relx=0.5, rely=0.68 , anchor="center")

result_label = tkinter.Label(root, font=('arial', 14), bg='white', fg="black")
result_label.place(relx=0.5, rely=0.75, anchor='center')
root.mainloop()
