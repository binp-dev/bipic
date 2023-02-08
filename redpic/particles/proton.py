from scipy.constants import elementary_charge, proton_mass

from redpic.particles.base import BaseParticle


class Proton(BaseParticle):
    """Class for protons.

    Parameters
    ----------
    x : float
        The x-coordinate of the proton.
    y : float
        The y-coordinate of the proton.
    z : float
        The z-coordinate of the proton.
    px : float
        The x-component of the momentum.
    py : float
        The y-component of the momentum.
    pz : float
        The z-component of the momentum.
    """
    def __init__(self, x, y, z, px, py, pz):
        super().__init__(x, y, z, px, py, pz, proton_mass, elementary_charge)

    def __str__(self):
        """Return a string representation of the proton."""
        return f"Proton {self.id} at ({self.x}, {self.y}, {self.z}) with " \
               f"momentum ({self.px}, {self.py}, {self.pz})"
