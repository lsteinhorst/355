import sys
import math as m

try:
    from OpenGL.GLUT import *
    from OpenGL.GL import *
    from OpenGL.GLU import *
    from OpenGL.GL import glOrtho
    from OpenGL.GLU import gluPerspective
    from OpenGL.GL import glRotated
    from OpenGL.GL import glTranslated
    from OpenGL.GL import glLoadIdentity
    from OpenGL.GL import glMatrixMode
    from OpenGL.GL import GL_MODELVIEW
    from OpenGL.GL import GL_PROJECTION
    from OpenGL.GL import glPushMatrix
    from OpenGL.GL import glPopMatrix
    #from OpenGL.GL import glutTimerFunc
except:
    print("ERROR: PyOpenGL not installed properly. ")

DISPLAY_WIDTH = 500.0
DISPLAY_HEIGHT = 500.0
x_coord = 0
y_coord = -3
z_coord  = -20
angle = 0
ortho = False
x_car = 10
y_car = 0
z_car = 15
angle_car = 0

def init():
    glClearColor (0.0, 0.0, 0.0, 0.0)
    glShadeModel (GL_FLAT)
    #initHouse()

def drawHouse ():
    glLineWidth(2.5)
    glColor3f(1.0, 0.0, 0.0)
    #Floor
    glBegin(GL_LINES)
    glVertex3f(-5.0, 0.0, -5.0)
    glVertex3f(5, 0, -5)
    glVertex3f(5, 0, -5)
    glVertex3f(5, 0, 5)
    glVertex3f(5, 0, 5)
    glVertex3f(-5, 0, 5)
    glVertex3f(-5, 0, 5)
    glVertex3f(-5, 0, -5)
    #Ceiling
    glVertex3f(-5, 5, -5)
    glVertex3f(5, 5, -5)
    glVertex3f(5, 5, -5)
    glVertex3f(5, 5, 5)
    glVertex3f(5, 5, 5)
    glVertex3f(-5, 5, 5)
    glVertex3f(-5, 5, 5)
    glVertex3f(-5, 5, -5)
    #Walls
    glVertex3f(-5, 0, -5)
    glVertex3f(-5, 5, -5)
    glVertex3f(5, 0, -5)
    glVertex3f(5, 5, -5)
    glVertex3f(5, 0, 5)
    glVertex3f(5, 5, 5)
    glVertex3f(-5, 0, 5)
    glVertex3f(-5, 5, 5)
    #Door
    glVertex3f(-1, 0, 5)
    glVertex3f(-1, 3, 5)
    glVertex3f(-1, 3, 5)
    glVertex3f(1, 3, 5)
    glVertex3f(1, 3, 5)
    glVertex3f(1, 0, 5)
    #Roof
    glVertex3f(-5, 5, -5)

    glVertex3f(0, 8, -5)
    glVertex3f(0, 8, -5)
    glVertex3f(5, 5, -5)
    glVertex3f(-5, 5, 5)
    glVertex3f(0, 8, 5)
    glVertex3f(0, 8, 5)
    glVertex3f(5, 5, 5)
    glVertex3f(0, 8, 5)
    glVertex3f(0, 8, -5)
    glEnd()

def drawCar():
    glLineWidth(2.5)
    glColor3f(0.0, 1.0, 0.0)
    glBegin(GL_LINES)
    #Front Side
    glVertex3f(-3, 2, 2)
    glVertex3f(-2, 3, 2)
    glVertex3f(-2, 3, 2)
    glVertex3f(2, 3, 2)
    glVertex3f(2, 3, 2)
    glVertex3f(3, 2, 2)
    glVertex3f(3, 2, 2)
    glVertex3f(3, 1, 2)
    glVertex3f(3, 1, 2)
    glVertex3f(-3, 1, 2)
    glVertex3f(-3, 1, 2)
    glVertex3f(-3, 2, 2)
    #Back Side
    glVertex3f(-3, 2, -2)
    glVertex3f(-2, 3, -2)
    glVertex3f(-2, 3, -2)
    glVertex3f(2, 3, -2)
    glVertex3f(2, 3, -2)
    glVertex3f(3, 2, -2)
    glVertex3f(3, 2, -2)
    glVertex3f(3, 1, -2)
    glVertex3f(3, 1, -2)
    glVertex3f(-3, 1, -2)
    glVertex3f(-3, 1, -2)
    glVertex3f(-3, 2, -2)
    #Connectors
    glVertex3f(-3, 2, 2)
    glVertex3f(-3, 2, -2)
    glVertex3f(-2, 3, 2)
    glVertex3f(-2, 3, -2)
    glVertex3f(2, 3, 2)
    glVertex3f(2, 3, -2)
    glVertex3f(3, 2, 2)
    glVertex3f(3, 2, -2)
    glVertex3f(3, 1, 2)
    glVertex3f(3, 1, -2)
    glVertex3f(-3, 1, 2)
    glVertex3f(-3, 1, -2)
    glEnd()

