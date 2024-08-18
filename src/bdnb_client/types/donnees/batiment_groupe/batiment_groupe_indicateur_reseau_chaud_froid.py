# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["BatimentGroupeIndicateurReseauChaudFroid"]


class BatimentGroupeIndicateurReseauChaudFroid(BaseModel):
    batiment_groupe_id: Optional[str] = None
    """(bdnb) Clé d'Intéropérabilité du bâtiment dans la BDNB"""

    code_departement_insee: Optional[str] = None
    """Code département INSEE"""

    consommation_chaleur_par_rapport_distance_au_reseau: Optional[str] = None
    """Indication sur la consommation de chaleur du bâtiment et sa distance au réseau.

    Plus un bâtiment consomme plus celui-ci peut àªtre éloigné du réseau et malgré
    tout àªtre raccordé. Ici, si la distance entre le bâtiment et le réseau est
    suffisamment proche par rapport à sa consommation, la consommation est noté
    'suffisante', sinon elle est notée 'trop faible'.
    """

    id_reseau: Optional[str] = None
    """(France chaleur urbaine) Identifiant national du réseau."""

    id_reseau_bdnb: Optional[str] = None
    """
    Identifiant BDNB, lié au réseau de chaleur, car des données sources ne disposent
    pas d'identifiant unique pour chacune des entrées (traces et points).
    """

    indicateur_distance_au_reseau: Optional[str] = None
    """
    Indication sur la distance entre le bâtiment et le point au réseau de chaleur le
    plus proche en vue d'un potentiel raccordement au réseau.
    """

    indicateur_systeme_chauffage: Optional[str] = None
    """
    Indication sur le système de chauffage en vue d'un potentiel raccordement au
    réseau de chaleur
    """

    potentiel_obligation_raccordement: Optional[str] = None
    """
    Indique si le bâtiment est éventuellement dans l'obligation de se raccorder lors
    de certains travaux de rénovation. Pour que potentiel_obligation_raccordement
    soit possible, le bâtiment doit àªtre situé à moins de 100m d'un réseau classé
    et son système de chauffage indiqué comme collectif. Attention, cet indicateur
    n'est qu'à titre d'information.
    """

    potentiel_raccordement_reseau_chaleur: Optional[str] = None
    """Indicateur de potentiel de raccordement au réseau de chaleur.

    L'indicateur dépend de la distance entre le bâtiment et le réseau et du type de
    circuit de chauffage existant du bâtiment. Enfin, si le bâtiment est déjà
    raccordé alors il est indiqué comme tel.
    """
