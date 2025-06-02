#!/usr/bin/env python
# coding: utf-8

# # purpose: reads in completed datasets.xml and saves individual datasets as xml file fragments

import os
import xml.etree.ElementTree as ET

#change this to the pathname to your ERDDAP directory
erddap_path = '~/erddap_[ERDDAP_NAME]'

#input the entire pathname of your current datasets.xml
inputFilename = input('Enter a datasets.xml to read in: ')

parser = ET.XMLParser(target=ET.TreeBuilder(insert_comments=True))
tree = ET.parse(inputFilename, parser)
root = tree.getroot()

for elemental in root.iter('dataset'):
    did = elemental.attrib['datasetID']#finds the datasetID in the <dataset> tag
    with open(erddap_path + '/datasets_xml_fragments/' + did + '.xml','w') as f:#I prefer to add a subdirectory for all the xml fragments so the main directory is cleaner
        f.write(ET.tostring(elemental, encoding='unicode'))#writes the dataset's <dataset> tag, inclusive, to an xml file named with the datasetID
