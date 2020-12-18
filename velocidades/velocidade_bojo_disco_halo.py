from typing import List
import math
import numpy as np
from scipy.constants import gravitational_constant, parsec
from astropy.constants import M_sun
from scipy.special import i0, i1, k0, k1


def vb(r: List[float], a: float, M: float) -> List[float]:
    """
        r: Raios em kpc
        a: Parâmetro de escala do bojo, em kpc
        M: Massa total do Bojo em Massas Solares

        return:
            Velocidades caudadas pelo bojo em km/s
    """
    G = gravitational_constant
    kpc = 1000*parsec
    Msol = M_sun.to_value()
    C = math.sqrt(G * (M*Msol)/(a*kpc))

    x = r/a
    v = C * np.sqrt((1-np.exp(-x)*(1+x+x*x/2.0))/x)
    v /= 1000.0

    return v

def vd(r: List[float], a: float, M: float) -> List[float]:
    """
        r: Raios em kpc
        a: Parâmetro de escala do disco, em kpc
        M: Massa total do Bojo em Massas Solares

        return:
            Velocidades caudadas pelo bojo em km/s
    """
    G = gravitational_constant
    kpc = 1000*parsec
    Msol = M_sun.to_value()
    C = math.sqrt(G * (M*Msol)/(a*kpc))

    x = r/(2.0*a)
    v = C * np.sqrt( x*x*(i0(x)*k0(x) -i1(x)*k1(x)))
    v /= 1000.0

    return v

def vh(r: List[float], a: float, vc: float) -> List[float]:
    """
        r: Raios em kpc
        a: Parâmetro de escala do halo, em kpc
        vc: velocidade terminal

        return:
            Velocidades caudadas pelo bojo em km/s
    """

    x =r/a
    v = vc * np.sqrt(1- np.arcsin(x)/x)

    return v