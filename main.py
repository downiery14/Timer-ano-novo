from PySide6.QtWidgets import QApplication
from pathlib import Path
from main_window import MainWindow

# from PySide6.QtMultimedia import QMediaDevices
#
# devices = QMediaDevices.audioOutputs()
# for device in devices:
#     print("Device: ", device.description())

app = QApplication()
app.setStyleSheet(Path('style.qss').read_text())

main_window = MainWindow(app)
# app.aboutToQuit.connect(main_window.widget(2).parar_animacao_label_feliz_ano_novo())

app.exec()
