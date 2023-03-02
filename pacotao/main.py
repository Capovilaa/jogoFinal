import os
import random
import sys
import time

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip, QLabel, QLineEdit
from PyQt5.QtGui import QMovie, QIcon
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5 import QtGui

#TODO _______________________ Menu _______________________
class Menu (QMainWindow):
    def __init__(self):
        super().__init__()
        #Tela menu
        self.topo = 40
        self.esquerda = 50
        self.largura = 1280
        self.altura = 720
        self.titulo = 'Menu'
        self.setWindowIcon(QIcon('../img/haunter.png'))

        #Background menu
        self.movie = QMovie('../gif/menu.gif')
        self.gif = QLabel(self)
        self.gif.setMovie(self.movie)
        self.gif.resize(1280,720)
        self.gif.setScaledContents(True)
        self.movie.start()

        # Botao Jokenpo
        self.btJokenpo = QPushButton('', self)
        self.btJokenpo.move(1050, 560)
        self.btJokenpo.resize(200, 80)
        self.btJokenpo.setStyleSheet('QPushButton {background-color:transparent}')
        self.btJokenpo.clicked.connect(self.abrirJokenpo)

        #Botao velha
        self.btVelha = QPushButton('', self)
        self.btVelha.move(1050,460)
        self.btVelha.resize(200,80)
        self.btVelha.setStyleSheet('QPushButton {background-color:transparent}')
        self.btVelha.clicked.connect(self.abrirVelha)

        # Botao forca
        self.btForca = QPushButton('', self)
        self.btForca.move(1050, 360)
        self.btForca.resize(200, 80)
        self.btForca.setStyleSheet('QPushButton {background-color:transparent}')
        self.btForca.clicked.connect(self.abrirForca)

        #Botão secreto
        self.btSecreto = QPushButton('', self)
        self.btSecreto.move(30, 350)
        self.btSecreto.resize(40, 35)
        self.btSecreto.setStyleSheet('QPushButton {background-color:transparent}')
        self.btSecreto.clicked.connect(self.abrirSecreto)

        #Media
        self.player = QMediaPlayer()
        self.playerClick = QMediaPlayer()

        #NAO APAGAR LINHA DE BAIXO
        self.carregarJanela()

    #Funções
    def carregarJanela(self):
        self.musicaMenu()
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.setMinimumSize(1280,720)
        self.setMaximumSize(1280,720)
        self.show()

    def sairTelaSecreta(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.setMinimumSize(1280,720)
        self.setMaximumSize(1280,720)
        self.show()

    def abrirVelha(self):
        self.musicaClick()
        self.close()
        self.player.stop()
        velha.carregarJanela()

    def abrirForca(self):
        self.musicaClick()
        self.close()
        self.player.stop()
        forca.carregarJanela()

    def abrirJokenpo(self):
        self.musicaClick()
        self.close()
        self.player.stop()
        jokenpo.carregarJanela()

    def abrirSecreto(self):
        self.musicaClick()
        self.close()
        menuSecreto.carregarJanela()

    def musicaMenu(self):
        file = os.path.join(os.getcwd(),'../efeitoSonoro/emerald.mp3')
        url = QUrl.fromLocalFile(file)
        content = QMediaContent(url)
        self.player.setMedia(content)
        self.player.play()

    def musicaClick(self):
        file = os.path.join(os.getcwd(),'../efeitoSonoro/click.mp3')
        url = QUrl.fromLocalFile(file)
        content = QMediaContent(url)
        self.playerClick.setMedia(content)
        self.playerClick.play()

    def pararMusica(self):
        self.player.stop()

#TODO _______________________ Menu Secreto _______________________

class MenuSecreto (QMainWindow):
    def __init__(self):
        super().__init__()
        #Tela menu
        self.topo = 40
        self.esquerda = 50
        self.largura = 1280
        self.altura = 720
        self.titulo = 'Secreto'
        self.setWindowIcon(QIcon('../img/haunter.png'))

        #Background menu
        self.movie = QMovie('../gif/menu2.gif')
        self.gif = QLabel(self)
        self.gif.setMovie(self.movie)
        self.gif.resize(1280,720)
        self.gif.setScaledContents(True)
        self.movie.start()

        # Botao Voltar
        self.btVoltar = QPushButton('', self)
        self.btVoltar.move(570, 480)
        self.btVoltar.resize(150, 60)
        self.btVoltar.setStyleSheet('QPushButton {background-color:transparent}')
        self.btVoltar.clicked.connect(self.voltarMenu)

        #Media
        self.player = QMediaPlayer()
        self.playerClick = QMediaPlayer()

    def carregarJanela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.setMinimumSize(1280,720)
        self.setMaximumSize(1280,720)
        self.show()

    def voltarMenu(self):
        menu.musicaClick()
        self.close()
        menu.sairTelaSecreta()

#TODO _______________________ Forca _______________________

class Forca(QMainWindow):
    def __init__(self):
        super().__init__()
        #Tela menu
        self.topo = 40
        self.esquerda = 50
        self.largura = 1280
        self.altura = 720
        self.titulo = 'Forca'
        self.setWindowIcon(QIcon('../img/haunter.png'))

        #Background menu
        self.movie = QMovie('../gif/forca.gif')
        self.gif = QLabel(self)
        self.gif.setMovie(self.movie)
        self.gif.resize(1280,720)
        self.gif.setScaledContents(True)
        self.movie.start()

        #Label vida
        self.lbVida = QLabel(self)
        self.lbVida.setText('')
        self.lbVida.move(25, 650)
        self.lbVida.setStyleSheet('QLabel {font:bold; font-size:30px; color:"black"}')
        self.lbVida.resize(250,45)

        #Caixa de texto (para inserir a letra)
        self.caixaTexto = QLineEdit(self)
        self.caixaTexto.setStyleSheet('QLineEdit{font:bold; font-size:30px; color:"black"}')
        self.caixaTexto.move(1050,305)
        self.caixaTexto.resize(34,35)

        #Botao enviar letra
        self.btEnviarLetra = QPushButton('', self)
        self.btEnviarLetra.move(1090, 305)
        self.btEnviarLetra.resize(102, 34)
        self.btEnviarLetra.setStyleSheet('QPushButton {font:bold; font-size:28px; background-color:transparent}')
        self.btEnviarLetra.clicked.connect(self.enviarLetraForca)

        #Label dica
        self.lbDica = QLabel(self)
        self.lbDica.setText('Dica: ')
        self.lbDica.move(560, 50)
        self.lbDica.setStyleSheet('QLabel {font:bold; font-size:20px; color:"black"}')
        self.lbDica.resize(250, 25)

        #Label dica2
        self.lbDica2 = QLabel(self)
        self.lbDica2.setText('')
        self.lbDica2.move(620, 50)
        self.lbDica2.setStyleSheet('QLabel {font:bold; font-size:20px; color:"black"}')
        self.lbDica2.resize(250, 25)

        #Label palavra
        self.lbPalavra = QLabel(self)
        self.lbPalavra.setText('')
        self.lbPalavra.move(620, 195)
        self.lbPalavra.setStyleSheet('QLabel {font:bold; font-size:35px; color:"black"}')
        self.lbPalavra.resize(500, 250)

        # Label letras chutadas
        self.lbChutes = QLabel(self)
        self.lbChutes.setText('')
        self.lbChutes.move(790, 50)
        self.lbChutes.setStyleSheet('QLabel {font:bold; font-size:20px; color:"black"}')
        self.lbChutes.resize(250, 25)

        #Botao voltar
        self.btSairForca = QPushButton('', self)
        self.btSairForca.move(16, 16)
        self.btSairForca.resize(26, 26)
        self.btSairForca.setStyleSheet('QPushButton {background-color:transparent}')
        self.btSairForca.clicked.connect(self.voltarForca)

        #Botao sair
        self.btRestartForca = QPushButton('', self)
        self.btRestartForca.move(16, 45)
        self.btRestartForca.resize(26, 26)
        self.btRestartForca.setStyleSheet('QPushButton {background-color:transparent}')
        self.btRestartForca.clicked.connect(self.resetartForca)

        #TODO Variáveis
        self.vidasRestantes = 5
        self.listaPalavras = ['arquiteto','ventoinha','browser','embarcacao']
        self.listaDicas = ['profissão','computador','navegação','flutua']
        self.listaLetrasChutadas = []
        self.palavraAtual = ''
        self.listaPalavraAtual = []
        self.texto = ''
        self.textoChute = ''

        # Media
        self.player = QMediaPlayer()

        #Inicia forca
        self.iniciarForca()

    #Funções
    def iniciarForca(self):
        self.aleatorio = random.randint(0, len(self.listaPalavras) - 1)
        self.palavraAtual = self.listaPalavras[self.aleatorio]
        self.lbDica2.setText(self.listaDicas[self.aleatorio])

        #Adiciona na lista underline
        for i in range(len(self.palavraAtual)):
            self.listaPalavraAtual.append('_ ')

        self.lbPalavra.setText('_ ' * len(self.listaPalavraAtual))
        self.lbVida.setText(str(self.vidasRestantes)+'x')

    def carregarJanela(self):
        self.musicaForca()
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.setMinimumSize(1280, 720)
        self.setMaximumSize(1280, 720)
        self.show()

    def keyPressEvent(self, event):
        self.enviarLetraForca()

    def musicaForca(self):
        file = os.path.join(os.getcwd(),'../efeitoSonoro/floresta.mp3')
        url = QUrl.fromLocalFile(file)
        content = QMediaContent(url)
        self.player.setMedia(content)
        self.player.play()

    def carregarVitoriaForca(self):
        self.player.stop()
        vitoriaForca.musicaVitoria()
        self.close()
        vitoriaForca.carregarJanela()

    def carregarDerrotaForca(self):
        self.player.stop()
        derrotaForca.musicaDerrota()
        self.close()
        derrotaForca.carregarJanela()

    def voltarForca(self):
        menu.musicaClick()
        self.resetartForca()
        self.player.stop()
        self.close()
        menu.carregarJanela()

    def resetartForca(self):
        self.vidasRestantes = 5
        self.listaLetrasChutadas.clear()
        self.listaPalavraAtual.clear()
        self.lbPalavra.setText('')
        self.lbDica2.setText('')
        self.lbChutes.setText('')
        self.caixaTexto.setFocus()
        self.iniciarForca()

    def enviarLetraForca(self):
        self.caixaTexto.text().strip().lower()
        if len(self.caixaTexto.text())==1 and self.caixaTexto.text()!= ' ':
            for i in range(len(self.palavraAtual)):
                if self.palavraAtual[i] == self.caixaTexto.text():
                    for j, k in enumerate(self.palavraAtual):
                        if k == self.caixaTexto.text():
                            self.listaPalavraAtual[j] = self.caixaTexto.text()+' '
                else:
                    if not self.listaLetrasChutadas.__contains__(self.caixaTexto.text().upper()+ ' '):
                        self.listaLetrasChutadas.append(self.caixaTexto.text().upper()+' ')
                        for l in self.listaLetrasChutadas:
                            self.textoChute += l
                        self.lbChutes.setText(self.textoChute)
                    self.textoChute = ''
            if self.caixaTexto.text() not in self.palavraAtual:
                self.vidasRestantes-=1
                self.lbVida.setText(str(self.vidasRestantes)+'x')

        for i in self.listaPalavraAtual:
            self.texto += i

        self.lbPalavra.setText(self.texto)
        self.texto = ''
        self.verificarVitoria()
        self.verificaDerrota()
        self.caixaTexto.setText('')
        self.caixaTexto.setFocus()

    def verificarVitoria(self):
        if not self.listaPalavraAtual.__contains__('_ '):
            self.carregarVitoriaForca()

    def verificaDerrota(self):
        if self.vidasRestantes < 1:
            self.carregarDerrotaForca()

#TODO _______________________ Vitória Forca _______________________

class VitoriaForca (QMainWindow):
    def __init__(self):
        super().__init__()
        #Tela menu
        self.topo = 40
        self.esquerda = 50
        self.largura = 1280
        self.altura = 720
        self.titulo = 'Secreto'
        self.setWindowIcon(QIcon('../img/haunter.png'))

        #Background menu
        self.movie = QMovie('../gif/vitoriaForca.gif')
        self.gif = QLabel(self)
        self.gif.setMovie(self.movie)
        self.gif.resize(1280,720)
        self.gif.setScaledContents(True)
        self.movie.start()

        # Botao voltar para o menu
        self.btMenu = QPushButton('', self)
        self.btMenu.move(750, 430)
        self.btMenu.resize(150, 60)
        self.btMenu.setStyleSheet('QPushButton {background-color:transparent}')
        self.btMenu.clicked.connect(self.voltarMenu)

        # Botao jogar de novo
        self.btJogarAgain = QPushButton('', self)
        self.btJogarAgain.move(400, 425)
        self.btJogarAgain.resize(150, 60)
        self.btJogarAgain.setStyleSheet('QPushButton {background-color:transparent}')
        self.btJogarAgain.clicked.connect(self.jogarNovamente)

        # Botao voltar para menu
        self.btJogar = QPushButton('', self)
        self.btJogar.move(570, 480)
        self.btJogar.resize(150, 60)
        self.btJogar.setStyleSheet('QPushButton {background-color:transparent}')
        self.btJogar.clicked.connect(self.voltarMenu)

        # Media
        self.player = QMediaPlayer()

    def carregarJanela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.setMinimumSize(1280,720)
        self.setMaximumSize(1280,720)
        self.show()

    def musicaVitoria(self):
        file = os.path.join(os.getcwd(), '../efeitoSonoro/vitoria.mp3')
        url = QUrl.fromLocalFile(file)
        content = QMediaContent(url)
        self.player.setMedia(content)
        self.player.play()

    def jogarNovamente(self):
        menu.musicaClick()
        forca.resetartForca()
        self.player.stop()
        self.close()
        forca.carregarJanela()

    def voltarMenu(self):
        menu.musicaClick()
        self.player.stop()
        self.close()
        forca.resetartForca()
        menu.carregarJanela()

#TODO _______________________ Derrota Forca _______________________

class DerrotaForca (QMainWindow):
    def __init__(self):
        super().__init__()
        #Tela menu
        self.topo = 40
        self.esquerda = 50
        self.largura = 1280
        self.altura = 720
        self.titulo = 'Secreto'
        self.setWindowIcon(QIcon('../img/haunter.png'))

        #Background menu
        self.movie = QMovie('../gif/derrotaForca.gif')
        self.gif = QLabel(self)
        self.gif.setMovie(self.movie)
        self.gif.resize(1280,720)
        self.gif.setScaledContents(True)
        self.movie.start()

        # Botao voltar para o menu
        self.btMenu = QPushButton('', self)
        self.btMenu.move(750, 430)
        self.btMenu.resize(150, 60)
        self.btMenu.setStyleSheet('QPushButton {background-color:transparent}')
        self.btMenu.clicked.connect(self.voltarMenu)

        # Botao jogar de novo
        self.btJogarAgain = QPushButton('', self)
        self.btJogarAgain.move(400, 425)
        self.btJogarAgain.resize(150, 60)
        self.btJogarAgain.setStyleSheet('QPushButton {background-color:transparent}')
        self.btJogarAgain.clicked.connect(self.jogarNovamente)

        # Botao voltar para menu
        self.btJogar = QPushButton('', self)
        self.btJogar.move(570, 480)
        self.btJogar.resize(150, 60)
        self.btJogar.setStyleSheet('QPushButton {background-color:transparent}')
        self.btJogar.clicked.connect(self.voltarMenu)

        #Media
        self.player = QMediaPlayer()

    def carregarJanela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.setMinimumSize(1280,720)
        self.setMaximumSize(1280,720)
        self.show()

    def musicaDerrota(self):
        file = os.path.join(os.getcwd(), '../efeitoSonoro/derrota.mp3')
        url = QUrl.fromLocalFile(file)
        content = QMediaContent(url)
        self.player.setMedia(content)
        self.player.play()

    def jogarNovamente(self):
        menu.musicaClick()
        forca.resetartForca()
        self.player.stop()
        self.close()
        forca.carregarJanela()

    def voltarMenu(self):
        menu.musicaClick()
        self.player.stop()
        self.close()
        forca.resetartForca()
        menu.carregarJanela()

#TODO _______________________ Jogo da velha _______________________
class Velha (QMainWindow):
    def __init__(self):
        super().__init__()
        #Tela menu
        self.topo = 40
        self.esquerda = 50
        self.largura = 1280
        self.altura = 720
        self.titulo = 'Jogo da Velha'
        self.setWindowIcon(QIcon('../img/haunter.png'))

        #Background menu
        self.movie = QMovie('../gif/velha.gif')
        self.gif = QLabel(self)
        self.gif.setMovie(self.movie)
        self.gif.resize(1280,720)
        self.gif.setScaledContents(True)
        self.movie.start()

        # Botao sair velha
        self.btSairVelha = QPushButton('', self)
        self.btSairVelha.move(16, 16)
        self.btSairVelha.resize(26, 26)
        self.btSairVelha.setStyleSheet('QPushButton {background-color:transparent}')
        self.btSairVelha.clicked.connect(self.sairVelha)

        # Botao resetar velha
        self.btResetartVelha = QPushButton('', self)
        self.btResetartVelha.move(16, 45)
        self.btResetartVelha.resize(26, 26)
        self.btResetartVelha.setStyleSheet('QPushButton {background-color:transparent}')
        self.btResetartVelha.clicked.connect(self.resetar)

        #Label placar jogador
        self.lbPlacarJogador = QLabel(self)
        self.lbPlacarJogador.setText('0')
        self.lbPlacarJogador.move(1150, 40)
        self.lbPlacarJogador.setStyleSheet('QLabel {font:bold; font-size:30px; color:"white"}')
        self.lbPlacarJogador.resize(30, 40)

        # Label placar computador
        self.lbPlacarComputador = QLabel(self)
        self.lbPlacarComputador.setText('0')
        self.lbPlacarComputador.move(1205, 40)
        self.lbPlacarComputador.setStyleSheet('QLabel {font:bold; font-size:30px; color:"white"}')
        self.lbPlacarComputador.resize(30, 40)

        #TODO botões grade da velha

        #Botão 0
        self.btVelha0 = QPushButton('', self)
        self.btVelha0.move(370, 100)
        self.btVelha0.resize(160, 160)
        self.btVelha0.setStyleSheet('QPushButton {background-color:transparent}')
        self.btVelha0.clicked.connect(self.jogadorJogou0)

        # Botão 1
        self.btVelha1 = QPushButton('', self)
        self.btVelha1.move(550, 100)
        self.btVelha1.resize(160, 160)
        self.btVelha1.setStyleSheet('QPushButton {background-color:transparent}')
        self.btVelha1.clicked.connect(self.jogadorJogou1)

        # Botão 2
        self.btVelha2 = QPushButton('', self)
        self.btVelha2.move(740, 100)
        self.btVelha2.resize(160, 160)
        self.btVelha2.setStyleSheet('QPushButton {background-color:transparent}')
        self.btVelha2.clicked.connect(self.jogadorJogou2)

        # Botão 3
        self.btVelha3 = QPushButton('', self)
        self.btVelha3.move(370, 285)
        self.btVelha3.resize(160, 160)
        self.btVelha3.setStyleSheet('QPushButton {background-color:transparent}')
        self.btVelha3.clicked.connect(self.jogadorJogou3)

        # Botão 4
        self.btVelha4 = QPushButton('', self)
        self.btVelha4.move(550, 285)
        self.btVelha4.resize(160, 160)
        self.btVelha4.setStyleSheet('QPushButton {background-color:transparent}')
        self.btVelha4.clicked.connect(self.jogadorJogou4)

        # Botão 5
        self.btVelha5 = QPushButton('', self)
        self.btVelha5.move(740, 285)
        self.btVelha5.resize(160, 160)
        self.btVelha5.setStyleSheet('QPushButton {background-color:transparent}')
        self.btVelha5.clicked.connect(self.jogadorJogou5)

        # Botão 6
        self.btVelha6 = QPushButton('', self)
        self.btVelha6.move(370, 465)
        self.btVelha6.resize(160, 160)
        self.btVelha6.setStyleSheet('QPushButton {background-color:transparent}')
        self.btVelha6.clicked.connect(self.jogadorJogou6)

        # Botão 7
        self.btVelha7 = QPushButton('', self)
        self.btVelha7.move(550, 465)
        self.btVelha7.resize(160, 160)
        self.btVelha7.setStyleSheet('QPushButton {background-color:transparent}')
        self.btVelha7.clicked.connect(self.jogadorJogou7)

        # Botão 8
        self.btVelha8 = QPushButton('', self)
        self.btVelha8.move(740, 465)
        self.btVelha8.resize(160, 160)
        self.btVelha8.setStyleSheet('QPushButton {background-color:transparent}')
        self.btVelha8.clicked.connect(self.jogadorJogou8)

        #Media
        self.player = QMediaPlayer()

        #TODO variáveis
        self.contadorJogador = 0
        self.contadorComputador = 0
        self.listaVelha = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]

    def carregarJanela(self):
        self.musicaVelha()
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.setMinimumSize(1280,720)
        self.setMaximumSize(1280,720)
        self.show()

    def musicaVelha(self):
        file = os.path.join(os.getcwd(),'../efeitoSonoro/navio.mp3')
        url = QUrl.fromLocalFile(file)
        content = QMediaContent(url)
        self.player.setMedia(content)
        self.player.play()

    def sairVelha(self):
        menu.musicaClick()
        self.player.stop()
        self.contadorJogador = 0
        self.contadorComputador = 0
        self.close()
        self.resetar()
        self.lbPlacarComputador.setText('')
        self.lbPlacarJogador.setText('')
        menu.carregarJanela()

    def computadorJogou0(self):
        self.btVelha0.setStyleSheet('border-image: url(../img/haunter.png);')
        self.btVelha0.setDisabled(True)
        self.listaVelha[0][0] = 2
        if not self.verificaVitoria():
            self.travarVelha(False)

    def computadorJogou1(self):
        self.btVelha1.setStyleSheet('border-image: url(../img/haunter.png);')
        self.btVelha1.setDisabled(True)
        self.listaVelha[0][1] = 2
        if not self.verificaVitoria():
            self.travarVelha(False)

    def computadorJogou2(self):
        self.btVelha2.setStyleSheet('border-image: url(../img/haunter.png);')
        self.btVelha2.setDisabled(True)
        self.listaVelha[0][2] = 2
        if not self.verificaVitoria():
            self.travarVelha(False)

    def computadorJogou3(self):
        self.btVelha3.setStyleSheet('border-image: url(../img/haunter.png);')
        self.btVelha3.setDisabled(True)
        self.listaVelha[1][0] = 2
        if not self.verificaVitoria():
            self.travarVelha(False)

    def computadorJogou4(self):
        self.btVelha4.setStyleSheet('border-image: url(../img/haunter.png);')
        self.btVelha4.setDisabled(True)
        self.listaVelha[1][1] = 2
        if not self.verificaVitoria():
            self.travarVelha(False)

    def computadorJogou5(self):
        self.btVelha5.setStyleSheet('border-image: url(../img/haunter.png);')
        self.btVelha5.setDisabled(True)
        self.listaVelha[1][2] = 2
        if not self.verificaVitoria():
            self.travarVelha(False)

    def computadorJogou6(self):
        self.btVelha6.setStyleSheet('border-image: url(../img/haunter.png);')
        self.btVelha6.setDisabled(True)
        self.listaVelha[2][0] = 2
        if not self.verificaVitoria():
            self.travarVelha(False)

    def computadorJogou7(self):
        self.btVelha7.setStyleSheet('border-image: url(../img/haunter.png);')
        self.btVelha7.setDisabled(True)
        self.listaVelha[2][1] = 2
        if not self.verificaVitoria():
            self.travarVelha(False)

    def computadorJogou8(self):
        self.btVelha0.setStyleSheet('border-image: url(../img/haunter.png);')
        self.btVelha0.setDisabled(True)
        self.listaVelha[2][2] = 2
        if not self.verificaVitoria():
            self.travarVelha(False)

    #Jogadas jogador
    def jogadorJogou0(self):
        self.btVelha0.setStyleSheet('border-image: url(../img/charizard.png);')
        self.btVelha0.setDisabled(True)
        self.listaVelha[0][0] = 1
        if self.verificaVitoria():
            self.jogadaPc()

    def jogadorJogou1(self):
        self.btVelha1.setStyleSheet('border-image: url(../img/charizard.png);')
        self.btVelha1.setDisabled(True)
        self.listaVelha[0][1] = 1
        if self.verificaVitoria():
            self.jogadaPc()

    def jogadorJogou2(self):
        self.btVelha2.setStyleSheet('border-image: url(../img/charizard.png);')
        self.btVelha2.setDisabled(True)
        self.listaVelha[0][2] = 1
        if self.verificaVitoria():
            self.jogadaPc()

    def jogadorJogou3(self):
        self.btVelha3.setStyleSheet('border-image: url(../img/charizard.png);')
        self.btVelha3.setDisabled(True)
        self.listaVelha[1][0] = 1
        if self.verificaVitoria():
            self.jogadaPc()

    def jogadorJogou4(self):
        self.btVelha4.setStyleSheet('border-image: url(../img/charizard.png);')
        self.btVelha4.setDisabled(True)
        self.listaVelha[1][1] = 1
        if self.verificaVitoria():
            self.jogadaPc()

    def jogadorJogou5(self):
        self.btVelha5.setStyleSheet('border-image: url(../img/charizard.png);')
        self.btVelha5.setDisabled(True)
        self.listaVelha[1][2] = 1
        if self.verificaVitoria():
            self.jogadaPc()

    def jogadorJogou6(self):
        self.btVelha6.setStyleSheet('border-image: url(../img/charizard.png);')
        self.btVelha6.setDisabled(True)
        self.listaVelha[2][0] = 1
        if self.verificaVitoria():
            self.jogadaPc()

    def jogadorJogou7(self):
        self.btVelha7.setStyleSheet('border-image: url(../img/charizard.png);')
        self.btVelha7.setDisabled(True)
        self.listaVelha[2][1] = 1
        if self.verificaVitoria():
            self.jogadaPc()

    def jogadorJogou8(self):
        self.btVelha8.setStyleSheet('border-image: url(../img/charizard.png);')
        self.btVelha8.setDisabled(True)
        self.listaVelha[2][2] = 1
        if self.verificaVitoria():
            self.jogadaPc()

    def jogadaPc(self):
        aleatorio = random.randint(0,8)
        if aleatorio == 0:
            if self.listaVelha[0][0] == 0:
                self.computadorJogou0()
            else:
                self.jogadaPc()
        elif aleatorio == 1:
            if self.listaVelha[0][1] == 0:
                self.computadorJogou1()
            else:
                self.jogadaPc()
        elif aleatorio == 2:
            if self.listaVelha[0][2] == 0:
                self.computadorJogou2()
            else:
                self.jogadaPc()
        elif aleatorio == 3:
            if self.listaVelha[1][0] == 0:
                self.computadorJogou3()
            else:
                self.jogadaPc()
        elif aleatorio == 4:
            if self.listaVelha[1][1] == 0:
                self.computadorJogou4()
            else:
                self.jogadaPc()
        elif aleatorio == 5:
            if self.listaVelha[1][2] == 0:
                self.computadorJogou5()
            else:
                self.jogadaPc()
        elif aleatorio == 6:
            if self.listaVelha[2][0] == 0:
                self.computadorJogou6()
            else:
                self.jogadaPc()
        elif aleatorio == 7:
            if self.listaVelha[2][1] == 0:
                self.computadorJogou7()
            else:
                self.jogadaPc()
        elif aleatorio ==8:
            if self.listaVelha[2][2] == 0:
                self.computadorJogou8()
            else:
                self.jogadaPc()

    def verificaVitoria(self):
        linha1 = self.listaVelha[0]
        linha2 = self.listaVelha[1]
        linha3 = self.listaVelha[2]
        coluna1 = [self.listaVelha[0][0], self.listaVelha[1][0], self.listaVelha[2][0]]
        coluna2 = [self.listaVelha[0][1], self.listaVelha[1][1], self.listaVelha[2][1]]
        coluna3 = [self.listaVelha[0][2], self.listaVelha[1][2], self.listaVelha[2][2]]
        diagonal1 = [self.listaVelha[0][0], self.listaVelha[1][1], self.listaVelha[2][2]]
        diagonal2 = [self.listaVelha[2][0], self.listaVelha[1][1], self.listaVelha[0][2]]
        velha = [linha1,linha2,linha3,coluna1,coluna2,coluna3,diagonal1,diagonal2]
        for v in velha:
            if v == [1,1,1]:
                int(self.contadorJogador)
                self.contadorJogador+=1
                self.lbPlacarJogador.setText('')
                self.lbPlacarJogador.setText(str(self.contadorJogador))
                self.travarVelha(False)
                return False
            elif v == [2,2,2]:
                int(self.contadorComputador)
                self.contadorComputador+=1
                self.lbPlacarComputador.setText('')
                self.lbPlacarComputador.setText(str(self.contadorComputador))
                self.travarVelha(False)
                return False
        return True

    def travarVelha(self,condicao):
        self.btVelha0.setEnabled(condicao)
        self.btVelha1.setEnabled(condicao)
        self.btVelha2.setEnabled(condicao)
        self.btVelha3.setEnabled(condicao)
        self.btVelha4.setEnabled(condicao)
        self.btVelha5.setEnabled(condicao)
        self.btVelha6.setEnabled(condicao)
        self.btVelha7.setEnabled(condicao)
        self.btVelha8.setEnabled(condicao)

    def resetar(self):
        self.travarVelha(True)
        self.btVelha0.setStyleSheet('background-image:none; background-color:transparent')
        self.btVelha1.setStyleSheet('background-image:none; background-color:transparent')
        self.btVelha2.setStyleSheet('background-image:none; background-color:transparent')
        self.btVelha3.setStyleSheet('background-image:none; background-color:transparent')
        self.btVelha4.setStyleSheet('background-image:none; background-color:transparent')
        self.btVelha5.setStyleSheet('background-image:none; background-color:transparent')
        self.btVelha6.setStyleSheet('background-image:none; background-color:transparent')
        self.btVelha7.setStyleSheet('background-image:none; background-color:transparent')
        self.btVelha8.setStyleSheet('background-image:none; background-color:transparent')
        self.listaVelha = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]

