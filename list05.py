import pyxel


pyxel.init(128,128, title="inu")

pyxel.load("inu.pyxres")

x=0
y=pyxel.height - 16 * 2
dx = 0
dy = 0
pldir = 1
jump = 0
score = 0

chkpoint = [(1,0),(8,0),(14,0), (1,8),(14,8), (1,15),(8,15),(14,15)]
fruits = [(6,2,1000,"meat"),(8,2,300,"cherry"),(10,2,500,"banana"),(12,2,1000,"heart"),(14,2,100,"orange")]

playerImg = { "stay":[(2,0),(2,0),(2,0),(2,0),(4,0),(4,0),(4,0),(4,0)],"walk":[(2,0),(6,0),(2,0),(8,0)],"jump":[(10,0)]}

def chkwall(cx, cy):
    c = 0
    if cx < 0 or pyxel.width- 1 - 16 < cx:
        c = c + 1

    if pyxel.height- 1 - 16  < cy:
         c = c + 1

    for cpx, cpy in chkpoint:
        xi = (cx + cpx) // 8
        yi = (cy + cpy) // 8
        if (0,2) == pyxel.tilemap(0).pget(xi,yi) or (2,2) == pyxel.tilemap(0).pget(xi,yi):
            c = c + 1
        elif (0,2) == pyxel.tilemap(0).pget(xi+16,yi+16) or (2,2) == pyxel.tilemap(0).pget(xi+16,yi+16):
            c = c + 1
    
    return c



def update():
    global x,y,dx,dy,pldir,jump,score

    # 操作判定
    if pyxel.btn(pyxel.KEY_LEFT):
        if -3 < dx:
            dx = dx - 1
        pldir = -1
    elif pyxel.btn(pyxel.KEY_RIGHT):
        if dx < 3:
            dx = dx + 1
        pldir = 1
    else:
        dx = int(dx * 0.7)

    # 横移動
    lr = pyxel.sgn(dx)
    loop = abs(dx)
    while 0 < loop:
        if chkwall(x + lr,y) != 0:
            dx = 0
            break
        x = x + lr
        loop = loop - 1

    # ジャンプと落下
    if jump == 0:
        if chkwall(x, y+1) == 0:
            jump = 2 #床がなければ落下
        if pyxel.btnp(pyxel.KEY_SPACE):
            dy = 10
            jump = 1 #上昇開始
    else:
        dy = dy - 1
        if dy < 0:
            jump = 2 #落下開始
    
    ud = pyxel.sgn(dy)
    loop = abs(dy)
    while 0 < loop:
        if chkwall(x,y - ud) != 0:
            dy = 0
            if jump == 1:
                jump = 2
            elif jump == 2:
                jump = 0
            break
        y = y - ud
        loop = loop - 1
    
    # 取得判定
    xi = (x + 4) // 8
    yi = (y + 4) // 8 

    for fruit in fruits:
        if (fruit[0], fruit[1]) == pyxel.tilemap(0).pget(xi,yi) or (15,3) == pyxel.tilemap(0).pget(xi,yi):
            score = score + fruit[2]
            # TODO: ゴリ押し
            pyxel.tilemap(0).pset(xi, yi, (0,0))
            pyxel.tilemap(0).pset(xi+1, yi, (0,0))
            pyxel.tilemap(0).pset(xi, yi+1, (0,0))
            pyxel.tilemap(0).pset(xi+1, yi+1, (0,0))
        # if (14,3) == pyxel.tilemap(0).pget(xi,yi) or (15,3) == pyxel.tilemap(0).pget(xi,yi):



    return

def chkPlayerStatus():
    if jump != 0:
        return "jump"
    elif dx != 0:
        return "walk"
    return "stay"

def getPlayerImg(status):
    koma = pyxel.frame_count // 8 % len(playerImg[status]) # 8F単位で切替
    return playerImg[status][koma]

def draw():
    pyxel.cls(0)
    pyxel.bltm( 0,0, 0, 0,0, pyxel.width,pyxel.height, 0)
    player = getPlayerImg(chkPlayerStatus())
    pyxel.blt( x,y, 0, player[0]*8,player[1]*8, pldir * 16,16 , 0)

    # pyxel.text(5,5, "x=" + str(x) + " y="+str(y), 7)
    pyxel.text(5,12, "score:" + str(score), 7)
    # pyxel.text(5,19, "status:" + str(chkPlayerStatus()), 7)


    return


pyxel.run(update,draw)