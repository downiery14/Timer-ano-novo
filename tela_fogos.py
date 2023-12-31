from PySide6.QtWidgets import QWidget, QStackedWidget, QVBoxLayout, QHBoxLayout
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtCore import Qt
from minha_tela import MinhaTela

from datetime import timedelta


class TelaLetra(MinhaTela):
    def __init__(self, tela_principal: QStackedWidget):
        super().__init__(tela_principal)
        self.setObjectName('telaLetra')

        layout_tela_letra = QVBoxLayout()
        layout_tela_letra.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        layout_video = QHBoxLayout()
        layout_video.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.video_widget = QVideoWidget()
        self.video_widget.setObjectName('videoWidget')
        self.video_widget.setFixedSize(864, 240)
        self.tela_principal.player.setVideoOutput(self.video_widget)
        layout_video.addWidget(self.video_widget)

        self.container_feliz_ano_novo.hide()

        container_layout_ieadern_tempo_restante = QWidget()
        self.layout_ieadern_tempo_restante = QHBoxLayout()
        self.layout_ieadern_tempo_restante.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.layout_ieadern_tempo_restante.addStretch(1)
        self.layout_ieadern_tempo_restante.addWidget(self.container_logo_ieadern)
        self.layout_ieadern_tempo_restante.addStretch(1)
        self.layout_ieadern_tempo_restante.addWidget(self.container_tempo_restante)
        # self.layout_ieadern_tempo_restante.addStretch(1)
        self.layout_ieadern_tempo_restante.addWidget(self.container_feliz_ano_novo)
        self.layout_ieadern_tempo_restante.addStretch(1)
        container_layout_ieadern_tempo_restante.setLayout(self.layout_ieadern_tempo_restante)

        layout_tela_letra.addWidget(container_layout_ieadern_tempo_restante)
        layout_tela_letra.addLayout(layout_video)
        layout_tela_letra.addLayout(self.layout_hora_atual)
        self.setLayout(layout_tela_letra)

    def desejar_feliz_ano_novo(self):
        self.container_tempo_restante.hide()
        self.container_feliz_ano_novo.show()

    def atualizar_timers(self):
        self._atualizar_tempo_restante()
        self._atualizar_hora_atual()
        if self.tempo_restante == timedelta(hours=0, minutes=0, seconds=0) and self.tela_principal.currentIndex() == 1:
            self.__mudar_tela()

    def __mudar_tela(self):
        self.tela_principal.ir_para_tela('TelaFelizAnoNovo')
