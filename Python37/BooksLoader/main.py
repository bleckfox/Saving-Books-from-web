# -*- coding: utf-8 -*-
import os
import requests
import bs4
import img2pdf
import natsort
import datetime
import pyperclip
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.title('Скачать книгу с сайта chem21.info')
width, height = 400,200
root.maxsize(width, height)
root.minsize(width, height)

canvas = tk.Canvas(root, width=width, height=height, bg = '#f8f8f8', relief = 'groove')
canvas.pack()

#Menu --helpMe вызывает окно справки----------------------------------------------------
def helpMe():
    top = tk.Toplevel()
    top.title('Справка')
    width, height = 450, 210
    top.maxsize(width, height)
    top.minsize(width, height)
    msg = tk.Label(top, text="Копируем ссылку из браузера. Она должна иметь вид \n-> https://chem21.info/...\n"
                             "Ставим ссылку комбинацией клавиш Ctrl+V. \nИли нажимаем кнопку 'Вставить ссылку'.\n"
                             "Кнопка 'Очистить строку' очищает поле ввода.\n"
                             "Выбираем место, куда будем загружать и название книги.\n"
                             "Жмем кнопку 'Поехали', и ожидаем завершения.")
    msg.config(justify='left', font=('calibri', 11), height=8, width=50)
    msg.pack()
    closeButton = tk.Button(top, text='Закрыть', command=top.destroy, relief='groove', width=10, font=('calibri', 11))
    closeButton.pack()

menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Справка", command=helpMe)
menubar.add_cascade(label="Помощь", menu=filemenu)
root.config(menu=menubar)

# Label--------------------------------------------------------------------------------
label = tk.Label(root, text='Сюда поставить ссылку', bg = '#f8f8f8', font=('calibri', 11))
canvas.create_window(95, 30, window=label)

#Line edit field-------------------------------------------------------------------------
linkField = tk.Entry(root, width = 50, font=('calibri', 11))
canvas.create_window(200, 60, window=linkField)
# Load done------------------------------------------------------------------------------
def loadDone():
    top = tk.Toplevel()
    top.title('Готово')
    width, height = 250, 200
    top.maxsize(width, height)
    top.minsize(width, height)
    msg = tk.Label(top, text="Загрузка завершена.\nНачало загрузки - %s \nКонец загрузки - %s" % (startTime, endTime))
    msg.config(justify='left', font=('calibri', 11), height=8, width=50)
    msg.pack()
    closeButton = tk.Button(top, text='Закрыть', command=top.destroy, relief='groove', width=10, font=('calibri', 11))
    closeButton.pack()

#Start Button---------------------------------------------------------------------------
def startCreate():
    global startTime, endTime
    dirname = os.path.dirname(save_file_path)  # получаем путь до папки, в которой храним книгу
    book_name = os.path.basename(save_file_path)[:-4]  # получаем имя файла, под которым храним книгу
    os.makedirs(book_name, exist_ok=True)  # создаем папку с именем книги
    book_dir = r'\\' + book_name  # имя папки, в которой храним книгу
    path_to_book = dirname + book_dir  # путь до картинок книги, для объединения в pdf
    linkAddress = linkField.get()  # получаем адресс ссылки до книги
    main_url = 'https://chem21.info'
    url = linkAddress
    counter = 1  # счетчик для названия картинок
    sTime = datetime.datetime.now()
    startTime = sTime.strftime("%H:%M:%S")
    # Скачиваем страницу
    while not url.endswith('#'):
        res = requests.get(url)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, features='html.parser')

        # Выбираем картинку из всей страницы
        imgElement = soup.select('nav.sidebar img')
        if imgElement == []:
            print('Не найдено изображение')
        else:
            imgURL = main_url + imgElement[0].get('src')
            # Скачиваем картинку
            img = requests.get(imgURL)
            img.raise_for_status()
            imgFile = open(os.path.join(book_name, str(counter) + os.path.basename(imgURL)[-4:]), 'wb')
            for i in img.iter_content(100000):
                imgFile.write(i)
            imgFile.close()

        # Получаем ссылку на следующую страницу
        nextPage = soup.select('nav.sidebar p > a')[1]
        if nextPage.text == '[Стр. >>]':
            url = main_url + nextPage.get('href')
        else:
            break
        counter += 1

    # Создаем PDF-------------------------------------------------
    with open(str(book_name) + '.pdf', 'wb') as pdf:
        img = []
        for filename in os.listdir(path_to_book):
            # Если имя файла не заканчивается на '.png', то продолжить
            if not filename.endswith('.png'):
                continue
            # получаем путь до картинки
            path = os.path.join(path_to_book, filename)
            # Если это папка, то продолжить
            if os.path.isdir(path):
                continue
            img.append(path)    # дополняем список картинок
        # конвертируем в pdf сортированный список картинок
        pdf.write(img2pdf.convert(natsort.natsorted(img)))
        eTime = datetime.datetime.now()
        endTime = eTime.strftime("%H:%M:%S")

    loadDone()

startButton = tk.Button(root, text='Поехали!', command=startCreate, relief='groove', font=('calibri', 11))
canvas.create_window(60, 160, window=startButton)

# Save Button-------------------------------------------------------------------------
def saveLocation():
    global save_file_path
    save_file_path = filedialog.asksaveasfilename(defaultextension='.pdf',
                                                  filetypes=(("PDF files", "*.pdf"),("All files", "*.*")))

saveButton = tk.Button(root, text='Куда сохранить?', command=saveLocation, relief='groove', font=('calibri', 11))
canvas.create_window(240, 160, window=saveButton)

# Insert Link Button-----------------------------------------------------------------
def insertLink():
    linkField.insert(0,pyperclip.paste())

insertButton = tk.Button(root, text='Вставить ссылку', command=insertLink, relief='groove', font=('calibri', 11))
canvas.create_window(80, 100, window=insertButton)

# Delete Link field Button------------------------------------------------------------
def deleteField():
    linkField.delete(0,'end')

deleteButton = tk.Button(root, text='Очистить строку', command=deleteField, relief='groove', font=('calibri', 11))
canvas.create_window(240, 100, window=deleteButton)

if __name__ == '__main__':
    canvas.mainloop()
