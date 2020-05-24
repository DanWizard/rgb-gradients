from PIL import  Image

img = Image.new("RGBA", (500,500))

for i in range(500):
    for j in range(500):
        img.putpixel((i,j),(0,0,int(j/4)))

img.show()