#TODO _______________________ Jokenpo _______________________

class Jokenpo (QMainWindow):
    def __init__(self):
        super().__init__()
        #Tela menu
        self.topo = 40
        self.esquerda = 50
        self.largura = 1280
        self.altura = 720
        self.titulo = 'Jokenpo'
        self.setWindowIcon(QIcon('../img/haunter.png'))

        #Background menu
        self.movie = QMovie('../gif/jokenpoStart.gif')
        self.gif = QLabel(self)
        self.gif.setMovie(self.movie)
        self.gif.resize(1280,720)
        self.gif.setScaledContents(True)
        self.movie.start()

        # Botao voltar para o menu
        self.btMenu = QPushButton('', self)
        self.btMenu.move(16, 16)
        self.btMenu.resize(26, 26)
        self.btMenu.setStyleSheet('QPushButton {background-color:transparent}')
        self.btMenu.clicked.connect(self.voltarMenu)

        # Botao jogar de novo
        self.btJogarAgain = QPushButton('', self)
        self.btJogarAgain.move(16, 45)
        self.btJogarAgain.resize(26, 26)
        self.btJogarAgain.setStyleSheet('QPushButton {background-color:transparent}')
        self.btJogarAgain.clicked.connect(self.jogarNovamente)

        # Label jogada jogador
        self.lbJogadaJogador = QLabel(self)
        self.lbJogadaJogador.move(570, 400)
        self.lbJogadaJogador.resize(95, 80)
        self.lbJogadaJogador.setScaledContents(True)

        # Label jogada computador
        self.lbJogadaComputador = QLabel(self)
        self.lbJogadaComputador.move(730, 200)
        self.lbJogadaComputador.resize(95, 80)
        self.lbJogadaComputador.setScaledContents(True)

        # Botao jogar pedra
        self.btPedra = QPushButton('', self)
        self.btPedra.move(665, 560)
        self.btPedra.resize(150, 60)
        self.btPedra.setStyleSheet('QPushButton {background-color:transparent}')
        self.btPedra.clicked.connect(lambda : self.jogadajogador(1))

        # Botao jogar papel
        self.btPapel = QPushButton('', self)
        self.btPapel.move(980, 560)
        self.btPapel.resize(150, 60)
        self.btPapel.setStyleSheet('QPushButton {background-color:transparent}')
        self.btPapel.clicked.connect(lambda : self.jogadajogador(2))

        # Botao jogar tesoura
        self.btTesoura = QPushButton('', self)
        self.btTesoura.move(665, 650)
        self.btTesoura.resize(220, 60)
        self.btTesoura.setStyleSheet('QPushButton {background-color:transparent}')
        self.btTesoura.clicked.connect(lambda : self.jogadajogador(3))

        # Botao start
        self.btStart = QPushButton('', self)
        self.btStart.move(1020, 650)
        self.btStart.resize(150, 60)
        self.btStart.setStyleSheet('QPushButton {background-color:transparent}')
        self.btStart.clicked.connect(self.comecarJogo)

        #Label placar jogador
        self.lbPlacarJogador = QLabel(self)
        self.lbPlacarJogador.setText('0')
        self.lbPlacarJogador.move(1150, 40)
        self.lbPlacarJogador.setStyleSheet('QLabel {font:bold; font-size:23px; color:"white"}')
        self.lbPlacarJogador.resize(30, 40)

        # Label placar computador
        self.lbPlacarComputador = QLabel(self)
        self.lbPlacarComputador.setText('0')
        self.lbPlacarComputador.move(1205, 40)
        self.lbPlacarComputador.setStyleSheet('QLabel {font:bold; font-size:23px; color:"white"}')
        self.lbPlacarComputador.resize(30, 40)

        # Label Console
        self.lbConsole = QLabel(self)
        self.lbConsole.setText('Aperte Start para iniciar')
        self.lbConsole.move(55, 565)
        self.lbConsole.setStyleSheet('QLabel {font:bold; font-size:24px; color:"white"; font-family:"Brick Sans"}')
        self.lbConsole.resize(600, 40)

        #Media
        self.player = QMediaPlayer()

        #TODO variáevies
        self.contadorJogador = 0
        self.contadorComputador = 0
        self.escolhaComputador = 0
        self.escolhaJogador = 0
        self.contadorGeral = 0

        #Timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.sortearJogadaComputador)

    def carregarJanela(self):
        self.musicajokenpo()
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.setMinimumSize(1280,720)
        self.setMaximumSize(1280,720)
        self.btPedra.setDisabled(True)
        self.btPapel.setDisabled(True)
        self.btTesoura.setDisabled(True)
        self.show()

    def comecarJogo(self):
        menu.musicaClick()
        self.contadorJogador = 0
        self.contadorComputador = 0
        self.contadorGeral = 0
        self.lbConsole.setText('Começando...')
        self.gif.setPixmap(QtGui.QPixmap('../img/jokenpo.png'))
        self.btPedra.setEnabled(True)
        self.btPapel.setEnabled(True)
        self.btTesoura.setEnabled(True)
        self.btStart.setEnabled(False)
        self.timer.start(2000)

    def musicajokenpo(self):
        file = os.path.join(os.getcwd(), '../efeitoSonoro/batalha.mp3')
        url = QUrl.fromLocalFile(file)
        content = QMediaContent(url)
        self.player.setMedia(content)
        self.player.play()

    def sortearJogadaComputador(self):
        self.verificaJogada()
        aleatorio = random.randint(1,3)
        if aleatorio == 1:
            self.lbJogadaComputador.setPixmap(QtGui.QPixmap('../img/pedra.png'))
            self.escolhaComputador = 1
        elif aleatorio ==2:
            self.lbJogadaComputador.setPixmap(QtGui.QPixmap('../img/papel.png'))
            self.escolhaComputador = 2
        else:
            self.lbJogadaComputador.setPixmap(QtGui.QPixmap('../img/tesoura.png'))
            self.escolhaComputador = 3

    def jogadajogador(self, escJogador):
        if escJogador ==1:
            self.lbJogadaJogador.setPixmap(QtGui.QPixmap('../img/pedra.png'))
            self.escolhaJogador = 1
        elif escJogador ==2:
            self.lbJogadaJogador.setPixmap(QtGui.QPixmap('../img/papel.png'))
            self.escolhaJogador = 2
        else:
            self.lbJogadaJogador.setPixmap(QtGui.QPixmap('../img/tesoura.png'))
            self.escolhaJogador = 3
        self.verificaJogada()

    def verificaJogada(self):
        if self.contadorGeral == 24:
            self.jogarNovamente()
        if self.escolhaJogador == self.escolhaComputador:
            self.lbConsole.setText('Empate')
        elif self.escolhaJogador == 1 and self.escolhaComputador == 3 or self.escolhaJogador == 2 and self.escolhaComputador == 1 or self.escolhaJogador == 3 and self.escolhaComputador == 2:
            self.contadorJogador +=1
            self.lbConsole.setText('Vencedor: Jogador')
            self.contadorGeral += 1
        elif self.escolhaJogador == 0 or self.escolhaComputador == 1 and self.escolhaJogador == 3 or self.escolhaComputador == 2 and self.escolhaJogador == 1 or self.escolhaComputador == 3 and self.escolhaJogador ==2:
            if self.escolhaJogador == 0:
                self.lbJogadaJogador.setPixmap(QtGui.QPixmap(''))
            self.contadorComputador += 1
            self.lbConsole.setText('Vencedor: Computador')
            self.contadorGeral += 1
        self.lbPlacarJogador.setText(str(self.contadorJogador))
        self.lbPlacarComputador.setText(str(self.contadorComputador))
        self.escolhaJogador = 0

    def jogarNovamente(self):
        menu.musicaClick()
        self.btStart.setEnabled(True)
        self.btPedra.setDisabled(True)
        self.btPapel.setDisabled(True)
        self.btTesoura.setDisabled(True)
        if self.contadorGeral == 24:
            if self.contadorComputador > self.contadorJogador:
                self.lbConsole.setText('Computador fez mais pontos')
            elif self.contadorJogador > self.contadorComputador:
                self.lbConsole.setText('Jogador fez mais pontos')
        self.gif.setPixmap(QtGui.QPixmap('../gif/jokenpoStart.gif'))
        self.gif.setMovie(self.movie)
        self.lbJogadaJogador.setPixmap(QtGui.QPixmap(''))
        self.lbJogadaComputador.setPixmap(QtGui.QPixmap(''))
        self.timer.stop()

    def voltarMenu(self):
        menu.musicaClick()
        self.player.stop()
        self.close()
        self.gif.setMovie(self.movie)
        self.movie.start()
        self.btStart.setEnabled(True)
        menu.carregarJanela()

#TODO _______________________ Main _______________________

if __name__ == '__main__':
    aplicacao = QApplication(sys.argv)
    menu = Menu()
    vitoriaForca = VitoriaForca()
    derrotaForca = DerrotaForca()
    menuSecreto = MenuSecreto()
    forca = Forca()
    velha = Velha()
    jokenpo = Jokenpo()
    sys.exit(aplicacao.exec_())
