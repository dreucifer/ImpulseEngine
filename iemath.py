"""The Vec2 and Mat2 classes for impulse engine"""
from math import sqrt, sin, cos, ceil

PI = 3.141592741
EPSILON = 0.0001

class Vec2( object ):
    """Vector class with x and y magnitudes"""
    xval = yval = None

    def __init__( self, xval, yval ):
        self.xval = float(xval)
        self.yval = float(yval)

    def __mul__(self, val):
        if isinstance(val, Vec2):
            return Vec2( self.xval * val.xval, self.yval * val.yval )
        else:
            return Vec2( self.xval * val, self.yval * val )

    def __div__( self, val ):
        return Vec2( self.xval / val, self.yval / val )

    def __imul__( self, val ):
        if isinstance(val, Vec2):
            return Vec2( self.xval * val.xval, self.yval * val.yval )
        else:
            self.xval *= val
            self.yval *= val

    def __add__( self, val ):
        if isinstance(val, Vec2):
            return Vec2( self.xval + val.xval, self.yval + val.yval )
        else:
            return Vec2( self.xval + val, self.yval + val )

    def __iadd__( self, val ):
        if isinstance(val, Vec2):
            self.xval += val.x
            self.yval += val.y
        else:
            self.xval += val
            self.yval += val

    def __sub__( self, val ):
        if isinstance(val, Vec2):
            return Vec2( self.xval - val.xval, self.yval - val.yval )
        elif val != None:
            return Vec2( self.xval - val, self.yval - val )
        elif val == None:
            return Vec2( -self.xval, -self.yval )

    def __isub__( self, val ):
        if isinstance(val, Vec2):
            self.xval -= val.x
            self.yval -= val.y
        else:
            self.xval -= val
            self.yval -= val

    def set( self, xval, yval ):
        """Set the x and y values"""
        self.xval = float(xval)
        self.yval = float(yval)

    def len_sqr( self ):
        """Get the squared length of the vector"""
        return self.xval**2 + self.yval**2

    def len( self ):
        """Get the true length of the vector"""
        return sqrt( self.xval**2 + self.yval**2 )

    def rotate( self, radian ):
        """Rotate the vector a certain number of radians"""
        cosine = cos( radian )
        sine = sin( radian )

        self.xval = ( self.xval * cosine ) - ( self.yval * sine )
        self.yval = ( self.xval * sine ) - ( self.yval * cosine )

    def normalize(self):
        """Normalize the vector"""
        length = self.len()
        if length > EPSILON:
            inv_len = 1.0 / length
            self.xval *= inv_len
            self.yval *= inv_len

class Mat2:
    """2-by-2 matrix class for impulse engine"""
    v = [  ]
    m00 = m01 = m10 = m11 = 0
    matrix = [ [ m00 , m01 ], [ m10 , m11 ] ]

    def __init__( self, *args ):
        if len(args) == 1:
            radians = args[0]
            cosine = cos( radians )
            sine = sin( radians )

            self.m00 = self.m11 = cosine
            self.m10 = sine
            self.m01 = -sine
        elif len(args) == 4:
            m00, m01, m10, m11 = args
            self.m00 = m00
            self.m01 = m01
            self.m10 = m10
            self.m11 = m11
        else:
            self.m00 = 0
            self.m01 = 0
            self.m10 = 0
            self.m11 = 0

    def __mul__( self, val ):
        if isinstance( val, Vec2 ):
            return Vec2( self.m00 * val.x + self.m01 * val.y,
                    self.m10 * val.x + self.m11 * val.y )
        elif isinstance( val, Mat2 ):
            return Mat2(
                    self.m00 * val.m00 + self.m01 * val.m10,
                    self.m00 * val.m01 + self.m01 * val.m11,
                    self.m10 * val.m00 + self.m11 * val.m10,
                    self.m10 * val.m01 + self.m11 * val.m11
                )
        else:
            pass

    def set( self, m00, m01, m10, m11 ):
        """Set the points of the matrix"""
        self.m00 = m00
        self.m01 = m01
        self.m10 = m10
        self.m11 = m11

    def abs( self ):
        """Get matrix of absolute values"""
        return Mat2( 
                abs( self.m00 ),
                abs( self.m01 ),
                abs( self.m10 ),
                abs( self.m11 )
            )

    def axis_x( self ):
        """create a vector of the x-axis"""
        return Vec2( self.m00, self.m10 )

    def axis_y( self ):
        """create a vector of the y-axis"""
        return Vec2( self.m01, self.m11 )

    def transpose( self ):
        """transpose the vector"""
        return Mat2( self.m00, self.m10, self.m01, self.m11 )

def vec_min( vec_a, vec_b ):
    """find the minimal value of two vectors"""
    if isinstance( (vec_a, vec_b), Vec2 ):
        return Vec2( min( vec_a.x, vec_b.x ), min( vec_a.y, vec_b.y ) )

def vec_max( vec_a, vec_b ):
    """find the maximal value of two vectors"""
    if isinstance( (vec_a, vec_b), Vec2 ):
        return Vec2( max( vec_a.x, vec_b.x ), max( vec_a.y, vec_b.y ) )

def dot( vec_a, vec_b ):
    """apply the dot operation to a vector"""
    if isinstance( (vec_a, vec_b), Vec2 ):
        return vec_a.xval * vec_b.xval + vec_a.yval * vec_b.yval
    else:
        pass

def dist_sqr( vec_a, vec_b ):
    """Find the distance squared of two vectors"""
    if isinstance( (vec_a, vec_b), Vec2 ):
        vec_c = vec_a - vec_b
        return dot( vec_c, vec_c )

def cross( arg_a, arg_b ):
    """Finds the cross between either two vectors, a vector and  value,
    or a value and a vector

    :arg_a: Vec2 or real value
    :arg_b: real value or Vec2
    :returns: a vector or a value

    """
    if isinstance( (arg_a, arg_b), Vec2 ):
        vec_a, vec_b = arg_a, arg_b
        return vec_a.xval * vec_b.yval - vec_a.yval * vec_b.xval
    elif isinstance( arg_a, Vec2 ) and not isinstance( arg_b, Vec2 ):
        vector, value = arg_a, arg_b
        return Vec2( value * vector.yval, -value * vector.xval )
    elif not isinstance( arg_a, Vec2 ) and isinstance( arg_b, Vec2 ):
        vector, value = arg_b, arg_a
        return Vec2( -value * vector.yval, value * vector.xval )

def equal( val_a, val_b ):
    """Comparison with tolerance of EPSILON

    :returns: True or False

    """
    return True if abs( val_a - val_b ) <= EPSILON else False

def sqr(arg):
    """square the argument"""
    return arg**2

def clamp( minimum, maximum, value):
    """Clamp value to range( minimum, maximum )"""
    if value < minimum:
        return minimum
    if value > maximum:
        return maximum
    return value

def bias_greater_than(arg_a, arg_b):
    """@todo: Docstring for bias_greater_than"""
    k_bias_relative = 0.95
    k_bias_absolute = 0.01
    return arg_a >= arg_b * k_bias_relative + arg_a * k_bias_absolute

GRAVITY_SCALE = 5.0
GRAVITY = Vec2( 0, 10.0 * GRAVITY_SCALE )
DT = 1.0 / 60.0
