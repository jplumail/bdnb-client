# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["BatimentGroupeAdresse"]


class BatimentGroupeAdresse(BaseModel):
    batiment_groupe_id: Optional[str] = None
    """Identifiant du groupe de bâtiment au sens de la BDNB

    Note: This is a Primary Key.<pk/>
    """

    cle_interop_adr_principale_ban: Optional[str] = None
    """Clé d'interopérabilité de l'adresse principale (issue de la BAN)"""

    code_departement_insee: Optional[str] = None
    """Code département INSEE"""

    fiabilite_cr_adr_niv_1: Optional[str] = None
    """
    Fiabilité des données croisées à l'adresse ('données croisées à l'adresse
    fiables', 'données croisées à l'adresse fiables à l'echelle de la parcelle
    unifiee', 'données croisées à l'adresse moyennement fiables', 'problème de
    géocodage')
    """

    fiabilite_cr_adr_niv_2: Optional[str] = None
    """Fiabilité détaillée des données croisées à l'adresse"""

    libelle_adr_principale_ban: Optional[str] = None
    """Libellé complet de l'adresse principale (issue de la BAN)"""

    nb_adresse_valid_ban: Optional[int] = None
    """
    Nombre d'adresses valides différentes provenant de la BAN qui desservent le
    groupe de bâtiment
    """
