from PySide6.QtWidgets import QStackedWidget, QVBoxLayout
from PySide6.QtCore import Qt, QTimer, QThreadPool
from minha_tela import MinhaTela
from animacao_label import AnimacaoLabels


class TelaFelizAnoNovo(MinhaTela):
    def __init__(self, tela_principal: QStackedWidget):
        super().__init__(tela_principal)
        self.setObjectName('telaFelizAnoNovo')

        self.animacao_labels = AnimacaoLabels([self.label_feliz_ano_novo_1,
                                          self.label_feliz_ano_novo_2])
        self.__threadpool = QThreadPool()

        layout_tela_feliz_ano_novo = QVBoxLayout()
        layout_tela_feliz_ano_novo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout_tela_feliz_ano_novo.addStretch(1)
        layout_tela_feliz_ano_novo.addWidget(self.container_logo_ieadern)
        layout_tela_feliz_ano_novo.addStretch(3)
        layout_tela_feliz_ano_novo.addWidget(self.container_feliz_ano_novo)
        layout_tela_feliz_ano_novo.addStretch(3)
        layout_tela_feliz_ano_novo.addLayout(self.layout_hora_atual)
        layout_tela_feliz_ano_novo.addStretch(1)

        self.setLayout(layout_tela_feliz_ano_novo)

    def animar_label_feliz_ano_novo(self):
        # for i in range(0, 16, 2):
        #     QTimer.singleShot(750 * i, self.tela_principal.app,
        #                       lambda: self.mudar_cor_labels_feliz_ano_novo('#99701F'))
        #     QTimer.singleShot(750 * (i + 1), self.tela_principal.app,
        #                       lambda: self.mudar_cor_labels_feliz_ano_novo('#FFFFFF'))
        #     print('batata')
        self.__threadpool.start(self.animacao_labels)

    def mudar_cor_labels_feliz_ano_novo(self, cor: str):
        self.label_feliz_ano_novo_1.setStyleSheet(f'color: {cor};')
        self.label_feliz_ano_novo_2.setStyleSheet(f'color: {cor};')

    def parar_animacao_label_feliz_ano_novo(self):
        self.animacao_labels.interromper_execucao = True
