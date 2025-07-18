# -*- coding: utf-8 -*-
"""
Created on Wed Mar 12 19:24:40 2017

@author: da_angel
"""
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import platform

# from sklearn.cluster import KMeans


__version__ = "1.1.0"

try:
    _fromUtf8 = str.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.createwidget()

    def createwidget(self):

        settings = QSettings()
        self.clipboard = QApplication.clipboard()

        size = settings.value("MainWindow/Size", QVariant(QSize(590, 490)))
        self.resize(size)
        position = settings.value("MainWindow/Position", QVariant(QPoint(0, 0)))
        self.move(position)

        StyleSheet = """
                QLineEdit { color: darkgreen; }
                QToolBar, QPushButton, QStatusBar{
                background-color: rgb(90,90,90);
                color: white;
                }
                """

        self.setStyleSheet(StyleSheet)

        self.f1 = QFont(settings.value('font', QVariant(QFont('Verdana', 12))))

        f = QFrame()
        mainLayout = QHBoxLayout()

        translateLayout = QVBoxLayout()
        # horizontalSpacer1 = QSpacerItem(100, 100, QSizePolicy.Minimum, QSizePolicy.Expanding)
        # translateLayout.addItem(horizontalSpacer1)
        self.englabel = QLabel('Enter French  Sntence:')
        translateLayout.addWidget(self.englabel)
        self.engSen = QLineEdit('')
        translateLayout.addWidget(self.engSen)
        self.notValidlabel = QLabel('')
        translateLayout.addWidget(self.notValidlabel)
        self.wordForWordLabel = QLabel('Word for word translation')
        translateLayout.addWidget(self.wordForWordLabel)
        self.wordForWord = QLineEdit('')
        self.wordForWord.setEnabled(False)
        translateLayout.addWidget(self.wordForWord)
        self.yorTextlabel = QLabel('Yoruba Text')
        translateLayout.addWidget(self.yorTextlabel)
        self.yorTrans = QLineEdit('')
        self.yorTrans.setEnabled(False)
        translateLayout.addWidget(self.yorTrans)

        buttonLayout = QHBoxLayout()
        buttonLayout.addStretch(1)
        self.transButton = QPushButton('Translate')

        self.transButton.clicked.connect(self.process1)
        self.engSen.returnPressed.connect(self.process1)
        buttonLayout.addWidget(self.transButton)
        self.transButton.setToolTip(u'Translate Sentence to Yoruba text')
        self.transButton.setStatusTip(u'Translate Sentence to Yoruba text')
        self.resetButton = QPushButton('Reset')
        self.resetButton.clicked.connect(self.reset)
        buttonLayout.addWidget(self.resetButton)
        translateLayout.addLayout(buttonLayout)
        horizontalSpacer2 = QSpacerItem(100, 100, QSizePolicy.Minimum, QSizePolicy.Expanding)
        translateLayout.addItem(horizontalSpacer2)

        mainLayout.addLayout(translateLayout)
        # verticalSpacer = QSpacerItem(20, 100, QSizePolicy.Minimum, QSizePolicy.Expanding)
        # mainLayout.addItem(verticalSpacer)
        f.setLayout(mainLayout)

        pallette = QPalette()
        pallette.setColor(QPalette.Foreground, Qt.red)

        self.setCentralWidget(f)
        self.addNewWordAction = self.createAction("&Add", "Ctrl+N", "new", "Add new word (Ctrl+N)", False,
                                                  self.addNewWord)
        self.fileQuitAction = self.createAction("&Quit", "Ctrl+Q", "close", "Close the application (Ctrl+Q)", False,
                                                self.close)
        self.viewDefaultAction = self.createAction('Restore Default View', '', 'default', 'Restore Default workspace',
                                                   False, self.restoreDefaultState)

        # self.helpAction = self.createAction('&Help','','help','Show help',False,self.fg)
        self.helpAboutAction = self.createAction('&About', '', 'info', 'Show information about software', False,
                                                 self.about)
        self.helphelpAction = self.createAction('&Help', '', 'help', 'Show more information about software', False,
                                                 self.help)

        fileMenu = self.menuBar().addMenu('&File')
        self.addActions(fileMenu, (self.addNewWordAction, None, self.fileQuitAction, None))

        helpMenu = self.menuBar().addMenu("&Help")
        self.addActions(helpMenu,(self.helpAboutAction,None,self.helphelpAction))

        self.fileToolbar = self.addToolBar("ToolBar")
        self.fileToolbar.setObjectName('Tool Bar')
        self.addActions(self.fileToolbar,
                        (self.addNewWordAction, self.fileQuitAction, None, self.helpAboutAction, self.helphelpAction))

        separator = QAction(self)
        separator.setSeparator(True)
        self.state = self.saveState()
        status = self.statusBar()

        """if(settings.contains('MainWindow/State')):
            self.restoreState(settings.value("MainWindow/State").toByteArray())
        else:
            self.restoreDefaultState()"""

    def addNewWord(self):
        self.window = QWidget()
        self.addword = AddingWord(self.window)
        # self.hide()
        self.addword.show()

    def restoreDefaultState(self):
        settings = QSettings()
        if (settings.contains('MainWindow/State')):
            settings.remove('MainWindow/State')
            settings.remove('font')
        self.restoreState(self.state)

    def reset(self):
        self.engSen.setText('')
        self.notValidlabel.setText('')
        self.wordForWord.setText('')
        self.yorTrans.setText('')

    def about(self):
        QMessageBox.about(self, u"About French-to-Yoruba Machine Translator",
                          u"""<h2>French-to-Yoruba Machine Translator v {0}</h2>

                          <p>This application translates French sentence to Yoruba text.
                          <p><b>Credit:</b> <br/>
                             <b>E-mail:</b> <br/>
                             <b>Phone: <br><br/>

                          <p>Python {1} - Qt {2} - PyQt {3} on {4}""".format(
                              __version__, platform.python_version(),
                              QT_VERSION_STR, PYQT_VERSION_STR,
                              platform.system()))
    def help(self):
        QMessageBox.about(self, u"About French-to-Yoruba Machine Translator",
                          u"""<h2>French-to-Yoruba Machine Translator v {0}</h2>

                          <p>The following are the part of speech used in this application.
                          <p><b>N:</b>Noun <br/>
                            <b>V:</b>Verb <br/>
                            <b>P:</b>Preposition <br/>
                            <b>Adj:</b>Adjective <br/>
                            <b>Pr:</b>Pronoun <br/>
                            <b>Adv:</b>Adverb <br/>
                            <b>D:</b>Determinant <br/>
                            <b>Ppr:</b>Poccessive pronoun <br/>
                            <b>DAdj:</b><br/>

                          <p>Python {1} - Qt {2} - PyQt {3} on {4}""".format(
                              __version__, platform.python_version(),
                              QT_VERSION_STR, PYQT_VERSION_STR,
                              platform.system()))

    def addActions(self, target, actions):
        for action in actions:
            if action is None:
                target.addSeparator()
            else:
                target.addAction(action)

    def createAction(self, text, shortcut=None, icon=None, tip=None, checkable=False, slot=None, signal="triggered()"):
        action = QAction(text, self)
        if icon is not None:
            action.setIcon(QIcon("icons/%s.png" % icon))
        if shortcut is not None:
            action.setShortcut(shortcut)
        if tip is not None:
            action.setToolTip('<b>' + icon + '</b><br>' + tip)
            action.setStatusTip(tip)
        if slot is not None:
            # self.connect(action, SIGNAL(signal), slot)
            action.triggered.connect(slot)

        if checkable:
            action.setCheckable(True)
        return action

    def process1(self):
        self.engPhrase = str(self.engSen.text())
        if self.engPhrase != '':
            try:
                from translatorCore import TranslatorCore, RuleNotImplemented
                tranObj = TranslatorCore()
                self.yorTrans.setText(tranObj.translate(tranObj.preprocess(self.engPhrase)))
                self.wordForWord.setText(tranObj.transwordForWord(self.engPhrase))
            except ValueError:
                QMessageBox.warning(self, "Wrong Input", 'Enter a Sentence!!!')
            except KeyError as e:
                QMessageBox.warning(self, "Word not Found!!!", e.args[0] + " not found in database")
            except RuleNotImplemented:
                QMessageBox.warning(self, "Rule not Implemented", "Rule not Implemented")

    def closeEvent(self, event):
        settings = QSettings()
        settings.setValue("MainWindow/Size", QVariant(self.size()))
        settings.setValue("MainWindow/Position", QVariant(self.pos()))
        settings.setValue("MainWindow/State", QVariant(self.saveState()))


