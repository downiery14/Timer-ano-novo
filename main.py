from PySide6.QtWidgets import QApplication
from pathlib import Path
from main_window import MainWindow

app = QApplication()
app.setStyleSheet(Path('style.qss').read_text())

main_window = MainWindow(app)

app.exec()
