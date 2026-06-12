#!/bin/bash

#change this to the pathname to your ERDDAP directory
erddap_path='~/erddap_[ERDDAP_NAME]'

#runs transitiondatasets_xinclude.py
python $erddap_path/transitiondatasets_xinclude.py

#concatenates first.xml, xinclude_xml.xml (the interior of the datasets.xml), and last.xml into a single datasetsxoncat.xml
cat $erddap_path/first.xml $erddap_path/xinclude_xml.xml $erddap_path/last.xml > $erddap_path/datasetsconcat.xml

#copies datasetsconcat.xml to your real datasets.xml
cp $erddap_path/datasetsconcat.xml ~/tomcat/content/erddap/datasets.xml
