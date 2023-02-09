import sys
from abc import ABC, abstractmethod


class BaseBeam(ABC):
    """Base class for beams.

    Parameters
    ----------
    particles : list
        The list of particles in the beam.
    """

    def __init__(self, particles):
        self.particles = particles

    @abstractmethod
    def __str__(self):
        """Return a string representation of the beam."""
        pass

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.particles == other.particles

    def __len__(self):
        return len(self.particles)

    def __getitem__(self, index):
        return self.particles[index]

    def __setitem__(self, index, value):
        self.particles[index] = value

    def __delitem__(self, index):
        del self.particles[index]

    def __iter__(self):
        return iter(self.particles)

    def __reversed__(self):
        return reversed(self.particles)

    def __contains__(self, item):
        return item in self.particles

    def __add__(self, other):
        return self.particles + other.particles

    def __iadd__(self, other):
        self.particles += other.particles
        return self

    def __bool__(self):
        return bool(self.particles)

    def __copy__(self):
        return self.__class__(self.particles)

    def __deepcopy__(self, memo):
        return self.__class__(copy.deepcopy(self.particles, memo))

    def __getstate__(self):
        return self.particles

    def __setstate__(self, state):
        self.particles = state

    def __reduce__(self):
        return self.__class__, (self.particles,)

    def __reduce_ex__(self, protocol):
        return self.__reduce__()

    def __sizeof__(self):
        return sys.getsizeof(self.particles)

    @abstractmethod
    def generate(self):
        """Generate the beam."""
        return self.particles
