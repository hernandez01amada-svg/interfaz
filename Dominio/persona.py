class Persona:
#clase que permite crear objetos de tipo persona
    def __init__(self,cedula:str, nombre:str, apellido:str, sexo:str
              ,email:str=None):
        self._nombre = nombre
        self._apellido = apellido
        self._cedula = cedula
        self._email = email
        self._sexo = sexo
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self,nuevo_nombre):
        self._nombre = nuevo_nombre
    @property
    def apellido(self):
        return self._apellido
    @apellido.setter
    def apellido(self,nuevo_apellido):
        self._apellido = nuevo_apellido
    @property
    def cedula(self):
        return self._cedula
    @cedula.setter
    def cedula(self,nuevo_cedula):
        self._cedula = nuevo_cedula
    @property
    def email(self):
        return self._email
    @email.setter
    def email(self,nuevo_email):
        self._email = nuevo_email
    @property
    def sexo(self):
        return self._sexo
    @sexo.setter
    def sexo(self,nuevo_sexo):
        self._sexo = nuevo_sexo

    def __str__(self):
        return (f"Persona [Nombre:{self._nombre},Apellido:{self._apellido},Cédula:{self._cedula},"
                f"Email:{self._email},Sexo:{self._sexo}]")


#def to_dict(self):
   # return {
      #  "nombre": self.nombre,
       # "apellido": self.apellido,
        #"cedula": self.cedula,
        #"email": self.email,
        #"sexo": self.sexo
    #}