def drawTire():
    glLineWidth(2.5)
    glColor3f(0.0, 0.0, 1.0)
    glBegin(GL_LINES)
    #Front Side
    glVertex3f(-1, .5, .5)
    glVertex3f(-.5, 1, .5)
    glVertex3f(-.5, 1, .5)
    glVertex3f(.5, 1, .5)
    glVertex3f(.5, 1, .5)
    glVertex3f(1, .5, .5)
    glVertex3f(1, .5, .5)
    glVertex3f(1, -.5, .5)
    glVertex3f(1, -.5, .5)
    glVertex3f(.5, -1, .5)
    glVertex3f(.5, -1, .5)
    glVertex3f(-.5, -1, .5)
    glVertex3f(-.5, -1, .5)
    glVertex3f(-1, -.5, .5)
    glVertex3f(-1, -.5, .5)
    glVertex3f(-1, .5, .5)
    #Back Side
    glVertex3f(-1, .5, -.5)
    glVertex3f(-.5, 1, -.5)
    glVertex3f(-.5, 1, -.5)
    glVertex3f(.5, 1, -.5)
    glVertex3f(.5, 1, -.5)
    glVertex3f(1, .5, -.5)
    glVertex3f(1, .5, -.5)
    glVertex3f(1, -.5, -.5)
    glVertex3f(1, -.5, -.5)
    glVertex3f(.5, -1, -.5)
    glVertex3f(.5, -1, -.5)
    glVertex3f(-.5, -1, -.5)
    glVertex3f(-.5, -1, -.5)
    glVertex3f(-1, -.5, -.5)
    glVertex3f(-1, -.5, -.5)
    glVertex3f(-1, .5, -.5)
    #Connectors
    glVertex3f(-1, .5, .5)
    glVertex3f(-1, .5, -.5)
    glVertex3f(-.5, 1, .5)
    glVertex3f(-.5, 1, -.5)
    glVertex3f(.5, 1, .5)
    glVertex3f(.5, 1, -.5)
    glVertex3f(1, .5, .5)
    glVertex3f(1, .5, -.5)
    glVertex3f(1, -.5, .5)
    glVertex3f(1, -.5, -.5)
    glVertex3f(.5, -1, .5)
    glVertex3f(.5, -1, -.5)
    glVertex3f(-.5, -1, .5)
    glVertex3f(-.5, -1, -.5)
    glVertex3f(-1, -.5, .5)
    glVertex3f(-1, -.5, -.5)
    glEnd()

def initHouse():
    print("in init")
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45,1,.5,50)
    glMatrixMode(GL_MODELVIEW)
    glTranslated(0,-3,-20)
    # x = 0
    # y = -3
    # z = -20
    # angle = 0
    # ortho = False

def tire():
    translate(1,0,1)
    drawTire()
    glPopMatrix()
    glPushMatrix()



