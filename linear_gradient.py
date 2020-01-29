from PIL import Image,ImageDraw
from random import randint as rint

def formula(start_val, end_val, index, distance):
    return_value = start_val + ((end_val - start_val) * (index/distance-1))
    return int(return_value)

def random_gradient(name):
    img = Image.new("RGB", (500,500), "#FFFFFF")
    draw = ImageDraw.Draw(img)
    #start_color
    r0,g0,b0 =  rint(0,255), rint(0,255), rint(0,255)
    #middle_color
    r1,g1,b1 =  rint(0,255), rint(0,255), rint(0,255)
    #end_color
    # r2,g2,b2 =  rint(0,255), rint(0,255), rint(0,255)
    # r_container = [r0, r1, r2]
    # g_container = [g0, g1, g2]
    # b_container = [b0, b1, b2]
    # color_index = 0
    position = 0
    for i in range(500):
        
        # if i == 250:
        #     color_index += 1
        # if color_index > 0:
        #     position = 0

        print(position)
        r = formula(r0, r1, position, rint(100, 500))
        g = formula(g0, g1, position, rint(100, 500)) 
        b = formula(b0, b1, position, rint(100, 500))
        print(r, g, b)
        position += 1
        draw.line((i, 0, i, 500), fill=(r, g, b))
    img.save(name+".png", "PNG")



if __name__ == "__main__":
    for name in range(1):
        random_gradient(str(name))