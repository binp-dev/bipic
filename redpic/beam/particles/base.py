from abc import ABC, abstractmethod


class BaseParticle(ABC):
    """Base class for particles.

    Parameters
    ----------
    x : float
        The x-coordinate of the particle.
    y : float
        The y-coordinate of the particle.
    z : float
        The z-coordinate of the particle.
    px : float
        The x-component of the momentum.
    py : float
        The y-component of the momentum.
    pz : float
        The z-component of the momentum.
    mass : float
        The mass of the particle.
    charge : float
        The charge of the particle.
    """

    def __init__(self, x, y, z, px, py, pz, mass, charge):
        self.id = id(self)
        self.x = x
        self.y = y
        self.z = z
        self.px = px
        self.py = py
        self.pz = pz
        self.mass = mass
        self.charge = charge

    @abstractmethod
    def __str__(self):
        """Return a string representation of the particle."""
        pass

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.id == other.id
