from PySide6.QtWidgets import QStackedWidget, QApplication
from PySide6.QtCore import QUrl
from PySide6.QtMultimedia import QAudioOutput, QMediaPlayer

from tela_timer import TelaTimer
from tela_fogos import TelaFogos
from tela_feliz_ano_novo import TelaFelizAnoNovo


class MainWindow(QStackedWidget):
    def __init__(self, app: QApplication):
        super().__init__()
        self.app = app
        self.setGeometry(0, 0, 1024, 768)

        self.__player = QMediaPlayer()
        self.__audio_output = QAudioOutput()
        self.__audio_output.setVolume(0.3)
        self.__player.setSource('')

        self.nome_tela = {
            'TelaTimer': 0,
            'TelaFogos': 1,
            'TelaFelizAnoNovo': 2
        }

        self.addWidget(TelaTimer(self))
        self.addWidget(TelaFogos(self))
        self.addWidget(TelaFelizAnoNovo(self))

        self.show()

    def ir_para_tela(self, nome_tela_destino: str):
        if nome_tela_destino == 'TelaFogos':
            self.widget(self.nome_tela[nome_tela_destino]).iniciar_tela()

        self.setCurrentIndex(self.nome_tela[nome_tela_destino])

    def iniciar_musica(self):
        self.__player.setAudioOutput(self.__audio_output)
        self.__player.setSource(QUrl('assets/video/fogos-artificio.mp4'))
