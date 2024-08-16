# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["BatimentGroupeAdresseAPIExpert"]


class BatimentGroupeAdresseAPIExpert(BaseModel):
    batiment_groupe_id: Optional[str] = None
    """Identifiant du groupe de bÃ¢timent au sens de la BDNB

    Note: This is a Primary Key.<pk/>
    """

    cle_interop_adr_principale_ban: Optional[str] = None
    """ClÃ© d'interopÃ©rabilitÃ© de l'adresse principale (issue de la BAN)"""

    code_departement_insee: Optional[str] = None
    """Code dÃ©partement INSEE"""

    fiabilite_cr_adr_niv_1: Optional[str] = None
    """
    FiabilitÃ© des donnÃ©es croisÃ©es Ã l'adresse ('donnÃ©es croisÃ©es Ã l'adresse
    fiables', 'donnÃ©es croisÃ©es Ã l'adresse fiables Ã l'echelle de la parcelle
    unifiee', 'donnÃ©es croisÃ©es Ã l'adresse moyennement fiables', 'problÃ¨me de
    gÃ©ocodage')
    """

    fiabilite_cr_adr_niv_2: Optional[str] = None
    """FiabilitÃ© dÃ©taillÃ©e des donnÃ©es croisÃ©es Ã l'adresse"""

    libelle_adr_principale_ban: Optional[str] = None
    """LibellÃ© complet de l'adresse principale (issue de la BAN)"""

    nb_adresse_valid_ban: Optional[int] = None
    """
    Nombre d'adresses valides diffÃ©rentes provenant de la BAN qui desservent le
    groupe de bÃ¢timent
    """
