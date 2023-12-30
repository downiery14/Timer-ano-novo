from PySide6.QtWidgets import QApplication, QMainWindow
from pathlib import Path
from tela_timer import TelaTimer
from main_window import MainWindow

app = QApplication()
app.setStyleSheet(Path('style.qss').read_text())

main_window = MainWindow(app)

app.exec()
