from productos import *

class FabricaAbstracta():
    def crear_vistafre(self): pass
    def crear_vistaatras(self): pass
    def crear_vistaiz(self): pass
    def crear_vistade(self): pass
    

class FabricaSpritesJugador_uno(FabricaAbstracta):
   
    def crear_vistafre(self): 
        frente = FrenteJugador_uno()
        return frente.get_sprites()

    def crear_vistaatras(self): 
        atras = AtrasJugador_uno()
        return atras.get_sprites()

    def crear_vistaiz(self): 
        izquierda = IzquierdaJugador_uno()
        return izquierda.get_sprites()

    def crear_vistade(self): 
        derecha = DerechaJugador_uno()
        return derecha.get_sprites()

class FabricaSpritesJugador_dos(FabricaAbstracta):
   
    def crear_vistafre(self): 
        frente = FrenteJugador_dos()
        return frente.get_sprites()

    def crear_vistaatras(self): 
        atras = AtrasJugador_dos()
        return atras.get_sprites()

    def crear_vistaiz(self): 
        izquierda = IzquierdaJugador_dos()
        return izquierda.get_sprites()

    def crear_vistade(self): 
        derecha = DerechaJugador_dos()
        return derecha.get_sprites()