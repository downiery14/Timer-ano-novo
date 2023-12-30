from PySide6.QtWidgets import QWidget, QStackedWidget


class TelaFelizAnoNovo(QWidget):
    def __init__(self, tela_principal: QStackedWidget):
        super().__init__()
        self.tela_principal = tela_principal
        self.app = self.tela_principal.app
