import numpy as np
import scipy.constants as scc

class LaserProfile(object):
    """
    Base class for all laser profiles.

    Any new laser profile should inherit from this class, and define its own
    `evaluate` method, using the same signature as the method below.
    """
    def __init__( self, wavelength, pol ):
        """
        Initialize the propagation direction of the laser.
        (Each subclass should call this method at initialization.)

        Parameters:
        -----------
        wavelength: scalar
            Central wavelength for which the laser pulse envelope is defined.

        pol: list of 2 complex numbers
            Polarization vector that multiplies array_in to get the Ex and Ey fields.
            The envelope of each component of the electric field is given by:
            - Ex_env = array_in*pol(0)
            - Ey_env = array_in*pol(1)
            Standard polarizations can be obtained from:
            - Linear polarization in x: pol = (1,0)
            - Linear polarization in y: pol = (0,1)
            - Circular polarization: pol = (1,j)/sqrt(2) (j is the imaginary number)
            The polarization vector is normalized to have a unitary magnitude.
        """
        assert(len(pol) == 2)
        norm_pol = np.sqrt(np.abs(pol[0])**2 + np.abs(pol[1])**2)
        self.pol = np.array([pol[0]/norm_pol, pol[1]/norm_pol])
        self.lambda0 = wavelength
        self.omega0 = 2*scc.pi*scc.c/self.lambda0

    def evaluate( self, dim, envelope, *axes ):
        """
        Fills the envelope field of the laser
        Usage: evaluate(dim, envelope, x, y, t) (3D Cartesian) or
               evaluate(dim, envelope, r, t) (2D cylindrical)

        Parameters
        -----------
        dim: string
            'rt' or 'xyt'

        envelope: ndarrays (V/m)
            Contains the values of the envelope field, to be filled

        axes: Coordinates at which the envelope should be evaluated.
            Can be 2 elements in cylindrical geometry (r,t) or
            3 elements in Cartesian geometry (x,y,t).
        """
        # The base class only defines dummy fields
        # (This should be replaced by any class that inherits from this one.)
        pass
