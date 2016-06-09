import OpenGL.GL as gl
import OpenGL.GLUT as glut

W_WIDTH = 800
W_HEIGHT = 800

angle = 0.0
#xRotated = 33
#yRotated = 40

def Display ():
	global angle

	gl.glMatrixMode(gl.GL_MODELVIEW)
	#Borramos la escena
	gl.glClear (gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)

	#Dibuja taza
	gl.glPushMatrix()
	gl.glColor3f (1.0, 1.0, 1.0)
	gl.glTranslatef(0.0,0.0,-1.0)
	gl.glRotatef(angle,0.0,1.0,0.0)
	glut.glutSolidTeapot(0.3)
	gl.glPopMatrix()

	#Dibuja Cubo
	gl.glPushMatrix()
	gl.glColor3f (0.0, 1.0, 0.0)
	gl.glTranslatef(0.0,0.0,-4.0)
	gl.glRotatef(angle,0.0,1.0,0.0)
	#gl.glRotatef(angle,0.0,1.0,0.0)
	gl.glTranslatef(1.0,0.0,0.0)
	glut.glutSolidCube(0.1)
	gl.glPopMatrix()

	glut.glutSwapBuffers()
	gl.glFlush()


# Funcion que se ejecuta cuando el sistema no esta ocupado
def Idle ():
	global angle

	angle += 0.3

	glut.glutPostRedisplay()
# Se ejucata cuando se modifica el tamao de la ventana
def Reshape (width, height):
    if height == 0:
    	height = 1

	ratio = width / height

	gl.glMatrixMode(gl.GL_PROJECTION)
	gl.glLoadIdentity();
	gl.glViewport(0,0,width,height)
	if ratio >= 1:
		gl.glFrustum (-1.0*ratio,1.0*ratio, -1.0, 1.0, 1.0, 10.0)
	else:
		gl.glFrustum (-1.0,1.0, -1.0/ratio,1.0/ratio, 1.0, 10.0)
	gl.glMatrixMode(gl.GL_MODELVIEW)



glut.glutInit()
# Indicamos como ha de ser la nueva ventana
glut.glutInitWindowPosition (100,100)
glut.glutInitWindowSize (W_WIDTH, W_HEIGHT)
glut.glutInitDisplayMode (glut.GLUT_RGBA | glut.GLUT_DOUBLE)
#Habilitado el test de profundiad
gl.glEnable(gl.GL_DEPTH_TEST)

glut.glutCreateWindow ("Etapa 3")

# Indicamos cuales son las funciones de redibujado e idle
glut.glutDisplayFunc(Display)
glut.glutIdleFunc(Idle)
glut.glutReshapeFunc(Reshape)
glut.glutKeyboardFunc(Keyboard)

#El color de fondo sera el negro (RGBA, RGB + Alpha channel)
gl.glClearColor (0.5, 0.5, 0.5, 1.0)
gl.glMatrixMode(gl.GL_PROJECTION)
gl.glLoadIdentity()
gl.glFrustum (-1.0, 1.0, -1.0, 1.0, 1, 5)
gl.glMatrixMode(gl.GL_MODELVIEW)


#Comienza la ejecucion del core de GLUT
glut.glutMainLoop()
