name = "thousandtrails"

#Build Hull
from PIL import Image
hull = Image.open(name + ".dds")
crophull = hull.crop((87, 113, 886, 1580))
#size = 180, 360
#crophull.thumbnail(size)
#crophull.putpixel((167,329), (0, 0, 0))
#crophull.putpixel((168,329), (0, 0, 0))

#Build Wing
wing = Image.open(name + ".dds")
cropwing = wing.crop((21, 1774, 673, 1939))
#wsize = 134, 50
#cropwing.thumbnail(wsize)
cropwing.rotate(180).save(name + "wing.jpg", "JPEG")

#Build Canard
canard = Image.open(name + ".dds")
cropcanard = canard.crop((279, 1446, 712, 1559))
#cansize = 120, 40
#cropcanard.thumbnail(cansize)
cropcanard.save(name + "canard.jpg", "JPEG")

#Build Cockpit - Set black to transparent?
#cockpit = Image.open(name + "cockpit.dds")
#cropcockpit = cockpit.crop((257, 198, 370, 490))
#csize = 30, 90
#cropcockpit.thumbnail(csize)
#cropcockpit.save(name + "cockpit.jpg")

#Build Final Sprite
wingCopy = Image.open(name + "wing.jpg")
canardCopy = Image.open(name + "canard.jpg")
cockpitCopy = Image.open(name + "cockpit.jpg")
crophull.paste(wingCopy, (80,0))
#crophull.paste(cockpitCopy, (77,215)) #what does 3rd value do?
crophull.paste(canardCopy, (194, 1140))

#for x1 in range(5):
#    for y1 in range(212):
#        crophull.putpixel((x1,y1),(0,0,0))
#for x2 in range((crophull.width - 5),crophull.width):
#    for y2 in range(211):
#        crophull.putpixel((x2,y2),(0,0,0))

crophull.save(name +".jpg", "JPEG")
crophull.show()
