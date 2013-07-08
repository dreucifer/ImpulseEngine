"""@todo: to be defined """

from precompiled import GRAVITY

class Scene(object):
    """Docstring for Scene """

    def __init__(self, deltat, iterations):
        """@todo: to be defined """

    def step(self):
        """@todo: to be defined """
        pass

    def render(self):
        """@todo: to be defined """
        pass

    def add(self, shape, x_val, y_val):
        """@todo: to be defined """
        pass

    def clear(self):
        """@todo: to be defined """
        pass

    m_dt = m_iterations = bodies = contacts = None


def integrate_forces(body, delta_time):
    """@todo: define integrate_forces"""
    if( body.im == 0.0 ):
        return

    body.velocity += ( body.force * body.im + GRAVITY ) * ( delta_time / 2.0 )
    body.angular_velocity += body.torque * body.ii * ( delta_time / 2.0 )
