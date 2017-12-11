import zipfile
import os
from docxtpl import DocxTemplate
from just.notary.colect import *

notary_len = len(number_place)

def notary_app():
    for i in list(range(notary_len)):
        zf = zipfile.ZipFile(os.path.abspath('downloads/notary_downloads/notary_app.zip'), mode='a')
        if name_place[i][0:3] == 'Лун':
            motor_place = u'финансового директора Лунина Виктора Алексеевича'
        elif name_place[i][0:5] == 'Алекс' or 'Алєкс':
            motor_place = u'заместителя директора по правовым вопросам Алексеевой Елены Ивановны'
        else:
            motor_place = '________________________________________________________________________________________'
        if notary_name[i][0] == 'П':
            doc = DocxTemplate(os.path.abspath("just/notary/template_pudlik.docx"))
            notary_name[i] = 'Пудлік І.М.'
        elif notary_name[i][0] == 'Р':
            doc = DocxTemplate(os.path.abspath("just/notary/template_romancov.docx"))
            notary_name[i] = 'Романцов І.А.'
        context = {'number_place': number_place[i],
                   'date_place_ua': date_ua[i],
                   'date_place_ru': date_ru[i],
                   'price_place': price_place[i],
                   'name_place': motor_place}
        doc.render(context)
        doc.save(os.path.abspath("generated/Cчет №%s %s.docx") % (number_place[i], notary_name[i]))
        zf.write(os.path.abspath("generated/Cчет №%s %s.docx") % (number_place[i], notary_name[i]),
                 arcname="Cчет №%s %s.docx" % (number_place[i], notary_name[i]))
        os.remove(os.path.abspath("generated/Cчет №%s %s.docx") % (number_place[i], notary_name[i]))
        zf.close()
