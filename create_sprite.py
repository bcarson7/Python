name = ""

#Build Hull
from PIL import Image
hull = Image.open(name + ".dds")
crophull = hull.crop((87, 113, 886, 1580))
size = 180, 360
crophull.thumbnail(size)
crophull.putpixel((167,329), (0, 0, 0))
crophull.putpixel((168,329), (0, 0, 0))

#Build Wing
wing = Image.open(name + ".dds")
cropwing = wing.crop((21, 1774, 673, 1939))
wsize = 134, 50
cropwing.thumbnail(wsize)
cropwing.rotate(180).save(name + "wing.jpg", "JPEG")

#Build Cockpit - Set black to transparent?
cockpit = Image.open(name + "cockpit.dds")
cropcockpit = cockpit.crop((257, 198, 370, 490))
csize = 30, 90
cropcockpit.thumbnail(csize)

#Build Final Sprite
#wingCopy = cropwing.copy()
wingCopy = Image.open(name + "wing.jpg")
cockpitCopy = cropcockpit.copy()
crophull.paste(wingCopy, (25,0))
crophull.paste(cockpitCopy, (77,215)) #what does 3rd value do?
crophull.save(name +".jpg", "JPEG")
crophull.show()
