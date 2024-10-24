# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .bpe import (
    BpeResource,
    AsyncBpeResource,
    BpeResourceWithRawResponse,
    AsyncBpeResourceWithRawResponse,
    BpeResourceWithStreamingResponse,
    AsyncBpeResourceWithStreamingResponse,
)
from .qpv import (
    QpvResource,
    AsyncQpvResource,
    QpvResourceWithRawResponse,
    AsyncQpvResourceWithRawResponse,
    QpvResourceWithStreamingResponse,
    AsyncQpvResourceWithStreamingResponse,
)
from .rnc import (
    RncResource,
    AsyncRncResource,
    RncResourceWithRawResponse,
    AsyncRncResourceWithRawResponse,
    RncResourceWithStreamingResponse,
    AsyncRncResourceWithStreamingResponse,
)
from .hthd import (
    HthdResource,
    AsyncHthdResource,
    HthdResourceWithRawResponse,
    AsyncHthdResourceWithRawResponse,
    HthdResourceWithStreamingResponse,
    AsyncHthdResourceWithStreamingResponse,
)
from .radon import (
    RadonResource,
    AsyncRadonResource,
    RadonResourceWithRawResponse,
    AsyncRadonResourceWithRawResponse,
    RadonResourceWithStreamingResponse,
    AsyncRadonResourceWithStreamingResponse,
)
from .geospx import (
    GeospxResource,
    AsyncGeospxResource,
    GeospxResourceWithRawResponse,
    AsyncGeospxResourceWithRawResponse,
    GeospxResourceWithStreamingResponse,
    AsyncGeospxResourceWithStreamingResponse,
)
from .adresse import (
    AdresseResource,
    AsyncAdresseResource,
    AdresseResourceWithRawResponse,
    AsyncAdresseResourceWithRawResponse,
    AdresseResourceWithStreamingResponse,
    AsyncAdresseResourceWithStreamingResponse,
)
from .argiles import (
    ArgilesResource,
    AsyncArgilesResource,
    ArgilesResourceWithRawResponse,
    AsyncArgilesResourceWithRawResponse,
    ArgilesResourceWithStreamingResponse,
    AsyncArgilesResourceWithStreamingResponse,
)
from .complet import (
    CompletResource,
    AsyncCompletResource,
    CompletResourceWithRawResponse,
    AsyncCompletResourceWithRawResponse,
    CompletResourceWithStreamingResponse,
    AsyncCompletResourceWithStreamingResponse,
)
from .ffo_bat import (
    FfoBatResource,
    AsyncFfoBatResource,
    FfoBatResourceWithRawResponse,
    AsyncFfoBatResourceWithRawResponse,
    FfoBatResourceWithStreamingResponse,
    AsyncFfoBatResourceWithStreamingResponse,
)
from .merimee import (
    MerimeeResource,
    AsyncMerimeeResource,
    MerimeeResourceWithRawResponse,
    AsyncMerimeeResourceWithRawResponse,
    MerimeeResourceWithStreamingResponse,
    AsyncMerimeeResourceWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform, strip_not_given
from .wall_dict import (
    WallDictResource,
    AsyncWallDictResource,
    WallDictResourceWithRawResponse,
    AsyncWallDictResourceWithRawResponse,
    WallDictResourceWithStreamingResponse,
    AsyncWallDictResourceWithStreamingResponse,
)
from ...._compat import cached_property
from .bdtopo_bat import (
    BdtopoBatResource,
    AsyncBdtopoBatResource,
    BdtopoBatResourceWithRawResponse,
    AsyncBdtopoBatResourceWithRawResponse,
    BdtopoBatResourceWithStreamingResponse,
    AsyncBdtopoBatResourceWithStreamingResponse,
)
from .bdtopo_equ import (
    BdtopoEquResource,
    AsyncBdtopoEquResource,
    BdtopoEquResourceWithRawResponse,
    AsyncBdtopoEquResourceWithRawResponse,
    BdtopoEquResourceWithStreamingResponse,
    AsyncBdtopoEquResourceWithStreamingResponse,
)
from .bdtopo_zoac import (
    BdtopoZoacResource,
    AsyncBdtopoZoacResource,
    BdtopoZoacResourceWithRawResponse,
    AsyncBdtopoZoacResourceWithRawResponse,
    BdtopoZoacResourceWithStreamingResponse,
    AsyncBdtopoZoacResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .dle_gaz_2020 import (
    DleGaz2020Resource,
    AsyncDleGaz2020Resource,
    DleGaz2020ResourceWithRawResponse,
    AsyncDleGaz2020ResourceWithRawResponse,
    DleGaz2020ResourceWithStreamingResponse,
    AsyncDleGaz2020ResourceWithStreamingResponse,
)
from ....pagination import SyncDefault, AsyncDefault
from .dle_elec_2020 import (
    DleElec2020Resource,
    AsyncDleElec2020Resource,
    DleElec2020ResourceWithRawResponse,
    AsyncDleElec2020ResourceWithRawResponse,
    DleElec2020ResourceWithStreamingResponse,
    AsyncDleElec2020ResourceWithStreamingResponse,
)
from ...._base_client import AsyncPaginator, make_request_options
from .complet.complet import CompletResource, AsyncCompletResource
from .simulations_dpe import (
    SimulationsDpeResource,
    AsyncSimulationsDpeResource,
    SimulationsDpeResourceWithRawResponse,
    AsyncSimulationsDpeResourceWithRawResponse,
    SimulationsDpeResourceWithStreamingResponse,
    AsyncSimulationsDpeResourceWithStreamingResponse,
)
from .simulations_dvf import (
    SimulationsDvfResource,
    AsyncSimulationsDvfResource,
    SimulationsDvfResourceWithRawResponse,
    AsyncSimulationsDvfResourceWithRawResponse,
    SimulationsDvfResourceWithStreamingResponse,
    AsyncSimulationsDvfResourceWithStreamingResponse,
)
from ....types.donnees import batiment_groupe_list_params
from .dle_reseaux_2020 import (
    DleReseaux2020Resource,
    AsyncDleReseaux2020Resource,
    DleReseaux2020ResourceWithRawResponse,
    AsyncDleReseaux2020ResourceWithRawResponse,
    DleReseaux2020ResourceWithStreamingResponse,
    AsyncDleReseaux2020ResourceWithStreamingResponse,
)
from .synthese_enveloppe import (
    SyntheseEnveloppeResource,
    AsyncSyntheseEnveloppeResource,
    SyntheseEnveloppeResourceWithRawResponse,
    AsyncSyntheseEnveloppeResourceWithRawResponse,
    SyntheseEnveloppeResourceWithStreamingResponse,
    AsyncSyntheseEnveloppeResourceWithStreamingResponse,
)
from .dvf_open_statistique import (
    DvfOpenStatistiqueResource,
    AsyncDvfOpenStatistiqueResource,
    DvfOpenStatistiqueResourceWithRawResponse,
    AsyncDvfOpenStatistiqueResourceWithRawResponse,
    DvfOpenStatistiqueResourceWithStreamingResponse,
    AsyncDvfOpenStatistiqueResourceWithStreamingResponse,
)
from .delimitation_enveloppe import (
    DelimitationEnveloppeResource,
    AsyncDelimitationEnveloppeResource,
    DelimitationEnveloppeResourceWithRawResponse,
    AsyncDelimitationEnveloppeResourceWithRawResponse,
    DelimitationEnveloppeResourceWithStreamingResponse,
    AsyncDelimitationEnveloppeResourceWithStreamingResponse,
)
from .dle_gaz_multimillesime import (
    DleGazMultimillesimeResource,
    AsyncDleGazMultimillesimeResource,
    DleGazMultimillesimeResourceWithRawResponse,
    AsyncDleGazMultimillesimeResourceWithRawResponse,
    DleGazMultimillesimeResourceWithStreamingResponse,
    AsyncDleGazMultimillesimeResourceWithStreamingResponse,
)
from .dvf_open_representatif import (
    DvfOpenRepresentatifResource,
    AsyncDvfOpenRepresentatifResource,
    DvfOpenRepresentatifResourceWithRawResponse,
    AsyncDvfOpenRepresentatifResourceWithRawResponse,
    DvfOpenRepresentatifResourceWithStreamingResponse,
    AsyncDvfOpenRepresentatifResourceWithStreamingResponse,
)
from .dle_elec_multimillesime import (
    DleElecMultimillesimeResource,
    AsyncDleElecMultimillesimeResource,
    DleElecMultimillesimeResourceWithRawResponse,
    AsyncDleElecMultimillesimeResourceWithRawResponse,
    DleElecMultimillesimeResourceWithStreamingResponse,
    AsyncDleElecMultimillesimeResourceWithStreamingResponse,
)
from .dpe_statistique_logement import (
    DpeStatistiqueLogementResource,
    AsyncDpeStatistiqueLogementResource,
    DpeStatistiqueLogementResourceWithRawResponse,
    AsyncDpeStatistiqueLogementResourceWithRawResponse,
    DpeStatistiqueLogementResourceWithStreamingResponse,
    AsyncDpeStatistiqueLogementResourceWithStreamingResponse,
)
from .simulations_valeur_verte import (
    SimulationsValeurVerteResource,
    AsyncSimulationsValeurVerteResource,
    SimulationsValeurVerteResourceWithRawResponse,
    AsyncSimulationsValeurVerteResourceWithRawResponse,
    SimulationsValeurVerteResourceWithStreamingResponse,
    AsyncSimulationsValeurVerteResourceWithStreamingResponse,
)
from .dle_reseaux_multimillesime import (
    DleReseauxMultimillesimeResource,
    AsyncDleReseauxMultimillesimeResource,
    DleReseauxMultimillesimeResourceWithRawResponse,
    AsyncDleReseauxMultimillesimeResourceWithRawResponse,
    DleReseauxMultimillesimeResourceWithStreamingResponse,
    AsyncDleReseauxMultimillesimeResourceWithStreamingResponse,
)
from .dpe_representatif_logement import (
    DpeRepresentatifLogementResource,
    AsyncDpeRepresentatifLogementResource,
    DpeRepresentatifLogementResourceWithRawResponse,
    AsyncDpeRepresentatifLogementResourceWithRawResponse,
    DpeRepresentatifLogementResourceWithStreamingResponse,
    AsyncDpeRepresentatifLogementResourceWithStreamingResponse,
)
from .iris_contexte_geographique import (
    IrisContexteGeographiqueResource,
    AsyncIrisContexteGeographiqueResource,
    IrisContexteGeographiqueResourceWithRawResponse,
    AsyncIrisContexteGeographiqueResourceWithRawResponse,
    IrisContexteGeographiqueResourceWithStreamingResponse,
    AsyncIrisContexteGeographiqueResourceWithStreamingResponse,
)
from .indicateur_reseau_chaud_froid import (
    IndicateurReseauChaudFroidResource,
    AsyncIndicateurReseauChaudFroidResource,
    IndicateurReseauChaudFroidResourceWithRawResponse,
    AsyncIndicateurReseauChaudFroidResourceWithRawResponse,
    IndicateurReseauChaudFroidResourceWithStreamingResponse,
    AsyncIndicateurReseauChaudFroidResourceWithStreamingResponse,
)
from .iris_simulations_valeur_verte import (
    IrisSimulationsValeurVerteResource,
    AsyncIrisSimulationsValeurVerteResource,
    IrisSimulationsValeurVerteResourceWithRawResponse,
    AsyncIrisSimulationsValeurVerteResourceWithRawResponse,
    IrisSimulationsValeurVerteResourceWithStreamingResponse,
    AsyncIrisSimulationsValeurVerteResourceWithStreamingResponse,
)
from ....types.donnees.batiment_groupe.batiment_groupe import BatimentGroupe

__all__ = ["BatimentGroupeResource", "AsyncBatimentGroupeResource"]


class BatimentGroupeResource(SyncAPIResource):
    @cached_property
    def complet(self) -> CompletResource:
        return CompletResource(self._client)

    @cached_property
    def bdtopo_zoac(self) -> BdtopoZoacResource:
        return BdtopoZoacResource(self._client)

    @cached_property
    def geospx(self) -> GeospxResource:
        return GeospxResource(self._client)

    @cached_property
    def dvf_open_statistique(self) -> DvfOpenStatistiqueResource:
        return DvfOpenStatistiqueResource(self._client)

    @cached_property
    def qpv(self) -> QpvResource:
        return QpvResource(self._client)

    @cached_property
    def synthese_enveloppe(self) -> SyntheseEnveloppeResource:
        return SyntheseEnveloppeResource(self._client)

    @cached_property
    def simulations_dpe(self) -> SimulationsDpeResource:
        return SimulationsDpeResource(self._client)

    @cached_property
    def bdtopo_equ(self) -> BdtopoEquResource:
        return BdtopoEquResource(self._client)

    @cached_property
    def dpe_representatif_logement(self) -> DpeRepresentatifLogementResource:
        return DpeRepresentatifLogementResource(self._client)

    @cached_property
    def dle_gaz_2020(self) -> DleGaz2020Resource:
        return DleGaz2020Resource(self._client)

    @cached_property
    def dle_elec_2020(self) -> DleElec2020Resource:
        return DleElec2020Resource(self._client)

    @cached_property
    def merimee(self) -> MerimeeResource:
        return MerimeeResource(self._client)

    @cached_property
    def dle_reseaux_2020(self) -> DleReseaux2020Resource:
        return DleReseaux2020Resource(self._client)

    @cached_property
    def adresse(self) -> AdresseResource:
        return AdresseResource(self._client)

    @cached_property
    def dle_gaz_multimillesime(self) -> DleGazMultimillesimeResource:
        return DleGazMultimillesimeResource(self._client)

    @cached_property
    def radon(self) -> RadonResource:
        return RadonResource(self._client)

    @cached_property
    def dvf_open_representatif(self) -> DvfOpenRepresentatifResource:
        return DvfOpenRepresentatifResource(self._client)

    @cached_property
    def simulations_dvf(self) -> SimulationsDvfResource:
        return SimulationsDvfResource(self._client)

    @cached_property
    def dpe_statistique_logement(self) -> DpeStatistiqueLogementResource:
        return DpeStatistiqueLogementResource(self._client)

    @cached_property
    def dle_reseaux_multimillesime(self) -> DleReseauxMultimillesimeResource:
        return DleReseauxMultimillesimeResource(self._client)

    @cached_property
    def rnc(self) -> RncResource:
        return RncResource(self._client)

    @cached_property
    def bpe(self) -> BpeResource:
        return BpeResource(self._client)

    @cached_property
    def ffo_bat(self) -> FfoBatResource:
        return FfoBatResource(self._client)

    @cached_property
    def argiles(self) -> ArgilesResource:
        return ArgilesResource(self._client)

    @cached_property
    def hthd(self) -> HthdResource:
        return HthdResource(self._client)

    @cached_property
    def bdtopo_bat(self) -> BdtopoBatResource:
        return BdtopoBatResource(self._client)

    @cached_property
    def dle_elec_multimillesime(self) -> DleElecMultimillesimeResource:
        return DleElecMultimillesimeResource(self._client)

    @cached_property
    def wall_dict(self) -> WallDictResource:
        return WallDictResource(self._client)

    @cached_property
    def indicateur_reseau_chaud_froid(self) -> IndicateurReseauChaudFroidResource:
        return IndicateurReseauChaudFroidResource(self._client)

    @cached_property
    def delimitation_enveloppe(self) -> DelimitationEnveloppeResource:
        return DelimitationEnveloppeResource(self._client)

    @cached_property
    def simulations_valeur_verte(self) -> SimulationsValeurVerteResource:
        return SimulationsValeurVerteResource(self._client)

    @cached_property
    def iris_simulations_valeur_verte(self) -> IrisSimulationsValeurVerteResource:
        return IrisSimulationsValeurVerteResource(self._client)

    @cached_property
    def iris_contexte_geographique(self) -> IrisContexteGeographiqueResource:
        return IrisContexteGeographiqueResource(self._client)

    @cached_property
    def with_raw_response(self) -> BatimentGroupeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jplumail/bdnb-client#accessing-raw-response-data-eg-headers
        """
        return BatimentGroupeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BatimentGroupeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jplumail/bdnb-client#with_streaming_response
        """
        return BatimentGroupeResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        batiment_groupe_id: str | NotGiven = NOT_GIVEN,
        code_commune_insee: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        code_epci_insee: str | NotGiven = NOT_GIVEN,
        code_iris: str | NotGiven = NOT_GIVEN,
        code_qp: str | NotGiven = NOT_GIVEN,
        code_region_insee: str | NotGiven = NOT_GIVEN,
        contient_fictive_geom_groupe: str | NotGiven = NOT_GIVEN,
        geom_groupe: str | NotGiven = NOT_GIVEN,
        geom_groupe_pos_wgs84: str | NotGiven = NOT_GIVEN,
        libelle_commune_insee: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        nom_qp: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        quartier_prioritaire: str | NotGiven = NOT_GIVEN,
        s_geom_groupe: str | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncDefault[BatimentGroupe]:
        """
        Complexes de bâtiments au sens de la BDNB

        Args:
          batiment_groupe_id: Identifiant du groupe de bâtiment au sens de la BDNB

          code_commune_insee: Code INSEE de la commune

          code_departement_insee: Code département INSEE

          code_epci_insee: Code de l'EPCI

          code_iris: Code iris INSEE

          code_qp: identifiant de la table qpv

          code_region_insee: Code région INSEE

          contient_fictive_geom_groupe: Vaut "vrai", si la géométrie du groupe de bâtiment est générée automatiquement
              et ne représente pas la géométrie du groupe de bâtiment.

          geom_groupe: Géométrie multipolygonale du groupe de bâtiment (Lambert-93)

          geom_groupe_pos_wgs84: Point sur la surface du groupe de bâtiment en WSG84

          libelle_commune_insee: (insee) Libellé de la commune accueillant le groupe de bâtiment

          limit: Limiting and Pagination

          nom_qp: Nom du quartier prioritaire dans lequel se trouve le bâtiment

          offset: Limiting and Pagination

          order: Ordering

          quartier_prioritaire: Est situé dans un quartier prioritaire

          s_geom_groupe: Surface au sol de la géométrie du bâtiment groupe (geom_groupe)

          select: Filtering Columns

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "Range": range,
                    "Range-Unit": range_unit,
                }
            ),
            **(extra_headers or {}),
        }
        return self._get_api_list(
            "/donnees/batiment_groupe",
            page=SyncDefault[BatimentGroupe],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "batiment_groupe_id": batiment_groupe_id,
                        "code_commune_insee": code_commune_insee,
                        "code_departement_insee": code_departement_insee,
                        "code_epci_insee": code_epci_insee,
                        "code_iris": code_iris,
                        "code_qp": code_qp,
                        "code_region_insee": code_region_insee,
                        "contient_fictive_geom_groupe": contient_fictive_geom_groupe,
                        "geom_groupe": geom_groupe,
                        "geom_groupe_pos_wgs84": geom_groupe_pos_wgs84,
                        "libelle_commune_insee": libelle_commune_insee,
                        "limit": limit,
                        "nom_qp": nom_qp,
                        "offset": offset,
                        "order": order,
                        "quartier_prioritaire": quartier_prioritaire,
                        "s_geom_groupe": s_geom_groupe,
                        "select": select,
                    },
                    batiment_groupe_list_params.BatimentGroupeListParams,
                ),
            ),
            model=BatimentGroupe,
        )


class AsyncBatimentGroupeResource(AsyncAPIResource):
    @cached_property
    def complet(self) -> AsyncCompletResource:
        return AsyncCompletResource(self._client)

    @cached_property
    def bdtopo_zoac(self) -> AsyncBdtopoZoacResource:
        return AsyncBdtopoZoacResource(self._client)

    @cached_property
    def geospx(self) -> AsyncGeospxResource:
        return AsyncGeospxResource(self._client)

    @cached_property
    def dvf_open_statistique(self) -> AsyncDvfOpenStatistiqueResource:
        return AsyncDvfOpenStatistiqueResource(self._client)

    @cached_property
    def qpv(self) -> AsyncQpvResource:
        return AsyncQpvResource(self._client)

    @cached_property
    def synthese_enveloppe(self) -> AsyncSyntheseEnveloppeResource:
        return AsyncSyntheseEnveloppeResource(self._client)

    @cached_property
    def simulations_dpe(self) -> AsyncSimulationsDpeResource:
        return AsyncSimulationsDpeResource(self._client)

    @cached_property
    def bdtopo_equ(self) -> AsyncBdtopoEquResource:
        return AsyncBdtopoEquResource(self._client)

    @cached_property
    def dpe_representatif_logement(self) -> AsyncDpeRepresentatifLogementResource:
        return AsyncDpeRepresentatifLogementResource(self._client)

    @cached_property
    def dle_gaz_2020(self) -> AsyncDleGaz2020Resource:
        return AsyncDleGaz2020Resource(self._client)

    @cached_property
    def dle_elec_2020(self) -> AsyncDleElec2020Resource:
        return AsyncDleElec2020Resource(self._client)

    @cached_property
    def merimee(self) -> AsyncMerimeeResource:
        return AsyncMerimeeResource(self._client)

    @cached_property
    def dle_reseaux_2020(self) -> AsyncDleReseaux2020Resource:
        return AsyncDleReseaux2020Resource(self._client)

    @cached_property
    def adresse(self) -> AsyncAdresseResource:
        return AsyncAdresseResource(self._client)

    @cached_property
    def dle_gaz_multimillesime(self) -> AsyncDleGazMultimillesimeResource:
        return AsyncDleGazMultimillesimeResource(self._client)

    @cached_property
    def radon(self) -> AsyncRadonResource:
        return AsyncRadonResource(self._client)

    @cached_property
    def dvf_open_representatif(self) -> AsyncDvfOpenRepresentatifResource:
        return AsyncDvfOpenRepresentatifResource(self._client)

    @cached_property
    def simulations_dvf(self) -> AsyncSimulationsDvfResource:
        return AsyncSimulationsDvfResource(self._client)

    @cached_property
    def dpe_statistique_logement(self) -> AsyncDpeStatistiqueLogementResource:
        return AsyncDpeStatistiqueLogementResource(self._client)

    @cached_property
    def dle_reseaux_multimillesime(self) -> AsyncDleReseauxMultimillesimeResource:
        return AsyncDleReseauxMultimillesimeResource(self._client)

    @cached_property
    def rnc(self) -> AsyncRncResource:
        return AsyncRncResource(self._client)

    @cached_property
    def bpe(self) -> AsyncBpeResource:
        return AsyncBpeResource(self._client)

    @cached_property
    def ffo_bat(self) -> AsyncFfoBatResource:
        return AsyncFfoBatResource(self._client)

    @cached_property
    def argiles(self) -> AsyncArgilesResource:
        return AsyncArgilesResource(self._client)

    @cached_property
    def hthd(self) -> AsyncHthdResource:
        return AsyncHthdResource(self._client)

    @cached_property
    def bdtopo_bat(self) -> AsyncBdtopoBatResource:
        return AsyncBdtopoBatResource(self._client)

    @cached_property
    def dle_elec_multimillesime(self) -> AsyncDleElecMultimillesimeResource:
        return AsyncDleElecMultimillesimeResource(self._client)

    @cached_property
    def wall_dict(self) -> AsyncWallDictResource:
        return AsyncWallDictResource(self._client)

    @cached_property
    def indicateur_reseau_chaud_froid(self) -> AsyncIndicateurReseauChaudFroidResource:
        return AsyncIndicateurReseauChaudFroidResource(self._client)

    @cached_property
    def delimitation_enveloppe(self) -> AsyncDelimitationEnveloppeResource:
        return AsyncDelimitationEnveloppeResource(self._client)

    @cached_property
    def simulations_valeur_verte(self) -> AsyncSimulationsValeurVerteResource:
        return AsyncSimulationsValeurVerteResource(self._client)

    @cached_property
    def iris_simulations_valeur_verte(self) -> AsyncIrisSimulationsValeurVerteResource:
        return AsyncIrisSimulationsValeurVerteResource(self._client)

    @cached_property
    def iris_contexte_geographique(self) -> AsyncIrisContexteGeographiqueResource:
        return AsyncIrisContexteGeographiqueResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBatimentGroupeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jplumail/bdnb-client#accessing-raw-response-data-eg-headers
        """
        return AsyncBatimentGroupeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBatimentGroupeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jplumail/bdnb-client#with_streaming_response
        """
        return AsyncBatimentGroupeResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        batiment_groupe_id: str | NotGiven = NOT_GIVEN,
        code_commune_insee: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        code_epci_insee: str | NotGiven = NOT_GIVEN,
        code_iris: str | NotGiven = NOT_GIVEN,
        code_qp: str | NotGiven = NOT_GIVEN,
        code_region_insee: str | NotGiven = NOT_GIVEN,
        contient_fictive_geom_groupe: str | NotGiven = NOT_GIVEN,
        geom_groupe: str | NotGiven = NOT_GIVEN,
        geom_groupe_pos_wgs84: str | NotGiven = NOT_GIVEN,
        libelle_commune_insee: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        nom_qp: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        quartier_prioritaire: str | NotGiven = NOT_GIVEN,
        s_geom_groupe: str | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[BatimentGroupe, AsyncDefault[BatimentGroupe]]:
        """
        Complexes de bâtiments au sens de la BDNB

        Args:
          batiment_groupe_id: Identifiant du groupe de bâtiment au sens de la BDNB

          code_commune_insee: Code INSEE de la commune

          code_departement_insee: Code département INSEE

          code_epci_insee: Code de l'EPCI

          code_iris: Code iris INSEE

          code_qp: identifiant de la table qpv

          code_region_insee: Code région INSEE

          contient_fictive_geom_groupe: Vaut "vrai", si la géométrie du groupe de bâtiment est générée automatiquement
              et ne représente pas la géométrie du groupe de bâtiment.

          geom_groupe: Géométrie multipolygonale du groupe de bâtiment (Lambert-93)

          geom_groupe_pos_wgs84: Point sur la surface du groupe de bâtiment en WSG84

          libelle_commune_insee: (insee) Libellé de la commune accueillant le groupe de bâtiment

          limit: Limiting and Pagination

          nom_qp: Nom du quartier prioritaire dans lequel se trouve le bâtiment

          offset: Limiting and Pagination

          order: Ordering

          quartier_prioritaire: Est situé dans un quartier prioritaire

          s_geom_groupe: Surface au sol de la géométrie du bâtiment groupe (geom_groupe)

          select: Filtering Columns

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "Range": range,
                    "Range-Unit": range_unit,
                }
            ),
            **(extra_headers or {}),
        }
        return self._get_api_list(
            "/donnees/batiment_groupe",
            page=AsyncDefault[BatimentGroupe],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "batiment_groupe_id": batiment_groupe_id,
                        "code_commune_insee": code_commune_insee,
                        "code_departement_insee": code_departement_insee,
                        "code_epci_insee": code_epci_insee,
                        "code_iris": code_iris,
                        "code_qp": code_qp,
                        "code_region_insee": code_region_insee,
                        "contient_fictive_geom_groupe": contient_fictive_geom_groupe,
                        "geom_groupe": geom_groupe,
                        "geom_groupe_pos_wgs84": geom_groupe_pos_wgs84,
                        "libelle_commune_insee": libelle_commune_insee,
                        "limit": limit,
                        "nom_qp": nom_qp,
                        "offset": offset,
                        "order": order,
                        "quartier_prioritaire": quartier_prioritaire,
                        "s_geom_groupe": s_geom_groupe,
                        "select": select,
                    },
                    batiment_groupe_list_params.BatimentGroupeListParams,
                ),
            ),
            model=BatimentGroupe,
        )


