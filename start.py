from PIL import Image, ImageFont, ImageDraw
import textwrap

# The function is responsible to position the text in center of the image
def center_text(img, font, text, color=(50, 50, 50)):
    draw = ImageDraw.Draw(img)
    text_width, text_height = draw.textsize(text, font)
    position = ((strip_width-text_width)/2,(strip_height-text_height)/2)
    draw.text(position, text, color, font=font)
    img.save('example.png')

# Dimensions of the background
# 1080 x 1080 is the default for instagram posts
strip_width, strip_height = 1080, 1080

# Add the text which needs to be on the image
text = """The greatest glory in living lies not in never falling, but in rising every time we fall."""

# Setting up the background params
background = Image.new('RGB', (strip_width, strip_height), color=(248, 236, 236)) 

# Using the default times font with size 60
font = ImageFont.truetype("times", 60)

# Splitting up the text to create a text wrap if the limit exceeds
text = '\n'.join(textwrap.wrap(text, width=35))

# Calling the center text function
center_text(background, font, text)
