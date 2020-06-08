import os, requests, bs4

main_url = 'https://chem21.info'
url = 'https://chem21.info/page/043168248087208212074211060242166245226250019034'
book_name = 'Test'
os.makedirs(book_name, exist_ok=True)
counter = 1
while not url.endswith('#'):
    # Download Page
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, features='html.parser')

    # Select image element
    imgElem = soup.select('nav.sidebar img')
    if imgElem == []:
        print('Не найдено изображение')
    else:
        imgUrl = main_url + imgElem[0].get('src')
        # Download Image
        img = requests.get(imgUrl)
        img.raise_for_status()
        imgFile = open(os.path.join(book_name,str(counter) + os.path.basename(imgUrl)[-4:]), 'wb')
        for i in img.iter_content(100000):
            imgFile.write(i)
        imgFile.close()

    # Getting next page link
    nextPage = soup.select('nav.sidebar p > a')[1]
    if nextPage.text == '[Стр. >>]':
        url = main_url + nextPage.get('href')
    else:
        break
    counter+=1
# Гоголин
#https://www.chem21.info/page/034076236225208254222132025151124054179200018214/

# Курылев
#https://chem21.info/pic1/209249094148194038142047049062036162089245040079.png