class BatimentGroupeResourceWithRawResponse:
    def __init__(self, batiment_groupe: BatimentGroupeResource) -> None:
        self._batiment_groupe = batiment_groupe

        self.list = to_raw_response_wrapper(
            batiment_groupe.list,
        )

    @cached_property
    def complet(self) -> CompletResourceWithRawResponse:
        return CompletResourceWithRawResponse(self._batiment_groupe.complet)

    @cached_property
    def bdtopo_zoac(self) -> BdtopoZoacResourceWithRawResponse:
        return BdtopoZoacResourceWithRawResponse(self._batiment_groupe.bdtopo_zoac)

    @cached_property
    def geospx(self) -> GeospxResourceWithRawResponse:
        return GeospxResourceWithRawResponse(self._batiment_groupe.geospx)

    @cached_property
    def dvf_open_statistique(self) -> DvfOpenStatistiqueResourceWithRawResponse:
        return DvfOpenStatistiqueResourceWithRawResponse(self._batiment_groupe.dvf_open_statistique)

    @cached_property
    def qpv(self) -> QpvResourceWithRawResponse:
        return QpvResourceWithRawResponse(self._batiment_groupe.qpv)

    @cached_property
    def synthese_enveloppe(self) -> SyntheseEnveloppeResourceWithRawResponse:
        return SyntheseEnveloppeResourceWithRawResponse(self._batiment_groupe.synthese_enveloppe)

    @cached_property
    def simulations_dpe(self) -> SimulationsDpeResourceWithRawResponse:
        return SimulationsDpeResourceWithRawResponse(self._batiment_groupe.simulations_dpe)

    @cached_property
    def bdtopo_equ(self) -> BdtopoEquResourceWithRawResponse:
        return BdtopoEquResourceWithRawResponse(self._batiment_groupe.bdtopo_equ)

    @cached_property
    def dpe_representatif_logement(self) -> DpeRepresentatifLogementResourceWithRawResponse:
        return DpeRepresentatifLogementResourceWithRawResponse(self._batiment_groupe.dpe_representatif_logement)

    @cached_property
    def dle_gaz_2020(self) -> DleGaz2020ResourceWithRawResponse:
        return DleGaz2020ResourceWithRawResponse(self._batiment_groupe.dle_gaz_2020)

    @cached_property
    def dle_elec_2020(self) -> DleElec2020ResourceWithRawResponse:
        return DleElec2020ResourceWithRawResponse(self._batiment_groupe.dle_elec_2020)

    @cached_property
    def merimee(self) -> MerimeeResourceWithRawResponse:
        return MerimeeResourceWithRawResponse(self._batiment_groupe.merimee)

    @cached_property
    def dle_reseaux_2020(self) -> DleReseaux2020ResourceWithRawResponse:
        return DleReseaux2020ResourceWithRawResponse(self._batiment_groupe.dle_reseaux_2020)

    @cached_property
    def adresse(self) -> AdresseResourceWithRawResponse:
        return AdresseResourceWithRawResponse(self._batiment_groupe.adresse)

    @cached_property
    def dle_gaz_multimillesime(self) -> DleGazMultimillesimeResourceWithRawResponse:
        return DleGazMultimillesimeResourceWithRawResponse(self._batiment_groupe.dle_gaz_multimillesime)

    @cached_property
    def radon(self) -> RadonResourceWithRawResponse:
        return RadonResourceWithRawResponse(self._batiment_groupe.radon)

    @cached_property
    def dvf_open_representatif(self) -> DvfOpenRepresentatifResourceWithRawResponse:
        return DvfOpenRepresentatifResourceWithRawResponse(self._batiment_groupe.dvf_open_representatif)

    @cached_property
    def simulations_dvf(self) -> SimulationsDvfResourceWithRawResponse:
        return SimulationsDvfResourceWithRawResponse(self._batiment_groupe.simulations_dvf)

    @cached_property
    def dpe_statistique_logement(self) -> DpeStatistiqueLogementResourceWithRawResponse:
        return DpeStatistiqueLogementResourceWithRawResponse(self._batiment_groupe.dpe_statistique_logement)

    @cached_property
    def dle_reseaux_multimillesime(self) -> DleReseauxMultimillesimeResourceWithRawResponse:
        return DleReseauxMultimillesimeResourceWithRawResponse(self._batiment_groupe.dle_reseaux_multimillesime)

    @cached_property
    def rnc(self) -> RncResourceWithRawResponse:
        return RncResourceWithRawResponse(self._batiment_groupe.rnc)

    @cached_property
    def bpe(self) -> BpeResourceWithRawResponse:
        return BpeResourceWithRawResponse(self._batiment_groupe.bpe)

    @cached_property
    def ffo_bat(self) -> FfoBatResourceWithRawResponse:
        return FfoBatResourceWithRawResponse(self._batiment_groupe.ffo_bat)

    @cached_property
    def argiles(self) -> ArgilesResourceWithRawResponse:
        return ArgilesResourceWithRawResponse(self._batiment_groupe.argiles)

    @cached_property
    def hthd(self) -> HthdResourceWithRawResponse:
        return HthdResourceWithRawResponse(self._batiment_groupe.hthd)

    @cached_property
    def bdtopo_bat(self) -> BdtopoBatResourceWithRawResponse:
        return BdtopoBatResourceWithRawResponse(self._batiment_groupe.bdtopo_bat)

    @cached_property
    def dle_elec_multimillesime(self) -> DleElecMultimillesimeResourceWithRawResponse:
        return DleElecMultimillesimeResourceWithRawResponse(self._batiment_groupe.dle_elec_multimillesime)

    @cached_property
    def wall_dict(self) -> WallDictResourceWithRawResponse:
        return WallDictResourceWithRawResponse(self._batiment_groupe.wall_dict)

    @cached_property
    def indicateur_reseau_chaud_froid(self) -> IndicateurReseauChaudFroidResourceWithRawResponse:
        return IndicateurReseauChaudFroidResourceWithRawResponse(self._batiment_groupe.indicateur_reseau_chaud_froid)

    @cached_property
    def delimitation_enveloppe(self) -> DelimitationEnveloppeResourceWithRawResponse:
        return DelimitationEnveloppeResourceWithRawResponse(self._batiment_groupe.delimitation_enveloppe)

    @cached_property
    def simulations_valeur_verte(self) -> SimulationsValeurVerteResourceWithRawResponse:
        return SimulationsValeurVerteResourceWithRawResponse(self._batiment_groupe.simulations_valeur_verte)

    @cached_property
    def iris_simulations_valeur_verte(self) -> IrisSimulationsValeurVerteResourceWithRawResponse:
        return IrisSimulationsValeurVerteResourceWithRawResponse(self._batiment_groupe.iris_simulations_valeur_verte)

    @cached_property
    def iris_contexte_geographique(self) -> IrisContexteGeographiqueResourceWithRawResponse:
        return IrisContexteGeographiqueResourceWithRawResponse(self._batiment_groupe.iris_contexte_geographique)


