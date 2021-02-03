from PIL import Image
sekil=Image.open("huseyn.png")
blackAndWhite=Image.convert("L")
blackAndWhite.save("effectphoto.png")
blackAndWhite.show()