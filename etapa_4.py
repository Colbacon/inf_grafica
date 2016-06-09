from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np
import math

W_WIDTH = 800; W_HEIGHT = 800

#Tipos de vista
FIRST_PERSON_VIEW = 0
UP_VIEW = 1
THIRD_PERSON_VIEW = 2
actual_view = 0
#camera
cameraPos = np.array([0.0, 1.0, 3.0])
cameraFront = np.array([0.0, 0.0, -1.0])
cameraUp = np.array([0.0, 1.0, 0.0])
cameraSpeed = 0.1
cameraAngle = 0.0
angleLook =0.01
#Perspective parametres
nearVl = 0.1; farVl = 100.0
#Ortho parametres
edge = 100

keys = np.zeros(1024, dtype=bool)

angle = 0.0

def moveCamera():
	global cameraPos, cameraFrontm, cameraSpeed
	global cameraAngle, angleLook, actual_view
	#Movement calculation
	if keys[GLUT_KEY_UP]:
		cameraPos += cameraFront * cameraSpeed
	if keys[GLUT_KEY_DOWN]:
		cameraPos -= cameraFront * cameraSpeed
	if keys[GLUT_KEY_LEFT]:
		cameraAngle -= angleLook
		cameraFront[0] = math.sin(cameraAngle)
		cameraFront[2] = -math.cos(cameraAngle)
	if keys[GLUT_KEY_RIGHT]:
		cameraAngle += angleLook
		cameraFront[0] = math.sin(cameraAngle)
		cameraFront[2] = -math.cos(cameraAngle)

	if keys[GLUT_KEY_F1]:
		actual_view = FIRST_PERSON_VIEW
		Reshape(glutGet(GLUT_WINDOW_WIDTH), glutGet(GLUT_WINDOW_HEIGHT))
	if keys[GLUT_KEY_F2]:
		actual_view = UP_VIEW
		Reshape(glutGet(GLUT_WINDOW_WIDTH), glutGet(GLUT_WINDOW_HEIGHT))
	#Update camera position
	if actual_view == FIRST_PERSON_VIEW:
		cameraDir = cameraPos + cameraFront
		gluLookAt(	cameraPos[0], cameraPos[1], cameraPos[2],
					cameraDir[0], cameraDir[1], cameraDir[2],
					cameraUp [0], cameraUp [1], cameraUp [2])

	if actual_view ==  UP_VIEW: 
		gluLookAt(	0.0, 40.0, 0.0,
					0.0, 0.0, 0.0,
					1.0, 0.0, 0.0)

def drawAltar():
	#Draw base
	glColor3f (1.0, 1.0, 1.0)
	glutSolidCube(2)
	#Draw prisma
	glColor3f (0.0, 1.0, 0.0)
	glTranslatef(0.0, 2.0, 0.0)
	glRotatef(45.0, 1.0, 0.0, 1.0)
	glRotatef(angle,1.0,1.0,0.0)
	glutWireCube(1)

def Display ():
	glMatrixMode(GL_MODELVIEW)
	#Borramos la escena
	glClear (GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glLoadIdentity();
	#Move the camera
	moveCamera()

	#####Render objects
	#Draw de surface
	glPushMatrix()
	glColor3f (1.0, 1.0, 0.0)
	glBegin(GL_QUADS)
	glVertex3f(-10.0, 0, -10.0)
	glVertex3f(-10.0, 0, 10.0)
	glVertex3f(10.0, 0, 10.0)
	glVertex3f(10.0, 0, -10.0)
	glEnd()
	glPopMatrix()
	#Draw cube
	
	for i in range(2):
		for j in range(2):
			glPushMatrix()
			glTranslatef(-5+(10.0*i), 0.0, -5+(10.0*j))
			drawAltar()
			glPopMatrix()	
	
	#Dibuja taza
	glPushMatrix()
	glColor3f (1.0, 1.0, 1.0)
	#glTranslatef(0.0,0.0,-2.0)
	glRotatef(angle,0.0,1.0,0.0)
	glutSolidTeapot(1)
	glPopMatrix()

	#Dibuja Cubo
	glPushMatrix()
	glColor3f (0.0, 1.0, 0.0)
	glTranslatef(0.0,0.0,-5.0)
	glRotatef(angle,0.0,1.0,0.0)
	#gl.glRotatef(angle,0.0,1.0,0.0)
	glTranslatef(3.0,0.0,0.0)
	glutSolidCube(1)
	glPopMatrix()
	
	glFlush()
	glutSwapBuffers()


# Funcion que se ejecuta cuando el sistema no esta ocupado
def Idle ():
	global angle
	angle += 0.3

	glutPostRedisplay()

def Keyboard (key, mouse_x, mouse_y):
	keys[key] = True;
def SpecKeyboard (key, mouse_x, mouse_y):
	keys[key] = True;
def KeyboardUP (key, mouse_x, mouse_y):
	keys[key] = False;  
def SpecKeyboardUP (key, mouse_x, mouse_y):
	keys[key] = False;  

# Se ejucata cuando se modifica el tamao de la ventana
def Reshape (width, height):
    if height == 0:
    	height = 1

	ratio = width / height

	glMatrixMode(GL_PROJECTION)
	glLoadIdentity();
	glViewport(0,0,width,height)

	if actual_view == FIRST_PERSON_VIEW:
		gluPerspective (45.0, W_WIDTH/W_HEIGHT, nearVl, farVl)

	if actual_view == UP_VIEW:
		if ratio >= 1:
			glOrtho (-edge*ratio, edge*ratio, edge, edge, nearVl, farVl)
		else:
			glOrtho (-edge, edge, edge/ratio, edge/ratio, nearVl, farVl)
	glMatrixMode(GL_MODELVIEW)

def main ():

	glutInit()
	# Indicamos como ha de ser la nueva ventana
	glutInitWindowPosition (100,100)
	glutInitWindowSize (W_WIDTH, W_HEIGHT)
	glutInitDisplayMode (GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
	glutCreateWindow ("Etapa 4")

	#Habilitado el test de profundiad
	glEnable(GL_DEPTH_TEST)

	# Indicamos las funcciones de callback
	glutDisplayFunc(Display)
	glutIdleFunc(Idle)
	glutReshapeFunc(Reshape)
	#KeyBoard, key pressed
	glutKeyboardFunc(Keyboard)
	glutSpecialFunc(SpecKeyboard)
	#KeyBoar, key released
	glutKeyboardUpFunc(KeyboardUP)
	glutSpecialUpFunc(SpecKeyboardUP)

	#El color de fondo sera el negro (RGBA, RGB + Alpha channel)
	glClearColor (0.5, 0.5, 0.5, 1.0)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	#glOrtho (-15.0,15.0, -15.0,15.0, -15.0, 15.0)
	gluPerspective (45.0, W_WIDTH/W_HEIGHT, nearVl, farVl)
	glMatrixMode(GL_MODELVIEW)

	#Comienza la ejecucion del core de GLUT
	#print GLUT_KEY_DOWN
	glutMainLoop()

if __name__ == "__main__":
	main()