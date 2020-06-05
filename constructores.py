from fabricas import FabricaSpritesJugador_uno, FabricaSpritesJugador_dos
from jugador import Jugador


class Director():
    __builder = None

    def setBuilder(self, builder):
        self.__builder = builder
    
    def getJugador(self):
        jugador = Jugador()
        jugador.set_sprites(self.__builder.get_sprites())
        
        return jugador

class Constructor():
    def get_sprites(self): pass

class ConstructorJugador_uno(Constructor):
    def __init__(self):
        self.fabrica = FabricaSpritesJugador_uno()


    def get_sprites(self):
        return [self.fabrica.crear_vistafre(),
                self.fabrica.crear_vistaatras(),
                self.fabrica.crear_vistaiz(),
                self.fabrica.crear_vistade()] 

class ConstructorJugador_dos(Constructor):
    def __init__(self):
        self.fabrica = FabricaSpritesJugador_dos()


    def get_sprites(self):
        return [self.fabrica.crear_vistafre(),
                self.fabrica.crear_vistaatras(),
                self.fabrica.crear_vistaiz(),
                self.fabrica.crear_vistade()] 