# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["IrisSimulationsValeurVerte"]


class IrisSimulationsValeurVerte(BaseModel):
    batiment_groupe_id: Optional[str] = None
    """Identifiant du groupe de bâtiment au sens de la BDNB"""

    code_departement_insee: Optional[str] = None
    """Code département INSEE"""

    gain_classe_b_vers_a: Optional[float] = None
    """
    (simulations) gain en % de la valeur immobilière lorsqu'on simule le changement
    de DPE B vers A.
    """

    gain_classe_c_vers_a: Optional[object] = None
    """
    (simulations) gain en % de la valeur immobilière lorsqu'on simule le changement
    de DPE C vers A.
    """

    gain_classe_c_vers_b: Optional[object] = None
    """
    (simulations) gain en % de la valeur immobilière lorsqu'on simule le changement
    de DPE C vers B.
    """

    gain_classe_d_vers_a: Optional[object] = None
    """
    (simulations) gain en % de la valeur immobilière lorsqu'on simule le changement
    de DPE D vers A.
    """

    gain_classe_d_vers_b: Optional[object] = None
    """
    (simulations) gain en % de la valeur immobilière lorsqu'on simule le changement
    de DPE D vers B.
    """

    gain_classe_d_vers_c: Optional[object] = None
    """
    (simulations) gain en % de la valeur immobilière lorsqu'on simule le changement
    de DPE D vers C.
    """

    gain_classe_e_vers_a: Optional[object] = None
    """
    (simulations) gain en % de la valeur immobilière lorsqu'on simule le changement
    de DPE E vers A.
    """

    gain_classe_e_vers_b: Optional[object] = None
    """
    (simulations) gain en % de la valeur immobilière lorsqu'on simule le changement
    de DPE E vers B.
    """

    gain_classe_e_vers_c: Optional[object] = None
    """
    (simulations) gain en % de la valeur immobilière lorsqu'on simule le changement
    de DPE E vers C.
    """

    gain_classe_e_vers_d: Optional[object] = None
    """
    (simulations) gain en % de la valeur immobilière lorsqu'on simule le changement
    de DPE E vers D.
    """

    gain_classe_f_vers_a: Optional[object] = None
    """
    (simulations) gain en % de la valeur immobilière lorsqu'on simule le changement
    de DPE F vers A.
    """

    gain_classe_f_vers_b: Optional[object] = None
    """
    (simulations) gain en % de la valeur immobilière lorsqu'on simule le changement
    de DPE F vers B.
    """

    gain_classe_f_vers_c: Optional[object] = None
    """
    (simulations) gain en % de la valeur immobilière lorsqu'on simule le changement
    de DPE F vers C.
    """

    gain_classe_f_vers_d: Optional[object] = None
    """
    (simulations) gain en % de la valeur immobilière lorsqu'on simule le changement
    de DPE F vers D.
    """

    gain_classe_f_vers_e: Optional[object] = None
    """
    (simulations) gain en % de la valeur immobilière lorsqu'on simule le changement
    de DPE F vers E.
    """

    gain_classe_g_vers_a: Optional[object] = None
    """
    (simulations) gain en % de la valeur immobilière lorsqu'on simule le changement
    de DPE G vers A.
    """

    gain_classe_g_vers_b: Optional[object] = None
    """
    (simulations) gain en % de la valeur immobilière lorsqu'on simule le changement
    de DPE G vers B.
    """

    gain_classe_g_vers_c: Optional[object] = None
    """
    (simulations) gain en % de la valeur immobilière lorsqu'on simule le changement
    de DPE G vers C.
    """

    gain_classe_g_vers_d: Optional[object] = None
    """
    (simulations) gain en % de la valeur immobilière lorsqu'on simule le changement
    de DPE G vers D.
    """

    gain_classe_g_vers_e: Optional[object] = None
    """
    (simulations) gain en % de la valeur immobilière lorsqu'on simule le changement
    de DPE G vers E.
    """

    gain_classe_g_vers_f: Optional[object] = None
    """
    (simulations) gain en % de la valeur immobilière lorsqu'on simule le changement
    de DPE G vers F.
    """

    renovation: Optional[float] = None
    """
    (simulations) gain en % de la valeur immobilière lorsqu'on simule une
    rénovation.
    """