class AsyncBatimentGroupeResourceWithRawResponse:
    def __init__(self, batiment_groupe: AsyncBatimentGroupeResource) -> None:
        self._batiment_groupe = batiment_groupe

        self.list = async_to_raw_response_wrapper(
            batiment_groupe.list,
        )

    @cached_property
    def complet(self) -> AsyncCompletResourceWithRawResponse:
        return AsyncCompletResourceWithRawResponse(self._batiment_groupe.complet)

    @cached_property
    def bdtopo_zoac(self) -> AsyncBdtopoZoacResourceWithRawResponse:
        return AsyncBdtopoZoacResourceWithRawResponse(self._batiment_groupe.bdtopo_zoac)

    @cached_property
    def geospx(self) -> AsyncGeospxResourceWithRawResponse:
        return AsyncGeospxResourceWithRawResponse(self._batiment_groupe.geospx)

    @cached_property
    def dvf_open_statistique(self) -> AsyncDvfOpenStatistiqueResourceWithRawResponse:
        return AsyncDvfOpenStatistiqueResourceWithRawResponse(self._batiment_groupe.dvf_open_statistique)

    @cached_property
    def qpv(self) -> AsyncQpvResourceWithRawResponse:
        return AsyncQpvResourceWithRawResponse(self._batiment_groupe.qpv)

    @cached_property
    def synthese_enveloppe(self) -> AsyncSyntheseEnveloppeResourceWithRawResponse:
        return AsyncSyntheseEnveloppeResourceWithRawResponse(self._batiment_groupe.synthese_enveloppe)

    @cached_property
    def simulations_dpe(self) -> AsyncSimulationsDpeResourceWithRawResponse:
        return AsyncSimulationsDpeResourceWithRawResponse(self._batiment_groupe.simulations_dpe)

    @cached_property
    def bdtopo_equ(self) -> AsyncBdtopoEquResourceWithRawResponse:
        return AsyncBdtopoEquResourceWithRawResponse(self._batiment_groupe.bdtopo_equ)

    @cached_property
    def dpe_representatif_logement(self) -> AsyncDpeRepresentatifLogementResourceWithRawResponse:
        return AsyncDpeRepresentatifLogementResourceWithRawResponse(self._batiment_groupe.dpe_representatif_logement)

    @cached_property
    def dle_gaz_2020(self) -> AsyncDleGaz2020ResourceWithRawResponse:
        return AsyncDleGaz2020ResourceWithRawResponse(self._batiment_groupe.dle_gaz_2020)

    @cached_property
    def dle_elec_2020(self) -> AsyncDleElec2020ResourceWithRawResponse:
        return AsyncDleElec2020ResourceWithRawResponse(self._batiment_groupe.dle_elec_2020)

    @cached_property
    def merimee(self) -> AsyncMerimeeResourceWithRawResponse:
        return AsyncMerimeeResourceWithRawResponse(self._batiment_groupe.merimee)

    @cached_property
    def dle_reseaux_2020(self) -> AsyncDleReseaux2020ResourceWithRawResponse:
        return AsyncDleReseaux2020ResourceWithRawResponse(self._batiment_groupe.dle_reseaux_2020)

    @cached_property
    def adresse(self) -> AsyncAdresseResourceWithRawResponse:
        return AsyncAdresseResourceWithRawResponse(self._batiment_groupe.adresse)

    @cached_property
    def dle_gaz_multimillesime(self) -> AsyncDleGazMultimillesimeResourceWithRawResponse:
        return AsyncDleGazMultimillesimeResourceWithRawResponse(self._batiment_groupe.dle_gaz_multimillesime)

    @cached_property
    def radon(self) -> AsyncRadonResourceWithRawResponse:
        return AsyncRadonResourceWithRawResponse(self._batiment_groupe.radon)

    @cached_property
    def dvf_open_representatif(self) -> AsyncDvfOpenRepresentatifResourceWithRawResponse:
        return AsyncDvfOpenRepresentatifResourceWithRawResponse(self._batiment_groupe.dvf_open_representatif)

    @cached_property
    def simulations_dvf(self) -> AsyncSimulationsDvfResourceWithRawResponse:
        return AsyncSimulationsDvfResourceWithRawResponse(self._batiment_groupe.simulations_dvf)

    @cached_property
    def dpe_statistique_logement(self) -> AsyncDpeStatistiqueLogementResourceWithRawResponse:
        return AsyncDpeStatistiqueLogementResourceWithRawResponse(self._batiment_groupe.dpe_statistique_logement)

    @cached_property
    def dle_reseaux_multimillesime(self) -> AsyncDleReseauxMultimillesimeResourceWithRawResponse:
        return AsyncDleReseauxMultimillesimeResourceWithRawResponse(self._batiment_groupe.dle_reseaux_multimillesime)

    @cached_property
    def rnc(self) -> AsyncRncResourceWithRawResponse:
        return AsyncRncResourceWithRawResponse(self._batiment_groupe.rnc)

    @cached_property
    def bpe(self) -> AsyncBpeResourceWithRawResponse:
        return AsyncBpeResourceWithRawResponse(self._batiment_groupe.bpe)

    @cached_property
    def ffo_bat(self) -> AsyncFfoBatResourceWithRawResponse:
        return AsyncFfoBatResourceWithRawResponse(self._batiment_groupe.ffo_bat)

    @cached_property
    def argiles(self) -> AsyncArgilesResourceWithRawResponse:
        return AsyncArgilesResourceWithRawResponse(self._batiment_groupe.argiles)

    @cached_property
    def hthd(self) -> AsyncHthdResourceWithRawResponse:
        return AsyncHthdResourceWithRawResponse(self._batiment_groupe.hthd)

    @cached_property
    def bdtopo_bat(self) -> AsyncBdtopoBatResourceWithRawResponse:
        return AsyncBdtopoBatResourceWithRawResponse(self._batiment_groupe.bdtopo_bat)

    @cached_property
    def dle_elec_multimillesime(self) -> AsyncDleElecMultimillesimeResourceWithRawResponse:
        return AsyncDleElecMultimillesimeResourceWithRawResponse(self._batiment_groupe.dle_elec_multimillesime)

    @cached_property
    def wall_dict(self) -> AsyncWallDictResourceWithRawResponse:
        return AsyncWallDictResourceWithRawResponse(self._batiment_groupe.wall_dict)

    @cached_property
    def indicateur_reseau_chaud_froid(self) -> AsyncIndicateurReseauChaudFroidResourceWithRawResponse:
        return AsyncIndicateurReseauChaudFroidResourceWithRawResponse(
            self._batiment_groupe.indicateur_reseau_chaud_froid
        )

    @cached_property
    def delimitation_enveloppe(self) -> AsyncDelimitationEnveloppeResourceWithRawResponse:
        return AsyncDelimitationEnveloppeResourceWithRawResponse(self._batiment_groupe.delimitation_enveloppe)

    @cached_property
    def simulations_valeur_verte(self) -> AsyncSimulationsValeurVerteResourceWithRawResponse:
        return AsyncSimulationsValeurVerteResourceWithRawResponse(self._batiment_groupe.simulations_valeur_verte)

    @cached_property
    def iris_simulations_valeur_verte(self) -> AsyncIrisSimulationsValeurVerteResourceWithRawResponse:
        return AsyncIrisSimulationsValeurVerteResourceWithRawResponse(
            self._batiment_groupe.iris_simulations_valeur_verte
        )

    @cached_property
    def iris_contexte_geographique(self) -> AsyncIrisContexteGeographiqueResourceWithRawResponse:
        return AsyncIrisContexteGeographiqueResourceWithRawResponse(self._batiment_groupe.iris_contexte_geographique)


