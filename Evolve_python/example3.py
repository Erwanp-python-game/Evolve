import pygame
from pygame.locals import *
import pickle
from OpenGL.GL import *
from OpenGL.GLU import *

verticies = (
    ( 1, -1, -1), # 0
    ( 1,  1, -1), # 1
    (-1,  1, -1), # 2
    (-1, -1, -1), # 3
    ( 1, -1,  1), # 4
    ( 1,  1,  1), # 5
    (-1, -1,  1), # 6
    (-1,  1,  1), # 7
    )

surfaces = (
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6),
    )
normals = [
    ( 0,  0, -1),  # surface 0
    (-1,  0,  0),  # surface 1
    ( 0,  0,  1),  # surface 2
    ( 1,  0,  0),  # surface 3
    ( 0,  1,  0),  # surface 4
    ( 0, -1,  0)   # surface 5
]

colors = (
    (1,1,1),
    (0,1,0),
    (0,0,1),
    (0,1,0),
    (0,0,1),
    (1,0,1),
    (0,1,0),
    (1,0,1),
    (0,1,0),
    (0,0,1),
    )
edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7),
    )

def loadTexture():
    textureSurface = pygame.image.load('wood.png')
    textureData = pygame.image.tostring(textureSurface, "RGBA", 1)
    width = textureSurface.get_width()
    height = textureSurface.get_height()

    glEnable(GL_TEXTURE_2D)
    texid = glGenTextures(1)

    glBindTexture(GL_TEXTURE_2D, texid)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height,
                 0, GL_RGBA, GL_UNSIGNED_BYTE, textureData)

    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

    return texid



def Cube():
	glBegin(GL_QUADS)
	for i_surface, surface in enumerate(surfaces):
		x = 0
		glNormal3fv(normals[i_surface])
		
		for vertex in surface:
			x+=1
			glColor3fv((1,0,0))
			if x==1:
				glTexCoord2f(0.0, 0.0)
			if x==2:
				glTexCoord2f(0, 1.0)
			if x==3:
				glTexCoord2f(1, 00)
			if x==4:
				glTexCoord2f(1, 1.0)
			glVertex3fv(verticies[vertex])
	glEnd()
	glColor3fv(colors[0])
	glBegin(GL_LINES)
	for edge in edges:
		for vertex in edge:
			glVertex3fv(verticies[vertex])
	glEnd()
	
def read():
	global surfaces,verticies,normals
	surfaces=[]
	verticies=[]
	normals=[]
	f = open("cuby", "rb")
	g=pickle.load(f)
	while g!='fin':
		surfaces.append((g[0][0],g[1][0],g[2][0]))
		g=pickle.load(f)
	g=pickle.load(f)
	while g!='fin':
		verticies.append((g[1],g[2],g[3]))
		g=pickle.load(f)
	g=pickle.load(f)
	while g!='fin':
		normals.append((g[1],g[2],g[3]))
		g=pickle.load(f)
read()
print(len(normals),len(verticies))

def objdraw():
	glBegin(GL_TRIANGLES)
	for i_surface, surface in enumerate(surfaces):
		x = 0
		#
		
		for vertex in surface:
			x+=1
			glColor3fv((1,0,0))
			if x==1:
				glTexCoord2f(0.0, 0.0)
			if x==2:
				glTexCoord2f(0, 1.0)
			if x==3:
				glTexCoord2f(1, 00)
			if x==4:
				glTexCoord2f(1, 1.0)
			
			glNormal3fv(normals[vertex-1])
			glVertex3fv(verticies[vertex-1])
	glEnd()
	#glColor3fv(colors[0])
	#glBegin(GL_LINES)
	#for edge in edges:
		#for vertex in edge:
			#glVertex3fv(verticies[vertex])
	#glEnd()

def drawText(x, y, text):                                                
    position = (x, y, 0)                                                       
    font = pygame.font.Font(None, 64)                                          
    textSurface = font.render(text, True, (255,255,255,255),                   
                              (0,0,0,255))                                     
    textData = pygame.image.tostring(textSurface, "RGBA", True)                
    glRasterPos3d(*position)                                                
    glDrawPixels(textSurface.get_width(), textSurface.get_height(),GL_RGBA, GL_UNSIGNED_BYTE, textData)      


def main():
    global surfaces

    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    clock = pygame.time.Clock()
    loadTexture()
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glMatrixMode(GL_MODELVIEW)
    glTranslatef(0, 0, -5)
    #glLight(GL_LIGHT0, GL_POSITION,  (0, 0, 1, 0)) # directional light from the front
    glLight(GL_LIGHT0, GL_POSITION,  (5, 5, 5, 1)) # point light from the left, top, front
    glLightfv(GL_LIGHT0, GL_AMBIENT, (0, 0, 0, 1))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (1, 1, 1, 1))

    glEnable(GL_DEPTH_TEST) 

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()      
		
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glEnable(GL_COLOR_MATERIAL)
        glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE )

        glRotatef(1, 3, 1, 1)
        objdraw()
        drawText(400,600,'gnap')
        glDisable(GL_LIGHT0)
        glDisable(GL_LIGHTING)
        glDisable(GL_COLOR_MATERIAL)

        pygame.display.flip()
        clock.tick(60)

main()
