import util

class Frente():
    def get_sprites(self): pass

class FrenteJugador_uno(Frente):
    def get_sprites(self):
        return [util.cargar_imagen('imagenes/PF0.png'),
                util.cargar_imagen('imagenes/PF1.png'),
                util.cargar_imagen('imagenes/PF2.png'),
                util.cargar_imagen('imagenes/PF3.png')]

class FrenteJugador_dos(Frente):
    def get_sprites(self):
        return [util.cargar_imagen('imagenes/PF0.png'),
                util.cargar_imagen('imagenes/PF1.png'),
                util.cargar_imagen('imagenes/PF2.png'),
                util.cargar_imagen('imagenes/PF3.png')]

class Atras():
    def get_sprites(self): pass

class AtrasJugador_uno(Atras):
    def get_sprites(self):
        return [util.cargar_imagen('imagenes/A0.png'),
                util.cargar_imagen('imagenes/A1.png'),
                util.cargar_imagen('imagenes/A2.png'),
                util.cargar_imagen('imagenes/A3.png')]

class AtrasJugador_dos(Atras):
    def get_sprites(self):
        return [util.cargar_imagen('imagenes/PA0.png'),
                util.cargar_imagen('imagenes/PA1.png'),
                util.cargar_imagen('imagenes/PA2.png'),
                util.cargar_imagen('imagenes/PA3.png')]

class Izquierda():
    def get_sprites(self): pass

class IzquierdaJugador_uno(Izquierda):
    def get_sprites(self):
        return [util.cargar_imagen('imagenes/I0.png'),
                util.cargar_imagen('imagenes/I1.png'),
                util.cargar_imagen('imagenes/I2.png'),
                util.cargar_imagen('imagenes/I3.png')]

class IzquierdaJugador_dos(Izquierda):
    def get_sprites(self):
        return [util.cargar_imagen('imagenes/PI0.png'),
                util.cargar_imagen('imagenes/PI1.png'),
                util.cargar_imagen('imagenes/PI2.png'),
                util.cargar_imagen('imagenes/PI3.png')]

class Derecha():
    def get_sprites(self): pass

class DerechaJugador_uno(Derecha):
    def get_sprites(self):
        return [util.cargar_imagen('imagenes/D0.png'),
                util.cargar_imagen('imagenes/D1.png'),
                util.cargar_imagen('imagenes/D2.png'),
                util.cargar_imagen('imagenes/D3.png')]

class DerechaJugador_dos(Derecha):
    def get_sprites(self):
        return [util.cargar_imagen('imagenes/PD0.png'),
                util.cargar_imagen('imagenes/PD1.png'),
                util.cargar_imagen('imagenes/PD2.png'),
                util.cargar_imagen('imagenes/PD3.png')]