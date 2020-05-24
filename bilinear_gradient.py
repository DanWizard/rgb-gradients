from PIL import  Image
from random import randint as rint

def generate_color():
    r = rint(0,255)
    g = rint(0,255)
    b = rint(0,255)
    return  [r,g,b]

def formula(start_val, end_val, index, distance):
    return_value = start_val + ((end_val - start_val) * (index/distance))
    return int(return_value)

def bilinear():
    q1 = generate_color()
    q2 = generate_color()
    q3 = generate_color()
    q4 = generate_color()

    img = Image.new("RGBA", (500,500))
    
    for i in range(500):
        q1q4r = formula(q1[0],q4[0], i, 500)
        q1q4g = formula(q1[1],q4[1], i, 500)
        q1q4b = formula(q1[2],q4[2], i, 500)
        q2q3r = formula(q2[0],q3[0], i, 500)
        q2q3g = formula(q2[1],q3[1], i, 500)
        q2q3b = formula(q2[2],q3[2], i, 500)
        for j in range(500):
            r = formula(q1q4r, q2q3r, j, 500)
            g = formula(q1q4g, q2q3g, j, 500)
            b = formula(q1q4b, q2q3b, j, 500)
            img.putpixel((j,i),(r,g,b))
    img.save("1.png", "PNG")

bilinear()