# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["RelBatimentGroupeRncAPIExpert"]


class RelBatimentGroupeRncAPIExpert(BaseModel):
    adresse_brut: Optional[str] = None
    """adresse brute envoyÃ©e au gÃ©ocodeur"""

    adresse_geocodee: Optional[str] = None
    """libelle de l'adresse retournÃ©e par le gÃ©ocodeur"""

    batiment_groupe_id: Optional[str] = None
    """Identifiant du groupe de bÃ¢timent au sens de la BDNB"""

    cle_interop_adr: Optional[str] = None
    """ClÃ© d'interopÃ©rabilitÃ© de l'adresse postale"""

    code_departement_insee: Optional[str] = None
    """Code dÃ©partement INSEE"""

    fiabilite_geocodage: Optional[str] = None
    """fiabilitÃ© du gÃ©ocodage"""

    fiabilite_globale: Optional[str] = None
    """fiabilitÃ© du global du croisement"""

    numero_immat: Optional[str] = None
    """identifiant de la table rnc"""

    parcelle_id: Optional[str] = None
    """
    (ffo:idpar) Identifiant de parcelle (ConcatÃ©nation de ccodep, ccocom, ccopre,
    ccosec, dnupla)
    """
