#!/bin/bash
clear

time_ui=$(stat -c %Y "mainwindow.ui")
time_py=$(stat -c %Y "ui_main_win.py")

if (($time_ui > $time_py)); then
    echo -n "recompiling UI class..."

    pyside2-uic mainwindow.ui > ui_main_win.py

    echo "done"
else
    echo "no need to recompile UI"
fi