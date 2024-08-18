# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .ancqpv import (
    AncqpvResource,
    AsyncAncqpvResource,
    AncqpvResourceWithRawResponse,
    AsyncAncqpvResourceWithRawResponse,
    AncqpvResourceWithStreamingResponse,
    AsyncAncqpvResourceWithStreamingResponse,
)
from .adresse import (
    AdresseResource,
    AsyncAdresseResource,
    AdresseResourceWithRawResponse,
    AsyncAdresseResourceWithRawResponse,
    AdresseResourceWithStreamingResponse,
    AsyncAdresseResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .proprietaire import (
    ProprietaireResource,
    AsyncProprietaireResource,
    ProprietaireResourceWithRawResponse,
    AsyncProprietaireResourceWithRawResponse,
    ProprietaireResourceWithStreamingResponse,
    AsyncProprietaireResourceWithStreamingResponse,
)
from .batiment_groupe import (
    BatimentGroupeResource,
    AsyncBatimentGroupeResource,
    BatimentGroupeResourceWithRawResponse,
    AsyncBatimentGroupeResourceWithRawResponse,
    BatimentGroupeResourceWithStreamingResponse,
    AsyncBatimentGroupeResourceWithStreamingResponse,
)
from .batiment_groupe_bpe import (
    BatimentGroupeBpeResource,
    AsyncBatimentGroupeBpeResource,
    BatimentGroupeBpeResourceWithRawResponse,
    AsyncBatimentGroupeBpeResourceWithRawResponse,
    BatimentGroupeBpeResourceWithStreamingResponse,
    AsyncBatimentGroupeBpeResourceWithStreamingResponse,
)
from .batiment_groupe_qpv import (
    BatimentGroupeQpvResource,
    AsyncBatimentGroupeQpvResource,
    BatimentGroupeQpvResourceWithRawResponse,
    AsyncBatimentGroupeQpvResourceWithRawResponse,
    BatimentGroupeQpvResourceWithStreamingResponse,
    AsyncBatimentGroupeQpvResourceWithStreamingResponse,
)
from .batiment_groupe_rnc import (
    BatimentGroupeRncResource,
    AsyncBatimentGroupeRncResource,
    BatimentGroupeRncResourceWithRawResponse,
    AsyncBatimentGroupeRncResourceWithRawResponse,
    BatimentGroupeRncResourceWithStreamingResponse,
    AsyncBatimentGroupeRncResourceWithStreamingResponse,
)
from .batiment_groupe_hthd import (
    BatimentGroupeHthdResource,
    AsyncBatimentGroupeHthdResource,
    BatimentGroupeHthdResourceWithRawResponse,
    AsyncBatimentGroupeHthdResourceWithRawResponse,
    BatimentGroupeHthdResourceWithStreamingResponse,
    AsyncBatimentGroupeHthdResourceWithStreamingResponse,
)
from .batiment_groupe_radon import (
    BatimentGroupeRadonResource,
    AsyncBatimentGroupeRadonResource,
    BatimentGroupeRadonResourceWithRawResponse,
    AsyncBatimentGroupeRadonResourceWithRawResponse,
    BatimentGroupeRadonResourceWithStreamingResponse,
    AsyncBatimentGroupeRadonResourceWithStreamingResponse,
)
from .batiment_groupe_geospx import (
    BatimentGroupeGeospxResource,
    AsyncBatimentGroupeGeospxResource,
    BatimentGroupeGeospxResourceWithRawResponse,
    AsyncBatimentGroupeGeospxResourceWithRawResponse,
    BatimentGroupeGeospxResourceWithStreamingResponse,
    AsyncBatimentGroupeGeospxResourceWithStreamingResponse,
)
from .batiments_construction import (
    BatimentsConstructionResource,
    AsyncBatimentsConstructionResource,
    BatimentsConstructionResourceWithRawResponse,
    AsyncBatimentsConstructionResourceWithRawResponse,
    BatimentsConstructionResourceWithStreamingResponse,
    AsyncBatimentsConstructionResourceWithStreamingResponse,
)
from .batiment_groupe_adresse import (
    BatimentGroupeAdresseResource,
    AsyncBatimentGroupeAdresseResource,
    BatimentGroupeAdresseResourceWithRawResponse,
    AsyncBatimentGroupeAdresseResourceWithRawResponse,
    BatimentGroupeAdresseResourceWithStreamingResponse,
    AsyncBatimentGroupeAdresseResourceWithStreamingResponse,
)
from .batiment_groupe_argiles import (
    BatimentGroupeArgilesResource,
    AsyncBatimentGroupeArgilesResource,
    BatimentGroupeArgilesResourceWithRawResponse,
    AsyncBatimentGroupeArgilesResourceWithRawResponse,
    BatimentGroupeArgilesResourceWithStreamingResponse,
    AsyncBatimentGroupeArgilesResourceWithStreamingResponse,
)
from .batiment_groupe_complet import (
    BatimentGroupeCompletResource,
    AsyncBatimentGroupeCompletResource,
    BatimentGroupeCompletResourceWithRawResponse,
    AsyncBatimentGroupeCompletResourceWithRawResponse,
    BatimentGroupeCompletResourceWithStreamingResponse,
    AsyncBatimentGroupeCompletResourceWithStreamingResponse,
)
from .batiment_groupe_ffo_bat import (
    BatimentGroupeFfoBatResource,
    AsyncBatimentGroupeFfoBatResource,
    BatimentGroupeFfoBatResourceWithRawResponse,
    AsyncBatimentGroupeFfoBatResourceWithRawResponse,
    BatimentGroupeFfoBatResourceWithStreamingResponse,
    AsyncBatimentGroupeFfoBatResourceWithStreamingResponse,
)
from .batiment_groupe_merimee import (
    BatimentGroupeMerimeeResource,
    AsyncBatimentGroupeMerimeeResource,
    BatimentGroupeMerimeeResourceWithRawResponse,
    AsyncBatimentGroupeMerimeeResourceWithRawResponse,
    BatimentGroupeMerimeeResourceWithStreamingResponse,
    AsyncBatimentGroupeMerimeeResourceWithStreamingResponse,
)
from .rel_batiment_groupe_qpv import (
    RelBatimentGroupeQpvResource,
    AsyncRelBatimentGroupeQpvResource,
    RelBatimentGroupeQpvResourceWithRawResponse,
    AsyncRelBatimentGroupeQpvResourceWithRawResponse,
    RelBatimentGroupeQpvResourceWithStreamingResponse,
    AsyncRelBatimentGroupeQpvResourceWithStreamingResponse,
)
from .rel_batiment_groupe_rnc import (
    RelBatimentGroupeRncResource,
    AsyncRelBatimentGroupeRncResource,
    RelBatimentGroupeRncResourceWithRawResponse,
    AsyncRelBatimentGroupeRncResourceWithRawResponse,
    RelBatimentGroupeRncResourceWithStreamingResponse,
    AsyncRelBatimentGroupeRncResourceWithStreamingResponse,
)
from .batiment_groupe_wall_dict import (
    BatimentGroupeWallDictResource,
    AsyncBatimentGroupeWallDictResource,
    BatimentGroupeWallDictResourceWithRawResponse,
    AsyncBatimentGroupeWallDictResourceWithRawResponse,
    BatimentGroupeWallDictResourceWithStreamingResponse,
    AsyncBatimentGroupeWallDictResourceWithStreamingResponse,
)
from .referentiel_administratif import (
    ReferentielAdministratifResource,
    AsyncReferentielAdministratifResource,
    ReferentielAdministratifResourceWithRawResponse,
    AsyncReferentielAdministratifResourceWithRawResponse,
    ReferentielAdministratifResourceWithStreamingResponse,
    AsyncReferentielAdministratifResourceWithStreamingResponse,
)
from .batiment_groupe_bdtopo_bat import (
    BatimentGroupeBdtopoBatResource,
    AsyncBatimentGroupeBdtopoBatResource,
    BatimentGroupeBdtopoBatResourceWithRawResponse,
    AsyncBatimentGroupeBdtopoBatResourceWithRawResponse,
    BatimentGroupeBdtopoBatResourceWithStreamingResponse,
    AsyncBatimentGroupeBdtopoBatResourceWithStreamingResponse,
)
from .batiment_groupe_bdtopo_equ import (
    BatimentGroupeBdtopoEquResource,
    AsyncBatimentGroupeBdtopoEquResource,
    BatimentGroupeBdtopoEquResourceWithRawResponse,
    AsyncBatimentGroupeBdtopoEquResourceWithRawResponse,
    BatimentGroupeBdtopoEquResourceWithStreamingResponse,
    AsyncBatimentGroupeBdtopoEquResourceWithStreamingResponse,
)
from .iris_contexte_geographique import (
    IrisContexteGeographiqueResource,
    AsyncIrisContexteGeographiqueResource,
    IrisContexteGeographiqueResourceWithRawResponse,
    AsyncIrisContexteGeographiqueResourceWithRawResponse,
    IrisContexteGeographiqueResourceWithStreamingResponse,
    AsyncIrisContexteGeographiqueResourceWithStreamingResponse,
)
from .batiment_groupe_bdtopo_zoac import (
    BatimentGroupeBdtopoZoacResource,
    AsyncBatimentGroupeBdtopoZoacResource,
    BatimentGroupeBdtopoZoacResourceWithRawResponse,
    AsyncBatimentGroupeBdtopoZoacResourceWithRawResponse,
    BatimentGroupeBdtopoZoacResourceWithStreamingResponse,
    AsyncBatimentGroupeBdtopoZoacResourceWithStreamingResponse,
)
from .rel_batiment_groupe_adresse import (
    RelBatimentGroupeAdresseResource,
    AsyncRelBatimentGroupeAdresseResource,
    RelBatimentGroupeAdresseResourceWithRawResponse,
    AsyncRelBatimentGroupeAdresseResourceWithRawResponse,
    RelBatimentGroupeAdresseResourceWithStreamingResponse,
    AsyncRelBatimentGroupeAdresseResourceWithStreamingResponse,
)
from .rel_batiment_groupe_merimee import (
    RelBatimentGroupeMerimeeResource,
    AsyncRelBatimentGroupeMerimeeResource,
    RelBatimentGroupeMerimeeResourceWithRawResponse,
    AsyncRelBatimentGroupeMerimeeResourceWithRawResponse,
    RelBatimentGroupeMerimeeResourceWithStreamingResponse,
    AsyncRelBatimentGroupeMerimeeResourceWithStreamingResponse,
)
from .batiment_groupe_dle_gaz_2020 import (
    BatimentGroupeDleGaz2020Resource,
    AsyncBatimentGroupeDleGaz2020Resource,
    BatimentGroupeDleGaz2020ResourceWithRawResponse,
    AsyncBatimentGroupeDleGaz2020ResourceWithRawResponse,
    BatimentGroupeDleGaz2020ResourceWithStreamingResponse,
    AsyncBatimentGroupeDleGaz2020ResourceWithStreamingResponse,
)
from .rel_batiment_groupe_parcelle import (
    RelBatimentGroupeParcelleResource,
    AsyncRelBatimentGroupeParcelleResource,
    RelBatimentGroupeParcelleResourceWithRawResponse,
    AsyncRelBatimentGroupeParcelleResourceWithRawResponse,
    RelBatimentGroupeParcelleResourceWithStreamingResponse,
    AsyncRelBatimentGroupeParcelleResourceWithStreamingResponse,
)
from .batiment_groupe_dle_elec_2020 import (
    BatimentGroupeDleElec2020Resource,
    AsyncBatimentGroupeDleElec2020Resource,
    BatimentGroupeDleElec2020ResourceWithRawResponse,
    AsyncBatimentGroupeDleElec2020ResourceWithRawResponse,
    BatimentGroupeDleElec2020ResourceWithStreamingResponse,
    AsyncBatimentGroupeDleElec2020ResourceWithStreamingResponse,
)
from .iris_simulations_valeur_verte import (
    IrisSimulationsValeurVerteResource,
    AsyncIrisSimulationsValeurVerteResource,
    IrisSimulationsValeurVerteResourceWithRawResponse,
    AsyncIrisSimulationsValeurVerteResourceWithRawResponse,
    IrisSimulationsValeurVerteResourceWithStreamingResponse,
    AsyncIrisSimulationsValeurVerteResourceWithStreamingResponse,
)
from .batiment_groupe_simulations_dpe import (
    BatimentGroupeSimulationsDpeResource,
    AsyncBatimentGroupeSimulationsDpeResource,
    BatimentGroupeSimulationsDpeResourceWithRawResponse,
    AsyncBatimentGroupeSimulationsDpeResourceWithRawResponse,
    BatimentGroupeSimulationsDpeResourceWithStreamingResponse,
    AsyncBatimentGroupeSimulationsDpeResourceWithStreamingResponse,
)
from .batiment_groupe_simulations_dvf import (
    BatimentGroupeSimulationsDvfResource,
    AsyncBatimentGroupeSimulationsDvfResource,
    BatimentGroupeSimulationsDvfResourceWithRawResponse,
    AsyncBatimentGroupeSimulationsDvfResourceWithRawResponse,
    BatimentGroupeSimulationsDvfResourceWithStreamingResponse,
    AsyncBatimentGroupeSimulationsDvfResourceWithStreamingResponse,
)
from .batiment_groupe_dle_reseaux_2020 import (
    BatimentGroupeDleReseaux2020Resource,
    AsyncBatimentGroupeDleReseaux2020Resource,
    BatimentGroupeDleReseaux2020ResourceWithRawResponse,
    AsyncBatimentGroupeDleReseaux2020ResourceWithRawResponse,
    BatimentGroupeDleReseaux2020ResourceWithStreamingResponse,
    AsyncBatimentGroupeDleReseaux2020ResourceWithStreamingResponse,
)
from .rel_batiment_construction_adresse import (
    RelBatimentConstructionAdresseResource,
    AsyncRelBatimentConstructionAdresseResource,
    RelBatimentConstructionAdresseResourceWithRawResponse,
    AsyncRelBatimentConstructionAdresseResourceWithRawResponse,
    RelBatimentConstructionAdresseResourceWithStreamingResponse,
    AsyncRelBatimentConstructionAdresseResourceWithStreamingResponse,
)
from .rel_batiment_groupe_siren_complet import (
    RelBatimentGroupeSirenCompletResource,
    AsyncRelBatimentGroupeSirenCompletResource,
    RelBatimentGroupeSirenCompletResourceWithRawResponse,
    AsyncRelBatimentGroupeSirenCompletResourceWithRawResponse,
    RelBatimentGroupeSirenCompletResourceWithStreamingResponse,
    AsyncRelBatimentGroupeSirenCompletResourceWithStreamingResponse,
)
from .rel_batiment_groupe_siret_complet import (
    RelBatimentGroupeSiretCompletResource,
    AsyncRelBatimentGroupeSiretCompletResource,
    RelBatimentGroupeSiretCompletResourceWithRawResponse,
    AsyncRelBatimentGroupeSiretCompletResourceWithRawResponse,
    RelBatimentGroupeSiretCompletResourceWithStreamingResponse,
    AsyncRelBatimentGroupeSiretCompletResourceWithStreamingResponse,
)
from .batiment_groupe_synthese_enveloppe import (
    BatimentGroupeSyntheseEnveloppeResource,
    AsyncBatimentGroupeSyntheseEnveloppeResource,
    BatimentGroupeSyntheseEnveloppeResourceWithRawResponse,
    AsyncBatimentGroupeSyntheseEnveloppeResourceWithRawResponse,
    BatimentGroupeSyntheseEnveloppeResourceWithStreamingResponse,
    AsyncBatimentGroupeSyntheseEnveloppeResourceWithStreamingResponse,
)
from .batiment_groupe_dvf_open_statistique import (
    BatimentGroupeDvfOpenStatistiqueResource,
    AsyncBatimentGroupeDvfOpenStatistiqueResource,
    BatimentGroupeDvfOpenStatistiqueResourceWithRawResponse,
    AsyncBatimentGroupeDvfOpenStatistiqueResourceWithRawResponse,
    BatimentGroupeDvfOpenStatistiqueResourceWithStreamingResponse,
    AsyncBatimentGroupeDvfOpenStatistiqueResourceWithStreamingResponse,
)
from .batiment_groupe_delimitation_enveloppe import (
    BatimentGroupeDelimitationEnveloppeResource,
    AsyncBatimentGroupeDelimitationEnveloppeResource,
    BatimentGroupeDelimitationEnveloppeResourceWithRawResponse,
    AsyncBatimentGroupeDelimitationEnveloppeResourceWithRawResponse,
    BatimentGroupeDelimitationEnveloppeResourceWithStreamingResponse,
    AsyncBatimentGroupeDelimitationEnveloppeResourceWithStreamingResponse,
)
from .batiment_groupe_dle_gaz_multimillesime import (
    BatimentGroupeDleGazMultimillesimeResource,
    AsyncBatimentGroupeDleGazMultimillesimeResource,
    BatimentGroupeDleGazMultimillesimeResourceWithRawResponse,
    AsyncBatimentGroupeDleGazMultimillesimeResourceWithRawResponse,
    BatimentGroupeDleGazMultimillesimeResourceWithStreamingResponse,
    AsyncBatimentGroupeDleGazMultimillesimeResourceWithStreamingResponse,
)
from .batiment_groupe_dvf_open_representatif import (
    BatimentGroupeDvfOpenRepresentatifResource,
    AsyncBatimentGroupeDvfOpenRepresentatifResource,
    BatimentGroupeDvfOpenRepresentatifResourceWithRawResponse,
    AsyncBatimentGroupeDvfOpenRepresentatifResourceWithRawResponse,
    BatimentGroupeDvfOpenRepresentatifResourceWithStreamingResponse,
    AsyncBatimentGroupeDvfOpenRepresentatifResourceWithStreamingResponse,
)
from .rel_batiment_groupe_proprietaire_siren import (
    RelBatimentGroupeProprietaireSirenResource,
    AsyncRelBatimentGroupeProprietaireSirenResource,
    RelBatimentGroupeProprietaireSirenResourceWithRawResponse,
    AsyncRelBatimentGroupeProprietaireSirenResourceWithRawResponse,
    RelBatimentGroupeProprietaireSirenResourceWithStreamingResponse,
    AsyncRelBatimentGroupeProprietaireSirenResourceWithStreamingResponse,
)
from .batiment_groupe_dle_elec_multimillesime import (
    BatimentGroupeDleElecMultimillesimeResource,
    AsyncBatimentGroupeDleElecMultimillesimeResource,
    BatimentGroupeDleElecMultimillesimeResourceWithRawResponse,
    AsyncBatimentGroupeDleElecMultimillesimeResourceWithRawResponse,
    BatimentGroupeDleElecMultimillesimeResourceWithStreamingResponse,
    AsyncBatimentGroupeDleElecMultimillesimeResourceWithStreamingResponse,
)
from .batiment_groupe_dpe_statistique_logement import (
    BatimentGroupeDpeStatistiqueLogementResource,
    AsyncBatimentGroupeDpeStatistiqueLogementResource,
    BatimentGroupeDpeStatistiqueLogementResourceWithRawResponse,
    AsyncBatimentGroupeDpeStatistiqueLogementResourceWithRawResponse,
    BatimentGroupeDpeStatistiqueLogementResourceWithStreamingResponse,
    AsyncBatimentGroupeDpeStatistiqueLogementResourceWithStreamingResponse,
)
from .batiment_groupe_simulations_valeur_verte import (
    BatimentGroupeSimulationsValeurVerteResource,
    AsyncBatimentGroupeSimulationsValeurVerteResource,
    BatimentGroupeSimulationsValeurVerteResourceWithRawResponse,
    AsyncBatimentGroupeSimulationsValeurVerteResourceWithRawResponse,
    BatimentGroupeSimulationsValeurVerteResourceWithStreamingResponse,
    AsyncBatimentGroupeSimulationsValeurVerteResourceWithStreamingResponse,
)
from .batiment_groupe_dle_reseaux_multimillesime import (
    BatimentGroupeDleReseauxMultimillesimeResource,
    AsyncBatimentGroupeDleReseauxMultimillesimeResource,
    BatimentGroupeDleReseauxMultimillesimeResourceWithRawResponse,
    AsyncBatimentGroupeDleReseauxMultimillesimeResourceWithRawResponse,
    BatimentGroupeDleReseauxMultimillesimeResourceWithStreamingResponse,
    AsyncBatimentGroupeDleReseauxMultimillesimeResourceWithStreamingResponse,
)
from .batiment_groupe_dpe_representatif_logement import (
    BatimentGroupeDpeRepresentatifLogementResource,
    AsyncBatimentGroupeDpeRepresentatifLogementResource,
    BatimentGroupeDpeRepresentatifLogementResourceWithRawResponse,
    AsyncBatimentGroupeDpeRepresentatifLogementResourceWithRawResponse,
    BatimentGroupeDpeRepresentatifLogementResourceWithStreamingResponse,
    AsyncBatimentGroupeDpeRepresentatifLogementResourceWithStreamingResponse,
)
from .rel_batiment_groupe_proprietaire_siren_open import (
    RelBatimentGroupeProprietaireSirenOpenResource,
    AsyncRelBatimentGroupeProprietaireSirenOpenResource,
    RelBatimentGroupeProprietaireSirenOpenResourceWithRawResponse,
    AsyncRelBatimentGroupeProprietaireSirenOpenResourceWithRawResponse,
    RelBatimentGroupeProprietaireSirenOpenResourceWithStreamingResponse,
    AsyncRelBatimentGroupeProprietaireSirenOpenResourceWithStreamingResponse,
)
from .batiment_groupe_indicateur_reseau_chaud_froid import (
    BatimentGroupeIndicateurReseauChaudFroidResource,
    AsyncBatimentGroupeIndicateurReseauChaudFroidResource,
    BatimentGroupeIndicateurReseauChaudFroidResourceWithRawResponse,
    AsyncBatimentGroupeIndicateurReseauChaudFroidResourceWithRawResponse,
    BatimentGroupeIndicateurReseauChaudFroidResourceWithStreamingResponse,
    AsyncBatimentGroupeIndicateurReseauChaudFroidResourceWithStreamingResponse,
)
from .batiment_groupe_complet.batiment_groupe_complet import (
    BatimentGroupeCompletResource,
    AsyncBatimentGroupeCompletResource,
)
from .referentiel_administratif.referentiel_administratif import (
    ReferentielAdministratifResource,
    AsyncReferentielAdministratifResource,
)

__all__ = ["DonneesResource", "AsyncDonneesResource"]


class DonneesResource(SyncAPIResource):
    @cached_property
    def batiment_groupe_complet(self) -> BatimentGroupeCompletResource:
        return BatimentGroupeCompletResource(self._client)

    @cached_property
    def batiments_construction(self) -> BatimentsConstructionResource:
        return BatimentsConstructionResource(self._client)

    @cached_property
    def batiment_groupe_bdtopo_zoac(self) -> BatimentGroupeBdtopoZoacResource:
        return BatimentGroupeBdtopoZoacResource(self._client)

    @cached_property
    def batiment_groupe_geospx(self) -> BatimentGroupeGeospxResource:
        return BatimentGroupeGeospxResource(self._client)

    @cached_property
    def rel_batiment_groupe_proprietaire_siren(self) -> RelBatimentGroupeProprietaireSirenResource:
        return RelBatimentGroupeProprietaireSirenResource(self._client)

    @cached_property
    def batiment_groupe_dvf_open_statistique(self) -> BatimentGroupeDvfOpenStatistiqueResource:
        return BatimentGroupeDvfOpenStatistiqueResource(self._client)

    @cached_property
    def rel_batiment_groupe_qpv(self) -> RelBatimentGroupeQpvResource:
        return RelBatimentGroupeQpvResource(self._client)

    @cached_property
    def batiment_groupe_qpv(self) -> BatimentGroupeQpvResource:
        return BatimentGroupeQpvResource(self._client)

    @cached_property
    def rel_batiment_construction_adresse(self) -> RelBatimentConstructionAdresseResource:
        return RelBatimentConstructionAdresseResource(self._client)

    @cached_property
    def rel_batiment_groupe_adresse(self) -> RelBatimentGroupeAdresseResource:
        return RelBatimentGroupeAdresseResource(self._client)

    @cached_property
    def batiment_groupe_synthese_enveloppe(self) -> BatimentGroupeSyntheseEnveloppeResource:
        return BatimentGroupeSyntheseEnveloppeResource(self._client)

    @cached_property
    def batiment_groupe_simulations_dpe(self) -> BatimentGroupeSimulationsDpeResource:
        return BatimentGroupeSimulationsDpeResource(self._client)

    @cached_property
    def batiment_groupe_bdtopo_equ(self) -> BatimentGroupeBdtopoEquResource:
        return BatimentGroupeBdtopoEquResource(self._client)

    @cached_property
    def batiment_groupe_dpe_representatif_logement(self) -> BatimentGroupeDpeRepresentatifLogementResource:
        return BatimentGroupeDpeRepresentatifLogementResource(self._client)

    @cached_property
    def batiment_groupe_dle_gaz_2020(self) -> BatimentGroupeDleGaz2020Resource:
        return BatimentGroupeDleGaz2020Resource(self._client)

    @cached_property
    def batiment_groupe(self) -> BatimentGroupeResource:
        return BatimentGroupeResource(self._client)

    @cached_property
    def rel_batiment_groupe_merimee(self) -> RelBatimentGroupeMerimeeResource:
        return RelBatimentGroupeMerimeeResource(self._client)

    @cached_property
    def batiment_groupe_dle_elec_2020(self) -> BatimentGroupeDleElec2020Resource:
        return BatimentGroupeDleElec2020Resource(self._client)

    @cached_property
    def batiment_groupe_merimee(self) -> BatimentGroupeMerimeeResource:
        return BatimentGroupeMerimeeResource(self._client)

    @cached_property
    def batiment_groupe_dle_reseaux_2020(self) -> BatimentGroupeDleReseaux2020Resource:
        return BatimentGroupeDleReseaux2020Resource(self._client)

    @cached_property
    def ancqpv(self) -> AncqpvResource:
        return AncqpvResource(self._client)

    @cached_property
    def batiment_groupe_adresse(self) -> BatimentGroupeAdresseResource:
        return BatimentGroupeAdresseResource(self._client)

    @cached_property
    def batiment_groupe_dle_gaz_multimillesime(self) -> BatimentGroupeDleGazMultimillesimeResource:
        return BatimentGroupeDleGazMultimillesimeResource(self._client)

    @cached_property
    def rel_batiment_groupe_parcelle(self) -> RelBatimentGroupeParcelleResource:
        return RelBatimentGroupeParcelleResource(self._client)

    @cached_property
    def batiment_groupe_radon(self) -> BatimentGroupeRadonResource:
        return BatimentGroupeRadonResource(self._client)

    @cached_property
    def batiment_groupe_dvf_open_representatif(self) -> BatimentGroupeDvfOpenRepresentatifResource:
        return BatimentGroupeDvfOpenRepresentatifResource(self._client)

    @cached_property
    def batiment_groupe_simulations_dvf(self) -> BatimentGroupeSimulationsDvfResource:
        return BatimentGroupeSimulationsDvfResource(self._client)

    @cached_property
    def batiment_groupe_dpe_statistique_logement(self) -> BatimentGroupeDpeStatistiqueLogementResource:
        return BatimentGroupeDpeStatistiqueLogementResource(self._client)

    @cached_property
    def iris_simulations_valeur_verte(self) -> IrisSimulationsValeurVerteResource:
        return IrisSimulationsValeurVerteResource(self._client)

    @cached_property
    def iris_contexte_geographique(self) -> IrisContexteGeographiqueResource:
        return IrisContexteGeographiqueResource(self._client)

    @cached_property
    def rel_batiment_groupe_siren_complet(self) -> RelBatimentGroupeSirenCompletResource:
        return RelBatimentGroupeSirenCompletResource(self._client)

    @cached_property
    def rel_batiment_groupe_siret_complet(self) -> RelBatimentGroupeSiretCompletResource:
        return RelBatimentGroupeSiretCompletResource(self._client)

    @cached_property
    def batiment_groupe_dle_reseaux_multimillesime(self) -> BatimentGroupeDleReseauxMultimillesimeResource:
        return BatimentGroupeDleReseauxMultimillesimeResource(self._client)

    @cached_property
    def batiment_groupe_rnc(self) -> BatimentGroupeRncResource:
        return BatimentGroupeRncResource(self._client)

    @cached_property
    def batiment_groupe_bpe(self) -> BatimentGroupeBpeResource:
        return BatimentGroupeBpeResource(self._client)

    @cached_property
    def batiment_groupe_ffo_bat(self) -> BatimentGroupeFfoBatResource:
        return BatimentGroupeFfoBatResource(self._client)

    @cached_property
    def rel_batiment_groupe_rnc(self) -> RelBatimentGroupeRncResource:
        return RelBatimentGroupeRncResource(self._client)

    @cached_property
    def batiment_groupe_argiles(self) -> BatimentGroupeArgilesResource:
        return BatimentGroupeArgilesResource(self._client)

    @cached_property
    def batiment_groupe_hthd(self) -> BatimentGroupeHthdResource:
        return BatimentGroupeHthdResource(self._client)

    @cached_property
    def proprietaire(self) -> ProprietaireResource:
        return ProprietaireResource(self._client)

    @cached_property
    def batiment_groupe_bdtopo_bat(self) -> BatimentGroupeBdtopoBatResource:
        return BatimentGroupeBdtopoBatResource(self._client)

    @cached_property
    def rel_batiment_groupe_proprietaire_siren_open(self) -> RelBatimentGroupeProprietaireSirenOpenResource:
        return RelBatimentGroupeProprietaireSirenOpenResource(self._client)

    @cached_property
    def batiment_groupe_dle_elec_multimillesime(self) -> BatimentGroupeDleElecMultimillesimeResource:
        return BatimentGroupeDleElecMultimillesimeResource(self._client)

    @cached_property
    def adresse(self) -> AdresseResource:
        return AdresseResource(self._client)

    @cached_property
    def batiment_groupe_wall_dict(self) -> BatimentGroupeWallDictResource:
        return BatimentGroupeWallDictResource(self._client)

    @cached_property
    def batiment_groupe_indicateur_reseau_chaud_froid(self) -> BatimentGroupeIndicateurReseauChaudFroidResource:
        return BatimentGroupeIndicateurReseauChaudFroidResource(self._client)

    @cached_property
    def batiment_groupe_delimitation_enveloppe(self) -> BatimentGroupeDelimitationEnveloppeResource:
        return BatimentGroupeDelimitationEnveloppeResource(self._client)

    @cached_property
    def batiment_groupe_simulations_valeur_verte(self) -> BatimentGroupeSimulationsValeurVerteResource:
        return BatimentGroupeSimulationsValeurVerteResource(self._client)

    @cached_property
    def referentiel_administratif(self) -> ReferentielAdministratifResource:
        return ReferentielAdministratifResource(self._client)

    @cached_property
    def with_raw_response(self) -> DonneesResourceWithRawResponse:
        return DonneesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DonneesResourceWithStreamingResponse:
        return DonneesResourceWithStreamingResponse(self)


class AsyncDonneesResource(AsyncAPIResource):
    @cached_property
    def batiment_groupe_complet(self) -> AsyncBatimentGroupeCompletResource:
        return AsyncBatimentGroupeCompletResource(self._client)

    @cached_property
    def batiments_construction(self) -> AsyncBatimentsConstructionResource:
        return AsyncBatimentsConstructionResource(self._client)

    @cached_property
    def batiment_groupe_bdtopo_zoac(self) -> AsyncBatimentGroupeBdtopoZoacResource:
        return AsyncBatimentGroupeBdtopoZoacResource(self._client)

    @cached_property
    def batiment_groupe_geospx(self) -> AsyncBatimentGroupeGeospxResource:
        return AsyncBatimentGroupeGeospxResource(self._client)

    @cached_property
    def rel_batiment_groupe_proprietaire_siren(self) -> AsyncRelBatimentGroupeProprietaireSirenResource:
        return AsyncRelBatimentGroupeProprietaireSirenResource(self._client)

    @cached_property
    def batiment_groupe_dvf_open_statistique(self) -> AsyncBatimentGroupeDvfOpenStatistiqueResource:
        return AsyncBatimentGroupeDvfOpenStatistiqueResource(self._client)

    @cached_property
    def rel_batiment_groupe_qpv(self) -> AsyncRelBatimentGroupeQpvResource:
        return AsyncRelBatimentGroupeQpvResource(self._client)

    @cached_property
    def batiment_groupe_qpv(self) -> AsyncBatimentGroupeQpvResource:
        return AsyncBatimentGroupeQpvResource(self._client)

    @cached_property
    def rel_batiment_construction_adresse(self) -> AsyncRelBatimentConstructionAdresseResource:
        return AsyncRelBatimentConstructionAdresseResource(self._client)

    @cached_property
    def rel_batiment_groupe_adresse(self) -> AsyncRelBatimentGroupeAdresseResource:
        return AsyncRelBatimentGroupeAdresseResource(self._client)

    @cached_property
    def batiment_groupe_synthese_enveloppe(self) -> AsyncBatimentGroupeSyntheseEnveloppeResource:
        return AsyncBatimentGroupeSyntheseEnveloppeResource(self._client)

    @cached_property
    def batiment_groupe_simulations_dpe(self) -> AsyncBatimentGroupeSimulationsDpeResource:
        return AsyncBatimentGroupeSimulationsDpeResource(self._client)

    @cached_property
    def batiment_groupe_bdtopo_equ(self) -> AsyncBatimentGroupeBdtopoEquResource:
        return AsyncBatimentGroupeBdtopoEquResource(self._client)

    @cached_property
    def batiment_groupe_dpe_representatif_logement(self) -> AsyncBatimentGroupeDpeRepresentatifLogementResource:
        return AsyncBatimentGroupeDpeRepresentatifLogementResource(self._client)

    @cached_property
    def batiment_groupe_dle_gaz_2020(self) -> AsyncBatimentGroupeDleGaz2020Resource:
        return AsyncBatimentGroupeDleGaz2020Resource(self._client)

    @cached_property
    def batiment_groupe(self) -> AsyncBatimentGroupeResource:
        return AsyncBatimentGroupeResource(self._client)

    @cached_property
    def rel_batiment_groupe_merimee(self) -> AsyncRelBatimentGroupeMerimeeResource:
        return AsyncRelBatimentGroupeMerimeeResource(self._client)

    @cached_property
    def batiment_groupe_dle_elec_2020(self) -> AsyncBatimentGroupeDleElec2020Resource:
        return AsyncBatimentGroupeDleElec2020Resource(self._client)

    @cached_property
    def batiment_groupe_merimee(self) -> AsyncBatimentGroupeMerimeeResource:
        return AsyncBatimentGroupeMerimeeResource(self._client)

    @cached_property
    def batiment_groupe_dle_reseaux_2020(self) -> AsyncBatimentGroupeDleReseaux2020Resource:
        return AsyncBatimentGroupeDleReseaux2020Resource(self._client)

    @cached_property
    def ancqpv(self) -> AsyncAncqpvResource:
        return AsyncAncqpvResource(self._client)

    @cached_property
    def batiment_groupe_adresse(self) -> AsyncBatimentGroupeAdresseResource:
        return AsyncBatimentGroupeAdresseResource(self._client)

    @cached_property
    def batiment_groupe_dle_gaz_multimillesime(self) -> AsyncBatimentGroupeDleGazMultimillesimeResource:
        return AsyncBatimentGroupeDleGazMultimillesimeResource(self._client)

    @cached_property
    def rel_batiment_groupe_parcelle(self) -> AsyncRelBatimentGroupeParcelleResource:
        return AsyncRelBatimentGroupeParcelleResource(self._client)

    @cached_property
    def batiment_groupe_radon(self) -> AsyncBatimentGroupeRadonResource:
        return AsyncBatimentGroupeRadonResource(self._client)

    @cached_property
    def batiment_groupe_dvf_open_representatif(self) -> AsyncBatimentGroupeDvfOpenRepresentatifResource:
        return AsyncBatimentGroupeDvfOpenRepresentatifResource(self._client)

    @cached_property
    def batiment_groupe_simulations_dvf(self) -> AsyncBatimentGroupeSimulationsDvfResource:
        return AsyncBatimentGroupeSimulationsDvfResource(self._client)

    @cached_property
    def batiment_groupe_dpe_statistique_logement(self) -> AsyncBatimentGroupeDpeStatistiqueLogementResource:
        return AsyncBatimentGroupeDpeStatistiqueLogementResource(self._client)

    @cached_property
    def iris_simulations_valeur_verte(self) -> AsyncIrisSimulationsValeurVerteResource:
        return AsyncIrisSimulationsValeurVerteResource(self._client)

    @cached_property
    def iris_contexte_geographique(self) -> AsyncIrisContexteGeographiqueResource:
        return AsyncIrisContexteGeographiqueResource(self._client)

    @cached_property
    def rel_batiment_groupe_siren_complet(self) -> AsyncRelBatimentGroupeSirenCompletResource:
        return AsyncRelBatimentGroupeSirenCompletResource(self._client)

    @cached_property
    def rel_batiment_groupe_siret_complet(self) -> AsyncRelBatimentGroupeSiretCompletResource:
        return AsyncRelBatimentGroupeSiretCompletResource(self._client)

    @cached_property
    def batiment_groupe_dle_reseaux_multimillesime(self) -> AsyncBatimentGroupeDleReseauxMultimillesimeResource:
        return AsyncBatimentGroupeDleReseauxMultimillesimeResource(self._client)

    @cached_property
    def batiment_groupe_rnc(self) -> AsyncBatimentGroupeRncResource:
        return AsyncBatimentGroupeRncResource(self._client)

    @cached_property
    def batiment_groupe_bpe(self) -> AsyncBatimentGroupeBpeResource:
        return AsyncBatimentGroupeBpeResource(self._client)

    @cached_property
    def batiment_groupe_ffo_bat(self) -> AsyncBatimentGroupeFfoBatResource:
        return AsyncBatimentGroupeFfoBatResource(self._client)

    @cached_property
    def rel_batiment_groupe_rnc(self) -> AsyncRelBatimentGroupeRncResource:
        return AsyncRelBatimentGroupeRncResource(self._client)

    @cached_property
    def batiment_groupe_argiles(self) -> AsyncBatimentGroupeArgilesResource:
        return AsyncBatimentGroupeArgilesResource(self._client)

    @cached_property
    def batiment_groupe_hthd(self) -> AsyncBatimentGroupeHthdResource:
        return AsyncBatimentGroupeHthdResource(self._client)

    @cached_property
    def proprietaire(self) -> AsyncProprietaireResource:
        return AsyncProprietaireResource(self._client)

    @cached_property
    def batiment_groupe_bdtopo_bat(self) -> AsyncBatimentGroupeBdtopoBatResource:
        return AsyncBatimentGroupeBdtopoBatResource(self._client)

    @cached_property
    def rel_batiment_groupe_proprietaire_siren_open(self) -> AsyncRelBatimentGroupeProprietaireSirenOpenResource:
        return AsyncRelBatimentGroupeProprietaireSirenOpenResource(self._client)

    @cached_property
    def batiment_groupe_dle_elec_multimillesime(self) -> AsyncBatimentGroupeDleElecMultimillesimeResource:
        return AsyncBatimentGroupeDleElecMultimillesimeResource(self._client)

    @cached_property
    def adresse(self) -> AsyncAdresseResource:
        return AsyncAdresseResource(self._client)

    @cached_property
    def batiment_groupe_wall_dict(self) -> AsyncBatimentGroupeWallDictResource:
        return AsyncBatimentGroupeWallDictResource(self._client)

    @cached_property
    def batiment_groupe_indicateur_reseau_chaud_froid(self) -> AsyncBatimentGroupeIndicateurReseauChaudFroidResource:
        return AsyncBatimentGroupeIndicateurReseauChaudFroidResource(self._client)

    @cached_property
    def batiment_groupe_delimitation_enveloppe(self) -> AsyncBatimentGroupeDelimitationEnveloppeResource:
        return AsyncBatimentGroupeDelimitationEnveloppeResource(self._client)

    @cached_property
    def batiment_groupe_simulations_valeur_verte(self) -> AsyncBatimentGroupeSimulationsValeurVerteResource:
        return AsyncBatimentGroupeSimulationsValeurVerteResource(self._client)

    @cached_property
    def referentiel_administratif(self) -> AsyncReferentielAdministratifResource:
        return AsyncReferentielAdministratifResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDonneesResourceWithRawResponse:
        return AsyncDonneesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDonneesResourceWithStreamingResponse:
        return AsyncDonneesResourceWithStreamingResponse(self)


class DonneesResourceWithRawResponse:
    def __init__(self, donnees: DonneesResource) -> None:
        self._donnees = donnees

    @cached_property
    def batiment_groupe_complet(self) -> BatimentGroupeCompletResourceWithRawResponse:
        return BatimentGroupeCompletResourceWithRawResponse(self._donnees.batiment_groupe_complet)

    @cached_property
    def batiments_construction(self) -> BatimentsConstructionResourceWithRawResponse:
        return BatimentsConstructionResourceWithRawResponse(self._donnees.batiments_construction)

    @cached_property
    def batiment_groupe_bdtopo_zoac(self) -> BatimentGroupeBdtopoZoacResourceWithRawResponse:
        return BatimentGroupeBdtopoZoacResourceWithRawResponse(self._donnees.batiment_groupe_bdtopo_zoac)

    @cached_property
    def batiment_groupe_geospx(self) -> BatimentGroupeGeospxResourceWithRawResponse:
        return BatimentGroupeGeospxResourceWithRawResponse(self._donnees.batiment_groupe_geospx)

    @cached_property
    def rel_batiment_groupe_proprietaire_siren(self) -> RelBatimentGroupeProprietaireSirenResourceWithRawResponse:
        return RelBatimentGroupeProprietaireSirenResourceWithRawResponse(
            self._donnees.rel_batiment_groupe_proprietaire_siren
        )

    @cached_property
    def batiment_groupe_dvf_open_statistique(self) -> BatimentGroupeDvfOpenStatistiqueResourceWithRawResponse:
        return BatimentGroupeDvfOpenStatistiqueResourceWithRawResponse(
            self._donnees.batiment_groupe_dvf_open_statistique
        )

    @cached_property
    def rel_batiment_groupe_qpv(self) -> RelBatimentGroupeQpvResourceWithRawResponse:
        return RelBatimentGroupeQpvResourceWithRawResponse(self._donnees.rel_batiment_groupe_qpv)

    @cached_property
    def batiment_groupe_qpv(self) -> BatimentGroupeQpvResourceWithRawResponse:
        return BatimentGroupeQpvResourceWithRawResponse(self._donnees.batiment_groupe_qpv)

    @cached_property
    def rel_batiment_construction_adresse(self) -> RelBatimentConstructionAdresseResourceWithRawResponse:
        return RelBatimentConstructionAdresseResourceWithRawResponse(self._donnees.rel_batiment_construction_adresse)

    @cached_property
    def rel_batiment_groupe_adresse(self) -> RelBatimentGroupeAdresseResourceWithRawResponse:
        return RelBatimentGroupeAdresseResourceWithRawResponse(self._donnees.rel_batiment_groupe_adresse)

    @cached_property
    def batiment_groupe_synthese_enveloppe(self) -> BatimentGroupeSyntheseEnveloppeResourceWithRawResponse:
        return BatimentGroupeSyntheseEnveloppeResourceWithRawResponse(self._donnees.batiment_groupe_synthese_enveloppe)

    @cached_property
    def batiment_groupe_simulations_dpe(self) -> BatimentGroupeSimulationsDpeResourceWithRawResponse:
        return BatimentGroupeSimulationsDpeResourceWithRawResponse(self._donnees.batiment_groupe_simulations_dpe)

    @cached_property
    def batiment_groupe_bdtopo_equ(self) -> BatimentGroupeBdtopoEquResourceWithRawResponse:
        return BatimentGroupeBdtopoEquResourceWithRawResponse(self._donnees.batiment_groupe_bdtopo_equ)

    @cached_property
    def batiment_groupe_dpe_representatif_logement(
        self,
    ) -> BatimentGroupeDpeRepresentatifLogementResourceWithRawResponse:
        return BatimentGroupeDpeRepresentatifLogementResourceWithRawResponse(
            self._donnees.batiment_groupe_dpe_representatif_logement
        )

    @cached_property
    def batiment_groupe_dle_gaz_2020(self) -> BatimentGroupeDleGaz2020ResourceWithRawResponse:
        return BatimentGroupeDleGaz2020ResourceWithRawResponse(self._donnees.batiment_groupe_dle_gaz_2020)

    @cached_property
    def batiment_groupe(self) -> BatimentGroupeResourceWithRawResponse:
        return BatimentGroupeResourceWithRawResponse(self._donnees.batiment_groupe)

    @cached_property
    def rel_batiment_groupe_merimee(self) -> RelBatimentGroupeMerimeeResourceWithRawResponse:
        return RelBatimentGroupeMerimeeResourceWithRawResponse(self._donnees.rel_batiment_groupe_merimee)

    @cached_property
    def batiment_groupe_dle_elec_2020(self) -> BatimentGroupeDleElec2020ResourceWithRawResponse:
        return BatimentGroupeDleElec2020ResourceWithRawResponse(self._donnees.batiment_groupe_dle_elec_2020)

    @cached_property
    def batiment_groupe_merimee(self) -> BatimentGroupeMerimeeResourceWithRawResponse:
        return BatimentGroupeMerimeeResourceWithRawResponse(self._donnees.batiment_groupe_merimee)

    @cached_property
    def batiment_groupe_dle_reseaux_2020(self) -> BatimentGroupeDleReseaux2020ResourceWithRawResponse:
        return BatimentGroupeDleReseaux2020ResourceWithRawResponse(self._donnees.batiment_groupe_dle_reseaux_2020)

    @cached_property
    def ancqpv(self) -> AncqpvResourceWithRawResponse:
        return AncqpvResourceWithRawResponse(self._donnees.ancqpv)

    @cached_property
    def batiment_groupe_adresse(self) -> BatimentGroupeAdresseResourceWithRawResponse:
        return BatimentGroupeAdresseResourceWithRawResponse(self._donnees.batiment_groupe_adresse)

    @cached_property
    def batiment_groupe_dle_gaz_multimillesime(self) -> BatimentGroupeDleGazMultimillesimeResourceWithRawResponse:
        return BatimentGroupeDleGazMultimillesimeResourceWithRawResponse(
            self._donnees.batiment_groupe_dle_gaz_multimillesime
        )

    @cached_property
    def rel_batiment_groupe_parcelle(self) -> RelBatimentGroupeParcelleResourceWithRawResponse:
        return RelBatimentGroupeParcelleResourceWithRawResponse(self._donnees.rel_batiment_groupe_parcelle)

    @cached_property
    def batiment_groupe_radon(self) -> BatimentGroupeRadonResourceWithRawResponse:
        return BatimentGroupeRadonResourceWithRawResponse(self._donnees.batiment_groupe_radon)

    @cached_property
    def batiment_groupe_dvf_open_representatif(self) -> BatimentGroupeDvfOpenRepresentatifResourceWithRawResponse:
        return BatimentGroupeDvfOpenRepresentatifResourceWithRawResponse(
            self._donnees.batiment_groupe_dvf_open_representatif
        )

    @cached_property
    def batiment_groupe_simulations_dvf(self) -> BatimentGroupeSimulationsDvfResourceWithRawResponse:
        return BatimentGroupeSimulationsDvfResourceWithRawResponse(self._donnees.batiment_groupe_simulations_dvf)

    @cached_property
    def batiment_groupe_dpe_statistique_logement(self) -> BatimentGroupeDpeStatistiqueLogementResourceWithRawResponse:
        return BatimentGroupeDpeStatistiqueLogementResourceWithRawResponse(
            self._donnees.batiment_groupe_dpe_statistique_logement
        )

    @cached_property
    def iris_simulations_valeur_verte(self) -> IrisSimulationsValeurVerteResourceWithRawResponse:
        return IrisSimulationsValeurVerteResourceWithRawResponse(self._donnees.iris_simulations_valeur_verte)

    @cached_property
    def iris_contexte_geographique(self) -> IrisContexteGeographiqueResourceWithRawResponse:
        return IrisContexteGeographiqueResourceWithRawResponse(self._donnees.iris_contexte_geographique)

    @cached_property
    def rel_batiment_groupe_siren_complet(self) -> RelBatimentGroupeSirenCompletResourceWithRawResponse:
        return RelBatimentGroupeSirenCompletResourceWithRawResponse(self._donnees.rel_batiment_groupe_siren_complet)

    @cached_property
    def rel_batiment_groupe_siret_complet(self) -> RelBatimentGroupeSiretCompletResourceWithRawResponse:
        return RelBatimentGroupeSiretCompletResourceWithRawResponse(self._donnees.rel_batiment_groupe_siret_complet)

    @cached_property
    def batiment_groupe_dle_reseaux_multimillesime(
        self,
    ) -> BatimentGroupeDleReseauxMultimillesimeResourceWithRawResponse:
        return BatimentGroupeDleReseauxMultimillesimeResourceWithRawResponse(
            self._donnees.batiment_groupe_dle_reseaux_multimillesime
        )

    @cached_property
    def batiment_groupe_rnc(self) -> BatimentGroupeRncResourceWithRawResponse:
        return BatimentGroupeRncResourceWithRawResponse(self._donnees.batiment_groupe_rnc)

    @cached_property
    def batiment_groupe_bpe(self) -> BatimentGroupeBpeResourceWithRawResponse:
        return BatimentGroupeBpeResourceWithRawResponse(self._donnees.batiment_groupe_bpe)

    @cached_property
    def batiment_groupe_ffo_bat(self) -> BatimentGroupeFfoBatResourceWithRawResponse:
        return BatimentGroupeFfoBatResourceWithRawResponse(self._donnees.batiment_groupe_ffo_bat)

    @cached_property
    def rel_batiment_groupe_rnc(self) -> RelBatimentGroupeRncResourceWithRawResponse:
        return RelBatimentGroupeRncResourceWithRawResponse(self._donnees.rel_batiment_groupe_rnc)

    @cached_property
    def batiment_groupe_argiles(self) -> BatimentGroupeArgilesResourceWithRawResponse:
        return BatimentGroupeArgilesResourceWithRawResponse(self._donnees.batiment_groupe_argiles)

    @cached_property
    def batiment_groupe_hthd(self) -> BatimentGroupeHthdResourceWithRawResponse:
        return BatimentGroupeHthdResourceWithRawResponse(self._donnees.batiment_groupe_hthd)

    @cached_property
    def proprietaire(self) -> ProprietaireResourceWithRawResponse:
        return ProprietaireResourceWithRawResponse(self._donnees.proprietaire)

    @cached_property
    def batiment_groupe_bdtopo_bat(self) -> BatimentGroupeBdtopoBatResourceWithRawResponse:
        return BatimentGroupeBdtopoBatResourceWithRawResponse(self._donnees.batiment_groupe_bdtopo_bat)

    @cached_property
    def rel_batiment_groupe_proprietaire_siren_open(
        self,
    ) -> RelBatimentGroupeProprietaireSirenOpenResourceWithRawResponse:
        return RelBatimentGroupeProprietaireSirenOpenResourceWithRawResponse(
            self._donnees.rel_batiment_groupe_proprietaire_siren_open
        )

    @cached_property
    def batiment_groupe_dle_elec_multimillesime(self) -> BatimentGroupeDleElecMultimillesimeResourceWithRawResponse:
        return BatimentGroupeDleElecMultimillesimeResourceWithRawResponse(
            self._donnees.batiment_groupe_dle_elec_multimillesime
        )

    @cached_property
    def adresse(self) -> AdresseResourceWithRawResponse:
        return AdresseResourceWithRawResponse(self._donnees.adresse)

    @cached_property
    def batiment_groupe_wall_dict(self) -> BatimentGroupeWallDictResourceWithRawResponse:
        return BatimentGroupeWallDictResourceWithRawResponse(self._donnees.batiment_groupe_wall_dict)

    @cached_property
    def batiment_groupe_indicateur_reseau_chaud_froid(
        self,
    ) -> BatimentGroupeIndicateurReseauChaudFroidResourceWithRawResponse:
        return BatimentGroupeIndicateurReseauChaudFroidResourceWithRawResponse(
            self._donnees.batiment_groupe_indicateur_reseau_chaud_froid
        )

    @cached_property
    def batiment_groupe_delimitation_enveloppe(self) -> BatimentGroupeDelimitationEnveloppeResourceWithRawResponse:
        return BatimentGroupeDelimitationEnveloppeResourceWithRawResponse(
            self._donnees.batiment_groupe_delimitation_enveloppe
        )

    @cached_property
    def batiment_groupe_simulations_valeur_verte(self) -> BatimentGroupeSimulationsValeurVerteResourceWithRawResponse:
        return BatimentGroupeSimulationsValeurVerteResourceWithRawResponse(
            self._donnees.batiment_groupe_simulations_valeur_verte
        )

    @cached_property
    def referentiel_administratif(self) -> ReferentielAdministratifResourceWithRawResponse:
        return ReferentielAdministratifResourceWithRawResponse(self._donnees.referentiel_administratif)


class AsyncDonneesResourceWithRawResponse:
    def __init__(self, donnees: AsyncDonneesResource) -> None:
        self._donnees = donnees

    @cached_property
    def batiment_groupe_complet(self) -> AsyncBatimentGroupeCompletResourceWithRawResponse:
        return AsyncBatimentGroupeCompletResourceWithRawResponse(self._donnees.batiment_groupe_complet)

    @cached_property
    def batiments_construction(self) -> AsyncBatimentsConstructionResourceWithRawResponse:
        return AsyncBatimentsConstructionResourceWithRawResponse(self._donnees.batiments_construction)

    @cached_property
    def batiment_groupe_bdtopo_zoac(self) -> AsyncBatimentGroupeBdtopoZoacResourceWithRawResponse:
        return AsyncBatimentGroupeBdtopoZoacResourceWithRawResponse(self._donnees.batiment_groupe_bdtopo_zoac)

    @cached_property
    def batiment_groupe_geospx(self) -> AsyncBatimentGroupeGeospxResourceWithRawResponse:
        return AsyncBatimentGroupeGeospxResourceWithRawResponse(self._donnees.batiment_groupe_geospx)

    @cached_property
    def rel_batiment_groupe_proprietaire_siren(self) -> AsyncRelBatimentGroupeProprietaireSirenResourceWithRawResponse:
        return AsyncRelBatimentGroupeProprietaireSirenResourceWithRawResponse(
            self._donnees.rel_batiment_groupe_proprietaire_siren
        )

    @cached_property
    def batiment_groupe_dvf_open_statistique(self) -> AsyncBatimentGroupeDvfOpenStatistiqueResourceWithRawResponse:
        return AsyncBatimentGroupeDvfOpenStatistiqueResourceWithRawResponse(
            self._donnees.batiment_groupe_dvf_open_statistique
        )

    @cached_property
    def rel_batiment_groupe_qpv(self) -> AsyncRelBatimentGroupeQpvResourceWithRawResponse:
        return AsyncRelBatimentGroupeQpvResourceWithRawResponse(self._donnees.rel_batiment_groupe_qpv)

    @cached_property
    def batiment_groupe_qpv(self) -> AsyncBatimentGroupeQpvResourceWithRawResponse:
        return AsyncBatimentGroupeQpvResourceWithRawResponse(self._donnees.batiment_groupe_qpv)

    @cached_property
    def rel_batiment_construction_adresse(self) -> AsyncRelBatimentConstructionAdresseResourceWithRawResponse:
        return AsyncRelBatimentConstructionAdresseResourceWithRawResponse(
            self._donnees.rel_batiment_construction_adresse
        )

    @cached_property
    def rel_batiment_groupe_adresse(self) -> AsyncRelBatimentGroupeAdresseResourceWithRawResponse:
        return AsyncRelBatimentGroupeAdresseResourceWithRawResponse(self._donnees.rel_batiment_groupe_adresse)

    @cached_property
    def batiment_groupe_synthese_enveloppe(self) -> AsyncBatimentGroupeSyntheseEnveloppeResourceWithRawResponse:
        return AsyncBatimentGroupeSyntheseEnveloppeResourceWithRawResponse(
            self._donnees.batiment_groupe_synthese_enveloppe
        )

    @cached_property
    def batiment_groupe_simulations_dpe(self) -> AsyncBatimentGroupeSimulationsDpeResourceWithRawResponse:
        return AsyncBatimentGroupeSimulationsDpeResourceWithRawResponse(self._donnees.batiment_groupe_simulations_dpe)

    @cached_property
    def batiment_groupe_bdtopo_equ(self) -> AsyncBatimentGroupeBdtopoEquResourceWithRawResponse:
        return AsyncBatimentGroupeBdtopoEquResourceWithRawResponse(self._donnees.batiment_groupe_bdtopo_equ)

    @cached_property
    def batiment_groupe_dpe_representatif_logement(
        self,
    ) -> AsyncBatimentGroupeDpeRepresentatifLogementResourceWithRawResponse:
        return AsyncBatimentGroupeDpeRepresentatifLogementResourceWithRawResponse(
            self._donnees.batiment_groupe_dpe_representatif_logement
        )

    @cached_property
    def batiment_groupe_dle_gaz_2020(self) -> AsyncBatimentGroupeDleGaz2020ResourceWithRawResponse:
        return AsyncBatimentGroupeDleGaz2020ResourceWithRawResponse(self._donnees.batiment_groupe_dle_gaz_2020)

    @cached_property
    def batiment_groupe(self) -> AsyncBatimentGroupeResourceWithRawResponse:
        return AsyncBatimentGroupeResourceWithRawResponse(self._donnees.batiment_groupe)

    @cached_property
    def rel_batiment_groupe_merimee(self) -> AsyncRelBatimentGroupeMerimeeResourceWithRawResponse:
        return AsyncRelBatimentGroupeMerimeeResourceWithRawResponse(self._donnees.rel_batiment_groupe_merimee)

    @cached_property
    def batiment_groupe_dle_elec_2020(self) -> AsyncBatimentGroupeDleElec2020ResourceWithRawResponse:
        return AsyncBatimentGroupeDleElec2020ResourceWithRawResponse(self._donnees.batiment_groupe_dle_elec_2020)

    @cached_property
    def batiment_groupe_merimee(self) -> AsyncBatimentGroupeMerimeeResourceWithRawResponse:
        return AsyncBatimentGroupeMerimeeResourceWithRawResponse(self._donnees.batiment_groupe_merimee)

    @cached_property
    def batiment_groupe_dle_reseaux_2020(self) -> AsyncBatimentGroupeDleReseaux2020ResourceWithRawResponse:
        return AsyncBatimentGroupeDleReseaux2020ResourceWithRawResponse(self._donnees.batiment_groupe_dle_reseaux_2020)

    @cached_property
    def ancqpv(self) -> AsyncAncqpvResourceWithRawResponse:
        return AsyncAncqpvResourceWithRawResponse(self._donnees.ancqpv)

    @cached_property
    def batiment_groupe_adresse(self) -> AsyncBatimentGroupeAdresseResourceWithRawResponse:
        return AsyncBatimentGroupeAdresseResourceWithRawResponse(self._donnees.batiment_groupe_adresse)

    @cached_property
    def batiment_groupe_dle_gaz_multimillesime(self) -> AsyncBatimentGroupeDleGazMultimillesimeResourceWithRawResponse:
        return AsyncBatimentGroupeDleGazMultimillesimeResourceWithRawResponse(
            self._donnees.batiment_groupe_dle_gaz_multimillesime
        )

    @cached_property
    def rel_batiment_groupe_parcelle(self) -> AsyncRelBatimentGroupeParcelleResourceWithRawResponse:
        return AsyncRelBatimentGroupeParcelleResourceWithRawResponse(self._donnees.rel_batiment_groupe_parcelle)

    @cached_property
    def batiment_groupe_radon(self) -> AsyncBatimentGroupeRadonResourceWithRawResponse:
        return AsyncBatimentGroupeRadonResourceWithRawResponse(self._donnees.batiment_groupe_radon)

    @cached_property
    def batiment_groupe_dvf_open_representatif(self) -> AsyncBatimentGroupeDvfOpenRepresentatifResourceWithRawResponse:
        return AsyncBatimentGroupeDvfOpenRepresentatifResourceWithRawResponse(
            self._donnees.batiment_groupe_dvf_open_representatif
        )

    @cached_property
    def batiment_groupe_simulations_dvf(self) -> AsyncBatimentGroupeSimulationsDvfResourceWithRawResponse:
        return AsyncBatimentGroupeSimulationsDvfResourceWithRawResponse(self._donnees.batiment_groupe_simulations_dvf)

    @cached_property
    def batiment_groupe_dpe_statistique_logement(
        self,
    ) -> AsyncBatimentGroupeDpeStatistiqueLogementResourceWithRawResponse:
        return AsyncBatimentGroupeDpeStatistiqueLogementResourceWithRawResponse(
            self._donnees.batiment_groupe_dpe_statistique_logement
        )

    @cached_property
    def iris_simulations_valeur_verte(self) -> AsyncIrisSimulationsValeurVerteResourceWithRawResponse:
        return AsyncIrisSimulationsValeurVerteResourceWithRawResponse(self._donnees.iris_simulations_valeur_verte)

    @cached_property
    def iris_contexte_geographique(self) -> AsyncIrisContexteGeographiqueResourceWithRawResponse:
        return AsyncIrisContexteGeographiqueResourceWithRawResponse(self._donnees.iris_contexte_geographique)

    @cached_property
    def rel_batiment_groupe_siren_complet(self) -> AsyncRelBatimentGroupeSirenCompletResourceWithRawResponse:
        return AsyncRelBatimentGroupeSirenCompletResourceWithRawResponse(
            self._donnees.rel_batiment_groupe_siren_complet
        )

    @cached_property
    def rel_batiment_groupe_siret_complet(self) -> AsyncRelBatimentGroupeSiretCompletResourceWithRawResponse:
        return AsyncRelBatimentGroupeSiretCompletResourceWithRawResponse(
            self._donnees.rel_batiment_groupe_siret_complet
        )

    @cached_property
    def batiment_groupe_dle_reseaux_multimillesime(
        self,
    ) -> AsyncBatimentGroupeDleReseauxMultimillesimeResourceWithRawResponse:
        return AsyncBatimentGroupeDleReseauxMultimillesimeResourceWithRawResponse(
            self._donnees.batiment_groupe_dle_reseaux_multimillesime
        )

    @cached_property
    def batiment_groupe_rnc(self) -> AsyncBatimentGroupeRncResourceWithRawResponse:
        return AsyncBatimentGroupeRncResourceWithRawResponse(self._donnees.batiment_groupe_rnc)

    @cached_property
    def batiment_groupe_bpe(self) -> AsyncBatimentGroupeBpeResourceWithRawResponse:
        return AsyncBatimentGroupeBpeResourceWithRawResponse(self._donnees.batiment_groupe_bpe)

    @cached_property
    def batiment_groupe_ffo_bat(self) -> AsyncBatimentGroupeFfoBatResourceWithRawResponse:
        return AsyncBatimentGroupeFfoBatResourceWithRawResponse(self._donnees.batiment_groupe_ffo_bat)

    @cached_property
    def rel_batiment_groupe_rnc(self) -> AsyncRelBatimentGroupeRncResourceWithRawResponse:
        return AsyncRelBatimentGroupeRncResourceWithRawResponse(self._donnees.rel_batiment_groupe_rnc)

    @cached_property
    def batiment_groupe_argiles(self) -> AsyncBatimentGroupeArgilesResourceWithRawResponse:
        return AsyncBatimentGroupeArgilesResourceWithRawResponse(self._donnees.batiment_groupe_argiles)

    @cached_property
    def batiment_groupe_hthd(self) -> AsyncBatimentGroupeHthdResourceWithRawResponse:
        return AsyncBatimentGroupeHthdResourceWithRawResponse(self._donnees.batiment_groupe_hthd)

    @cached_property
    def proprietaire(self) -> AsyncProprietaireResourceWithRawResponse:
        return AsyncProprietaireResourceWithRawResponse(self._donnees.proprietaire)

    @cached_property
    def batiment_groupe_bdtopo_bat(self) -> AsyncBatimentGroupeBdtopoBatResourceWithRawResponse:
        return AsyncBatimentGroupeBdtopoBatResourceWithRawResponse(self._donnees.batiment_groupe_bdtopo_bat)

    @cached_property
    def rel_batiment_groupe_proprietaire_siren_open(
        self,
    ) -> AsyncRelBatimentGroupeProprietaireSirenOpenResourceWithRawResponse:
        return AsyncRelBatimentGroupeProprietaireSirenOpenResourceWithRawResponse(
            self._donnees.rel_batiment_groupe_proprietaire_siren_open
        )

    @cached_property
    def batiment_groupe_dle_elec_multimillesime(
        self,
    ) -> AsyncBatimentGroupeDleElecMultimillesimeResourceWithRawResponse:
        return AsyncBatimentGroupeDleElecMultimillesimeResourceWithRawResponse(
            self._donnees.batiment_groupe_dle_elec_multimillesime
        )

    @cached_property
    def adresse(self) -> AsyncAdresseResourceWithRawResponse:
        return AsyncAdresseResourceWithRawResponse(self._donnees.adresse)

    @cached_property
    def batiment_groupe_wall_dict(self) -> AsyncBatimentGroupeWallDictResourceWithRawResponse:
        return AsyncBatimentGroupeWallDictResourceWithRawResponse(self._donnees.batiment_groupe_wall_dict)

    @cached_property
    def batiment_groupe_indicateur_reseau_chaud_froid(
        self,
    ) -> AsyncBatimentGroupeIndicateurReseauChaudFroidResourceWithRawResponse:
        return AsyncBatimentGroupeIndicateurReseauChaudFroidResourceWithRawResponse(
            self._donnees.batiment_groupe_indicateur_reseau_chaud_froid
        )

    @cached_property
    def batiment_groupe_delimitation_enveloppe(self) -> AsyncBatimentGroupeDelimitationEnveloppeResourceWithRawResponse:
        return AsyncBatimentGroupeDelimitationEnveloppeResourceWithRawResponse(
            self._donnees.batiment_groupe_delimitation_enveloppe
        )

    @cached_property
    def batiment_groupe_simulations_valeur_verte(
        self,
    ) -> AsyncBatimentGroupeSimulationsValeurVerteResourceWithRawResponse:
        return AsyncBatimentGroupeSimulationsValeurVerteResourceWithRawResponse(
            self._donnees.batiment_groupe_simulations_valeur_verte
        )

    @cached_property
    def referentiel_administratif(self) -> AsyncReferentielAdministratifResourceWithRawResponse:
        return AsyncReferentielAdministratifResourceWithRawResponse(self._donnees.referentiel_administratif)


class DonneesResourceWithStreamingResponse:
    def __init__(self, donnees: DonneesResource) -> None:
        self._donnees = donnees

    @cached_property
    def batiment_groupe_complet(self) -> BatimentGroupeCompletResourceWithStreamingResponse:
        return BatimentGroupeCompletResourceWithStreamingResponse(self._donnees.batiment_groupe_complet)

    @cached_property
    def batiments_construction(self) -> BatimentsConstructionResourceWithStreamingResponse:
        return BatimentsConstructionResourceWithStreamingResponse(self._donnees.batiments_construction)

    @cached_property
    def batiment_groupe_bdtopo_zoac(self) -> BatimentGroupeBdtopoZoacResourceWithStreamingResponse:
        return BatimentGroupeBdtopoZoacResourceWithStreamingResponse(self._donnees.batiment_groupe_bdtopo_zoac)

    @cached_property
    def batiment_groupe_geospx(self) -> BatimentGroupeGeospxResourceWithStreamingResponse:
        return BatimentGroupeGeospxResourceWithStreamingResponse(self._donnees.batiment_groupe_geospx)

    @cached_property
    def rel_batiment_groupe_proprietaire_siren(self) -> RelBatimentGroupeProprietaireSirenResourceWithStreamingResponse:
        return RelBatimentGroupeProprietaireSirenResourceWithStreamingResponse(
            self._donnees.rel_batiment_groupe_proprietaire_siren
        )

    @cached_property
    def batiment_groupe_dvf_open_statistique(self) -> BatimentGroupeDvfOpenStatistiqueResourceWithStreamingResponse:
        return BatimentGroupeDvfOpenStatistiqueResourceWithStreamingResponse(
            self._donnees.batiment_groupe_dvf_open_statistique
        )

    @cached_property
    def rel_batiment_groupe_qpv(self) -> RelBatimentGroupeQpvResourceWithStreamingResponse:
        return RelBatimentGroupeQpvResourceWithStreamingResponse(self._donnees.rel_batiment_groupe_qpv)

    @cached_property
    def batiment_groupe_qpv(self) -> BatimentGroupeQpvResourceWithStreamingResponse:
        return BatimentGroupeQpvResourceWithStreamingResponse(self._donnees.batiment_groupe_qpv)

    @cached_property
    def rel_batiment_construction_adresse(self) -> RelBatimentConstructionAdresseResourceWithStreamingResponse:
        return RelBatimentConstructionAdresseResourceWithStreamingResponse(
            self._donnees.rel_batiment_construction_adresse
        )

    @cached_property
    def rel_batiment_groupe_adresse(self) -> RelBatimentGroupeAdresseResourceWithStreamingResponse:
        return RelBatimentGroupeAdresseResourceWithStreamingResponse(self._donnees.rel_batiment_groupe_adresse)

    @cached_property
    def batiment_groupe_synthese_enveloppe(self) -> BatimentGroupeSyntheseEnveloppeResourceWithStreamingResponse:
        return BatimentGroupeSyntheseEnveloppeResourceWithStreamingResponse(
            self._donnees.batiment_groupe_synthese_enveloppe
        )

    @cached_property
    def batiment_groupe_simulations_dpe(self) -> BatimentGroupeSimulationsDpeResourceWithStreamingResponse:
        return BatimentGroupeSimulationsDpeResourceWithStreamingResponse(self._donnees.batiment_groupe_simulations_dpe)

    @cached_property
    def batiment_groupe_bdtopo_equ(self) -> BatimentGroupeBdtopoEquResourceWithStreamingResponse:
        return BatimentGroupeBdtopoEquResourceWithStreamingResponse(self._donnees.batiment_groupe_bdtopo_equ)

    @cached_property
    def batiment_groupe_dpe_representatif_logement(
        self,
    ) -> BatimentGroupeDpeRepresentatifLogementResourceWithStreamingResponse:
        return BatimentGroupeDpeRepresentatifLogementResourceWithStreamingResponse(
            self._donnees.batiment_groupe_dpe_representatif_logement
        )

    @cached_property
    def batiment_groupe_dle_gaz_2020(self) -> BatimentGroupeDleGaz2020ResourceWithStreamingResponse:
        return BatimentGroupeDleGaz2020ResourceWithStreamingResponse(self._donnees.batiment_groupe_dle_gaz_2020)

    @cached_property
    def batiment_groupe(self) -> BatimentGroupeResourceWithStreamingResponse:
        return BatimentGroupeResourceWithStreamingResponse(self._donnees.batiment_groupe)

    @cached_property
    def rel_batiment_groupe_merimee(self) -> RelBatimentGroupeMerimeeResourceWithStreamingResponse:
        return RelBatimentGroupeMerimeeResourceWithStreamingResponse(self._donnees.rel_batiment_groupe_merimee)

    @cached_property
    def batiment_groupe_dle_elec_2020(self) -> BatimentGroupeDleElec2020ResourceWithStreamingResponse:
        return BatimentGroupeDleElec2020ResourceWithStreamingResponse(self._donnees.batiment_groupe_dle_elec_2020)

    @cached_property
    def batiment_groupe_merimee(self) -> BatimentGroupeMerimeeResourceWithStreamingResponse:
        return BatimentGroupeMerimeeResourceWithStreamingResponse(self._donnees.batiment_groupe_merimee)

    @cached_property
    def batiment_groupe_dle_reseaux_2020(self) -> BatimentGroupeDleReseaux2020ResourceWithStreamingResponse:
        return BatimentGroupeDleReseaux2020ResourceWithStreamingResponse(self._donnees.batiment_groupe_dle_reseaux_2020)

    @cached_property
    def ancqpv(self) -> AncqpvResourceWithStreamingResponse:
        return AncqpvResourceWithStreamingResponse(self._donnees.ancqpv)

    @cached_property
    def batiment_groupe_adresse(self) -> BatimentGroupeAdresseResourceWithStreamingResponse:
        return BatimentGroupeAdresseResourceWithStreamingResponse(self._donnees.batiment_groupe_adresse)

    @cached_property
    def batiment_groupe_dle_gaz_multimillesime(self) -> BatimentGroupeDleGazMultimillesimeResourceWithStreamingResponse:
        return BatimentGroupeDleGazMultimillesimeResourceWithStreamingResponse(
            self._donnees.batiment_groupe_dle_gaz_multimillesime
        )

    @cached_property
    def rel_batiment_groupe_parcelle(self) -> RelBatimentGroupeParcelleResourceWithStreamingResponse:
        return RelBatimentGroupeParcelleResourceWithStreamingResponse(self._donnees.rel_batiment_groupe_parcelle)

    @cached_property
    def batiment_groupe_radon(self) -> BatimentGroupeRadonResourceWithStreamingResponse:
        return BatimentGroupeRadonResourceWithStreamingResponse(self._donnees.batiment_groupe_radon)

    @cached_property
    def batiment_groupe_dvf_open_representatif(self) -> BatimentGroupeDvfOpenRepresentatifResourceWithStreamingResponse:
        return BatimentGroupeDvfOpenRepresentatifResourceWithStreamingResponse(
            self._donnees.batiment_groupe_dvf_open_representatif
        )

    @cached_property
    def batiment_groupe_simulations_dvf(self) -> BatimentGroupeSimulationsDvfResourceWithStreamingResponse:
        return BatimentGroupeSimulationsDvfResourceWithStreamingResponse(self._donnees.batiment_groupe_simulations_dvf)

    @cached_property
    def batiment_groupe_dpe_statistique_logement(
        self,
    ) -> BatimentGroupeDpeStatistiqueLogementResourceWithStreamingResponse:
        return BatimentGroupeDpeStatistiqueLogementResourceWithStreamingResponse(
            self._donnees.batiment_groupe_dpe_statistique_logement
        )

    @cached_property
    def iris_simulations_valeur_verte(self) -> IrisSimulationsValeurVerteResourceWithStreamingResponse:
        return IrisSimulationsValeurVerteResourceWithStreamingResponse(self._donnees.iris_simulations_valeur_verte)

    @cached_property
    def iris_contexte_geographique(self) -> IrisContexteGeographiqueResourceWithStreamingResponse:
        return IrisContexteGeographiqueResourceWithStreamingResponse(self._donnees.iris_contexte_geographique)

    @cached_property
    def rel_batiment_groupe_siren_complet(self) -> RelBatimentGroupeSirenCompletResourceWithStreamingResponse:
        return RelBatimentGroupeSirenCompletResourceWithStreamingResponse(
            self._donnees.rel_batiment_groupe_siren_complet
        )

    @cached_property
    def rel_batiment_groupe_siret_complet(self) -> RelBatimentGroupeSiretCompletResourceWithStreamingResponse:
        return RelBatimentGroupeSiretCompletResourceWithStreamingResponse(
            self._donnees.rel_batiment_groupe_siret_complet
        )

    @cached_property
    def batiment_groupe_dle_reseaux_multimillesime(
        self,
    ) -> BatimentGroupeDleReseauxMultimillesimeResourceWithStreamingResponse:
        return BatimentGroupeDleReseauxMultimillesimeResourceWithStreamingResponse(
            self._donnees.batiment_groupe_dle_reseaux_multimillesime
        )

    @cached_property
    def batiment_groupe_rnc(self) -> BatimentGroupeRncResourceWithStreamingResponse:
        return BatimentGroupeRncResourceWithStreamingResponse(self._donnees.batiment_groupe_rnc)

    @cached_property
    def batiment_groupe_bpe(self) -> BatimentGroupeBpeResourceWithStreamingResponse:
        return BatimentGroupeBpeResourceWithStreamingResponse(self._donnees.batiment_groupe_bpe)

    @cached_property
    def batiment_groupe_ffo_bat(self) -> BatimentGroupeFfoBatResourceWithStreamingResponse:
        return BatimentGroupeFfoBatResourceWithStreamingResponse(self._donnees.batiment_groupe_ffo_bat)

    @cached_property
    def rel_batiment_groupe_rnc(self) -> RelBatimentGroupeRncResourceWithStreamingResponse:
        return RelBatimentGroupeRncResourceWithStreamingResponse(self._donnees.rel_batiment_groupe_rnc)

    @cached_property
    def batiment_groupe_argiles(self) -> BatimentGroupeArgilesResourceWithStreamingResponse:
        return BatimentGroupeArgilesResourceWithStreamingResponse(self._donnees.batiment_groupe_argiles)

    @cached_property
    def batiment_groupe_hthd(self) -> BatimentGroupeHthdResourceWithStreamingResponse:
        return BatimentGroupeHthdResourceWithStreamingResponse(self._donnees.batiment_groupe_hthd)

    @cached_property
    def proprietaire(self) -> ProprietaireResourceWithStreamingResponse:
        return ProprietaireResourceWithStreamingResponse(self._donnees.proprietaire)

    @cached_property
    def batiment_groupe_bdtopo_bat(self) -> BatimentGroupeBdtopoBatResourceWithStreamingResponse:
        return BatimentGroupeBdtopoBatResourceWithStreamingResponse(self._donnees.batiment_groupe_bdtopo_bat)

    @cached_property
    def rel_batiment_groupe_proprietaire_siren_open(
        self,
    ) -> RelBatimentGroupeProprietaireSirenOpenResourceWithStreamingResponse:
        return RelBatimentGroupeProprietaireSirenOpenResourceWithStreamingResponse(
            self._donnees.rel_batiment_groupe_proprietaire_siren_open
        )

    @cached_property
    def batiment_groupe_dle_elec_multimillesime(
        self,
    ) -> BatimentGroupeDleElecMultimillesimeResourceWithStreamingResponse:
        return BatimentGroupeDleElecMultimillesimeResourceWithStreamingResponse(
            self._donnees.batiment_groupe_dle_elec_multimillesime
        )

    @cached_property
    def adresse(self) -> AdresseResourceWithStreamingResponse:
        return AdresseResourceWithStreamingResponse(self._donnees.adresse)

    @cached_property
    def batiment_groupe_wall_dict(self) -> BatimentGroupeWallDictResourceWithStreamingResponse:
        return BatimentGroupeWallDictResourceWithStreamingResponse(self._donnees.batiment_groupe_wall_dict)

    @cached_property
    def batiment_groupe_indicateur_reseau_chaud_froid(
        self,
    ) -> BatimentGroupeIndicateurReseauChaudFroidResourceWithStreamingResponse:
        return BatimentGroupeIndicateurReseauChaudFroidResourceWithStreamingResponse(
            self._donnees.batiment_groupe_indicateur_reseau_chaud_froid
        )

    @cached_property
    def batiment_groupe_delimitation_enveloppe(
        self,
    ) -> BatimentGroupeDelimitationEnveloppeResourceWithStreamingResponse:
        return BatimentGroupeDelimitationEnveloppeResourceWithStreamingResponse(
            self._donnees.batiment_groupe_delimitation_enveloppe
        )

    @cached_property
    def batiment_groupe_simulations_valeur_verte(
        self,
    ) -> BatimentGroupeSimulationsValeurVerteResourceWithStreamingResponse:
        return BatimentGroupeSimulationsValeurVerteResourceWithStreamingResponse(
            self._donnees.batiment_groupe_simulations_valeur_verte
        )

    @cached_property
    def referentiel_administratif(self) -> ReferentielAdministratifResourceWithStreamingResponse:
        return ReferentielAdministratifResourceWithStreamingResponse(self._donnees.referentiel_administratif)


class AsyncDonneesResourceWithStreamingResponse:
    def __init__(self, donnees: AsyncDonneesResource) -> None:
        self._donnees = donnees

    @cached_property
    def batiment_groupe_complet(self) -> AsyncBatimentGroupeCompletResourceWithStreamingResponse:
        return AsyncBatimentGroupeCompletResourceWithStreamingResponse(self._donnees.batiment_groupe_complet)

    @cached_property
    def batiments_construction(self) -> AsyncBatimentsConstructionResourceWithStreamingResponse:
        return AsyncBatimentsConstructionResourceWithStreamingResponse(self._donnees.batiments_construction)

    @cached_property
    def batiment_groupe_bdtopo_zoac(self) -> AsyncBatimentGroupeBdtopoZoacResourceWithStreamingResponse:
        return AsyncBatimentGroupeBdtopoZoacResourceWithStreamingResponse(self._donnees.batiment_groupe_bdtopo_zoac)

    @cached_property
    def batiment_groupe_geospx(self) -> AsyncBatimentGroupeGeospxResourceWithStreamingResponse:
        return AsyncBatimentGroupeGeospxResourceWithStreamingResponse(self._donnees.batiment_groupe_geospx)

    @cached_property
    def rel_batiment_groupe_proprietaire_siren(
        self,
    ) -> AsyncRelBatimentGroupeProprietaireSirenResourceWithStreamingResponse:
        return AsyncRelBatimentGroupeProprietaireSirenResourceWithStreamingResponse(
            self._donnees.rel_batiment_groupe_proprietaire_siren
        )

    @cached_property
    def batiment_groupe_dvf_open_statistique(
        self,
    ) -> AsyncBatimentGroupeDvfOpenStatistiqueResourceWithStreamingResponse:
        return AsyncBatimentGroupeDvfOpenStatistiqueResourceWithStreamingResponse(
            self._donnees.batiment_groupe_dvf_open_statistique
        )

    @cached_property
    def rel_batiment_groupe_qpv(self) -> AsyncRelBatimentGroupeQpvResourceWithStreamingResponse:
        return AsyncRelBatimentGroupeQpvResourceWithStreamingResponse(self._donnees.rel_batiment_groupe_qpv)

    @cached_property
    def batiment_groupe_qpv(self) -> AsyncBatimentGroupeQpvResourceWithStreamingResponse:
        return AsyncBatimentGroupeQpvResourceWithStreamingResponse(self._donnees.batiment_groupe_qpv)

    @cached_property
    def rel_batiment_construction_adresse(self) -> AsyncRelBatimentConstructionAdresseResourceWithStreamingResponse:
        return AsyncRelBatimentConstructionAdresseResourceWithStreamingResponse(
            self._donnees.rel_batiment_construction_adresse
        )

    @cached_property
    def rel_batiment_groupe_adresse(self) -> AsyncRelBatimentGroupeAdresseResourceWithStreamingResponse:
        return AsyncRelBatimentGroupeAdresseResourceWithStreamingResponse(self._donnees.rel_batiment_groupe_adresse)

    @cached_property
    def batiment_groupe_synthese_enveloppe(self) -> AsyncBatimentGroupeSyntheseEnveloppeResourceWithStreamingResponse:
        return AsyncBatimentGroupeSyntheseEnveloppeResourceWithStreamingResponse(
            self._donnees.batiment_groupe_synthese_enveloppe
        )

    @cached_property
    def batiment_groupe_simulations_dpe(self) -> AsyncBatimentGroupeSimulationsDpeResourceWithStreamingResponse:
        return AsyncBatimentGroupeSimulationsDpeResourceWithStreamingResponse(
            self._donnees.batiment_groupe_simulations_dpe
        )

    @cached_property
    def batiment_groupe_bdtopo_equ(self) -> AsyncBatimentGroupeBdtopoEquResourceWithStreamingResponse:
        return AsyncBatimentGroupeBdtopoEquResourceWithStreamingResponse(self._donnees.batiment_groupe_bdtopo_equ)

    @cached_property
    def batiment_groupe_dpe_representatif_logement(
        self,
    ) -> AsyncBatimentGroupeDpeRepresentatifLogementResourceWithStreamingResponse:
        return AsyncBatimentGroupeDpeRepresentatifLogementResourceWithStreamingResponse(
            self._donnees.batiment_groupe_dpe_representatif_logement
        )

    @cached_property
    def batiment_groupe_dle_gaz_2020(self) -> AsyncBatimentGroupeDleGaz2020ResourceWithStreamingResponse:
        return AsyncBatimentGroupeDleGaz2020ResourceWithStreamingResponse(self._donnees.batiment_groupe_dle_gaz_2020)

    @cached_property
    def batiment_groupe(self) -> AsyncBatimentGroupeResourceWithStreamingResponse:
        return AsyncBatimentGroupeResourceWithStreamingResponse(self._donnees.batiment_groupe)

    @cached_property
    def rel_batiment_groupe_merimee(self) -> AsyncRelBatimentGroupeMerimeeResourceWithStreamingResponse:
        return AsyncRelBatimentGroupeMerimeeResourceWithStreamingResponse(self._donnees.rel_batiment_groupe_merimee)

    @cached_property
    def batiment_groupe_dle_elec_2020(self) -> AsyncBatimentGroupeDleElec2020ResourceWithStreamingResponse:
        return AsyncBatimentGroupeDleElec2020ResourceWithStreamingResponse(self._donnees.batiment_groupe_dle_elec_2020)

    @cached_property
    def batiment_groupe_merimee(self) -> AsyncBatimentGroupeMerimeeResourceWithStreamingResponse:
        return AsyncBatimentGroupeMerimeeResourceWithStreamingResponse(self._donnees.batiment_groupe_merimee)

    @cached_property
    def batiment_groupe_dle_reseaux_2020(self) -> AsyncBatimentGroupeDleReseaux2020ResourceWithStreamingResponse:
        return AsyncBatimentGroupeDleReseaux2020ResourceWithStreamingResponse(
            self._donnees.batiment_groupe_dle_reseaux_2020
        )

    @cached_property
    def ancqpv(self) -> AsyncAncqpvResourceWithStreamingResponse:
        return AsyncAncqpvResourceWithStreamingResponse(self._donnees.ancqpv)

    @cached_property
    def batiment_groupe_adresse(self) -> AsyncBatimentGroupeAdresseResourceWithStreamingResponse:
        return AsyncBatimentGroupeAdresseResourceWithStreamingResponse(self._donnees.batiment_groupe_adresse)

    @cached_property
    def batiment_groupe_dle_gaz_multimillesime(
        self,
    ) -> AsyncBatimentGroupeDleGazMultimillesimeResourceWithStreamingResponse:
        return AsyncBatimentGroupeDleGazMultimillesimeResourceWithStreamingResponse(
            self._donnees.batiment_groupe_dle_gaz_multimillesime
        )

    @cached_property
    def rel_batiment_groupe_parcelle(self) -> AsyncRelBatimentGroupeParcelleResourceWithStreamingResponse:
        return AsyncRelBatimentGroupeParcelleResourceWithStreamingResponse(self._donnees.rel_batiment_groupe_parcelle)

    @cached_property
    def batiment_groupe_radon(self) -> AsyncBatimentGroupeRadonResourceWithStreamingResponse:
        return AsyncBatimentGroupeRadonResourceWithStreamingResponse(self._donnees.batiment_groupe_radon)

    @cached_property
    def batiment_groupe_dvf_open_representatif(
        self,
    ) -> AsyncBatimentGroupeDvfOpenRepresentatifResourceWithStreamingResponse:
        return AsyncBatimentGroupeDvfOpenRepresentatifResourceWithStreamingResponse(
            self._donnees.batiment_groupe_dvf_open_representatif
        )

    @cached_property
    def batiment_groupe_simulations_dvf(self) -> AsyncBatimentGroupeSimulationsDvfResourceWithStreamingResponse:
        return AsyncBatimentGroupeSimulationsDvfResourceWithStreamingResponse(
            self._donnees.batiment_groupe_simulations_dvf
        )

    @cached_property
    def batiment_groupe_dpe_statistique_logement(
        self,
    ) -> AsyncBatimentGroupeDpeStatistiqueLogementResourceWithStreamingResponse:
        return AsyncBatimentGroupeDpeStatistiqueLogementResourceWithStreamingResponse(
            self._donnees.batiment_groupe_dpe_statistique_logement
        )

    @cached_property
    def iris_simulations_valeur_verte(self) -> AsyncIrisSimulationsValeurVerteResourceWithStreamingResponse:
        return AsyncIrisSimulationsValeurVerteResourceWithStreamingResponse(self._donnees.iris_simulations_valeur_verte)

    @cached_property
    def iris_contexte_geographique(self) -> AsyncIrisContexteGeographiqueResourceWithStreamingResponse:
        return AsyncIrisContexteGeographiqueResourceWithStreamingResponse(self._donnees.iris_contexte_geographique)

    @cached_property
    def rel_batiment_groupe_siren_complet(self) -> AsyncRelBatimentGroupeSirenCompletResourceWithStreamingResponse:
        return AsyncRelBatimentGroupeSirenCompletResourceWithStreamingResponse(
            self._donnees.rel_batiment_groupe_siren_complet
        )

    @cached_property
    def rel_batiment_groupe_siret_complet(self) -> AsyncRelBatimentGroupeSiretCompletResourceWithStreamingResponse:
        return AsyncRelBatimentGroupeSiretCompletResourceWithStreamingResponse(
            self._donnees.rel_batiment_groupe_siret_complet
        )

    @cached_property
    def batiment_groupe_dle_reseaux_multimillesime(
        self,
    ) -> AsyncBatimentGroupeDleReseauxMultimillesimeResourceWithStreamingResponse:
        return AsyncBatimentGroupeDleReseauxMultimillesimeResourceWithStreamingResponse(
            self._donnees.batiment_groupe_dle_reseaux_multimillesime
        )

    @cached_property
    def batiment_groupe_rnc(self) -> AsyncBatimentGroupeRncResourceWithStreamingResponse:
        return AsyncBatimentGroupeRncResourceWithStreamingResponse(self._donnees.batiment_groupe_rnc)

    @cached_property
    def batiment_groupe_bpe(self) -> AsyncBatimentGroupeBpeResourceWithStreamingResponse:
        return AsyncBatimentGroupeBpeResourceWithStreamingResponse(self._donnees.batiment_groupe_bpe)

    @cached_property
    def batiment_groupe_ffo_bat(self) -> AsyncBatimentGroupeFfoBatResourceWithStreamingResponse:
        return AsyncBatimentGroupeFfoBatResourceWithStreamingResponse(self._donnees.batiment_groupe_ffo_bat)

    @cached_property
    def rel_batiment_groupe_rnc(self) -> AsyncRelBatimentGroupeRncResourceWithStreamingResponse:
        return AsyncRelBatimentGroupeRncResourceWithStreamingResponse(self._donnees.rel_batiment_groupe_rnc)

    @cached_property
    def batiment_groupe_argiles(self) -> AsyncBatimentGroupeArgilesResourceWithStreamingResponse:
        return AsyncBatimentGroupeArgilesResourceWithStreamingResponse(self._donnees.batiment_groupe_argiles)

    @cached_property
    def batiment_groupe_hthd(self) -> AsyncBatimentGroupeHthdResourceWithStreamingResponse:
        return AsyncBatimentGroupeHthdResourceWithStreamingResponse(self._donnees.batiment_groupe_hthd)

    @cached_property
    def proprietaire(self) -> AsyncProprietaireResourceWithStreamingResponse:
        return AsyncProprietaireResourceWithStreamingResponse(self._donnees.proprietaire)

    @cached_property
    def batiment_groupe_bdtopo_bat(self) -> AsyncBatimentGroupeBdtopoBatResourceWithStreamingResponse:
        return AsyncBatimentGroupeBdtopoBatResourceWithStreamingResponse(self._donnees.batiment_groupe_bdtopo_bat)

    @cached_property
    def rel_batiment_groupe_proprietaire_siren_open(
        self,
    ) -> AsyncRelBatimentGroupeProprietaireSirenOpenResourceWithStreamingResponse:
        return AsyncRelBatimentGroupeProprietaireSirenOpenResourceWithStreamingResponse(
            self._donnees.rel_batiment_groupe_proprietaire_siren_open
        )

    @cached_property
    def batiment_groupe_dle_elec_multimillesime(
        self,
    ) -> AsyncBatimentGroupeDleElecMultimillesimeResourceWithStreamingResponse:
        return AsyncBatimentGroupeDleElecMultimillesimeResourceWithStreamingResponse(
            self._donnees.batiment_groupe_dle_elec_multimillesime
        )

    @cached_property
    def adresse(self) -> AsyncAdresseResourceWithStreamingResponse:
        return AsyncAdresseResourceWithStreamingResponse(self._donnees.adresse)

    @cached_property
    def batiment_groupe_wall_dict(self) -> AsyncBatimentGroupeWallDictResourceWithStreamingResponse:
        return AsyncBatimentGroupeWallDictResourceWithStreamingResponse(self._donnees.batiment_groupe_wall_dict)

    @cached_property
    def batiment_groupe_indicateur_reseau_chaud_froid(
        self,
    ) -> AsyncBatimentGroupeIndicateurReseauChaudFroidResourceWithStreamingResponse:
        return AsyncBatimentGroupeIndicateurReseauChaudFroidResourceWithStreamingResponse(
            self._donnees.batiment_groupe_indicateur_reseau_chaud_froid
        )

    @cached_property
    def batiment_groupe_delimitation_enveloppe(
        self,
    ) -> AsyncBatimentGroupeDelimitationEnveloppeResourceWithStreamingResponse:
        return AsyncBatimentGroupeDelimitationEnveloppeResourceWithStreamingResponse(
            self._donnees.batiment_groupe_delimitation_enveloppe
        )

    @cached_property
    def batiment_groupe_simulations_valeur_verte(
        self,
    ) -> AsyncBatimentGroupeSimulationsValeurVerteResourceWithStreamingResponse:
        return AsyncBatimentGroupeSimulationsValeurVerteResourceWithStreamingResponse(
            self._donnees.batiment_groupe_simulations_valeur_verte
        )

    @cached_property
    def referentiel_administratif(self) -> AsyncReferentielAdministratifResourceWithStreamingResponse:
        return AsyncReferentielAdministratifResourceWithStreamingResponse(self._donnees.referentiel_administratif)
