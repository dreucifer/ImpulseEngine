"""@todo: Render docstring"""
import precompiled as pc

def render_string( x_val, y_val, string ):
    """@todo: define renderstring"""
    glColor3f( 0.5, 0.5, 0.9 )
    glRasterPos2i( x_val, y_val )
    for character in string:
        glutBitmapCharacter( GLUT_BITMAP_9_BY_15, character )
