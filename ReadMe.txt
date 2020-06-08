На русском, ниже на английском. In Russian, below in English.

Проект скачивания книг с веб-сайта chem21.info.
На данном сайте находятся книги по технической тематики, некоторые книги больше нигде не найти. Но на сайте можно просматривать только по одной странице книги за раз, что весьма не удобно в плане навигации по книге. Поэтому была создана данная небольшая программа для скачивания книг с этого сайта. Страницы книги в форме картинок скачиваются с сайта на устройство, затем объединяются в формате .pdf

Выше вы найдете две папки.
В папке Python37 хранится весь программный код + файл .exe, полученный с помощью PyInstaller

В папке C Sharp хранятся 3 вложеные папки.
В папке Fix Error находятся файлы консольного проекта для установки библиотек Python для корректной работы программы. Fix Error -> bin -> Release -> .exe файл
--
В папке Installer находятся файлы программы устновщика для данной программы. Installer -> Release -> .exe or .msi файл
--
В папке Main Exe находятся файлы консольного проекта для запуска Python скрипта. Main Exe -> bin -> Release -> .exe файл

Сценарий 1. На устройстве установлен Python 3.x.
Скачиваем установщик программы из CSharp -> Installer. Затем запускаем "Загрузка книг.exe" - готово. Если будет получена ошибка, то сначала запускаем файл "Исправить ошибку.exe"

Сценарий 2. На устройстве нет Python 3.x или несколько версий сразу.
Скачиваем .exe файл из папки Python37, запускаем - готово.
Или скачиваем код вместе с виртуальной средой (virtualenv) и запускаем скрипт напрямую - готово.

------
English version.

Project for downloading books from a website chem21.info.
This site contains books on technical topics, some books can not be found anywhere else. But on the site you can only view one page of the book at a time, which is very inconvenient in terms of navigating the book. Therefore, this small program was created to download books from this site. Pages of the book in the form of images are downloaded from the site to the device, then combined in .pdf format

You will find two folders above.
The Python37 folder stores all the program code + the .exe file obtained using PyInstaller

The C Sharp folder contains 3 subfolders.
The Fix Error folder contains the console project files for installing Python libraries for the correct operation of the program. Fix Error - > bin -> Release ->. exe file
--
The Installer folder contains the installer program files for this program. Installer -> Release ->. exe or. msi file
--
The Main Exe folder contains the console project files for running the Python script. Main Exe -> bin -> Release ->. exe file

Script 1.Python 3.x is installed on the device.
Download the program installer from CSharp - > Installer. Then run "Download Knigge" - ready. If an error is received, first run the file " Fix the error.exe"

Script 2.the device does not Have Python 3. x or multiple versions at once.
Download the. exe file from the Python37 folder, run it-done.
Or download the code together with the virtual environment (virtualenv) and run the script directly - done.