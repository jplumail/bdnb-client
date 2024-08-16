# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["BatimentGroupeIndicateurReseauChaudFroidAPIExpert"]


class BatimentGroupeIndicateurReseauChaudFroidAPIExpert(BaseModel):
    batiment_groupe_id: Optional[str] = None
    """(bdnb) ClÃ© d'IntÃ©ropÃ©rabilitÃ© du bÃ¢timent dans la BDNB"""

    code_departement_insee: Optional[str] = None
    """Code dÃ©partement INSEE"""

    consommation_chaleur_par_rapport_distance_au_reseau: Optional[str] = None
    """Indication sur la consommation de chaleur du bÃ¢timent et sa distance au
    rÃ©seau.

    Plus un bÃ¢timent consomme plus celui-ci peut Ãªtre Ã©loignÃ© du rÃ©seau et
    malgrÃ© tout Ãªtre raccordÃ©. Ici, si la distance entre le bÃ¢timent et le
    rÃ©seau est suffisamment proche par rapport Ã sa consommation, la consommation
    est notÃ© 'suffisante', sinon elle est notÃ©e 'trop faible'.
    """

    id_reseau: Optional[str] = None
    """(France chaleur urbaine) Identifiant national du rÃ©seau."""

    id_reseau_bdnb: Optional[str] = None
    """
    Identifiant BDNB, liÃ© au rÃ©seau de chaleur, car des donnÃ©es sources ne
    disposent pas d'identifiant unique pour chacune des entrÃ©es (traces et points).
    """

    indicateur_distance_au_reseau: Optional[str] = None
    """
    Indication sur la distance entre le bÃ¢timent et le point au rÃ©seau de chaleur
    le plus proche en vue d'un potentiel raccordement au rÃ©seau.
    """

    indicateur_systeme_chauffage: Optional[str] = None
    """
    Indication sur le systÃ¨me de chauffage en vue d'un potentiel raccordement au
    rÃ©seau de chaleur
    """

    potentiel_obligation_raccordement: Optional[str] = None
    """
    Indique si le bÃ¢timent est Ã©ventuellement dans l'obligation de se raccorder
    lors de certains travaux de rÃ©novation. Pour que
    potentiel_obligation_raccordement soit possible, le bÃ¢timent doit Ãªtre situÃ©
    Ã moins de 100m d'un rÃ©seau classÃ© et son systÃ¨me de chauffage indiquÃ© comme
    collectif. Attention, cet indicateur n'est qu'Ã titre d'information.
    """

    potentiel_raccordement_reseau_chaleur: Optional[str] = None
    """Indicateur de potentiel de raccordement au rÃ©seau de chaleur.

    L'indicateur dÃ©pend de la distance entre le bÃ¢timent et le rÃ©seau et du type
    de circuit de chauffage existant du bÃ¢timent. Enfin, si le bÃ¢timent est dÃ©jÃ
    raccordÃ© alors il est indiquÃ© comme tel.
    """
