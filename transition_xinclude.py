#!/usr/bin/env python
# coding: utf-8

import os

#reads through all dataset xml fragments
ds_dir = '~/erddap_[ERDDAP_NAME]/datasets_xml_fragments/'
for root, dirs, dsfiles in os.walk(ds_dir):
    #print(dsfiles)
    continue

#for each dataset xml fragment, writes a new line
newlines = []
for f in dsfiles:
    newline = '<xi:include href="' + ds_dir + f + '"/>\n'
    newlines.append(newline)

#creates the file xinclude_xml.xml and writes each XInclude-styled newline as a line in the file
with open('~/erddap_[ERDDAP_NAME]/xinclude_xml.xml','w') as outXML:
    for line in newlines:
        outXML.write(line)
