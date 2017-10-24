import pandas as pd
import os

data_dir = os.path.abspath('uploads/reclamation_list.xls')

data_PARC = pd.read_excel(data_dir, 'list', skiprows=0)
data = data_PARC.to_dict(orient='list')

number_place = data['№']
date_place = data['Дата претензии']
name_place = data['Наименование поставщика']
address_place = data['Адрес Поставщика']
invoice_data = data['Данные накладной']
reclamation_data = data['Данные рекламации']
made_name_place = data['Наименование изготовителя']
made_address_place = data['Адрес Изготовителя']
production_data_clean = data['Брак']
deficit_data = data['Сумма убытков']
invalid_data = data['Стоимость замены брака']
add_data_clean = data['Приложения']

date_ru = []
date_verb_ru = [0, 'января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'Декабря']

for i in date_place:
    x = i.strftime('%m')
    date_ru.append(i.strftime('«%d» . %Y').replace('.',(date_verb_ru[int(x)])))



reclamation_len = len(number_place)
