from PIL import Image, ImageDraw, ImageFont
from window_app import ts_data

sample_image_width = 1654
sample_image_height = 2339
sample_image = Image.new('RGBA', (sample_image_width, sample_image_height), 'white')
header_image = Image.open('header.png')
sample_image.paste(header_image)


class TitleList:
    def __init__(self):
        wall_type = None
        size = (None, None)
        deal_name = None
        deal_id = None
        box = None
        projector = None
        hdmi = None
        hooks = None
        matt = None
        insurance = None
        walls = None
        start_date = None
        shipping_date = None


def create_centered_text(text, font_name, font_size, depth):
    global sample_image
    current_image_drawing = ImageDraw.Draw(sample_image)
    current_font = ImageFont.truetype(font_name, size=font_size)
    current_image_drawing.textsize(text, font=current_font)
    text_w, text_h = current_image_drawing.textsize(text, font=current_font)
    current_image_drawing.text((sample_image_width/2 - text_w/2, depth), text=text, font=current_font, fill='black')
    sample_image.save('sample_image.png')
    return None


def create_bottom_text(text, font_name, font_size, depth):
    global sample_image
    current_image_drawing = ImageDraw.Draw(sample_image)
    current_font = ImageFont.truetype(font_name, size=font_size)
    current_image_drawing.textsize(text, font=current_font)
    current_image_drawing.text((200, depth), text=text, font=current_font, fill='black')
    sample_image.save('sample_image.png')
    return None


create_centered_text(ts_data['wall_type'], 'arial.ttf', 140, 400)
create_centered_text(ts_data['size'], 'arial.ttf', 140, 600)
create_centered_text(ts_data['deal_name'], 'arial.ttf', 140, 800)
create_centered_text('id' + ts_data['deal_id'], 'arial.ttf', 140, 1100)

create_bottom_text('Короб: ', 'arial.ttf', 80, 1300)
create_bottom_text('Проектор: ', 'arial.ttf', 80, 1400)
create_bottom_text('HDMI: ', 'arial.ttf', 80, 1500)
create_bottom_text('Зацепы: ', 'arial.ttf', 80, 1600)
create_bottom_text('Мат: ', 'arial.ttf', 80, 1700)
create_bottom_text('Страховка: ', 'arial.ttf', 80, 1800)
create_bottom_text('Боковые стенки: ', 'arial.ttf', 80, 1900)
create_bottom_text('Дата постановки задачи: ', 'arial.ttf', 80, 2000)
create_bottom_text('День отправки: ', 'arial.ttf', 80, 2100)
