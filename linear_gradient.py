from PIL import Image,ImageDraw
from random import randint as rint

def formula(start_val, end_val, index, distance):
    return_value = start_val + ((end_val - start_val) * (index/distance))
    return int(return_value)

def buffer_color(arr_color):
    arr = []
    top_range = 255
    rand_switch = rint(0,2)
    count = 0
    for color in arr_color:
        buffered_color = 0
        if top_range - color < color:
            buffered_color = color - color/2
        else:
            buffered_color = color + color/2
        if rand_switch == count:
            buffered_color = 255 
        arr.append(buffered_color)
        count += 1
    # print(arr_color)
    # print(arr)
    return arr



def random_gradient(name):
    img = Image.new("RGB", (500,500), "#FFFFFF")
    draw = ImageDraw.Draw(img)
    #start_color
    r0,g0,b0 =  rint(0,255), rint(0,255), rint(0,255)
    #middle_color
    r1,g1,b1 =  buffer_color([r0,g0,b0])
    # print(r1,g1,b1)
    #end_color
    r2,g2,b2 =  rint(0,255), rint(0,255), rint(0,255)
    r_container = [r0, r1, r2]
    g_container = [g0, g1, g2]
    b_container = [b0, b1, b2]
    matrix = [r_container, g_container, b_container]
    color_index = 0
    position = 0
    last_index = 0
    for i in range(500):
        # if i == 0: 
        #     continue
        
        if i == 250:
            print(color_index)
            color_index += 1
        if color_index > last_index:
            print(position)
            position = 0
            last_index = color_index

        # print(position)
        r = formula(matrix[0][color_index], matrix[0][color_index+1], position, 250)
        g = formula(matrix[1][color_index], matrix[1][color_index+1], position, 250) 
        b = formula(matrix[2][color_index], matrix[2][color_index+1], position, 250)
        # print(r, g, b)
        position += 1
        draw.line((i, 0, i, 500), fill=(r, g, b))
    img.save(name+".png", "PNG")



if __name__ == "__main__":
    for name in range(1):
        random_gradient(str(name))