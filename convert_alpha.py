from PIL import Image

img = Image.open('thousandtrailscockpit.dds')
img = img.convert("RGBA")
datas = img.getdata()

newData = []
for item in datas:
    if item[0] < 5 and item[1] < 5 and item[2] < 5:
        newData.append((0, 0, 0, 0))
    else:
        newData.append(item)

img.putdata(newData)
img.save("thousandtrailscockpit.png", "PNG")
