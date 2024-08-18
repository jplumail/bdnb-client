# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["IndicateurReseauChaudFroidListParams"]


class IndicateurReseauChaudFroidListParams(TypedDict, total=False):
    batiment_groupe_id: str
    """(bdnb) Clé d'Intéropérabilité du bâtiment dans la BDNB"""

    code_departement_insee: str
    """Code département INSEE"""

    consommation_chaleur_par_rapport_distance_au_reseau: str
    """Indication sur la consommation de chaleur du bâtiment et sa distance au réseau.

    Plus un bâtiment consomme plus celui-ci peut àªtre éloigné du réseau et malgré
    tout àªtre raccordé. Ici, si la distance entre le bâtiment et le réseau est
    suffisamment proche par rapport à sa consommation, la consommation est noté
    'suffisante', sinon elle est notée 'trop faible'.
    """

    id_reseau: str
    """(France chaleur urbaine) Identifiant national du réseau."""

    id_reseau_bdnb: str
    """
    Identifiant BDNB, lié au réseau de chaleur, car des données sources ne disposent
    pas d'identifiant unique pour chacune des entrées (traces et points).
    """

    indicateur_distance_au_reseau: str
    """
    Indication sur la distance entre le bâtiment et le point au réseau de chaleur le
    plus proche en vue d'un potentiel raccordement au réseau.
    """

    indicateur_systeme_chauffage: str

    limit: str
    """Limiting and Pagination"""

    offset: str
    """Limiting and Pagination"""

    order: str
    """Ordering"""

    potentiel_obligation_raccordement: str
    """
    Indique si le bâtiment est éventuellement dans l'obligation de se raccorder lors
    de certains travaux de rénovation. Pour que potentiel_obligation_raccordement
    soit possible, le bâtiment doit àªtre situé à moins de 100m d'un réseau classé
    et son système de chauffage indiqué comme collectif. Attention, cet indicateur
    n'est qu'à titre d'information.
    """

    potentiel_raccordement_reseau_chaleur: str
    """Indicateur de potentiel de raccordement au réseau de chaleur.

    L'indicateur dépend de la distance entre le bâtiment et le réseau et du type de
    circuit de chauffage existant du bâtiment. Enfin, si le bâtiment est déjà
    raccordé alors il est indiqué comme tel.
    """

    select: str
    """Filtering Columns"""

    range: Annotated[str, PropertyInfo(alias="Range")]

    range_unit: Annotated[str, PropertyInfo(alias="Range-Unit")]
