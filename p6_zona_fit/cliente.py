class Cliente:
    def __init__(self, id=None, nombre=None, apellido=None, membresia=None):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.membresia = membresia
        #Se coloca None porque no siempre se va a necesitar modificar todos los parámetros

    def __str__(self):
        return (f'Id: {self.id}, Nombre: {self.nombre}, '
                f'Apellido: {self.apellido}, Membresia: {self.membresia}')
