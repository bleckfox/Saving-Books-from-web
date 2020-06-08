import os, img2pdf, natsort

dirname = os.path.dirname(r'F:\Code\Python\BooksLoader\test.py')
book_name = 'Test'
book_dir = r'\\' + book_name
path_to_img=dirname+book_dir

with open(str(book_name) + ".pdf","wb") as f:
    img = []
    for fname in os.listdir(path_to_img):
        if not fname.endswith(".png"):
            continue
        path = os.path.join(path_to_img, fname)
        if os.path.isdir(path):
            continue
        img.append(path)
    f.write(img2pdf.convert(natsort.natsorted(img)))