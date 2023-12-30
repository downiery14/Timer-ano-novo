from PySide6.QtWidgets import QWidget, QStackedWidget, QVBoxLayout
from PySide6.QtMultimedia import QAudioOutput, QMediaPlayer
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtCore import QUrl


class TelaFogos(QWidget):
    def __init__(self, tela_principal: QStackedWidget):
        super().__init__()
        self.tela_principal = tela_principal
        self.app = self.tela_principal.app
        self.setObjectName('telaFogos')

        layout = QVBoxLayout()
        self.__audio_output = QAudioOutput()
        self.__audio_output.setVolume(0.3)
        self.__player = QMediaPlayer()
        self.__player.setAudioOutput(self.__audio_output)
        self.__player.setSource(QUrl('assets/video/fogos-artificio.mp4'))

        self.__video_widget = QVideoWidget()
        self.__player.setVideoOutput(self.__video_widget)

        layout.addWidget(self.__video_widget)
        self.setLayout(layout)

    def iniciar_tela(self):
        self.__player.play()
        # self.tela_principal.setStyleSheet('background: none;')
