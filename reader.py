import xlrd
import json
import os

def xls_to_json(filename):
    doc = xlrd.open_workbook(filename)
    sheet = doc.sheet_by_index(0)
    nrows = sheet.nrows
    
    provincia = sheet.cell_value(1, 0)
    cod_provincia = sheet.cell_value(3, 0)
    municipios = []

    if not is_valid(sheet):
        print "Error en {0}, el archivo tiene un formato inesperado.".format(filename)
    
    for row in range(3, nrows):
        cod_mun = sheet.cell_value(row, 1)
        name_mun = sheet.cell_value(row, 3)
        municipios.append({ 'code': cod_mun, 'name': name_mun})

    data = {
        'municipios': municipios,
        'code'  : cod_provincia,
        'provincia' : provincia
    }

    fname = cod_provincia
    with open('{0}.json'.format(fname), 'wb') as fp:
        json_string = json.dumps(data, ensure_ascii=False).encode('utf8')
        fp.write(json_string)


def is_valid(sheet):
    if str(sheet.cell_value(2, 0)) != "CPRO":
        print "Se esperaba CPRO y se tiene {0}".format(sheet.cell_value(2, 0))
        return False
    if str(sheet.cell_value(2, 1)) != "CMUN":
        print "Se esperaba CMUN y se tiene {0}".format(sheet.cell_value(2, 1))
        return False
    if str(sheet.cell_value(2, 2)) != "DC":
        print "Se esperaba DC y se tiene {0}".format(sheet.cell_value(2, 2))
        return False
    if str(sheet.cell_value(2, 3)) != "NOMBRE":
        print "Se esperaba NOMBRE y se tiene {0}".format(sheet.cell_value(2, 3))
        return False
    return True

def generate_index(path):
    print "Generando indice..."
    index = []
    for file in os.listdir(path):
        if file.endswith("json"):
            json_data = open(path+"/"+file)
            data = json.load(json_data)
            index.append({ 'name': data['provincia'], 'code': data['code']})
    with open('json/index.json', 'wb') as fp:
        json_string = json.dumps(index, ensure_ascii=False).encode('utf8')
        fp.write(json_string)





