# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ....._models import BaseModel

__all__ = ["RelBatimentGroupeRnc"]


class RelBatimentGroupeRnc(BaseModel):
    adresse_brut: Optional[str] = None
    """adresse brute envoyée au géocodeur"""

    adresse_geocodee: Optional[str] = None
    """libelle de l'adresse retournée par le géocodeur"""

    batiment_groupe_id: Optional[str] = None
    """Identifiant du groupe de bâtiment au sens de la BDNB"""

    cle_interop_adr: Optional[str] = None
    """Clé d'interopérabilité de l'adresse postale"""

    code_departement_insee: Optional[str] = None
    """Code département INSEE"""

    fiabilite_geocodage: Optional[str] = None
    """fiabilité du géocodage"""

    fiabilite_globale: Optional[str] = None
    """fiabilité du global du croisement"""

    numero_immat: Optional[str] = None
    """identifiant de la table rnc"""

    parcelle_id: Optional[str] = None
    """
    (ffo:idpar) Identifiant de parcelle (Concaténation de ccodep, ccocom, ccopre,
    ccosec, dnupla)
    """
