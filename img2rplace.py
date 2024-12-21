from PIL import Image
import b64coder
import math

PALLETE = [
    (0,0,0),
    (105,105,105),
    (85,85,85),
    (128,128,128),
    (211,211,211),
    (255,255,255),
    (255,153,153),
    (204,51,51),
    (220,20,60),
    (153,0,0),
    (128,0,0),
    (255,87,0),
    (204,255,140),
    (129,222,118),
    (0,111,60),
    (58,85,150),
    (108,173,223),
    (140,217,255),
    (0,255,255),
    (183,125,255),
    (190,69,255),
    (250,57,131),
    (255,153,0),
    (255,230,0),
    (87,52,0)
]

FORCED_SIZE = (64,64)

FILE_PATH = "C:\\Path\\To\\Spy.webp"

img = Image.open(FILE_PATH).convert("RGBA").resize(FORCED_SIZE)
px = img.load()

img_str = ""

for y in range(img.size[1]):
    for x in range(img.size[0]):

        r,g,b,a = px[(x,y)]

        ap = a/255

        r = (r * ap) + (255 * (1-ap))
        g = (g * ap) + (255 * (1-ap))
        b = (b * ap) + (255 * (1-ap))

        closest_color_index = 0
        closest_color_distance = 10000000
        for i,color in enumerate(PALLETE):
            color_distance = math.sqrt((color[0] - r)**2 + (color[1] - g)**2 + (color[2] - b)**2)
            if (color_distance < closest_color_distance):
                closest_color_distance = color_distance
                closest_color_index = i

        img_str += b64coder.ToBase64(closest_color_index)

    img_str += "\n"

print(img_str)