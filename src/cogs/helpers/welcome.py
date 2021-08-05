try:
    from . import config
except ImportError:
    import config

import io
import requests

from discord import Member, File

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def join(member: Member=None, name='beispiel nutzer name', pic='https://cdn.discordapp.com/avatars/657900196189044736/4762ab6ad1b3ad64610eb0871db36b97.jpg?size=256'):
    PROFILE_PIC_RESIZE = 90
    PROFILE_PIC_X = 55
    PROFILE_PIC_Y = 70
    TEXT_X = 177
    TEXT_Y = 100
    # TEXT_COLOR_RGB = config.load()['design']['colors']['primary_rgb']
    # TEXT_COLOR = (TEXT_COLOR_RGB[0], TEXT_COLOR_RGB[1], TEXT_COLOR_RGB[2])
    TEXT_COLOR = 0xFFFFFF

    base_img = Image.open('media/welcome.jpg')


    name_text = name
    profile_pic = pic

    if member:
        name_text = member.nick if member.nick else member.name
        profile_pic = member.avatar_url_as(size=256)    
    
    profile_pic_path = f'temp/profile_pic_{member.id if member else name}.jpg'
    open(profile_pic_path, 'wb').write(requests.get(profile_pic).content)
    #profile_pic_bytes = io.BytesIO(profile_pic.read())
    profile_pic = Image.open(profile_pic_path)

    profile_pic = profile_pic.resize((PROFILE_PIC_RESIZE, PROFILE_PIC_RESIZE))
    base_img.paste(profile_pic, (PROFILE_PIC_X, PROFILE_PIC_Y))

    draw_img = ImageDraw.Draw(base_img)
    font = ImageFont.truetype('media/DejaVuSansMono-Bold.ttf', 24)
    draw_img.text((TEXT_X, TEXT_Y), name_text, TEXT_COLOR, font=font)

    path = f'temp/{member.id if member else name.replace(" ", "_")}.jpg'
    base_img.save(path)

    if __name__ == '__main__':
        base_img.show()

    return File(path)

if __name__ == '__main__':
    join()