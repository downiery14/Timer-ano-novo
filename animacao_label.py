from PySide6.QtCore import QRunnable, Slot
from PySide6.QtWidgets import QLabel
from time import sleep


class AnimacaoLabels(QRunnable):
    def __init__(self, labels: list, *args, **kwargs):
        super(AnimacaoLabels, self).__init__()
        self.args = args
        self.kwargs = kwargs
        self.__labels = labels
        self.__interromper_execucao = False
        self.setAutoDelete(True)

    @Slot()
    def run(self):
        while not self.interromper_execucao:
            for label in self.__labels:
                label.setStyleSheet('color: #CCA352')
            sleep(1.2)
            for label in self.__labels:
                label.setStyleSheet('color: #FFFFFF')
            sleep(1.2)
            print(self.interromper_execucao)

    @property
    def interromper_execucao(self) -> bool:
        return self.__interromper_execucao

    @interromper_execucao.setter
    def interromper_execucao(self, value: bool):
        self.__interromper_execucao = value
