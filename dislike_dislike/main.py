import tkinter

def like():
    global total_like,likes_label
    total_like +=1
    print (total_like)
    likes_label.config(text=f'лайков: {total_like}')

def dislike():
    global total_dislike,dislikes_label
    total_dislike +=1
    print (total_dislike)
    dislikes_label.config(text=f'Дизлайков: {total_dislike}')

total_like = 0
total_dislike = 0
root = tkinter.Tk()
root.title('лайк-дизлайк')

# Создаем и размещаем кнопку лайк
Like_button = tkinter.Button(root, text='лайк', width = 10, command= like)
Like_button.pack(pady= 10)

# Создаем и размещаем кнопку дизлайк
Like_button = tkinter.Button(root, text= 'Дизлайк', width = 10, command= dislike)
Like_button.pack(pady = 10)

#  Создаем контейнер  для кол-ва
likes_label = tkinter.Label(root, text='лайков: 0')
likes_label.pack()
#  Создаем контейнер  для
dislikes_label = tkinter.Label(root, text='дизлайков: 0')
dislikes_label.pack()


root.mainloop()