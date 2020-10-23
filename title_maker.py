from PIL import Image, ImageDraw, ImageFont
from window_app import ts_data

sample_image_width = 1654
sample_image_height = 2339
sample_image = Image.new('RGBA', (sample_image_width, sample_image_height), 'white')
header_image = Image.open('header.png')
sample_image.paste(header_image)


def split_text(text):
    modifier = 1
    for i in range(len(text)//2):
        modifier *= -1
        if text[len(text)//2 + i * modifier] == ' ':
            text0 = text[:len(text)//2 + i * modifier]
            text1 = text[len(text)//2 + i * modifier:]
            return text0, text1
    return 0


def create_centered_text(text, font_name, font_size, depth):
    global sample_image
    current_image_drawing = ImageDraw.Draw(sample_image)
    current_font = ImageFont.truetype(font_name, size=font_size)
    current_image_drawing.textsize(text, font=current_font)
    text_w, text_h = current_image_drawing.textsize(text, font=current_font)
    if text_w > sample_image_width:
        text0, text1 = split_text(text)
        depth0 = depth - font_size//2 + 35
        depth1 = depth + font_size//2 + 45
        create_centered_text(text0, font_name, font_size, depth0)
        create_centered_text(text1, font_name, font_size, depth1)
        return None
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


if ts_data['korob'] == 'V1':
    ts_data['korob'] = 'V1 (кронштейн 60х60)'
    ts_data['projector'] = 'нет'
if ts_data['korob'] == 'V2':
    ts_data['korob'] = 'V2 (кронштейн 40х40)'
    ts_data['projector'] = 'да'
    ts_data['hdmi'] = 'да (10м)'
else:
    ts_data['hdmi'] = 'нет'
if ts_data['korob'] == 'V2-':
    ts_data['korob'] = 'V2 (кронштейн 40х40)'
    ts_data['projector'] = 'нет'
    ts_data['hdmi'] = 'нет'

if ts_data['hooks'] != '0':
    ts_data['hooks'] = 'да (' + ts_data['hooks'] + ' шт.)'
else:
    ts_data['hooks'] = 'нет'

if ts_data['matt'] == 1:
    ts_data['matt'] = 'да (' + ts_data['size'].split('x')[0] + 'x1500x150 мм)'
else:
    ts_data['matt'] = 'нет'
if ts_data['insurance'] == 0:
    ts_data['insurance'] = 'нет'
else:
    ins_line_end = 'INSURANCE_ERROR!'
    if 1 < ts_data['insurance'] < 5:
        ins_line_end = 'линии'
    elif ts_data['insurance'] == 1:
        ins_line_end = 'линия'
    elif ts_data['insurance'] >= 5:
        ins_line_end = 'линий'
    ts_data['insurance'] = 'да (' + str(ts_data['insurance']) + ' ' + ins_line_end + ')'

if ts_data['walls'] == 0:
    ts_data['walls'] = 'нет'
else:
    ts_data['walls'] = 'да (' + str(ts_data['walls']) + ' мм)'


create_centered_text(ts_data['wall_type'], 'arial.ttf', 140, 400)
create_centered_text(ts_data['size'], 'arial.ttf', 140, 600)
create_centered_text(ts_data['deal_name'], 'arial.ttf', 140, 800)
create_centered_text('id' + ts_data['deal_id'], 'arial.ttf', 140, 1100)

create_bottom_text('Короб: ' + ts_data['korob'], 'arial.ttf', 80, 1300)
create_bottom_text('Проектор: ' + ts_data['projector'], 'arial.ttf', 80, 1400)
create_bottom_text('HDMI: ' + ts_data['hdmi'], 'arial.ttf', 80, 1500)
create_bottom_text('Зацепы: ' + ts_data['hooks'], 'arial.ttf', 80, 1600)
create_bottom_text('Мат: ' + ts_data['matt'], 'arial.ttf', 80, 1700)
create_bottom_text('Страховка: ' + ts_data['insurance'], 'arial.ttf', 80, 1800)
create_bottom_text('Боковые стенки: ' + ts_data['walls'], 'arial.ttf', 80, 1900)
create_bottom_text('Дата постановки задачи: ', 'arial.ttf', 80, 2000)
create_bottom_text('День отправки: ', 'arial.ttf', 80, 2100)
