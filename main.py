from PySide6.QtWidgets import QApplication
from pathlib import Path
from main_window import MainWindow
from PySide6.QtMultimedia import QMediaDevices

devices = QMediaDevices.audioOutputs()
for device in devices:
    print("Device: ", device.description())

app = QApplication()
app.setStyleSheet(Path('style.qss').read_text())

main_window = MainWindow(app)

app.exec()
