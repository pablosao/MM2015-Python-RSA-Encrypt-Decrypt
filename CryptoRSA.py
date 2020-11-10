# -*- coding: utf-8 -*-

#      Nombre: Encriptación RSA
#       Fecha:  10 de noviembre de 2020
#  Creado por:
#              Pablo Sao
#              Mirka Monzón
# Descripción: El programa genera las llaves (pública y privada) para
#              encriptar el texto contenido en un archivo .txt
#


from PyQt5 import QtCore, QtGui, QtWidgets
from pathlib import Path

class Ui_frmCryptoRSA(object):
    def setupUi(self, frmCryptoRSA):
        frmCryptoRSA.setObjectName("frmCryptoRSA")
        frmCryptoRSA.setWindowModality(QtCore.Qt.NonModal)
        frmCryptoRSA.resize(930, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(frmCryptoRSA.sizePolicy().hasHeightForWidth())
        frmCryptoRSA.setSizePolicy(sizePolicy)
        frmCryptoRSA.setMinimumSize(QtCore.QSize(700, 480))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("files/privacy.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        frmCryptoRSA.setWindowIcon(icon)
        frmCryptoRSA.setTabShape(QtWidgets.QTabWidget.Rounded)
        frmCryptoRSA.setDockNestingEnabled(True)
        frmCryptoRSA.setDockOptions(QtWidgets.QMainWindow.AllowNestedDocks|QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks|QtWidgets.QMainWindow.ForceTabbedDocks|QtWidgets.QMainWindow.VerticalTabs)
        self.mainWidget = QtWidgets.QWidget(frmCryptoRSA)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainWidget.sizePolicy().hasHeightForWidth())
        self.mainWidget.setSizePolicy(sizePolicy)
        self.mainWidget.setObjectName("mainWidget")
        self.tabcontrol = QtWidgets.QTabWidget(self.mainWidget)
        self.tabcontrol.setGeometry(QtCore.QRect(10, 10, 911, 581))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabcontrol.sizePolicy().hasHeightForWidth())
        self.tabcontrol.setSizePolicy(sizePolicy)
        self.tabcontrol.setMinimumSize(QtCore.QSize(680, 460))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.tabcontrol.setFont(font)
        self.tabcontrol.setTabPosition(QtWidgets.QTabWidget.West)
        self.tabcontrol.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabcontrol.setIconSize(QtCore.QSize(26, 26))
        self.tabcontrol.setObjectName("tabcontrol")
        self.tabencriptado = QtWidgets.QWidget()
        self.tabencriptado.setObjectName("tabencriptado")
        self.btubicacion_exporta_llave = QtWidgets.QPushButton(self.tabencriptado)
        self.btubicacion_exporta_llave.setGeometry(QtCore.QRect(790, 90, 51, 31))
        self.btubicacion_exporta_llave.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btubicacion_exporta_llave.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("files/file.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btubicacion_exporta_llave.setIcon(icon1)
        self.btubicacion_exporta_llave.setIconSize(QtCore.QSize(24, 24))
        self.btubicacion_exporta_llave.setAutoDefault(False)
        self.btubicacion_exporta_llave.setDefault(False)
        self.btubicacion_exporta_llave.setFlat(False)
        self.btubicacion_exporta_llave.setObjectName("btubicacion_exporta_llave")
        self.tbubicacion_exporta_key = QtWidgets.QLineEdit(self.tabencriptado)
        self.tbubicacion_exporta_key.setGeometry(QtCore.QRect(120, 90, 661, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.tbubicacion_exporta_key.setFont(font)
        self.tbubicacion_exporta_key.setReadOnly(True)
        self.tbubicacion_exporta_key.setObjectName("tbubicacion_exporta_key")
        self.lbdestino_llave = QtWidgets.QLabel(self.tabencriptado)
        self.lbdestino_llave.setGeometry(QtCore.QRect(30, 90, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.lbdestino_llave.setFont(font)
        self.lbdestino_llave.setObjectName("lbdestino_llave")
        self.lbarchivo_encriptar = QtWidgets.QLabel(self.tabencriptado)
        self.lbarchivo_encriptar.setGeometry(QtCore.QRect(40, 140, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.lbarchivo_encriptar.setFont(font)
        self.lbarchivo_encriptar.setObjectName("lbarchivo_encriptar")
        self.lbubicacion_archivo_enc = QtWidgets.QLineEdit(self.tabencriptado)
        self.lbubicacion_archivo_enc.setGeometry(QtCore.QRect(120, 140, 661, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lbubicacion_archivo_enc.setFont(font)
        self.lbubicacion_archivo_enc.setReadOnly(True)
        self.lbubicacion_archivo_enc.setObjectName("lbubicacion_archivo_enc")
        self.btubicacion_archivo_enc = QtWidgets.QPushButton(self.tabencriptado)
        self.btubicacion_archivo_enc.setGeometry(QtCore.QRect(790, 140, 51, 31))
        self.btubicacion_archivo_enc.setText("")
        self.btubicacion_archivo_enc.setIcon(icon1)
        self.btubicacion_archivo_enc.setIconSize(QtCore.QSize(24, 24))
        self.btubicacion_archivo_enc.setObjectName("btubicacion_archivo_enc")
        self.lbencriptado_archivo = QtWidgets.QLabel(self.tabencriptado)
        self.lbencriptado_archivo.setGeometry(QtCore.QRect(230, 30, 421, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.lbencriptado_archivo.setFont(font)
        self.lbencriptado_archivo.setObjectName("lbencriptado_archivo")
        self.temensaje_enc = QtWidgets.QTextEdit(self.tabencriptado)
        self.temensaje_enc.setEnabled(False)
        self.temensaje_enc.setGeometry(QtCore.QRect(30, 220, 811, 281))
        self.temensaje_enc.setObjectName("temensaje_enc")
        self.lbmensaje_enc = QtWidgets.QLabel(self.tabencriptado)
        self.lbmensaje_enc.setGeometry(QtCore.QRect(30, 180, 261, 31))
        self.lbmensaje_enc.setObjectName("lbmensaje_enc")
        self.btencriptar_archivo = QtWidgets.QPushButton(self.tabencriptado)
        self.btencriptar_archivo.setGeometry(QtCore.QRect(370, 510, 151, 51))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("files/btencripar.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btencriptar_archivo.setIcon(icon2)
        self.btencriptar_archivo.setIconSize(QtCore.QSize(32, 32))
        self.btencriptar_archivo.setObjectName("btencriptar_archivo")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("files/Encriptado.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabcontrol.addTab(self.tabencriptado, icon3, "")
        self.tabdesencriptado = QtWidgets.QWidget()
        self.tabdesencriptado.setObjectName("tabdesencriptado")
        self.lbdesencriptado_archivo = QtWidgets.QLabel(self.tabdesencriptado)
        self.lbdesencriptado_archivo.setGeometry(QtCore.QRect(190, 20, 461, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.lbdesencriptado_archivo.setFont(font)
        self.lbdesencriptado_archivo.setObjectName("lbdesencriptado_archivo")
        self.lbdestino_llave_2 = QtWidgets.QLabel(self.tabdesencriptado)
        self.lbdestino_llave_2.setGeometry(QtCore.QRect(50, 80, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.lbdestino_llave_2.setFont(font)
        self.lbdestino_llave_2.setObjectName("lbdestino_llave_2")
        self.btubicacion_archivo_desc = QtWidgets.QPushButton(self.tabdesencriptado)
        self.btubicacion_archivo_desc.setGeometry(QtCore.QRect(790, 130, 51, 31))
        self.btubicacion_archivo_desc.setText("")
        self.btubicacion_archivo_desc.setIcon(icon1)
        self.btubicacion_archivo_desc.setIconSize(QtCore.QSize(24, 24))
        self.btubicacion_archivo_desc.setObjectName("btubicacion_archivo_desc")
        self.lbmensaje_enc_2 = QtWidgets.QLabel(self.tabdesencriptado)
        self.lbmensaje_enc_2.setGeometry(QtCore.QRect(30, 170, 261, 31))
        self.lbmensaje_enc_2.setObjectName("lbmensaje_enc_2")
        self.btdesencriptar_archivo = QtWidgets.QPushButton(self.tabdesencriptado)
        self.btdesencriptar_archivo.setGeometry(QtCore.QRect(360, 500, 171, 61))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("files/btdesencripar.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btdesencriptar_archivo.setIcon(icon4)
        self.btdesencriptar_archivo.setIconSize(QtCore.QSize(32, 32))
        self.btdesencriptar_archivo.setObjectName("btdesencriptar_archivo")
        self.temensaje_desc = QtWidgets.QTextEdit(self.tabdesencriptado)
        self.temensaje_desc.setEnabled(True)
        self.temensaje_desc.setGeometry(QtCore.QRect(30, 210, 811, 281))
        self.temensaje_desc.setReadOnly(True)
        self.temensaje_desc.setObjectName("temensaje_desc")
        self.lbarchivo_encriptar_2 = QtWidgets.QLabel(self.tabdesencriptado)
        self.lbarchivo_encriptar_2.setGeometry(QtCore.QRect(40, 130, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.lbarchivo_encriptar_2.setFont(font)
        self.lbarchivo_encriptar_2.setObjectName("lbarchivo_encriptar_2")
        self.lbubicacion_archivo_desc = QtWidgets.QLineEdit(self.tabdesencriptado)
        self.lbubicacion_archivo_desc.setGeometry(QtCore.QRect(120, 130, 661, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lbubicacion_archivo_desc.setFont(font)
        self.lbubicacion_archivo_desc.setReadOnly(True)
        self.lbubicacion_archivo_desc.setObjectName("lbubicacion_archivo_desc")
        self.tbubicacion_key_desc = QtWidgets.QLineEdit(self.tabdesencriptado)
        self.tbubicacion_key_desc.setGeometry(QtCore.QRect(120, 80, 661, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.tbubicacion_key_desc.setFont(font)
        self.tbubicacion_key_desc.setReadOnly(True)
        self.tbubicacion_key_desc.setObjectName("tbubicacion_key_desc")
        self.btubicacion_llave_desc = QtWidgets.QPushButton(self.tabdesencriptado)
        self.btubicacion_llave_desc.setGeometry(QtCore.QRect(790, 80, 51, 31))
        self.btubicacion_llave_desc.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btubicacion_llave_desc.setText("")
        self.btubicacion_llave_desc.setIcon(icon1)
        self.btubicacion_llave_desc.setIconSize(QtCore.QSize(24, 24))
        self.btubicacion_llave_desc.setAutoDefault(False)
        self.btubicacion_llave_desc.setDefault(False)
        self.btubicacion_llave_desc.setFlat(False)
        self.btubicacion_llave_desc.setObjectName("btubicacion_llave_desc")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("files/Desencriptado.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabcontrol.addTab(self.tabdesencriptado, icon5, "")
        self.tabinformacion = QtWidgets.QWidget()
        self.tabinformacion.setObjectName("tabinformacion")
        self.minformacion = QtWidgets.QTextEdit(self.tabinformacion)
        self.minformacion.setGeometry(QtCore.QRect(10, 0, 861, 571))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.minformacion.setFont(font)
        self.minformacion.setAcceptDrops(False)
        self.minformacion.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.minformacion.setFrameShadow(QtWidgets.QFrame.Plain)
        self.minformacion.setLineWidth(0)
        self.minformacion.setReadOnly(True)
        self.minformacion.setObjectName("minformacion")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("files/generales.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabcontrol.addTab(self.tabinformacion, icon6, "")
        frmCryptoRSA.setCentralWidget(self.mainWidget)

        self.retranslateUi(frmCryptoRSA)
        self.tabcontrol.setCurrentIndex(2)

        """
            CONFIGURACIÓN DE EVENTOS
        """
        # Botón para seleccionar la ubicación donde se exportara la llave para desencriptar
        self.btubicacion_exporta_llave.clicked.connect(self.selectExportKey)

        # Botón para seleccionar el archivo que se desea encriptar
        self.btubicacion_archivo_enc.clicked.connect(self.selectEncFile)

        # Botón para iniciar encriptación
        self.btencriptar_archivo.clicked.connect(self.EncriptFile)

        self.btubicacion_archivo_desc.clicked.connect(self.btubicacion_archivo_desc.click)
        self.btubicacion_llave_desc.clicked.connect(self.btubicacion_llave_desc.click)
        self.btdesencriptar_archivo.clicked.connect(self.btdesencriptar_archivo.click)
        QtCore.QMetaObject.connectSlotsByName(frmCryptoRSA)

    def retranslateUi(self, frmCryptoRSA):
        _translate = QtCore.QCoreApplication.translate
        frmCryptoRSA.setWindowTitle(_translate("frmCryptoRSA", "CryptoRSA"))
        self.tbubicacion_exporta_key.setToolTip(_translate("frmCryptoRSA", "<html><head/><body><p><span style=\" font-size:10pt;\">Ubicación donde se almacenará la llave para desencriptar el mensaje. </span></p></body></html>"))
        self.lbdestino_llave.setText(_translate("frmCryptoRSA", "Exportar"))
        self.lbarchivo_encriptar.setText(_translate("frmCryptoRSA", "Archivo"))
        self.lbubicacion_archivo_enc.setToolTip(_translate("frmCryptoRSA", "<html><head/><body><p><span style=\" font-size:10pt;\">Ubicación del </span><span style=\" font-size:10pt; font-weight:600;\">archivo</span><span style=\" font-size:10pt;\"> de texto (</span><span style=\" font-size:10pt; font-weight:600;\">.txt</span><span style=\" font-size:10pt;\">) a encriptar. </span></p></body></html>"))
        self.lbencriptado_archivo.setText(_translate("frmCryptoRSA", "Encriptado de Archivo"))
        self.lbmensaje_enc.setText(_translate("frmCryptoRSA", "Mensaje a Encriptar"))
        self.btencriptar_archivo.setText(_translate("frmCryptoRSA", "Encriptar"))
        self.tabcontrol.setTabText(self.tabcontrol.indexOf(self.tabencriptado), _translate("frmCryptoRSA", "Encriptado"))
        self.lbdesencriptado_archivo.setText(_translate("frmCryptoRSA", "Desencriptado de Archivo"))
        self.lbdestino_llave_2.setText(_translate("frmCryptoRSA", "Llave"))
        self.lbmensaje_enc_2.setText(_translate("frmCryptoRSA", "Mensaje a Encriptar"))
        self.btdesencriptar_archivo.setText(_translate("frmCryptoRSA", "Desencriptar"))
        self.lbarchivo_encriptar_2.setText(_translate("frmCryptoRSA", "Archivo"))
        self.lbubicacion_archivo_desc.setToolTip(_translate("frmCryptoRSA", "<html><head/><body><p><span style=\" font-size:10pt;\">Ubicación del </span><span style=\" font-size:10pt; font-weight:600;\">archivo</span><span style=\" font-size:10pt;\"> (</span><span style=\" font-size:10pt; font-weight:600;\">.txt</span><span style=\" font-size:10pt;\">) a desencriptar. </span></p></body></html>"))
        self.tbubicacion_key_desc.setToolTip(_translate("frmCryptoRSA", "<html><head/><body><p><span style=\" font-size:10pt;\">Ubicación de la </span><span style=\" font-size:10pt; font-weight:600;\">llave para desencriptar el mensaje</span><span style=\" font-size:10pt;\">. </span></p></body></html>"))
        self.tabcontrol.setTabText(self.tabcontrol.indexOf(self.tabdesencriptado), _translate("frmCryptoRSA", "Desencriptado"))
        self.minformacion.setHtml(_translate("frmCryptoRSA", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:600;\">CrytpoRSA</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Universidad del Valle de Guatemala</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">MM2015 - Matemática Discreta 1</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Pablo Sao</span><span style=\" font-size:10pt;\"> (11530) y </span><span style=\" font-size:10pt; font-weight:600;\">Mirka Monzón</span><span style=\" font-size:10pt;\"> (18139)</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">25 de noviembre de 2020</span></p>\n"
"<hr />\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\',\'sans-serif\'; font-size:12pt;\">El proyecto consiste en escribir un programa capaz de encriptar y desencriptar un mensaje, utilizando el sistema criptográfico RSA. En la cual el criptosistema RSA es un ejemplo de los métodos de encriptación que utilizan una clave (o llave) pública. Este criptosistema fue desarrollado en la década de los 70\'s (y patentado en 1983) por Ronald Rivest, Adi Shamir y Leonard Adleman. Donde tomaron la primera letra del apellido de cada uno de los tres, para obtener el adjetivo RSA (Grimaldi y Ramana, 2004).</span> </p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Referencias</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Grimaldi, R. y Ramana, B. (2004). </span><span style=\" font-size:10pt; font-style:italic;\">Discrete and Combinatorial Mathematics: An Applied Introduction</span><span style=\" font-size:10pt;\">. Fifth Edition. Uttar Pradesh, India: Pearson. 793 - 797 pp.</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>"))
        self.tabcontrol.setTabText(self.tabcontrol.indexOf(self.tabinformacion), _translate("frmCryptoRSA", "Información"))

    def isNotBlank(self,myString):
        return bool(myString and myString.strip())

    def selectExportKey(self):
        #Limpiamos los campos
        self.clearFields()

        fname = QtWidgets.QFileDialog.getExistingDirectory()
        self.tbubicacion_exporta_key.setText(fname)

    def selectEncFile(self):

        try:
            # Solicitamos el ingreso del archivo
            fname, _ = QtWidgets.QFileDialog.getOpenFileName(None, caption="Select a file...",
                                                             directory='./', filter="Archivos de Texto (*.txt)")
            # Colocamos el path visible para el usuario
            self.lbubicacion_archivo_enc.setText(fname)

            # Creamos una ruta Path
            fname = Path(fname)

            # leemos archivo
            if(fname.exists()):
                # mostramos el texto
                self.temensaje_enc.setText(fname.read_text())
                #habilitamos el cambpo para edición
                self.temensaje_enc.setEnabled(True)
            else:
                self.temensaje_enc.setText("")
                # habilitamos el cambpo para edición
                self.temensaje_enc.setEnabled(False)
        except Exception as e:
            print(e)

    def EncriptFile(self):
        # Obtenemos los datos seleccionados por el usuario
        path_key = self.tbubicacion_exporta_key.text()
        path_file = self.lbubicacion_archivo_enc.text()
        message = self.temensaje_enc.toPlainText()

        #Comprobamos si los datos estan llenos
        if(self.isNotBlank(path_key)):
            print("ruta a exportar")
            
            if(self.isNotBlank(path_file)):
                print("selecciono archivo")

                if(self.isNotBlank(message)):
                    print("contiene mensaje")

                else:
                    print("El archivo que selecciono se encuentra vacio")
            else:
                print("Debe ingresar la ubicación del archivo a desencriptar")
        else:
            print("Debe ingresar la ubicación para guardar la llave para desencriptar")



    def clearFields(self):

        # Sección de encriptado
        self.tbubicacion_exporta_key.setText("")
        self.lbubicacion_archivo_enc.setText("")
        self.temensaje_enc.setText("")
        self.temensaje_enc.setEnabled(False)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    frmCryptoRSA = QtWidgets.QMainWindow()
    ui = Ui_frmCryptoRSA()
    ui.setupUi(frmCryptoRSA)
    frmCryptoRSA.show()
    sys.exit(app.exec_())
