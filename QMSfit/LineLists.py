from enum import Enum


class Lines(Enum):
    """The Lines enum class is used to store the wavelengths of the most 
       common lines. The wavelengths (vacuum) are in Angstroms.
    """
    OVI = 1033.82
    Lya = 1215.24
    NV = 1240.81
    OI1305 = 1305.53
    CII1335 = 1335.31
    SiIV = 1397.61
    OIV1399 = 1399.8
    CIV = 1549.48
    HeII1640 = 1640.4
    OIII1665 = 1665.85
    AlIII1857 = 1857.4
    CIII1908 = 1908.734
    CII2326 = 2326.0
    NeIV2439 = 2439.5
    MgII = 2799.117
    NeV3346 = 3346.79
    NeVI3426 = 3426.85
    OII3727 = 3727.092
    OII3729 = 3729.875
    HeI3889 = 3889.0
    SII4072 = 4072.3
    Hdelta = 4102.89
    Hd = 4102.89
    Hgamma = 4341.68
    Hg = 4341.68
    OIII4364 = 4364.436
    HeII4686 = 4686.0
    Hbeta = 4862.68
    Hb = 4862.68
    OIII4932 = 4932.603
    OIII4959 = 4960.295
    OIII5007 = 5008.240
    OI6302 = 6302.046
    OI6365 = 6365.536
    NI6529 = 6529.03
    NII6549 = 6549.86
    Halpha = 6564.61
    Ha = 6564.61
    NII6585 = 6585.27
    SII6718 = 6718.29
    SII6732 = 6732.67


def get_line_wavelength(line):
    """Return the wavelength of the line in Angstroms."""
    try:
        return Lines[line].value
    except KeyError:
        raise ValueError(f"Line {line} not found in the Lines enum.")