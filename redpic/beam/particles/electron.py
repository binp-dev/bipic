from scipy.constants import electron_mass, elementary_charge

from redpic.beam.particles.base import BaseParticle


class Electron(BaseParticle):
    """Class for electrons.

    Parameters
    ----------
    x : float
        The x-coordinate of the electron.
    y : float
        The y-coordinate of the electron.
    z : float
        The z-coordinate of the electron.
    px : float
        The x-component of the momentum.
    py : float
        The y-component of the momentum.
    pz : float
        The z-component of the momentum.
    """
    def __init__(self, x, y, z, px, py, pz):
        super().__init__(x, y, z, px, py, pz, electron_mass, elementary_charge)

    def __str__(self):
        """Return a string representation of the electron."""
        return f"Electron {self.id} at ({self.x}, {self.y}, {self.z}) with " \
               f"momentum ({self.px}, {self.py}, {self.pz})"
