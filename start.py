from PIL import Image, ImageFont, ImageDraw
import textwrap

def center_text(img, font, text, color=(50, 50, 50)):
    draw = ImageDraw.Draw(img)
    text_width, text_height = draw.textsize(text, font)
    position = ((strip_width-text_width)/2,(strip_height-text_height)/2)
    draw.text(position, text, color, font=font)
    img.save('quote.png')


strip_width, strip_height = 1080, 1080
text = """The greatest glory in living lies not in never falling, but in rising every time we fall."""

background = Image.new('RGB', (strip_width, strip_height), color=(248, 236, 236)) #creating the black strip
font = ImageFont.truetype("times", 60)
text = '\n'.join(textwrap.wrap(text, width=35))
center_text(background, font, text)
