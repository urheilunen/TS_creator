from tkinter import *

ts_data = {}


def submit_ts():
    global ts_data
    ts_data['wall_type'] = wall_type_value.get()
    ts_data['size'] = x_size_value.get() + 'x' + y_size_value.get()
    ts_data['deal_name'] = deal_name_value.get()
    ts_data['deal_id'] = deal_id_value.get()
    ts_data['korob'] = korob_value.get()
    ts_data['hooks'] = hooks_value.get()
    ts_data['matt'] = matt_value.get()
    ts_data['insurance'] = insurance_value.get()
    ts_data['walls'] = walls_value.get()
    Label(window, text='Готово. Можете закрыть окно или переделать.').place(relx=0.3, y=230)
    Label(window, text='В текущей директории созданы нужные файлы').place(relx=0.3, y=250)


window = Tk()
window.title('TS Creator 1.0')
window.geometry('500x300')

wall_type_value = StringVar()
wall_type_value.set(' ')
wall_type_label = Label(window, text="Скалодром ").grid(column=0, row=0)
wall_type_rad1 = Radiobutton(window, text='Скала', value='Скала', variable=wall_type_value).grid(column=1, row=0)
wall_type_rad2 = Radiobutton(window, text='Ракета', value='Ракета', variable=wall_type_value).grid(column=2, row=0)
wall_type_rad3 = Radiobutton(window, text='Эльбрус', value='Эльбрус', variable=wall_type_value).grid(column=3, row=0)

x_size_value = StringVar()
x_size_lbl = Label(window, text="Ширина ").grid(column=0, row=1)
x_size_txt = Entry(window, width=5, textvariable=x_size_value).grid(column=1, row=1)

y_size_value = StringVar()
y_size_lbl = Label(window, text="Высота ").grid(column=2, row=1)
y_size_txt = Entry(window, width=5, textvariable=y_size_value).grid(column=3, row=1)

deal_name_value = StringVar()
deal_name_lbl = Label(window, text="№. Имя ").grid(column=0, row=2)
deal_name_txt = Entry(window, width=20, textvariable=deal_name_value).grid(column=1, row=2)

deal_id_value = StringVar()
deal_id_lbl = Label(window, text="ID сделки").grid(column=0, row=3)
deal_id_txt = Entry(window, width=20, textvariable=deal_id_value).grid(column=1, row=3)

korob_value = StringVar()
korob_value.set(' ')
korob_lbl = Label(window, text="Короб").grid(column=0, row=4)
korob_rad1 = Radiobutton(window, text='V1', value='V1', variable=korob_value).grid(column=1, row=4)
korob_rad2 = Radiobutton(window, text='V2', value='V2', variable=korob_value).grid(column=2, row=4)
korob_rad3 = Radiobutton(window, text='V2 без проектора', value='V2-', variable=korob_value).grid(column=3, row=4)

hooks_value = StringVar()
hooks_lbl = Label(window, text='Зацепов').grid(column=0, row=5)
hooks_txt = Entry(window, width=3, textvariable=hooks_value).grid(column=1, row=5)

matt_value = BooleanVar()
matt_value.set(0)
matt_lbl = Label(window, text='Маты').grid(column=0, row=6)
matt_rad1 = Radiobutton(window, text='Да', value=1, variable=matt_value).grid(column=1, row=6)
matt_rad2 = Radiobutton(window, text='Нет', value=0, variable=matt_value).grid(column=2, row=6)

insurance_value = IntVar()
insurance_lbl = Label(window, text='Страх.линий').grid(column=0, row=7)
insurance_lbl1 = Label(window, text='шт').grid(column=2, row=7)
insurance_txt = Entry(window, width=3, textvariable=insurance_value).grid(column=1, row=7)

walls_value = IntVar()
walls_lbl = Label(window, text='Боковые стенки').grid(column=0, row=8)
walls_lbl1 = Label(window, text='мм').grid(column=2, row=8)
walls_txt = Entry(window, width=3, textvariable=walls_value).grid(column=1, row=8)

footer_note_lbl1 = Label(window, text='(если отсутствует - введите 0)').grid(column=3, row=7)
footer_note_lbl2 = Label(window, text='(если отсутствует - введите 0)').grid(column=3, row=8)
submit_btn = Button(window, text='Сделать красиво', command=submit_ts).grid(column=2, row=15)

window.mainloop()
