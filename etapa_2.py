import OpenGL.GL as gl
import OpenGL.GLUT as glut

W_WIDTH = 500
W_HEIGHT = 500

fAngulo = 0.0

def Display ():
	global fAngulo
	#Borramos la escena
	gl.glClear (gl.GL_COLOR_BUFFER_BIT)
	gl.glPushMatrix()
	# Rotamos las proximas primitivas
	gl.glRotatef (fAngulo, 0.0, 0.0, 1.0)
	# Creamos a continuacion dibujamos los tres poligonos
	gl.glBegin (gl.GL_POLYGON)
	gl.glColor3f (1.0, 1.0, 1.0)
	gl.glVertex3f(0.0, 0.0, 0.0)
	gl.glColor3f (0.0, 1.0, 0.0)
	gl.glVertex3f(1.0, 0.0, 0.0)
	gl.glColor3f (0.0, 1.0, 0.0)
	gl.glVertex3f(-0.5, 0.866, 0.0)
	gl.glEnd()

	gl.glBegin (gl.GL_POLYGON)
	gl.glColor3f (1.0, 1.0, 1.0)
	gl.glVertex3f(0.0, 0.0, 0.0)
	gl.glColor3f (1.0, 0.0, 0.0)
	gl.glVertex3f(1.0, 0.0, 0.0)
	gl.glColor3f (0.0, 0.0, 1.0)
	gl.glVertex3f(-0.5, -0.866, 0.0)
	gl.glEnd()

	gl.glBegin (gl.GL_POLYGON)
	gl.glColor3f (1.0, 1.0, 1.0)
	gl.glVertex3f(0.0, 0.0, 0.0)
	gl.glColor3f (0.0, 1.0, 1.0)
	gl.glVertex3f(-0.5, 0.866, 0.0)
	gl.glColor3f (0.0, 0.0, 1.0)
	gl.glVertex3f(-0.5, -0.866, 0.0)
	gl.glEnd()
	
	gl.glPopMatrix()

	glut.glutSwapBuffers()
	gl.glFlush()


# Funcion que se ejecuta cuando el sistema no esta ocupado
def Idle ():
	global fAngulo
	# Incrementamos el angulo
	fAngulo += 0.3
	# Si es mayor que dos pi la decrementamos
	if fAngulo > 360:
		fAngulo -= 360
	# Indicamos que es necesario repintar la pantalla
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
		gl.glOrtho (-2.0*ratio,2.0*ratio, -2.0,2.0, -1.0, 1.0)
	else:
		gl.glOrtho (-2.0,2.0, -2.0/ratio,2.0/ratio, -1.0, 1.0)
	gl.glMatrixMode(gl.GL_MODELVIEW)



glut.glutInit()
# Indicamos como ha de ser la nueva ventana
glut.glutInitWindowPosition (100,100)
glut.glutInitWindowSize (W_WIDTH, W_HEIGHT)
glut.glutInitDisplayMode (glut.GLUT_RGBA | glut.GLUT_DOUBLE)

glut.glutCreateWindow ("Etapa 2")

# Indicamos cuales son las funciones de redibujado e idle
glut.glutDisplayFunc(Display)
glut.glutIdleFunc(Idle)
glut.glutReshapeFunc(Reshape)

#El color de fondo sera el negro (RGBA, RGB + Alpha channel)
gl.glClearColor (1.0, 1.0, 1.0, 1.0)
gl.glMatrixMode(gl.GL_PROJECTION)
gl.glLoadIdentity()
gl.glOrtho (-1.0, 1.0, -1.0, 1.0, -1.0, 1.0)
gl.glMatrixMode(gl.GL_MODELVIEW)

#Comienza la ejecucion del core de GLUT
glut.glutMainLoop()

