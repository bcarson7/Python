name = " "

from PIL import Image

img = Image.open(name + "cockpit.dds")
img = img.convert("RGBA")
datas = img.getdata()

newData = []
for item in datas:
    if item[0] == 0 and item[1] == 0 and item[2] == 0:
        newData.append((0, 0, 0, 255))
    else:
        newData.append(item)

img.putdata(newData)
img.save(name + "cockpit.png", "PNG")
