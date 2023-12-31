from PySide6.QtWidgets import (QVBoxLayout, QStackedWidget)
from PySide6.QtCore import Qt
from minha_tela import MinhaTela


class TelaTimer(MinhaTela):
    def __init__(self, tela_principal: QStackedWidget):
        super().__init__(tela_principal)
        self.setObjectName('telaTimer')

        layout_tela_timer = QVBoxLayout()
        layout_tela_timer.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout_tela_timer.addStretch(1)
        layout_tela_timer.addWidget(self.container_logo_ieadern)
        layout_tela_timer.addStretch(4)
        layout_tela_timer.addWidget(self.container_tempo_restante)
        layout_tela_timer.addStretch(4)
        layout_tela_timer.addLayout(self.layout_hora_atual)
        layout_tela_timer.addStretch(1)

        self.setLayout(layout_tela_timer)

    def __mudar_tela(self):
        self.tela_principal.ir_para_tela('TelaLetra')

    def atualizar_timers(self):
        self._atualizar_tempo_restante()
        self._atualizar_hora_atual()
        horas, minutos, segundos = self.horas_minutos_segundos(self.tempo_restante)
        if horas == 0 and minutos <= 4 and segundos <= 15 and self.tela_principal.currentIndex() == 0:
            self.__mudar_tela()
