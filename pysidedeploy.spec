[app]
title = FlexSerial2
input_file = ./main.py
project_dir = .
project_file = 
exec_directory = ./pyflexserial

[python]
packages = nuitka==1.5.4,ordered_set,zstandard
python_path = ./VENV/bin/python3

[qt]
qml_files = ./empty.qml
excluded_qml_plugins = QtCharts,QtQuick,QtQuick3D,QtSensors,QtTest,QtWebEngine

[nuitka]
extra_args = --quiet --assume-yes-for-downloads --disable-console --noinclude-qt-translations=True

