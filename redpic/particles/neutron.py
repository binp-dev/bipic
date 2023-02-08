from scipy.constants import neutron_mass

from redpic.particles.base import BaseParticle


class Neutron(BaseParticle):
    """Class for neutrons.

    Parameters
    ----------
    x : float
        The x-coordinate of the neutron.
    y : float
        The y-coordinate of the neutron.
    z : float
        The z-coordinate of the neutron.
    px : float
        The x-component of the momentum.
    py : float
        The y-component of the momentum.
    pz : float
        The z-component of the momentum.
    """
    def __init__(self, x, y, z, px, py, pz):
        super().__init__(x, y, z, px, py, pz, neutron_mass, 0)

    def __str__(self):
        """Return a string representation of the neutron."""
        return f"Neutron {self.id} at ({self.x}, {self.y}, {self.z}) with " \
               f"momentum ({self.px}, {self.py}, {self.pz})"
