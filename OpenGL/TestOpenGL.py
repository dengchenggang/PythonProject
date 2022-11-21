#!/usr/bin/python3
# -*-coding: utf-8 -*-
from OpenGL import GLUT, GL
import glm


class CTestOpenGL(object):

    def __init__(self) -> None:
        GLUT.glutInit()
        GLUT.glutInitDisplayMode(GLUT.GLUT_SINGLE | GLUT.GLUT_RGBA)
        GLUT.glutInitWindowSize(1920, 1080)
        GLUT.glutCreateWindow("Just For Test")
        GLUT.glutDisplayFunc(self.OnDraw)
        GLUT.glutIdleFunc(self.OnDraw)
        GLUT.glutMainLoop()

    def OnDraw(self) -> None:
        GL.glClear(GL.GL_COLOR_BUFFER_BIT)
        GL.glRotatef(0.5, 0, 1, 0)
        GLUT.glutWireTeapot(0.5)
        GL.glFlush()

if __name__ == "__main__":
    r = glm.lookAt((0.0, 0.0, 0.0), (0.0, 1.0, 0.0), (0.0, 0.0, -1.0))
    print(r)
