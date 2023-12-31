from PySide6.QtWidgets import QLabel, QWidget, QHBoxLayout, QVBoxLayout, QSizePolicy
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, QTimer

from datetime import datetime, timedelta


class MinhaTela(QWidget):
    def __init__(self, tela_principal):
        super().__init__()
        self.tela_principal = tela_principal
        self.app = self.tela_principal.app

        # self._hora_final = datetime(year=2024, month=1, day=1)
        self._hora_final = datetime.now() + timedelta(minutes=4, seconds=23)

        self.__tempo_restante = self._hora_final - datetime.now()
        self._hora_atual = datetime.now() + timedelta(seconds=1)

        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.atualizar_timers)

        segundo_anterior = datetime.now().second
        while segundo_anterior == datetime.now().second:
            pass

        self.timer.start()
        # Logo IEADERN

        self.container_logo_ieadern = QWidget()
        layout_logo_ieadern = QHBoxLayout()
        layout_logo_ieadern.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label_ieadern = QLabel('')
        logo_ieadern = QPixmap('assets/img/logo_ieadern.png')
        label_ieadern.setPixmap(logo_ieadern)
        label_ieadern.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        layout_logo_ieadern.addWidget(label_ieadern)
        self.container_logo_ieadern.setLayout(layout_logo_ieadern)

        # Tempo restante
        self.container_tempo_restante = QWidget()
        self.container_tempo_restante.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        self.label_descricao_tempo_restante = QLabel('Tempo restante')
        self.label_descricao_tempo_restante.setObjectName('labelDescricaoTempoRestante')
        self.label_descricao_tempo_restante.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.label_tempo_restante = QLabel('00:00:00')
        self.label_tempo_restante.setObjectName('labelTempoRestante')
        self.label_tempo_restante.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        layout_tempo_restante = QVBoxLayout()
        layout_tempo_restante.setSpacing(0)
        layout_tempo_restante.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_descricao_tempo_restante = QHBoxLayout()
        layout_descricao_tempo_restante.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_descricao_tempo_restante.addWidget(self.label_descricao_tempo_restante)

        container_layout_label_tempo_restante = QWidget()
        # container_layout_label_tempo_restante.setMinimumWidth(800)
        layout_label_tempo_restante = QHBoxLayout()
        layout_label_tempo_restante.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_label_tempo_restante.addStretch(1)
        layout_label_tempo_restante.addWidget(self.label_tempo_restante)
        layout_label_tempo_restante.addStretch(1)
        container_layout_label_tempo_restante.setLayout(layout_label_tempo_restante)

        layout_tempo_restante.addLayout(layout_descricao_tempo_restante)
        layout_tempo_restante.addWidget(container_layout_label_tempo_restante)

        self.container_tempo_restante.setLayout(layout_tempo_restante)

        # Hora atual

        container_label_hora_atual = QWidget()
        container_label_hora_atual.setMinimumWidth(280)
        container_label_hora_atual.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        self.layout_hora_atual = QVBoxLayout()
        self.layout_hora_atual.setSpacing(0)
        self.layout_hora_atual.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_label_hora_atual = QHBoxLayout()
        layout_label_hora_atual.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout_descricao_hora_atual = QHBoxLayout()
        layout_descricao_hora_atual.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label_descricao_hora_atual = QLabel('Hora Atual')
        layout_descricao_hora_atual.addWidget(label_descricao_hora_atual)
        label_descricao_hora_atual.setObjectName('labelDescricaoHoraAtual')

        self.label_hora_atual = QLabel('00:00:00')
        self.label_hora_atual.setObjectName('labelHoraAtual')

        layout_label_hora_atual.addWidget(self.label_hora_atual)
        container_label_hora_atual.setLayout(layout_label_hora_atual)

        self.layout_hora_atual.addLayout(layout_descricao_hora_atual)
        self.layout_hora_atual.addWidget(container_label_hora_atual)

        # Feliz Ano Novo
        self.container_feliz_ano_novo = QWidget()

        layout_feliz_ano_novo = QVBoxLayout()
        layout_feliz_ano_novo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_feliz_ano_novo.setSpacing(0)
        self.label_feliz_ano_novo_1 = QLabel('Feliz ano')
        self.label_feliz_ano_novo_1.setObjectName('labelFelizAnoNovo')

        layout_label_feliz_ano_novo_2 = QHBoxLayout()
        layout_label_feliz_ano_novo_2.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.label_feliz_ano_novo_2 = QLabel('novo!')
        self.label_feliz_ano_novo_2.setObjectName('labelFelizAnoNovo')
        layout_label_feliz_ano_novo_2.addWidget(self.label_feliz_ano_novo_2)

        layout_feliz_ano_novo.addWidget(self.label_feliz_ano_novo_1)
        layout_feliz_ano_novo.addLayout(layout_label_feliz_ano_novo_2)
        self.container_feliz_ano_novo.setLayout(layout_feliz_ano_novo)

        self.atualizar_timers()

    def atualizar_timers(self):
        self._atualizar_tempo_restante()
        self._atualizar_hora_atual()

    def __mudar_tela(self):
        pass

    def _atualizar_tempo_restante(self):
        self.tempo_restante -= timedelta(seconds=1)
        texto_label_tempo_restante = ':'.join(self.preencher_com_zeros(self.horas_minutos_segundos(self.__tempo_restante)))
        self.label_tempo_restante.setText(texto_label_tempo_restante)

    def _atualizar_hora_atual(self):
        self._hora_atual += timedelta(seconds=1)
        texto_label_hora_atual = self._hora_atual.strftime('%H:%M:%S')
        self.label_hora_atual.setText(texto_label_hora_atual)

    @staticmethod
    def horas_minutos_segundos(td: timedelta):
        horas = td.seconds // 3600
        minutos = (td.seconds // 60) % 60
        segundos = td.seconds - horas * 3600 - minutos * 60
        indicadores = [horas, minutos, segundos]

        return indicadores

    @staticmethod
    def preencher_com_zeros(indicadores: list):
        for i, indicador in enumerate(indicadores):
            indicador = str(indicador)
            while len(indicador) < 2:
                indicador = '0' + indicador
            indicadores[i] = indicador

        return indicadores

    @property
    def tempo_restante(self):
        return self.__tempo_restante

    @tempo_restante.setter
    def tempo_restante(self, value):
        self.__tempo_restante = value

        horas, minutos, segundos = self.horas_minutos_segundos(self.tempo_restante)
        if horas == 23 and minutos == 59 and segundos == 59:
            self.__tempo_restante = timedelta(hours=0, minutes=0, seconds=0)

