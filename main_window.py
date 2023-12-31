from PySide6.QtWidgets import QStackedWidget, QApplication
from PySide6.QtCore import QUrl
from PySide6.QtMultimedia import QAudioOutput, QMediaPlayer

from tela_timer import TelaTimer
from tela_fogos import TelaLetra
from tela_feliz_ano_novo import TelaFelizAnoNovo


class MainWindow(QStackedWidget):
    def __init__(self, app: QApplication):
        super().__init__()
        self.app = app
        self.setGeometry(0, 0, 1024, 768)
        self.setWindowTitle('Timer da virada de ano')

        self.player = QMediaPlayer()
        self.__audio_output = QAudioOutput()
        self.__audio_output.setVolume(1)
        self.player.setSource(QUrl('assets/video/Letra Rompendo em Fé.mp4'))
        self.player.setAudioOutput(self.__audio_output)
        self.player.playingChanged.connect(self.esta_tocando)

        self.nome_tela = {
            'TelaTimer': 0,
            'TelaLetra': 1,
            'TelaFelizAnoNovo': 2
        }

        self.addWidget(TelaTimer(self))
        self.addWidget(TelaLetra(self))
        self.addWidget(TelaFelizAnoNovo(self))

        # self.player.setVideoOutput(self.widget(self.nome_tela['TelaLetra']).video_widget)

        self.ir_para_tela('TelaTimer')
        self.showFullScreen()

    def ir_para_tela(self, nome_tela_destino: str):
        if nome_tela_destino == 'TelaLetra':
            self.player.play()
        elif nome_tela_destino == 'TelaFelizAnoNovo':
            self.widget(self.nome_tela[nome_tela_destino]).animar_label_feliz_ano_novo()
            print('Tela felizada com')

        self.setCurrentIndex(self.nome_tela[nome_tela_destino])

    def esta_tocando(self, playing: bool):
        if not playing:
            self.widget(self.nome_tela['TelaFelizAnoNovo']).parar_animacao_label_feliz_ano_novo()

    def closeEvent(self, event):
        self.widget(self.nome_tela['TelaFelizAnoNovo']).parar_animacao_label_feliz_ano_novo()
        event.accept()