class AddingWord(QMainWindow):
    def __init__(self, parent=None, word=None):
        super().__init__(parent)
        self.addingGui(word)

    def addingGui(self, word=None):
        self.top = 10
        self.left = 10
        self.width = 400
        self.height = 400
        StyleSheet = """
                        QLineEdit {color:darkgreen;}
                        QToolBar, QPushButton, QStatusBar{
                        background-color: rgb(90,90,90);
                        color: white;
                        }
                        """
        self.setStyleSheet(StyleSheet)
        f = QFrame()
        # f.setFrameShape(QFrame.StyledPanel)
        # g = QFrame()
        # g.setFrameShape(QFrame.StyledPanel)
        # hbox = QHBoxLayout()
        self.wordLabel = QLabel("French word:", f)
        self.wordLabel.setGeometry(QRect(10, 30, 110, 30))
        self.word = QLineEdit(f)
        self.word.setText(word)
        self.word.setGeometry(QRect(115, 30, 210, 30))
        self.meaningLabel = QLabel("Yoruba Meaning:", f)
        self.meaningLabel.setGeometry(QRect(10, 70, 110, 30))
        self.meaning = QLineEdit(f)
        self.meaning.setGeometry(QRect(115, 70, 210, 30))
        self.posLabel = QLabel("Part of Speech:", f)
        self.posLabel.setGeometry(QRect(10, 110, 110, 30))
        self.pos = QComboBox(f)
        pos = ["N", "V", "P", "Adj", "Pr", "Adv", "D", "DAdj", "Ppr"]
        self.pos.addItems(pos)
        self.pos.setGeometry(QRect(115, 110, 100, 30))

        self.line = QFrame(f)
        self.line.setGeometry(QRect(10, 145, 330, 20))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.userNameLabel = QLabel("User Name:", f)
        self.userNameLabel.setGeometry(QRect(10, 170, 110, 30))
        self.userName = QLineEdit(f)
        self.userName.setGeometry(QRect(115, 170, 210, 30))
        self.passwordLabel = QLabel("Password:", f)
        self.passwordLabel.setGeometry(QRect(10, 210, 110, 30))
        self.password = QLineEdit(f)
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setGeometry(QRect(115, 210, 210, 30))

        self.loginButton = QPushButton("Login", f)
        # self.loginButton.setIcon()
        self.loginButton.setGeometry(QRect(115, 250, 100, 30))
        self.loginButton.clicked.connect(self.loginUser)

        self.cancelButton = QPushButton("Cancel", f)
        self.cancelButton.setGeometry(QRect(225, 250, 100, 30))
        self.cancelButton.clicked.connect(self.cancel)
        # splitter1 = QSplitter(Qt.Vertical)
        # splitter1.addWidget(f)
        # splitter1.addWidget(g)
        # splitter1.setSizes([300,200])
        # hbox.addWidget(splitter1)
        # self.setLayout(hbox)
        self.setCentralWidget(f)
        self.setWindowTitle('User Entry Interface')
        self.setGeometry(self.top, self.left, self.width, self.height)
        # self.statusBar().showMessage('Welcome Dear User!!!')
        self.show()

    def loginUser(self):
        self.window = QMainWindow()
        engWord = self.word.text()
        basword = self.meaning.text()
        pos = self.pos.currentText()
        username = self.userName.text()
        password = self.password.text()
        from databaseAccess import DatabaseAccess, NotAnAdmin
        if (engWord != "" and basword != "" and pos != "" and username != "" and password != ""):
            try:
                self.dat = DatabaseAccess()
                self.dat.addNewWord(engWord, basword, pos, username, password)
            except NotAnAdmin:
                QMessageBox.warning(self, "Not an Admin", "Sorry, You are not an Administrator!!!")
            except KeyError:
                QMessageBox.warning(self, "Not an Admin", "Sorry, You are not an Administrator!!!")
        self.hide()

    def cancel(self):
        self.window = QMainWindow()
        self.mainwindow = MainWindow(self.window)
        self.hide()
        # self.mainwindow.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    tranyoreng = MainWindow()
    # tranyoreng = AddingWord()
    tranyoreng.setWindowTitle(u'French-to-Yoruba Machine Translator')
    tranyoreng.resize(500, 350)
    # tranyoreng.setMaximumSize(500, 300)
    tranyoreng.show()
    app.exec_()