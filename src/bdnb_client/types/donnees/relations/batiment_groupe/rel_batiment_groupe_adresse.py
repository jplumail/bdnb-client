# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ....._models import BaseModel

__all__ = ["RelBatimentGroupeAdresse"]


class RelBatimentGroupeAdresse(BaseModel):
    batiment_groupe_id: Optional[str] = None
    """Identifiant du groupe de bâtiment au sens de la BDNB

    Note: This is a Foreign Key to
    `batiment_groupe.batiment_groupe_id`.<fk table='batiment_groupe' column='batiment_groupe_id'/>
    """

    classe: Optional[str] = None
    """Classe de méthodologie de croisement à l'adresse (Fichiers_fonciers, Cadastre)"""

    cle_interop_adr: Optional[str] = None
    """Clé d'interopérabilité de l'adresse postale

    Note: This is a Foreign Key to
    `adresse.cle_interop_adr`.<fk table='adresse' column='cle_interop_adr'/>
    """

    code_departement_insee: Optional[str] = None
    """Code département INSEE"""

    geom_bat_adresse: Optional[str] = None
    """
    Géolocalisant du trait reliant le point adresse à la géométrie du bâtiment
    groupe (Lambert-93, SRID=2154)
    """

    lien_valide: Optional[bool] = None
    """
    [DEPRECIEE] (bdnb) un couple (batiment_groupe ; adresse) est considéré comme
    valide si l'adresse est une adresse ban et que le batiment_groupe est associé à
    des fichiers fonciers
    """

    origine: Optional[str] = None
    """Origine de l'entrée bâtiment.

    Elle provient soit des données foncières (Fichiers Fonciers), soit d'un
    croisement géospatial entre le Cadastre, la BDTopo et des bases de données
    métiers (ex: BPE ou Mérimée)
    """