class BatimentGroupeResourceWithStreamingResponse:
    def __init__(self, batiment_groupe: BatimentGroupeResource) -> None:
        self._batiment_groupe = batiment_groupe

        self.list = to_streamed_response_wrapper(
            batiment_groupe.list,
        )

    @cached_property
    def complet(self) -> CompletResourceWithStreamingResponse:
        return CompletResourceWithStreamingResponse(self._batiment_groupe.complet)

    @cached_property
    def bdtopo_zoac(self) -> BdtopoZoacResourceWithStreamingResponse:
        return BdtopoZoacResourceWithStreamingResponse(self._batiment_groupe.bdtopo_zoac)

    @cached_property
    def geospx(self) -> GeospxResourceWithStreamingResponse:
        return GeospxResourceWithStreamingResponse(self._batiment_groupe.geospx)

    @cached_property
    def dvf_open_statistique(self) -> DvfOpenStatistiqueResourceWithStreamingResponse:
        return DvfOpenStatistiqueResourceWithStreamingResponse(self._batiment_groupe.dvf_open_statistique)

    @cached_property
    def qpv(self) -> QpvResourceWithStreamingResponse:
        return QpvResourceWithStreamingResponse(self._batiment_groupe.qpv)

    @cached_property
    def synthese_enveloppe(self) -> SyntheseEnveloppeResourceWithStreamingResponse:
        return SyntheseEnveloppeResourceWithStreamingResponse(self._batiment_groupe.synthese_enveloppe)

    @cached_property
    def simulations_dpe(self) -> SimulationsDpeResourceWithStreamingResponse:
        return SimulationsDpeResourceWithStreamingResponse(self._batiment_groupe.simulations_dpe)

    @cached_property
    def bdtopo_equ(self) -> BdtopoEquResourceWithStreamingResponse:
        return BdtopoEquResourceWithStreamingResponse(self._batiment_groupe.bdtopo_equ)

    @cached_property
    def dpe_representatif_logement(self) -> DpeRepresentatifLogementResourceWithStreamingResponse:
        return DpeRepresentatifLogementResourceWithStreamingResponse(self._batiment_groupe.dpe_representatif_logement)

    @cached_property
    def dle_gaz_2020(self) -> DleGaz2020ResourceWithStreamingResponse:
        return DleGaz2020ResourceWithStreamingResponse(self._batiment_groupe.dle_gaz_2020)

    @cached_property
    def dle_elec_2020(self) -> DleElec2020ResourceWithStreamingResponse:
        return DleElec2020ResourceWithStreamingResponse(self._batiment_groupe.dle_elec_2020)

    @cached_property
    def merimee(self) -> MerimeeResourceWithStreamingResponse:
        return MerimeeResourceWithStreamingResponse(self._batiment_groupe.merimee)

    @cached_property
    def dle_reseaux_2020(self) -> DleReseaux2020ResourceWithStreamingResponse:
        return DleReseaux2020ResourceWithStreamingResponse(self._batiment_groupe.dle_reseaux_2020)

    @cached_property
    def adresse(self) -> AdresseResourceWithStreamingResponse:
        return AdresseResourceWithStreamingResponse(self._batiment_groupe.adresse)

    @cached_property
    def dle_gaz_multimillesime(self) -> DleGazMultimillesimeResourceWithStreamingResponse:
        return DleGazMultimillesimeResourceWithStreamingResponse(self._batiment_groupe.dle_gaz_multimillesime)

    @cached_property
    def radon(self) -> RadonResourceWithStreamingResponse:
        return RadonResourceWithStreamingResponse(self._batiment_groupe.radon)

    @cached_property
    def dvf_open_representatif(self) -> DvfOpenRepresentatifResourceWithStreamingResponse:
        return DvfOpenRepresentatifResourceWithStreamingResponse(self._batiment_groupe.dvf_open_representatif)

    @cached_property
    def simulations_dvf(self) -> SimulationsDvfResourceWithStreamingResponse:
        return SimulationsDvfResourceWithStreamingResponse(self._batiment_groupe.simulations_dvf)

    @cached_property
    def dpe_statistique_logement(self) -> DpeStatistiqueLogementResourceWithStreamingResponse:
        return DpeStatistiqueLogementResourceWithStreamingResponse(self._batiment_groupe.dpe_statistique_logement)

    @cached_property
    def dle_reseaux_multimillesime(self) -> DleReseauxMultimillesimeResourceWithStreamingResponse:
        return DleReseauxMultimillesimeResourceWithStreamingResponse(self._batiment_groupe.dle_reseaux_multimillesime)

    @cached_property
    def rnc(self) -> RncResourceWithStreamingResponse:
        return RncResourceWithStreamingResponse(self._batiment_groupe.rnc)

    @cached_property
    def bpe(self) -> BpeResourceWithStreamingResponse:
        return BpeResourceWithStreamingResponse(self._batiment_groupe.bpe)

    @cached_property
    def ffo_bat(self) -> FfoBatResourceWithStreamingResponse:
        return FfoBatResourceWithStreamingResponse(self._batiment_groupe.ffo_bat)

    @cached_property
    def argiles(self) -> ArgilesResourceWithStreamingResponse:
        return ArgilesResourceWithStreamingResponse(self._batiment_groupe.argiles)

    @cached_property
    def hthd(self) -> HthdResourceWithStreamingResponse:
        return HthdResourceWithStreamingResponse(self._batiment_groupe.hthd)

    @cached_property
    def bdtopo_bat(self) -> BdtopoBatResourceWithStreamingResponse:
        return BdtopoBatResourceWithStreamingResponse(self._batiment_groupe.bdtopo_bat)

    @cached_property
    def dle_elec_multimillesime(self) -> DleElecMultimillesimeResourceWithStreamingResponse:
        return DleElecMultimillesimeResourceWithStreamingResponse(self._batiment_groupe.dle_elec_multimillesime)

    @cached_property
    def wall_dict(self) -> WallDictResourceWithStreamingResponse:
        return WallDictResourceWithStreamingResponse(self._batiment_groupe.wall_dict)

    @cached_property
    def indicateur_reseau_chaud_froid(self) -> IndicateurReseauChaudFroidResourceWithStreamingResponse:
        return IndicateurReseauChaudFroidResourceWithStreamingResponse(
            self._batiment_groupe.indicateur_reseau_chaud_froid
        )

    @cached_property
    def delimitation_enveloppe(self) -> DelimitationEnveloppeResourceWithStreamingResponse:
        return DelimitationEnveloppeResourceWithStreamingResponse(self._batiment_groupe.delimitation_enveloppe)

    @cached_property
    def simulations_valeur_verte(self) -> SimulationsValeurVerteResourceWithStreamingResponse:
        return SimulationsValeurVerteResourceWithStreamingResponse(self._batiment_groupe.simulations_valeur_verte)

    @cached_property
    def iris_simulations_valeur_verte(self) -> IrisSimulationsValeurVerteResourceWithStreamingResponse:
        return IrisSimulationsValeurVerteResourceWithStreamingResponse(
            self._batiment_groupe.iris_simulations_valeur_verte
        )

    @cached_property
    def iris_contexte_geographique(self) -> IrisContexteGeographiqueResourceWithStreamingResponse:
        return IrisContexteGeographiqueResourceWithStreamingResponse(self._batiment_groupe.iris_contexte_geographique)


