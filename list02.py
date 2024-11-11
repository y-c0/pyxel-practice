import pyxel


pyxel.init(80,64)

pyxel.load("inu.pyxres")


pyxel.cls(1)

pyxel.blt( 5,5, 0, 16,0, 16,16, 0)
pyxel.blt( 5,5, 0, 16,0, 32,16, 0)

pyxel.show()