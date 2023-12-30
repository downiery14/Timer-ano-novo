from PySide6.QtWidgets import (QWidget, QLabel, QHBoxLayout, QVBoxLayout, QStackedWidget)
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QPixmap
from datetime import datetime, timedelta


class TelaTimer(QWidget):
    def __init__(self, tela_principal: QStackedWidget):
        super().__init__()
        self.tela_principal = tela_principal
        self.app = self.tela_principal.app

        self.__hora_final = datetime.now() + timedelta(seconds=5)

        self.__tempo_restante = self.__hora_final - datetime.now()
        self.__hora_atual = datetime.now() + timedelta(seconds=1)

        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.__atualizar_timers)

        segundo_anterior = datetime.now().second
        while segundo_anterior == datetime.now().second:
            pass

        self.timer.start()

        layout_widget = QVBoxLayout()
        layout_widget.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout_logo_ieadern = QHBoxLayout()
        layout_logo_ieadern.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label_ieadern = QLabel('')
        logo_ieadern = QPixmap('assets/img/logo_ieadern.png')
        label_ieadern.setPixmap(logo_ieadern)
        layout_logo_ieadern.addWidget(label_ieadern)

        layout_tempo_restante = QVBoxLayout()
        layout_tempo_restante.setSpacing(0)
        layout_tempo_restante.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_descricao_tempo_restante = QHBoxLayout()
        layout_descricao_tempo_restante.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label_descricao_tempo_restante = QLabel('Tempo restante')
        layout_descricao_tempo_restante.addWidget(label_descricao_tempo_restante)
        label_descricao_tempo_restante.setObjectName('labelDescricaoTempoRestante')

        container_layout_label_tempo_restante = QWidget()
        container_layout_label_tempo_restante.setMinimumWidth(720)
        layout_label_tempo_restante = QHBoxLayout()
        layout_label_tempo_restante.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_tempo_restante = QLabel('00:00:00')
        self.label_tempo_restante.setObjectName('labelTempoRestante')
        layout_label_tempo_restante.addWidget(self.label_tempo_restante)
        container_layout_label_tempo_restante.setLayout(layout_label_tempo_restante)

        layout_tempo_restante.addLayout(layout_descricao_tempo_restante)
        layout_tempo_restante.addWidget(container_layout_label_tempo_restante)

        layout_hora_atual = QVBoxLayout()
        layout_hora_atual.setSpacing(12)
        layout_hora_atual.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_descricao_hora_atual = QHBoxLayout()
        layout_descricao_hora_atual.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label_descricao_hora_atual = QLabel('Hora Atual')
        layout_descricao_hora_atual.addWidget(label_descricao_hora_atual)
        label_descricao_hora_atual.setObjectName('labelDescricaoHoraAtual')
        self.label_hora_atual = QLabel('00:00:00')
        self.label_hora_atual.setObjectName('labelHoraAtual')

        layout_hora_atual.addLayout(layout_descricao_hora_atual)
        layout_hora_atual.addWidget(self.label_hora_atual)

        layout_widget.addStretch(1)
        layout_widget.addLayout(layout_logo_ieadern)
        layout_widget.addStretch(4)
        layout_widget.addLayout(layout_tempo_restante)
        layout_widget.addStretch(4)
        layout_widget.addLayout(layout_hora_atual)
        layout_widget.addStretch(1)

        self.__atualizar_timers()
        self.setLayout(layout_widget)

    def __atualizar_timers(self):
        self.__atualizar_tempo_restante()
        self.__atualizar_hora_atual()
        if datetime.now() + timedelta(seconds=1) >= self.__hora_final:
            self.timer.stop()
            self.__mudar_tela()

    def __atualizar_tempo_restante(self):
        self.__tempo_restante -= timedelta(seconds=1)
        texto_label_tempo_restante = ':'.join(self.__horas_minutos_segundos(self.__tempo_restante))
        self.label_tempo_restante.setText(texto_label_tempo_restante)

    def __atualizar_hora_atual(self):
        self.__hora_atual += timedelta(seconds=1)
        texto_label_hora_atual = self.__hora_atual.strftime('%H:%M:%S')
        self.label_hora_atual.setText(texto_label_hora_atual)

    def __mudar_tela(self):
        self.tela_principal.ir_para_tela('TelaFogos')

    def __horas_minutos_segundos(self, td: timedelta):
        horas = td.seconds // 3600
        minutos = (td.seconds // 60) % 60
        segundos = td.seconds - horas * 3600 - minutos * 60
        indicadores = [horas, minutos, segundos]

        for i, indicador in enumerate(indicadores):
            indicador = str(indicador)
            while len(indicador) < 2:
                indicador = '0' + indicador
            indicadores[i] = indicador

        return indicadores