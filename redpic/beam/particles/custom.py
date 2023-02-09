from redpic.beam.particles.base import BaseParticle


class CustomParticle(BaseParticle):
    """Class for custom particles.

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
        super().__init__(x, y, z, px, py, pz, mass, charge)

    def __str__(self):
        """Return a string representation of the particle."""
        return f"Particle {self.id} at ({self.x}, {self.y}, {self.z}) with " \
               f"momentum ({self.px}, {self.py}, {self.pz})"
