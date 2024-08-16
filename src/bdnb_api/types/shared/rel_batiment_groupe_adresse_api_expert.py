# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["RelBatimentGroupeAdresseAPIExpert"]


class RelBatimentGroupeAdresseAPIExpert(BaseModel):
    batiment_groupe_id: Optional[str] = None
    """Identifiant du groupe de bÃ¢timent au sens de la BDNB

    Note: This is a Foreign Key to
    `batiment_groupe.batiment_groupe_id`.<fk table='batiment_groupe' column='batiment_groupe_id'/>
    """

    classe: Optional[str] = None
    """Classe de mÃ©thodologie de croisement Ã l'adresse (Fichiers_fonciers, Cadastre)"""

    cle_interop_adr: Optional[str] = None
    """ClÃ© d'interopÃ©rabilitÃ© de l'adresse postale

    Note: This is a Foreign Key to
    `adresse.cle_interop_adr`.<fk table='adresse' column='cle_interop_adr'/>
    """

    code_departement_insee: Optional[str] = None
    """Code dÃ©partement INSEE"""

    geom_bat_adresse: Optional[str] = None
    """
    GÃ©olocalisant du trait reliant le point adresse Ã la gÃ©omÃ©trie du bÃ¢timent
    groupe (Lambert-93, SRID=2154)
    """

    lien_valide: Optional[bool] = None
    """
    [DEPRECIEE] (bdnb) un couple (batiment_groupe ; adresse) est considÃ©rÃ© comme
    valide si l'adresse est une adresse ban et que le batiment_groupe est associÃ© Ã
    des fichiers fonciers
    """

    origine: Optional[str] = None
    """Origine de l'entrÃ©e bÃ¢timent.

    Elle provient soit des donnÃ©es fonciÃ¨res (Fichiers Fonciers), soit d'un
    croisement gÃ©ospatial entre le Cadastre, la BDTopo et des bases de donnÃ©es
    mÃ©tiers (ex: BPE ou MÃ©rimÃ©e)
    """
