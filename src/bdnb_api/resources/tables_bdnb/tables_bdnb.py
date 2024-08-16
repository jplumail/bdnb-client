# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .adresse import (
    AdresseResource,
    AsyncAdresseResource,
    AdresseResourceWithRawResponse,
    AsyncAdresseResourceWithRawResponse,
    AdresseResourceWithStreamingResponse,
    AsyncAdresseResourceWithStreamingResponse,
)
from .donnees import (
    DonneesResource,
    AsyncDonneesResource,
    DonneesResourceWithRawResponse,
    AsyncDonneesResourceWithRawResponse,
    DonneesResourceWithStreamingResponse,
    AsyncDonneesResourceWithStreamingResponse,
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
from .donnees.donnees import DonneesResource, AsyncDonneesResource
from .batiment_groupe_hthd import (
    BatimentGroupeHthdResource,
    AsyncBatimentGroupeHthdResource,
    BatimentGroupeHthdResourceWithRawResponse,
    AsyncBatimentGroupeHthdResourceWithRawResponse,
    BatimentGroupeHthdResourceWithStreamingResponse,
    AsyncBatimentGroupeHthdResourceWithStreamingResponse,
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
from .batiment_groupe_delimitation_enveloppe import (
    BatimentGroupeDelimitationEnveloppeResource,
    AsyncBatimentGroupeDelimitationEnveloppeResource,
    BatimentGroupeDelimitationEnveloppeResourceWithRawResponse,
    AsyncBatimentGroupeDelimitationEnveloppeResourceWithRawResponse,
    BatimentGroupeDelimitationEnveloppeResourceWithStreamingResponse,
    AsyncBatimentGroupeDelimitationEnveloppeResourceWithStreamingResponse,
)
from .batiment_groupe_dle_elec_multimillesime import (
    BatimentGroupeDleElecMultimillesimeResource,
    AsyncBatimentGroupeDleElecMultimillesimeResource,
    BatimentGroupeDleElecMultimillesimeResourceWithRawResponse,
    AsyncBatimentGroupeDleElecMultimillesimeResourceWithRawResponse,
    BatimentGroupeDleElecMultimillesimeResourceWithStreamingResponse,
    AsyncBatimentGroupeDleElecMultimillesimeResourceWithStreamingResponse,
)
from .ext_batiment_groupe_l_bdtopo_bat_cleabs import (
    ExtBatimentGroupeLBdtopoBatCleabsResource,
    AsyncExtBatimentGroupeLBdtopoBatCleabsResource,
    ExtBatimentGroupeLBdtopoBatCleabsResourceWithRawResponse,
    AsyncExtBatimentGroupeLBdtopoBatCleabsResourceWithRawResponse,
    ExtBatimentGroupeLBdtopoBatCleabsResourceWithStreamingResponse,
    AsyncExtBatimentGroupeLBdtopoBatCleabsResourceWithStreamingResponse,
)
from .batiment_groupe_simulations_valeur_verte import (
    BatimentGroupeSimulationsValeurVerteResource,
    AsyncBatimentGroupeSimulationsValeurVerteResource,
    BatimentGroupeSimulationsValeurVerteResourceWithRawResponse,
    AsyncBatimentGroupeSimulationsValeurVerteResourceWithRawResponse,
    BatimentGroupeSimulationsValeurVerteResourceWithStreamingResponse,
    AsyncBatimentGroupeSimulationsValeurVerteResourceWithStreamingResponse,
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
from .referentiel_administratif.referentiel_administratif import (
    ReferentielAdministratifResource,
    AsyncReferentielAdministratifResource,
)

__all__ = ["TablesBdnbResource", "AsyncTablesBdnbResource"]


class TablesBdnbResource(SyncAPIResource):
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
    def donnees(self) -> DonneesResource:
        return DonneesResource(self._client)

    @cached_property
    def ext_batiment_groupe_l_bdtopo_bat_cleabs(self) -> ExtBatimentGroupeLBdtopoBatCleabsResource:
        return ExtBatimentGroupeLBdtopoBatCleabsResource(self._client)

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
    def referentiel_administratif(self) -> ReferentielAdministratifResource:
        return ReferentielAdministratifResource(self._client)

    @cached_property
    def with_raw_response(self) -> TablesBdnbResourceWithRawResponse:
        return TablesBdnbResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TablesBdnbResourceWithStreamingResponse:
        return TablesBdnbResourceWithStreamingResponse(self)


class AsyncTablesBdnbResource(AsyncAPIResource):
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
    def donnees(self) -> AsyncDonneesResource:
        return AsyncDonneesResource(self._client)

    @cached_property
    def ext_batiment_groupe_l_bdtopo_bat_cleabs(self) -> AsyncExtBatimentGroupeLBdtopoBatCleabsResource:
        return AsyncExtBatimentGroupeLBdtopoBatCleabsResource(self._client)

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
    def referentiel_administratif(self) -> AsyncReferentielAdministratifResource:
        return AsyncReferentielAdministratifResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTablesBdnbResourceWithRawResponse:
        return AsyncTablesBdnbResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTablesBdnbResourceWithStreamingResponse:
        return AsyncTablesBdnbResourceWithStreamingResponse(self)


class TablesBdnbResourceWithRawResponse:
    def __init__(self, tables_bdnb: TablesBdnbResource) -> None:
        self._tables_bdnb = tables_bdnb

    @cached_property
    def batiment_groupe_indicateur_reseau_chaud_froid(
        self,
    ) -> BatimentGroupeIndicateurReseauChaudFroidResourceWithRawResponse:
        return BatimentGroupeIndicateurReseauChaudFroidResourceWithRawResponse(
            self._tables_bdnb.batiment_groupe_indicateur_reseau_chaud_froid
        )

    @cached_property
    def batiment_groupe_delimitation_enveloppe(self) -> BatimentGroupeDelimitationEnveloppeResourceWithRawResponse:
        return BatimentGroupeDelimitationEnveloppeResourceWithRawResponse(
            self._tables_bdnb.batiment_groupe_delimitation_enveloppe
        )

    @cached_property
    def batiment_groupe_simulations_valeur_verte(self) -> BatimentGroupeSimulationsValeurVerteResourceWithRawResponse:
        return BatimentGroupeSimulationsValeurVerteResourceWithRawResponse(
            self._tables_bdnb.batiment_groupe_simulations_valeur_verte
        )

    @cached_property
    def donnees(self) -> DonneesResourceWithRawResponse:
        return DonneesResourceWithRawResponse(self._tables_bdnb.donnees)

    @cached_property
    def ext_batiment_groupe_l_bdtopo_bat_cleabs(self) -> ExtBatimentGroupeLBdtopoBatCleabsResourceWithRawResponse:
        return ExtBatimentGroupeLBdtopoBatCleabsResourceWithRawResponse(
            self._tables_bdnb.ext_batiment_groupe_l_bdtopo_bat_cleabs
        )

    @cached_property
    def batiment_groupe_hthd(self) -> BatimentGroupeHthdResourceWithRawResponse:
        return BatimentGroupeHthdResourceWithRawResponse(self._tables_bdnb.batiment_groupe_hthd)

    @cached_property
    def proprietaire(self) -> ProprietaireResourceWithRawResponse:
        return ProprietaireResourceWithRawResponse(self._tables_bdnb.proprietaire)

    @cached_property
    def batiment_groupe_bdtopo_bat(self) -> BatimentGroupeBdtopoBatResourceWithRawResponse:
        return BatimentGroupeBdtopoBatResourceWithRawResponse(self._tables_bdnb.batiment_groupe_bdtopo_bat)

    @cached_property
    def rel_batiment_groupe_proprietaire_siren_open(
        self,
    ) -> RelBatimentGroupeProprietaireSirenOpenResourceWithRawResponse:
        return RelBatimentGroupeProprietaireSirenOpenResourceWithRawResponse(
            self._tables_bdnb.rel_batiment_groupe_proprietaire_siren_open
        )

    @cached_property
    def batiment_groupe_dle_elec_multimillesime(self) -> BatimentGroupeDleElecMultimillesimeResourceWithRawResponse:
        return BatimentGroupeDleElecMultimillesimeResourceWithRawResponse(
            self._tables_bdnb.batiment_groupe_dle_elec_multimillesime
        )

    @cached_property
    def adresse(self) -> AdresseResourceWithRawResponse:
        return AdresseResourceWithRawResponse(self._tables_bdnb.adresse)

    @cached_property
    def batiment_groupe_wall_dict(self) -> BatimentGroupeWallDictResourceWithRawResponse:
        return BatimentGroupeWallDictResourceWithRawResponse(self._tables_bdnb.batiment_groupe_wall_dict)

    @cached_property
    def referentiel_administratif(self) -> ReferentielAdministratifResourceWithRawResponse:
        return ReferentielAdministratifResourceWithRawResponse(self._tables_bdnb.referentiel_administratif)


class AsyncTablesBdnbResourceWithRawResponse:
    def __init__(self, tables_bdnb: AsyncTablesBdnbResource) -> None:
        self._tables_bdnb = tables_bdnb

    @cached_property
    def batiment_groupe_indicateur_reseau_chaud_froid(
        self,
    ) -> AsyncBatimentGroupeIndicateurReseauChaudFroidResourceWithRawResponse:
        return AsyncBatimentGroupeIndicateurReseauChaudFroidResourceWithRawResponse(
            self._tables_bdnb.batiment_groupe_indicateur_reseau_chaud_froid
        )

    @cached_property
    def batiment_groupe_delimitation_enveloppe(self) -> AsyncBatimentGroupeDelimitationEnveloppeResourceWithRawResponse:
        return AsyncBatimentGroupeDelimitationEnveloppeResourceWithRawResponse(
            self._tables_bdnb.batiment_groupe_delimitation_enveloppe
        )

    @cached_property
    def batiment_groupe_simulations_valeur_verte(
        self,
    ) -> AsyncBatimentGroupeSimulationsValeurVerteResourceWithRawResponse:
        return AsyncBatimentGroupeSimulationsValeurVerteResourceWithRawResponse(
            self._tables_bdnb.batiment_groupe_simulations_valeur_verte
        )

    @cached_property
    def donnees(self) -> AsyncDonneesResourceWithRawResponse:
        return AsyncDonneesResourceWithRawResponse(self._tables_bdnb.donnees)

    @cached_property
    def ext_batiment_groupe_l_bdtopo_bat_cleabs(self) -> AsyncExtBatimentGroupeLBdtopoBatCleabsResourceWithRawResponse:
        return AsyncExtBatimentGroupeLBdtopoBatCleabsResourceWithRawResponse(
            self._tables_bdnb.ext_batiment_groupe_l_bdtopo_bat_cleabs
        )

    @cached_property
    def batiment_groupe_hthd(self) -> AsyncBatimentGroupeHthdResourceWithRawResponse:
        return AsyncBatimentGroupeHthdResourceWithRawResponse(self._tables_bdnb.batiment_groupe_hthd)

    @cached_property
    def proprietaire(self) -> AsyncProprietaireResourceWithRawResponse:
        return AsyncProprietaireResourceWithRawResponse(self._tables_bdnb.proprietaire)

    @cached_property
    def batiment_groupe_bdtopo_bat(self) -> AsyncBatimentGroupeBdtopoBatResourceWithRawResponse:
        return AsyncBatimentGroupeBdtopoBatResourceWithRawResponse(self._tables_bdnb.batiment_groupe_bdtopo_bat)

    @cached_property
    def rel_batiment_groupe_proprietaire_siren_open(
        self,
    ) -> AsyncRelBatimentGroupeProprietaireSirenOpenResourceWithRawResponse:
        return AsyncRelBatimentGroupeProprietaireSirenOpenResourceWithRawResponse(
            self._tables_bdnb.rel_batiment_groupe_proprietaire_siren_open
        )

    @cached_property
    def batiment_groupe_dle_elec_multimillesime(
        self,
    ) -> AsyncBatimentGroupeDleElecMultimillesimeResourceWithRawResponse:
        return AsyncBatimentGroupeDleElecMultimillesimeResourceWithRawResponse(
            self._tables_bdnb.batiment_groupe_dle_elec_multimillesime
        )

    @cached_property
    def adresse(self) -> AsyncAdresseResourceWithRawResponse:
        return AsyncAdresseResourceWithRawResponse(self._tables_bdnb.adresse)

    @cached_property
    def batiment_groupe_wall_dict(self) -> AsyncBatimentGroupeWallDictResourceWithRawResponse:
        return AsyncBatimentGroupeWallDictResourceWithRawResponse(self._tables_bdnb.batiment_groupe_wall_dict)

    @cached_property
    def referentiel_administratif(self) -> AsyncReferentielAdministratifResourceWithRawResponse:
        return AsyncReferentielAdministratifResourceWithRawResponse(self._tables_bdnb.referentiel_administratif)


class TablesBdnbResourceWithStreamingResponse:
    def __init__(self, tables_bdnb: TablesBdnbResource) -> None:
        self._tables_bdnb = tables_bdnb

    @cached_property
    def batiment_groupe_indicateur_reseau_chaud_froid(
        self,
    ) -> BatimentGroupeIndicateurReseauChaudFroidResourceWithStreamingResponse:
        return BatimentGroupeIndicateurReseauChaudFroidResourceWithStreamingResponse(
            self._tables_bdnb.batiment_groupe_indicateur_reseau_chaud_froid
        )

    @cached_property
    def batiment_groupe_delimitation_enveloppe(
        self,
    ) -> BatimentGroupeDelimitationEnveloppeResourceWithStreamingResponse:
        return BatimentGroupeDelimitationEnveloppeResourceWithStreamingResponse(
            self._tables_bdnb.batiment_groupe_delimitation_enveloppe
        )

    @cached_property
    def batiment_groupe_simulations_valeur_verte(
        self,
    ) -> BatimentGroupeSimulationsValeurVerteResourceWithStreamingResponse:
        return BatimentGroupeSimulationsValeurVerteResourceWithStreamingResponse(
            self._tables_bdnb.batiment_groupe_simulations_valeur_verte
        )

    @cached_property
    def donnees(self) -> DonneesResourceWithStreamingResponse:
        return DonneesResourceWithStreamingResponse(self._tables_bdnb.donnees)

    @cached_property
    def ext_batiment_groupe_l_bdtopo_bat_cleabs(self) -> ExtBatimentGroupeLBdtopoBatCleabsResourceWithStreamingResponse:
        return ExtBatimentGroupeLBdtopoBatCleabsResourceWithStreamingResponse(
            self._tables_bdnb.ext_batiment_groupe_l_bdtopo_bat_cleabs
        )

    @cached_property
    def batiment_groupe_hthd(self) -> BatimentGroupeHthdResourceWithStreamingResponse:
        return BatimentGroupeHthdResourceWithStreamingResponse(self._tables_bdnb.batiment_groupe_hthd)

    @cached_property
    def proprietaire(self) -> ProprietaireResourceWithStreamingResponse:
        return ProprietaireResourceWithStreamingResponse(self._tables_bdnb.proprietaire)

    @cached_property
    def batiment_groupe_bdtopo_bat(self) -> BatimentGroupeBdtopoBatResourceWithStreamingResponse:
        return BatimentGroupeBdtopoBatResourceWithStreamingResponse(self._tables_bdnb.batiment_groupe_bdtopo_bat)

    @cached_property
    def rel_batiment_groupe_proprietaire_siren_open(
        self,
    ) -> RelBatimentGroupeProprietaireSirenOpenResourceWithStreamingResponse:
        return RelBatimentGroupeProprietaireSirenOpenResourceWithStreamingResponse(
            self._tables_bdnb.rel_batiment_groupe_proprietaire_siren_open
        )

    @cached_property
    def batiment_groupe_dle_elec_multimillesime(
        self,
    ) -> BatimentGroupeDleElecMultimillesimeResourceWithStreamingResponse:
        return BatimentGroupeDleElecMultimillesimeResourceWithStreamingResponse(
            self._tables_bdnb.batiment_groupe_dle_elec_multimillesime
        )

    @cached_property
    def adresse(self) -> AdresseResourceWithStreamingResponse:
        return AdresseResourceWithStreamingResponse(self._tables_bdnb.adresse)

    @cached_property
    def batiment_groupe_wall_dict(self) -> BatimentGroupeWallDictResourceWithStreamingResponse:
        return BatimentGroupeWallDictResourceWithStreamingResponse(self._tables_bdnb.batiment_groupe_wall_dict)

    @cached_property
    def referentiel_administratif(self) -> ReferentielAdministratifResourceWithStreamingResponse:
        return ReferentielAdministratifResourceWithStreamingResponse(self._tables_bdnb.referentiel_administratif)


class AsyncTablesBdnbResourceWithStreamingResponse:
    def __init__(self, tables_bdnb: AsyncTablesBdnbResource) -> None:
        self._tables_bdnb = tables_bdnb

    @cached_property
    def batiment_groupe_indicateur_reseau_chaud_froid(
        self,
    ) -> AsyncBatimentGroupeIndicateurReseauChaudFroidResourceWithStreamingResponse:
        return AsyncBatimentGroupeIndicateurReseauChaudFroidResourceWithStreamingResponse(
            self._tables_bdnb.batiment_groupe_indicateur_reseau_chaud_froid
        )

    @cached_property
    def batiment_groupe_delimitation_enveloppe(
        self,
    ) -> AsyncBatimentGroupeDelimitationEnveloppeResourceWithStreamingResponse:
        return AsyncBatimentGroupeDelimitationEnveloppeResourceWithStreamingResponse(
            self._tables_bdnb.batiment_groupe_delimitation_enveloppe
        )

    @cached_property
    def batiment_groupe_simulations_valeur_verte(
        self,
    ) -> AsyncBatimentGroupeSimulationsValeurVerteResourceWithStreamingResponse:
        return AsyncBatimentGroupeSimulationsValeurVerteResourceWithStreamingResponse(
            self._tables_bdnb.batiment_groupe_simulations_valeur_verte
        )

    @cached_property
    def donnees(self) -> AsyncDonneesResourceWithStreamingResponse:
        return AsyncDonneesResourceWithStreamingResponse(self._tables_bdnb.donnees)

    @cached_property
    def ext_batiment_groupe_l_bdtopo_bat_cleabs(
        self,
    ) -> AsyncExtBatimentGroupeLBdtopoBatCleabsResourceWithStreamingResponse:
        return AsyncExtBatimentGroupeLBdtopoBatCleabsResourceWithStreamingResponse(
            self._tables_bdnb.ext_batiment_groupe_l_bdtopo_bat_cleabs
        )

    @cached_property
    def batiment_groupe_hthd(self) -> AsyncBatimentGroupeHthdResourceWithStreamingResponse:
        return AsyncBatimentGroupeHthdResourceWithStreamingResponse(self._tables_bdnb.batiment_groupe_hthd)

    @cached_property
    def proprietaire(self) -> AsyncProprietaireResourceWithStreamingResponse:
        return AsyncProprietaireResourceWithStreamingResponse(self._tables_bdnb.proprietaire)

    @cached_property
    def batiment_groupe_bdtopo_bat(self) -> AsyncBatimentGroupeBdtopoBatResourceWithStreamingResponse:
        return AsyncBatimentGroupeBdtopoBatResourceWithStreamingResponse(self._tables_bdnb.batiment_groupe_bdtopo_bat)

    @cached_property
    def rel_batiment_groupe_proprietaire_siren_open(
        self,
    ) -> AsyncRelBatimentGroupeProprietaireSirenOpenResourceWithStreamingResponse:
        return AsyncRelBatimentGroupeProprietaireSirenOpenResourceWithStreamingResponse(
            self._tables_bdnb.rel_batiment_groupe_proprietaire_siren_open
        )

    @cached_property
    def batiment_groupe_dle_elec_multimillesime(
        self,
    ) -> AsyncBatimentGroupeDleElecMultimillesimeResourceWithStreamingResponse:
        return AsyncBatimentGroupeDleElecMultimillesimeResourceWithStreamingResponse(
            self._tables_bdnb.batiment_groupe_dle_elec_multimillesime
        )

    @cached_property
    def adresse(self) -> AsyncAdresseResourceWithStreamingResponse:
        return AsyncAdresseResourceWithStreamingResponse(self._tables_bdnb.adresse)

    @cached_property
    def batiment_groupe_wall_dict(self) -> AsyncBatimentGroupeWallDictResourceWithStreamingResponse:
        return AsyncBatimentGroupeWallDictResourceWithStreamingResponse(self._tables_bdnb.batiment_groupe_wall_dict)

    @cached_property
    def referentiel_administratif(self) -> AsyncReferentielAdministratifResourceWithStreamingResponse:
        return AsyncReferentielAdministratifResourceWithStreamingResponse(self._tables_bdnb.referentiel_administratif)
