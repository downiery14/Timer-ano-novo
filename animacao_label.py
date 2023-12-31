from PySide6.QtCore import QRunnable, Slot
from time import sleep
from math import cos, radians


class AnimacaoLabels(QRunnable):
    def __init__(self, labels: list, *args, **kwargs):
        super(AnimacaoLabels, self).__init__()
        self.args = args
        self.kwargs = kwargs
        self.__labels = labels
        self.__interromper_execucao = False
        self.__n_execucao = 0
        self.__delay = 0.75
        self.setAutoDelete(True)

    @Slot()
    def run(self):
        while not self.interromper_execucao:
            for label in self.__labels:
                label.setStyleSheet('color: #CCA352')
            sleep(self.__delay)
            for label in self.__labels:
                label.setStyleSheet('color: #FFFFFF')
            sleep(self.__delay)
            self.__calcular_delay()

        return 0

    def __calcular_delay(self):
        self.__delay = 0.5 * self.__n_execucao ** 2 - 1.2 * self.__n_execucao + 0.75

        if self.__delay < 0.15:
            self.__delay = 0.15
            self.__n_execucao += 0.1

        self.__n_execucao += 0.08
        if self.__n_execucao >= 2.4:
            self.__n_execucao = 0
        print(self.__delay)
        print(self.__n_execucao)
        print()

    @property
    def interromper_execucao(self) -> bool:
        return self.__interromper_execucao

    @interromper_execucao.setter
    def interromper_execucao(self, value: bool):
        self.__interromper_execucao = value
