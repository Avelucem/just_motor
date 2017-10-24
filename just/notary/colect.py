import pandas as pd
import os

data_dir = os.path.abspath('uploads/paid.xls')

data_PARC = pd.read_excel(data_dir, 'list', skiprows=0)
data = data_PARC.to_dict(orient='list')

number_place = data[u'№ Рахунку']
date_place = data[u'Дата рахунку']
price_place = data[u'Сума нотаріальних послуг']
notary_name = data[u'Прізвище Нотаріусу']
name_place = data[u'Підписант від АТ "МС"']


date_ua = []
date_ru = []
date_verb_ru = [0, 'января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
date_verb_ua = [0, 'січня', 'лютого', 'березня', 'квітня', 'травня', 'червня', 'липня', 'серпня', 'вересня', 'жовтня', 'листопада', 'грудня']
for i in date_place:
    x = i.strftime('%m')
    date_ua.append(i.strftime('%d . %Y').replace('.',(date_verb_ua[int(x)])))
    date_ru.append(i.strftime('%d . %Y').replace('.',(date_verb_ru[int(x)])))

notary_len = len(number_place)
