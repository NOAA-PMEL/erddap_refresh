#!/bin/bash
#runs transitiondatasets_xinclude.py
python ~/erddap_[ERDDAP_NAME]/transitiondatasets_xinclude.py

#concatenates first.xml, xinclude_xml.xml (the interior of the datasets.xml), and last.xml into a single datasetsxoncat.xml
cat ~/erddap_[ERDDAP_NAME]/first.xml ~/erddap_[ERDDAP_NAME]/xinclude_xml.xml ~/erddap_[ERDDAP_NAME]/last.xml > ~/erddap_[ERDDAP_NAME]/datasetsconcat.xml

#copies datasetsconcat.xml to your real datasets.xml
cp ~/erddap_[ERDDAP_NAME]/datasetsconcat.xml ~/tomcat/content/erddap/datasets.xml
