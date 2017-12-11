import os
from docx import Document

# возвращает из docx текст по пораграфам
def dover_content(filename):
    if filename.endswith('docx'):
        doci = Document(filename)
        para_text = ''
        for para in doci.paragraphs:
            para_text += '\n'+para.text.replace('  ', ' ').replace('  ', ' ').replace('  ', ' ').replace('  ', ' ').replace('  ', ' ').replace('  ', ' ')
        return para_text


def first_letter(word):
    if word[0].isupper() and word[-1].islower():
        return word


def index_name(sentence):
    index_name = []
    for word in sentence:
        if first_letter(word) != None:
            index_name.append(sentence.index(first_letter(word)))
    return index_name


def name_poa(index, contents):
    for index_in_contents in list(range(len(index))):
        try:
            if index[index_in_contents] == index[index_in_contents+1]-1 == index[index_in_contents+2]-2:
                name_poa = contents[index[index_in_contents]] + ' ' + \
                    contents[index[index_in_contents+1]] + ' ' + \
                    contents[index[index_in_contents+2]]
                return name_poa
        except IndexError:
            pass


def content_data(item):
    if 'поручает' and 'Настоящая доверенность' in item:
        content_data = item
        return content_data[content_data.index('поручает'): content_data.index('Настоящая доверенность')]
    elif ('доручає' and 'Ця довіреність') in item:
        content_data = item
        return content_data[content_data.index('доручає'): content_data.index('Ця довіреність')]
    elif 'доручає' and 'Довіреність видана' in item:
        content_data = item
        return content_data[content_data.index('доручає'): content_data.index('Довіреність видана')]


def dover_app():
    dict_of_poa = {}
    for file in os.listdir():
        try:
            text = dover_content(file)
            index = index_name(content_data(text).split(' '))
            dict_of_poa[file] = [name_poa(index, content_data(text).split(' ')), content_data(text)]
        except:
            pass
    return dict_of_poa
