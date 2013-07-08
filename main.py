#!/usr/bin/env python
# encoding: utf-8
"""
    Copyright (c) 2013 Randy Gaul http://RandyGaul.net

    This software is provided 'as-is', without any express or implied
    warranty. In no event will the authors be held liable for any damages
    arising from the use of this software.

    Permission is granted to anyone to use this software for any purpose,
    including commercial applications, and to alter it and redistribute it
    freely, subject to the following restrictions:

      1. The origin of this software must not be misrepresented;
      you must not claim that you wrote the original software. If you
      use this software in a product, an acknowledgment in the product
      documentation would be appreciated but is not required.

      2. Altered source versions must be plainly marked as such, and must
      not be misrepresented as being the original software.

      3. This notice may not be removed or altered from any source
      distribution.
"""
import sys
from precompiled import *


def mouse(button, state, x_val, y_val):
    """@todo: define mouse()"""

    x_val /= 10.0
    y_val /= 10.0
    if state == GLUT_DOWN:
        if button == GLUT_LEFT_BUTTON:
            poly = PolygonShape
        count = random(3, MaxPolyVertexCount)
        vertices = Vec2[count]()
        e = Random(5, 10)
        for vertex in vertices:
            vertex.Set(Random(-e, e), Random(-e, e))
        poly.Set(vertices, count)
        b = SCENE.add(poly, x, y)
        b.SetOrient(Random(-PI, PI))
        b.restitution = 0.2
        b.dynamicFriction = 0.2
        b.staticFriction = 0.4
        del vertices
    elif button == GLUT_RIGHT_BUTTON:
        c = Circle(Random(1.0, 3.0))
        b = SCENE.add(c, x, y)


def keyboard(key, x, y):
    """@todo: define keyboard()"""

    if key == ESC_KEY:
        exit(0)
    elif key == 's':
        pass
    elif key == 'd':
        pass
    elif key == 'f':
        frame_stepping = False if frame_stepping else True
    elif key == ' ':
        canStep = True
    else:
        pass


def physics_loop():
    """@todo: define physics_loop()"""

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    RenderString(1, 2, "Left click to spawn a polygon")
    RenderString(1, 4, "Right click to spawn a circle")
    accumulator = 0
    accumulator += G_CLOCK.elapsed()
    G_CLOCK.start()
    accumulator = Clamp(0.0, 0.1, accumulator)
    while accumulator >= dt:
        if not frame_stepping:
            SCENE.step()
        else:
            if canStep:
                SCENE.step()
            canStep = False
        accumulator -= dt
    G_CLOCK.stop()
    SCENE.render()
    glutSwapBuffers()


def main():
    """@todo: define main()"""

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"PhyEngine")
    glutDisplayFunc(physics_loop)
    glutKeyboardFunc(keyboard)
    glutMouseFunc(mouse)
    glutIdleFunc(physics_loop)
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    gluOrtho2D(0, 80, 60, 0)
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()
    c = Circle( 5.0 )
    b = SCENE.add( c, 40, 40 )
    b.SetStatic()
    b.SetOrient( 0 )
    poly = PolygonShape()
    poly.setBox( 30.0, 1.0 )
    b = SCENE.add( poly, 40, 55 )
    b.SetStatic()
    b.SetOrient( 0 )
    srand( 1 )
    glutMainLoop()
    return 0

if __name__ == "__main__":
    ESC_KEY = 27
    SCENE = Scene(1.0 / 60.0, 10)
    G_CLOCK = Clock()
    FRAME_STEPPING = False
    CANSTEP = False

    main()
