import zipfile

from docxtpl import DocxTemplate,  R
from just.reclamation.colect import *

reclamation_len = len(number_place)
def reclamation_app():
    global deficit_data_place
    for i in list(range(reclamation_len)):
        zf = zipfile.ZipFile(os.path.abspath('downloads/reclamation_downloads/reclamation_app.zip'), mode = 'a')
        x = 0
        y = 0
        add_data_list = []
        add_data = ''
        production_data_list = []
        production_data = ''
        doc = DocxTemplate(os.path.abspath('just/reclamation/reclamation_template.docx'))
        for data in add_data_clean[i].split(';'):
            x+=1
            add_data_list.append(str(x) + '. ' + data + '\n')

        for data in add_data_list:
            add_data += data

        for data in production_data_clean[i].split(';'):
            y+=1
            production_data_list.append(str(y) + '. ' + data + '\n')

        for data in production_data_list:
            production_data += data

        if made_name_place[i] == '-':
            made_name_place[i] = name_place[i]

        if made_address_place[i] == '-':
            made_address_place[i] = address_place[i]

        if deficit_data[i] != 0:
            deficit_data_place = 'оплатить убытки от брака в сумме ' + str(deficit_data[i]) + 'грн., '
        elif deficit_data[i] == 0:
            deficit_data_place = ''

        context = {'number_place' : number_place[i],
            'date_place' : date_ru[i],
            'name_place' : name_place[i],
            'address_place' : address_place[i],
            'invoice_data' : invoice_data[i],
            'reclamation_data' : reclamation_data[i],
            'made_name_place' : made_name_place[i],
            'made_address_place' : made_address_place[i],
            'production_data' : R(production_data),
            'deficit_data' : deficit_data_place,
            'invalid_data' : str(invalid_data[i]),
            'add_data' : R(add_data)}

        doc.render(context)
        doc.save(os.path.abspath("generated/Рекламация № %s.docx" % number_place[i]))
        zf.write(os.path.abspath("generated/Рекламация № %s.docx" % number_place[i]), arcname= 'Рекламация № %s.docx' % number_place[i])
        os.remove(os.path.abspath("generated/Рекламация № %s.docx") % number_place[i])
        zf.close()