class AsyncBatimentGroupeResourceWithStreamingResponse:
    def __init__(self, batiment_groupe: AsyncBatimentGroupeResource) -> None:
        self._batiment_groupe = batiment_groupe

        self.list = async_to_streamed_response_wrapper(
            batiment_groupe.list,
        )

    @cached_property
    def complet(self) -> AsyncCompletResourceWithStreamingResponse:
        return AsyncCompletResourceWithStreamingResponse(self._batiment_groupe.complet)

    @cached_property
    def bdtopo_zoac(self) -> AsyncBdtopoZoacResourceWithStreamingResponse:
        return AsyncBdtopoZoacResourceWithStreamingResponse(self._batiment_groupe.bdtopo_zoac)

    @cached_property
    def geospx(self) -> AsyncGeospxResourceWithStreamingResponse:
        return AsyncGeospxResourceWithStreamingResponse(self._batiment_groupe.geospx)

    @cached_property
    def dvf_open_statistique(self) -> AsyncDvfOpenStatistiqueResourceWithStreamingResponse:
        return AsyncDvfOpenStatistiqueResourceWithStreamingResponse(self._batiment_groupe.dvf_open_statistique)

    @cached_property
    def qpv(self) -> AsyncQpvResourceWithStreamingResponse:
        return AsyncQpvResourceWithStreamingResponse(self._batiment_groupe.qpv)

    @cached_property
    def synthese_enveloppe(self) -> AsyncSyntheseEnveloppeResourceWithStreamingResponse:
        return AsyncSyntheseEnveloppeResourceWithStreamingResponse(self._batiment_groupe.synthese_enveloppe)

    @cached_property
    def simulations_dpe(self) -> AsyncSimulationsDpeResourceWithStreamingResponse:
        return AsyncSimulationsDpeResourceWithStreamingResponse(self._batiment_groupe.simulations_dpe)

    @cached_property
    def bdtopo_equ(self) -> AsyncBdtopoEquResourceWithStreamingResponse:
        return AsyncBdtopoEquResourceWithStreamingResponse(self._batiment_groupe.bdtopo_equ)

    @cached_property
    def dpe_representatif_logement(self) -> AsyncDpeRepresentatifLogementResourceWithStreamingResponse:
        return AsyncDpeRepresentatifLogementResourceWithStreamingResponse(
            self._batiment_groupe.dpe_representatif_logement
        )

    @cached_property
    def dle_gaz_2020(self) -> AsyncDleGaz2020ResourceWithStreamingResponse:
        return AsyncDleGaz2020ResourceWithStreamingResponse(self._batiment_groupe.dle_gaz_2020)

    @cached_property
    def dle_elec_2020(self) -> AsyncDleElec2020ResourceWithStreamingResponse:
        return AsyncDleElec2020ResourceWithStreamingResponse(self._batiment_groupe.dle_elec_2020)

    @cached_property
    def merimee(self) -> AsyncMerimeeResourceWithStreamingResponse:
        return AsyncMerimeeResourceWithStreamingResponse(self._batiment_groupe.merimee)

    @cached_property
    def dle_reseaux_2020(self) -> AsyncDleReseaux2020ResourceWithStreamingResponse:
        return AsyncDleReseaux2020ResourceWithStreamingResponse(self._batiment_groupe.dle_reseaux_2020)

    @cached_property
    def adresse(self) -> AsyncAdresseResourceWithStreamingResponse:
        return AsyncAdresseResourceWithStreamingResponse(self._batiment_groupe.adresse)

    @cached_property
    def dle_gaz_multimillesime(self) -> AsyncDleGazMultimillesimeResourceWithStreamingResponse:
        return AsyncDleGazMultimillesimeResourceWithStreamingResponse(self._batiment_groupe.dle_gaz_multimillesime)

    @cached_property
    def radon(self) -> AsyncRadonResourceWithStreamingResponse:
        return AsyncRadonResourceWithStreamingResponse(self._batiment_groupe.radon)

    @cached_property
    def dvf_open_representatif(self) -> AsyncDvfOpenRepresentatifResourceWithStreamingResponse:
        return AsyncDvfOpenRepresentatifResourceWithStreamingResponse(self._batiment_groupe.dvf_open_representatif)

    @cached_property
    def simulations_dvf(self) -> AsyncSimulationsDvfResourceWithStreamingResponse:
        return AsyncSimulationsDvfResourceWithStreamingResponse(self._batiment_groupe.simulations_dvf)

    @cached_property
    def dpe_statistique_logement(self) -> AsyncDpeStatistiqueLogementResourceWithStreamingResponse:
        return AsyncDpeStatistiqueLogementResourceWithStreamingResponse(self._batiment_groupe.dpe_statistique_logement)

    @cached_property
    def dle_reseaux_multimillesime(self) -> AsyncDleReseauxMultimillesimeResourceWithStreamingResponse:
        return AsyncDleReseauxMultimillesimeResourceWithStreamingResponse(
            self._batiment_groupe.dle_reseaux_multimillesime
        )

    @cached_property
    def rnc(self) -> AsyncRncResourceWithStreamingResponse:
        return AsyncRncResourceWithStreamingResponse(self._batiment_groupe.rnc)

    @cached_property
    def bpe(self) -> AsyncBpeResourceWithStreamingResponse:
        return AsyncBpeResourceWithStreamingResponse(self._batiment_groupe.bpe)

    @cached_property
    def ffo_bat(self) -> AsyncFfoBatResourceWithStreamingResponse:
        return AsyncFfoBatResourceWithStreamingResponse(self._batiment_groupe.ffo_bat)

    @cached_property
    def argiles(self) -> AsyncArgilesResourceWithStreamingResponse:
        return AsyncArgilesResourceWithStreamingResponse(self._batiment_groupe.argiles)

    @cached_property
    def hthd(self) -> AsyncHthdResourceWithStreamingResponse:
        return AsyncHthdResourceWithStreamingResponse(self._batiment_groupe.hthd)

    @cached_property
    def bdtopo_bat(self) -> AsyncBdtopoBatResourceWithStreamingResponse:
        return AsyncBdtopoBatResourceWithStreamingResponse(self._batiment_groupe.bdtopo_bat)

    @cached_property
    def dle_elec_multimillesime(self) -> AsyncDleElecMultimillesimeResourceWithStreamingResponse:
        return AsyncDleElecMultimillesimeResourceWithStreamingResponse(self._batiment_groupe.dle_elec_multimillesime)

    @cached_property
    def wall_dict(self) -> AsyncWallDictResourceWithStreamingResponse:
        return AsyncWallDictResourceWithStreamingResponse(self._batiment_groupe.wall_dict)

    @cached_property
    def indicateur_reseau_chaud_froid(self) -> AsyncIndicateurReseauChaudFroidResourceWithStreamingResponse:
        return AsyncIndicateurReseauChaudFroidResourceWithStreamingResponse(
            self._batiment_groupe.indicateur_reseau_chaud_froid
        )

    @cached_property
    def delimitation_enveloppe(self) -> AsyncDelimitationEnveloppeResourceWithStreamingResponse:
        return AsyncDelimitationEnveloppeResourceWithStreamingResponse(self._batiment_groupe.delimitation_enveloppe)

    @cached_property
    def simulations_valeur_verte(self) -> AsyncSimulationsValeurVerteResourceWithStreamingResponse:
        return AsyncSimulationsValeurVerteResourceWithStreamingResponse(self._batiment_groupe.simulations_valeur_verte)

    @cached_property
    def iris_simulations_valeur_verte(self) -> AsyncIrisSimulationsValeurVerteResourceWithStreamingResponse:
        return AsyncIrisSimulationsValeurVerteResourceWithStreamingResponse(
            self._batiment_groupe.iris_simulations_valeur_verte
        )

    @cached_property
    def iris_contexte_geographique(self) -> AsyncIrisContexteGeographiqueResourceWithStreamingResponse:
        return AsyncIrisContexteGeographiqueResourceWithStreamingResponse(
            self._batiment_groupe.iris_contexte_geographique
        )
