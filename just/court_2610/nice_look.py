import os
import json
def nice_look_data():
    ugly_file = open(os.path.abspath('uploads/text.txt'), 'r', encoding='utf-8')
    ugly_file_list = ugly_file.read().split('\n')
    data = []
    for i in range(len(ugly_file_list)-1):
        nice_data = ugly_file_list[i].split(';')
        href_data = nice_data[0]
        date_data = nice_data[1][-24:-4]
        court_proceeding_data = '"' + nice_data[2].split(':')[1]
        case_data = '"' + nice_data[3].split(':')[1]
        info_data = nice_data[4]
        nice_dict = {'href_data' : href_data,
            'date_data' : date_data,
            'court_proceeding_data' : court_proceeding_data,
            'case_data' : case_data,
            'info_data' : info_data,}
        data.append(nice_dict)
    return data

columns = [
  {
    "field": "href_data", # which is the field's name of data key
    "title": "Ссылка", # display as the table header's name
    "sortable": True,
  },
  {
    "field": "date_data",
    "title": "Дата распределения",
    "sortable": False,
  },
  {
    "field": "court_proceeding_data",
    "title": "Єдиний унікальний номер",
    "sortable": False,
  },
  {
    "field": "case_data",
    "title": "Номер провадження",
    "sortable": False,
  },
  {
    "field": "info_data",
    "title": "Информация",
    "sortable": False,
  }
]
#jdata=json.dumps(data)
