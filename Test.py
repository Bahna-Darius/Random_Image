import PIL
import os
import textwrap
import random

from PIL import Image, ImageDraw, ImageFont


image_dir = "imagess"
images = [os.path.join(image_dir, f)for f in os.listdir(image_dir)if f.endswith(".jpg")]
random_image=random.choice(images)
image = Image.open(random_image)
draw = ImageDraw.Draw(image)

# Text 1-   Titlul Evenimentului:
text = "Seara de a ne juca pe Laptop la Sebi!"

wrapped_text = textwrap.wrap(text, width=35)
font_path = "C:/Windows/Fonts/Arial.ttf"
# Aici mai jos putem modifica marimea Textului:
font = ImageFont.truetype(font_path, size=70)
font_size=30
color = (255, 255, 255)
x=550
y=100
draw.text((x, y), text, font=font, fill=color)

# Text 2-    Aici va fi Tema de discutie:
text2 ="Wow"

font2 = ImageFont.truetype("arial.ttf", size=50)
font_size2=36
color2 =(255, 255, 255)

x2= random.randint(0, image.size[0])
x2=670
text2_bbox = draw.textbbox((0, 0), text2, font=font2)
y2 = image.size[1] - text2_bbox[3]
y2=670
draw.text((x2,y2), text2, font=font2, fill=color2)

# Text 3- Data
text3="Duminica \n 17 Aprilie"

font3 = ImageFont.truetype("arial.ttf", size=40)
font_size3=36
color3 =(255, 255, 255)

x3= random.randint(0, image.size[0])
x3 =740
text3_bbox = draw.textbbox((0, 0), text3, font=font3)
y3 = image.size[1] - text3_bbox[3]
y3 =740
draw.text((x3,y3), text3, font=font3, fill=color3)

# Text 4- Ora
text4 = "18:00"

font4 = ImageFont.truetype("arial.ttf", size=40)
font_size4=40
color4 =(255, 255, 255)

x4= random.randint(0, image.size[0])
x4=770
text4_bbox = draw.textbbox((0, 0), text4, font=font4)
y3= image.size[1] - text4_bbox[3]
y4=500
draw.text((x4,y4), text4, font=font4, fill=color4)

# draw.line([(0, y3 + font3.getbbox(text3)[1] + 25), (image.size[0], y2 + font3.getbbox(text3)[1] + 25)], fill=(255, 255, 255), width=3)


# Locul in care se va Salva Poza:
image.save("C:/Users/Darius/Downloads/imagine_modificata.jpg")

x = 3



















