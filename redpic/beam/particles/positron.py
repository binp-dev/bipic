from scipy.constants import electron_mass, elementary_charge

from redpic.beam.particles.base import BaseParticle


class Positron(BaseParticle):
    """Class for positrons.

    Parameters
    ----------
    x : float
        The x-coordinate of the positron.
    y : float
        The y-coordinate of the positron.
    z : float
        The z-coordinate of the positron.
    px : float
        The x-component of the momentum.
    py : float
        The y-component of the momentum.
    pz : float
        The z-component of the momentum.
    """
    def __init__(self, x, y, z, px, py, pz):
        super().__init__(x, y, z, px, py, pz, electron_mass, -elementary_charge)

    def __str__(self):
        """Return a string representation of the positron."""
        return f"Positron {self.id} at ({self.x}, {self.y}, {self.z}) with " \
               f"momentum ({self.px}, {self.py}, {self.pz})"
