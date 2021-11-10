# Star Wars Empire at War Value Changer
# Author: JCStaples

import xml.etree.ElementTree as ET
import os    

fileDir = '/Users/jstaples/Desktop/EAW-RMK-Rebel/'
populationVal = 0
buildCostVal = 1
buildTimeVal = 1
addPopulationVal = 1000000
affiliationVal = 'Rebel'

def changeValue(tree, element, val, affi):
    root = tree.getroot()
    xpath = '*/[Affiliation = "{0}"]/{1}'.format(affi, element)
    for node in root.findall(xpath):
        node.text = str(val)

file_names = os.listdir(fileDir)
for file_name in file_names:
    if file_name.endswith('.xml') or file_name.endswith('.XML'):
        tree = ET.parse(fileDir + file_name)
        changeValue(tree, 'Population_Value', populationVal, affiliationVal)
        changeValue(tree, 'Build_Cost_Credits', buildCostVal, affiliationVal)
        changeValue(tree, 'Build_Time_Seconds', buildTimeVal, affiliationVal)
        changeValue(tree, 'Additional_Population_Capacity', addPopulationVal, affiliationVal)
        tree.write(fileDir + file_name, encoding='utf-8', xml_declaration=True)