def display():
    global x_coord
    global y_coord
    global z_coord
    global angle
    global ortho
    global x_car
    global y_car
    global z_car
    global angle_car


    glClear (GL_COLOR_BUFFER_BIT)
    glColor3f (1.0, 1.0, 1.0)
    # viewing transformation


    #Your Code Here
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glRotated(angle % 360, 0, 1, 0)
    glTranslated(x_coord ,y_coord ,z_coord )

    # drawHouse()
    #
    # glTranslated(15, 0, 0)
    #
    # drawHouse()
    #
    # glTranslated(15, 0, 0)
    #
    # drawHouse()
    #
    # glRotated(180, 0, 1, 0)
    # glTranslated(0,0,-30)
    #
    # drawHouse()
    #
    # glTranslated(15,0,0)
    #
    # drawHouse()
    #
    # glTranslated(15,0,0)
    #
    # drawHouse()


    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    if ortho:
        glOrtho(-20, 20, -20, 20, 0, 10000)
    else:
        gluPerspective(60, 1, 2, 200)


    glMatrixMode(GL_MODELVIEW)
    drawHouse()

    glTranslated(15, 0, 0)

    drawHouse()

    glTranslated(15, 0, 0)

    drawHouse()

    glRotated(180, 0, 1, 0)
    glTranslated(0,0,-30)

    drawHouse()

    glTranslated(15,0,0)

    drawHouse()

    glTranslated(15,0,0)

    drawHouse()


    glTranslated(x_car,y_car,z_car)
    drawCar()
    glPushMatrix()

    #glRotated(angle_car,0,0,1)
    glTranslate(1,0,1)
    glRotated(angle_car,0,0,1)
    drawTire()
    glPopMatrix()
    glPushMatrix()

    #glRotated(angle_car,0,0,1)
    glTranslate(1,0,-1)
    glRotated(angle_car,0,0,1)
    drawTire()
    glPopMatrix()
    glPushMatrix()

    #glRotated(angle_car,0,0,1)
    glTranslate(-1,0,-1)
    glRotated(angle_car,0,0,1)
    drawTire()
    glPopMatrix()
    glPushMatrix()

    #glRotated(angle_car,0,0,1)
    glTranslate(-1,0,1)
    glRotated(angle_car,0,0,1)
    drawTire()
    glPopMatrix()




    #drawCar()



    glFlush()

def timer(x):
    global x_coord
    global y_coord
    global z_coord
    global angle
    global ortho
    global x_car
    global y_car
    global z_car
    global angle_car

    x_car -= 1
    angle_car += 30
    glutPostRedisplay()
    glutTimerFunc(250,timer,0)




def keyboard(key, x, y):
    #look into how to do global varibles
    global x_coord
    global y_coord
    global z_coord
    global angle
    global ortho
    global x_car
    global y_car
    global z_car
    global angle_car


    if key == chr(27):
        import sys
        sys.exit(0)

    if key == b'w':
        print("W is pressed")

    if key == b'a':
        #glTranslated(-1,0,0)
        ang = (angle % 360)
        ang = ang*m.pi / 180

        x_coord += m.cos(ang)
        z_coord  += m.sin(ang)

    if key == b'd':
        #glTranslated(1,0,0)
        ang = (angle % 360)
        ang = ang*m.pi / 180

        x_coord  -= m.cos(ang)
        z_coord  -= m.sin(ang)

    if key == b'w':
        #glTranslated(0,0,1)
        ang = (angle % 360)
        ang = ang*m.pi / 180

        x_coord  -= m.sin(ang)
        z_coord  += m.cos(ang)
        #z_coord +=1

    if key == b's':
        #glTranslated(0,0,-1)
        ang = (angle % 360)
        ang = ang*m.pi / 180

        x_coord  += m.sin(ang)
        z_coord  -= m.cos(ang)
        #z_coord -= 1

    if key == b'q':
        #glRotated(1,0,-1,0)
        angle -= 2

    if key == b'e':
        #glRotated(1,0,1,0)
        angle += 2

    if key == b'r':
        #glTranslated(0,1,0)
        y_coord  -= 1

    if key == b'f':
        #glTranslated(0,-1,0)
        y_coord  += 1

    if key == b'h':
        #drawHouse()
        x_coord  = 0
        y_coord  = -3
        z_coord  = -20
        angle = 0
        x_car = 10
        y_car = 0
        z_car = 10
        angle_car = 0

    if key == b'o':
        #glOrtho(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0)  flips the house around
        #glOrtho(0.0, 500, 500, 0.0, 0, 1)
        ortho = True

    if key == b'p':
        #print("p")
        ortho = False

    glutPostRedisplay()


glutInit(sys.argv)
glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize (int(DISPLAY_WIDTH), int(DISPLAY_HEIGHT))
glutInitWindowPosition (100, 100)
glutCreateWindow (b'OpenGL Lab')
init ()
glutDisplayFunc(display)
glutKeyboardFunc(keyboard)
glutTimerFunc(250,timer,0)
glutMainLoop()
