import pyxel


pyxel.init(80,64)

pyxel.load("inu.pyxres")

x=0
y=0
status = 0

def update():
    global x,y,status
    x = pyxel.mouse_x
    y = pyxel.mouse_y

    if x == 1 and y == 1:
        status = 0
    else:
        status = 1
    return

def draw():
    pyxel.cls(1)
    pyxel.blt( 1,1, 0, 16,0, 16,16, 0)
    pyxel.blt( x,y, 0, 16,0, 16,16, 0)

    if status == 1:
        pyxel.text(30,30,"... ",7)
    else :
        #重ねるとテキストが出る
        pyxel.text(30,30,"hello!",7)
    return


pyxel.run(update,draw)