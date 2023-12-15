# Star Wars Empire at War Value Changer
# Author: JCStaples

import xml.etree.ElementTree as ET
import os
import logging

logging.basicConfig(level=logging.INFO)

# Variables
fileDir = 'D:\\Gaming\\EAW-Backup\\EAWR-EMP\\Buildings\\Ground\\GC'
populationVal = 1
buildCostVal = 1
buildTimeVal = 1
addPopulationVal = 1000000
affiliationVal = ""
recurse = False

def get_xml_files(fileDir, recurse):
    file_names = []
    if recurse:
        for dirpath, dirnames, filenames in os.walk(fileDir):
            for file in filenames:
                file_path = os.path.join(dirpath, file)
                if os.path.splitext(file_path)[1].lower() == '.xml':
                    file_names.append(file_path)
        return file_names
    else:
        for file in os.listdir(fileDir):
            file_path = os.path.join(fileDir, file)
            if os.path.splitext(file_path)[1].lower() == '.xml':
                file_names.append(file_path)
        return file_names

# Removes the XML declaration from the file
def remove_xml_declaration(content):
    return content.replace('<?xml version="1.0" encoding="UTF-8"?>', '', 1)

# Cleans any XML files that have anything before the XML declaration
def clean_xml(file_name):
    with open(file_name, 'r+') as f:
        content = f.read()
        first_declaration = content.find('<?xml')
        if first_declaration <= 0:
            return
        content = content[first_declaration:]
        content = remove_xml_declaration(content)
        f.seek(0)
        f.write(content)
        f.truncate()

# Changes the value of an element in an XML file based on the affiliation and element name
def changeValue(tree, element, val, affi=""):
    root = tree.getroot()
    if affi == "":
        xpath = f'*/{element}'
    else:
        xpath = f'*/[Affiliation = "{affi}"]/{element}'
    
    for node in root.findall(xpath):
        node.text = str(val)

# Gets all XML files in the directory
try:
    file_names = get_xml_files(fileDir, recurse)
    logging.info('\nGot files!')
except Exception as e:
    logging.error('\nError: %s', e)

# Changes the values of the XML files
errors = {}

elements_to_change = [
    ('Population_Value', populationVal),
    ('Build_Cost_Credits', buildCostVal),
    ('Build_Time_Seconds', buildTimeVal),
    ('Additional_Population_Capacity', addPopulationVal)
]

try:
    for file_name in file_names:
        try:
            clean_xml(file_name)
            exception_filename = file_name
            logging.info(file_name)
            tree = ET.parse(file_name)
            if affiliationVal.lower() in os.path.basename(file_name).lower():
                for element, val in elements_to_change:
                    changeValue(tree, element, val)
            else:
                for element, val in elements_to_change:
                    changeValue(tree, element, val, affiliationVal)
            tree.write(file_name, encoding='utf-8', xml_declaration=True)
        except Exception as e:
            errors[file_name] = str(e)

    logging.info('\nDone!')
except Exception as e:
    logging.error(f'\nError: {e}')

# Logs any errors
for file_name, error in errors.items():
    logging.error(f'\nError {file_name}: {error}')