
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtCore import QRegularExpression
from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import QMainWindow, QMessageBox

from Dominio.persona import Persona
from UI.vtnPrincipal import Ui_vtnPrincipal

class PersonaServicio(QMainWindow):
    ''''
    Clase que genera la logica de los objetos persona
    '''
    def __init__(self):
        super(PersonaServicio,self).__init__()
        self.ui = Ui_vtnPrincipal()
        self.ui.setupUi(self)
        self.ui.btnGuardar.clicked.connect(self.guardar)
        self.ui.TxTCedula.setValidator(QIntValidator())
        self.ui.btnLimpiar.clicked.connect(self.limpiar)
    #Validación del correo
        patron = r"^(?!.*\.{2})[a-zA-Z0-9._%+-]+@([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,6}$"
        self.regex_email = QRegularExpression(patron)
        self.email_validator = QRegularExpressionValidator(self.regex_email, self)
        self.ui.TxTEmail.setValidator(self.email_validator)

    def _es_email_valido(self, email):
        return self.regex_email.match(email).hasMatch()

    def guardar(self):
        nombre = self.ui.TxTNombre.text().strip()
        apellido = self.ui.TxTApellido.text().strip()
        cedula = self.ui.TxTCedula.text().strip()
        email = self.ui.TxTEmail.text().strip()
        sexo = self.ui.comboBox.currentText().strip()
        es_email_valido = self.regex_email.match(email).hasMatch()

        #validacion de los datos del formulario
        if nombre == "":
            QMessageBox.warning(self, "Advertencia", "Debe ingresar el nombre")
        elif apellido == "":
            QMessageBox.warning(self, "Advertencia", "Debe ingresar el apellido")
        elif len(cedula) < 10:
            QMessageBox.warning(self, "Advertencia", "Debe ingresar la cedula")
        elif not self._es_email_valido(email):
            QMessageBox.warning(self, "Advertencia", "El formato del correo es inválido.\n"
                                "Asegúrese de no usar puntos seguidos")
        elif sexo == "Seleccionar":
            QMessageBox.warning(self, "Advertencia", "Debe ingresar el sexo")
        else:
            persona =Persona(cedula=cedula,nombre=nombre,apellido=apellido,email=email,sexo=sexo)
            print(persona)
            self.ui.statusbar.showMessage('Se guardo la información', 500)
            #borrar campos del formulario
            self.ui.TxTNombre.setText('')
            self.ui.TxTApellido.setText('')
            self.ui.TxTCedula.setText('')
            self.ui.comboBox.setCurrentText(""'')
            self.ui.TxTEmail.setText('')
            self.ui.comboBox.setCurrentText("")
            self.ui.comboBox.setCurrentIndex(0)
    def limpiar(self):
        nombre = self.ui.TxTNombre.clear()
        apellido = self.ui.TxTApellido.clear()
        cedula = self.ui.TxTCedula.clear()
        correo = self.ui.TxTEmail.clear()
        sexo = self.ui.comboBox.setCurrentIndex(0)