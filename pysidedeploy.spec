[app]
title = FlexSerial2
input_file = /home/konrad/Desktop/FLEX_SERIAL_2/main.py
project_dir = .
project_file = 
exec_directory = ./pyflexserial

[python]
packages = nuitka==1.5.4,ordered_set,zstandard
python_path = /home/konrad/Desktop/FLEX_SERIAL_2/VENV/bin/python3

[qt]
qml_files = ./empty.qml
excluded_qml_plugins = QtCharts,QtQuick,QtQuick3D,QtSensors,QtTest,QtWebEngine

[nuitka]
extra_args = --quiet --noinclude-qt-translations=True

