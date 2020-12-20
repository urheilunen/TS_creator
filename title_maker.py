from PIL import Image, ImageDraw, ImageFont
from window_app import ts_data

TS_FONT = 'arial.ttf'

title_image_width = 1654
title_image_height = 2339
title_image = Image.new('RGBA', (title_image_width, title_image_height), 'white')
title_header_image = Image.open('src/header.png')
title_image.paste(title_header_image)


def split_text(text):
    modifier = 1
    for i in range(len(text)//2):
        modifier *= -1
        if text[len(text)//2 + i * modifier] == ' ':
            text0 = text[:len(text)//2 + i * modifier]
            text1 = text[len(text)//2 + i * modifier:]
            return text0, text1
    return 0


def create_centered_title_text(text, font_size, depth):
    global title_image
    current_image_drawing = ImageDraw.Draw(title_image)
    current_font = ImageFont.truetype(TS_FONT, size=font_size)
    current_image_drawing.textsize(text, font=current_font)
    text_w, text_h = current_image_drawing.textsize(text, font=current_font)
    if text_w > title_image_width:
        text0, text1 = split_text(text)
        depth0 = depth - font_size//2 + 35
        depth1 = depth + font_size//2 + 45
        create_centered_title_text(text0, font_size, depth0)
        create_centered_title_text(text1, font_size, depth1)
        return None
    current_image_drawing.text((title_image_width / 2 - text_w / 2, depth), text=text, font=current_font, fill='black')
    title_image.save('output/title_image.png')
    return None


def create_bottom_title_text(text, font_size, depth):
    global title_image
    current_image_drawing = ImageDraw.Draw(title_image)
    current_font = ImageFont.truetype(TS_FONT, size=font_size)
    current_image_drawing.textsize(text, font=current_font)
    current_image_drawing.text((200, depth), text=text, font=current_font, fill='black')
    title_image.save('output/title_image.png')
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


create_centered_title_text(ts_data['wall_type'], 140, 400)
create_centered_title_text(ts_data['size'], 140, 600)
create_centered_title_text(ts_data['deal_name'], 140, 800)
create_centered_title_text('id' + ts_data['deal_id'], 140, 1100)

create_bottom_title_text('Короб: ' + ts_data['korob'], 80, 1300)
create_bottom_title_text('Проектор: ' + ts_data['projector'], 80, 1400)
create_bottom_title_text('HDMI: ' + ts_data['hdmi'], 80, 1500)
create_bottom_title_text('Зацепы: ' + ts_data['hooks'], 80, 1600)
create_bottom_title_text('Мат: ' + ts_data['matt'], 80, 1700)
create_bottom_title_text('Страховка: ' + ts_data['insurance'], 80, 1800)
create_bottom_title_text('Боковые стенки: ' + ts_data['walls'], 80, 1900)
create_bottom_title_text('Дата постановки задачи: ', 80, 2000)
create_bottom_title_text('День отправки: ', 80, 2100)

# creating "blank" image
blank_image_width = 2339
blank_image_height = 1654
blank_image = Image.new('RGBA', (blank_image_width, blank_image_height), 'white')
raw_image = Image.open('src/blank_sample_1.png')
blank_image.paste(raw_image)


def create_centered_blank_text(text, font_size, depth, frame_w=800, frame_x=60, frame_y=70):
    global blank_image
    current_image_drawing = ImageDraw.Draw(blank_image)
    current_font = ImageFont.truetype(TS_FONT, size=font_size)
    current_image_drawing.textsize(text, font=current_font)
    text_w, text_h = current_image_drawing.textsize(text, font=current_font)
    if text_w > frame_w:
        text0, text1 = split_text(text)
        depth0 = depth - text_h // 2 + frame_y - 60
        depth1 = depth + text_h // 2 + frame_y - 50
        create_centered_blank_text(text0, font_size, depth0, frame_w, frame_x, frame_y)
        create_centered_blank_text(text1, font_size, depth1, frame_w, frame_x, frame_y)
        return None
    current_image_drawing.text((frame_w / 2 - text_w / 2 + frame_x, frame_y + depth), text=text, font=current_font, fill='black')
    blank_image.save('output/blank_1.png')
    return None


create_centered_blank_text(ts_data['wall_type'], 30, 10, frame_w=140)
create_centered_blank_text(ts_data['size'] + ' мм', 50, 20)
create_centered_blank_text(ts_data['deal_name'], 50, 100)
create_centered_blank_text('id' + ts_data['deal_id'], 50, 210)
