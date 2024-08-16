# Shared Types

```python
from bdnb_api.types import (
    BatimentConstructionAPIExpert,
    BatimentGroupeArgilesAPIExpert,
    BatimentGroupeBdtopoEquAPIExpert,
    BatimentGroupeBdtopoZoacAPIExpert,
    BatimentGroupeBpeAPIExpert,
    BatimentGroupeDelimitationEnveloppeAPIExpert,
    BatimentGroupeDleElec2020APIExpert,
    BatimentGroupeDleGaz2020APIExpert,
    BatimentGroupeDleReseaux2020APIExpert,
    BatimentGroupeDleReseauxMultimillesimeAPIExpert,
    BatimentGroupeDpeRepresentatifLogementAPIExpert,
    BatimentGroupeDvfOpenStatistiqueAPIExpert,
    BatimentGroupeGeospxAPIExpert,
    BatimentGroupeIndicateurReseauChaudFroidAPIExpert,
    BatimentGroupeRncAPIExpert,
    BatimentGroupeSimulationsDpeAPIExpert,
    BatimentGroupeSimulationsValeurVerteAPIExpert,
    BatimentGroupeSyntheseEnveloppeAPIExpert,
    ReferentielAdministratifIrisAPIExpert,
    RelBatimentConstructionAdresseAPIExpert,
    RelBatimentGroupeAdresseAPIExpert,
    RelBatimentGroupeMerimeeAPIExpert,
    RelBatimentGroupeProprietaireSirenAPIExpert,
    RelBatimentGroupeSirenAPIExpert,
)
```

# AutocompletionEntitesTextes

Types:

```python
from bdnb_api.types import (
    AutocompletionEntitesTexteAPIExpert,
    AutocompletionEntitesTexteListResponse,
)
```

Methods:

- <code title="get /autocompletion_entites_texte">client.autocompletion_entites_textes.<a href="./src/bdnb_api/resources/autocompletion_entites_textes.py">list</a>(\*\*<a href="src/bdnb_api/types/autocompletion_entites_texte_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/autocompletion_entites_texte_list_response.py">AutocompletionEntitesTexteListResponse</a></code>

# Geocodage

Types:

```python
from bdnb_api.types import GeocodageListResponse
```

Methods:

- <code title="get /geocodage">client.geocodage.<a href="./src/bdnb_api/resources/geocodage.py">list</a>(\*\*<a href="src/bdnb_api/types/geocodage_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/geocodage_list_response.py">object</a></code>

# Stats

## BatimentGroupes

Types:

```python
from bdnb_api.types.stats import BatimentGroupeJsonStats
```

Methods:

- <code title="get /stats/batiment_groupe">client.stats.batiment_groupes.<a href="./src/bdnb_api/resources/stats/batiment_groupes.py">list</a>(\*\*<a href="src/bdnb_api/types/stats/batiment_groupe_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/stats/batiment_groupe_json_stats.py">BatimentGroupeJsonStats</a></code>

# Donnees

Types:

```python
from bdnb_api.types import AncqpvAPIExpert
```

## BatimentsConstruction

Types:

```python
from bdnb_api.types.donnees import BatimentsConstructionListResponse
```

Methods:

- <code title="get /donnees/batiment_construction">client.donnees.batiments_construction.<a href="./src/bdnb_api/resources/donnees/batiments_construction.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/batiments_construction_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/batiments_construction_list_response.py">BatimentsConstructionListResponse</a></code>

## BatimentsGroupesComplets

Types:

```python
from bdnb_api.types.donnees import (
    BatimentGroupeCompletAPIExpert,
    BatimentsGroupesCompletListResponse,
)
```

Methods:

- <code title="get /donnees/batiment_groupe_complet">client.donnees.batiments_groupes_complets.<a href="./src/bdnb_api/resources/donnees/batiments_groupes_complets/batiments_groupes_complets.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/batiments_groupes_complet_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/batiments_groupes_complet_list_response.py">BatimentsGroupesCompletListResponse</a></code>

### Parcelles

Types:

```python
from bdnb_api.types.donnees.batiments_groupes_complets import (
    BatimentGroupeCompletParcelleAPIExpert,
    ParcelleListResponse,
)
```

Methods:

- <code title="get /donnees/batiment_groupe_complet/parcelle">client.donnees.batiments_groupes_complets.parcelles.<a href="./src/bdnb_api/resources/donnees/batiments_groupes_complets/parcelles.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/batiments_groupes_complets/parcelle_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/batiments_groupes_complets/parcelle_list_response.py">ParcelleListResponse</a></code>

### Adresses

Types:

```python
from bdnb_api.types.donnees.batiments_groupes_complets import (
    BatimentGroupeCompletAdresseAPIExpert,
    AdressListResponse,
)
```

Methods:

- <code title="get /donnees/batiment_groupe_complet/adresse">client.donnees.batiments_groupes_complets.adresses.<a href="./src/bdnb_api/resources/donnees/batiments_groupes_complets/adresses.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/batiments_groupes_complets/adress_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/batiments_groupes_complets/adress_list_response.py">AdressListResponse</a></code>

## TablesBdnb

Types:

```python
from bdnb_api.types.donnees import (
    BatimentGroupeFfoBatAPIExpert,
    BatimentGroupeMerimeeAPIExpert,
    BatimentGroupeQpvAPIExpert,
    IrisContexteGeographiqueAPIExpert,
    IrisSimulationsValeurVerteAPIExpert,
    RelBatimentGroupeQpvAPIExpert,
    RelBatimentGroupeRncAPIExpert,
    RelBatimentGroupeSiretCompletAPIExpert,
    TablesBdnbRetrieveBatimentGroupeBdtopoZoacResponse,
    TablesBdnbRetrieveBatimentGroupeDvfOpenStatistiqueResponse,
    TablesBdnbRetrieveBatimentGroupeGeospxResponse,
    TablesBdnbRetrieveBatimentGroupeQpvResponse,
    TablesBdnbRetrieveBatimentGroupeSyntheseEnveloppeResponse,
    TablesBdnbRetrieveReferentielAdministratifIrisResponse,
    TablesBdnbRetrieveRelBatimentConstructionAdresseResponse,
    TablesBdnbRetrieveRelBatimentGroupeAdresseResponse,
    TablesBdnbRetrieveRelBatimentGroupeProprietaireSirenResponse,
    TablesBdnbRetrieveRelBatimentGroupeQpvResponse,
)
```

Methods:

- <code title="get /donnees/batiment_groupe_bdtopo_zoac">client.donnees.tables_bdnb.<a href="./src/bdnb_api/resources/donnees/tables_bdnb/tables_bdnb.py">retrieve_batiment_groupe_bdtopo_zoac</a>(\*\*<a href="src/bdnb_api/types/donnees/tables_bdnb_retrieve_batiment_groupe_bdtopo_zoac_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/tables_bdnb_retrieve_batiment_groupe_bdtopo_zoac_response.py">TablesBdnbRetrieveBatimentGroupeBdtopoZoacResponse</a></code>
- <code title="get /donnees/batiment_groupe_dvf_open_statistique">client.donnees.tables_bdnb.<a href="./src/bdnb_api/resources/donnees/tables_bdnb/tables_bdnb.py">retrieve_batiment_groupe_dvf_open_statistique</a>(\*\*<a href="src/bdnb_api/types/donnees/tables_bdnb_retrieve_batiment_groupe_dvf_open_statistique_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/tables_bdnb_retrieve_batiment_groupe_dvf_open_statistique_response.py">TablesBdnbRetrieveBatimentGroupeDvfOpenStatistiqueResponse</a></code>
- <code title="get /donnees/batiment_groupe_geospx">client.donnees.tables_bdnb.<a href="./src/bdnb_api/resources/donnees/tables_bdnb/tables_bdnb.py">retrieve_batiment_groupe_geospx</a>(\*\*<a href="src/bdnb_api/types/donnees/tables_bdnb_retrieve_batiment_groupe_geospx_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/tables_bdnb_retrieve_batiment_groupe_geospx_response.py">TablesBdnbRetrieveBatimentGroupeGeospxResponse</a></code>
- <code title="get /donnees/batiment_groupe_qpv">client.donnees.tables_bdnb.<a href="./src/bdnb_api/resources/donnees/tables_bdnb/tables_bdnb.py">retrieve_batiment_groupe_qpv</a>(\*\*<a href="src/bdnb_api/types/donnees/tables_bdnb_retrieve_batiment_groupe_qpv_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/tables_bdnb_retrieve_batiment_groupe_qpv_response.py">TablesBdnbRetrieveBatimentGroupeQpvResponse</a></code>
- <code title="get /donnees/batiment_groupe_synthese_enveloppe">client.donnees.tables_bdnb.<a href="./src/bdnb_api/resources/donnees/tables_bdnb/tables_bdnb.py">retrieve_batiment_groupe_synthese_enveloppe</a>(\*\*<a href="src/bdnb_api/types/donnees/tables_bdnb_retrieve_batiment_groupe_synthese_enveloppe_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/tables_bdnb_retrieve_batiment_groupe_synthese_enveloppe_response.py">TablesBdnbRetrieveBatimentGroupeSyntheseEnveloppeResponse</a></code>
- <code title="get /donnees/referentiel_administratif_iris">client.donnees.tables_bdnb.<a href="./src/bdnb_api/resources/donnees/tables_bdnb/tables_bdnb.py">retrieve_referentiel_administratif_iris</a>(\*\*<a href="src/bdnb_api/types/donnees/tables_bdnb_retrieve_referentiel_administratif_iris_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/tables_bdnb_retrieve_referentiel_administratif_iris_response.py">TablesBdnbRetrieveReferentielAdministratifIrisResponse</a></code>
- <code title="get /donnees/rel_batiment_construction_adresse">client.donnees.tables_bdnb.<a href="./src/bdnb_api/resources/donnees/tables_bdnb/tables_bdnb.py">retrieve_rel_batiment_construction_adresse</a>(\*\*<a href="src/bdnb_api/types/donnees/tables_bdnb_retrieve_rel_batiment_construction_adresse_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/tables_bdnb_retrieve_rel_batiment_construction_adresse_response.py">TablesBdnbRetrieveRelBatimentConstructionAdresseResponse</a></code>
- <code title="get /donnees/rel_batiment_groupe_adresse">client.donnees.tables_bdnb.<a href="./src/bdnb_api/resources/donnees/tables_bdnb/tables_bdnb.py">retrieve_rel_batiment_groupe_adresse</a>(\*\*<a href="src/bdnb_api/types/donnees/tables_bdnb_retrieve_rel_batiment_groupe_adresse_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/tables_bdnb_retrieve_rel_batiment_groupe_adresse_response.py">TablesBdnbRetrieveRelBatimentGroupeAdresseResponse</a></code>
- <code title="get /donnees/rel_batiment_groupe_proprietaire_siren">client.donnees.tables_bdnb.<a href="./src/bdnb_api/resources/donnees/tables_bdnb/tables_bdnb.py">retrieve_rel_batiment_groupe_proprietaire_siren</a>(\*\*<a href="src/bdnb_api/types/donnees/tables_bdnb_retrieve_rel_batiment_groupe_proprietaire_siren_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/tables_bdnb_retrieve_rel_batiment_groupe_proprietaire_siren_response.py">TablesBdnbRetrieveRelBatimentGroupeProprietaireSirenResponse</a></code>
- <code title="get /donnees/rel_batiment_groupe_qpv">client.donnees.tables_bdnb.<a href="./src/bdnb_api/resources/donnees/tables_bdnb/tables_bdnb.py">retrieve_rel_batiment_groupe_qpv</a>(\*\*<a href="src/bdnb_api/types/donnees/tables_bdnb_retrieve_rel_batiment_groupe_qpv_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/tables_bdnb_retrieve_rel_batiment_groupe_qpv_response.py">TablesBdnbRetrieveRelBatimentGroupeQpvResponse</a></code>

### BatimentGroupe

Types:

```python
from bdnb_api.types.donnees.tables_bdnb import BatimentGroupeAPIExpert
```

## BatimentGroupeSimulationsDpe

Types:

```python
from bdnb_api.types.donnees import BatimentGroupeSimulationsDpeListResponse
```

Methods:

- <code title="get /donnees/batiment_groupe_simulations_dpe">client.donnees.batiment_groupe_simulations_dpe.<a href="./src/bdnb_api/resources/donnees/batiment_groupe_simulations_dpe.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/batiment_groupe_simulations_dpe_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/batiment_groupe_simulations_dpe_list_response.py">BatimentGroupeSimulationsDpeListResponse</a></code>

## BatimentGroupeBdtopoEqu

Types:

```python
from bdnb_api.types.donnees import BatimentGroupeBdtopoEquListResponse
```

Methods:

- <code title="get /donnees/batiment_groupe_bdtopo_equ">client.donnees.batiment_groupe_bdtopo_equ.<a href="./src/bdnb_api/resources/donnees/batiment_groupe_bdtopo_equ.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/batiment_groupe_bdtopo_equ_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/batiment_groupe_bdtopo_equ_list_response.py">BatimentGroupeBdtopoEquListResponse</a></code>

## BatimentGroupeDpeRepresentatifLogement

Types:

```python
from bdnb_api.types.donnees import BatimentGroupeDpeRepresentatifLogementListResponse
```

Methods:

- <code title="get /donnees/batiment_groupe_dpe_representatif_logement">client.donnees.batiment_groupe_dpe_representatif_logement.<a href="./src/bdnb_api/resources/donnees/batiment_groupe_dpe_representatif_logement.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/batiment_groupe_dpe_representatif_logement_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/batiment_groupe_dpe_representatif_logement_list_response.py">BatimentGroupeDpeRepresentatifLogementListResponse</a></code>

## BatimentGroupeDleGaz2020

Types:

```python
from bdnb_api.types.donnees import BatimentGroupeDleGaz2020ListResponse
```

Methods:

- <code title="get /donnees/batiment_groupe_dle_gaz_2020">client.donnees.batiment_groupe_dle_gaz_2020.<a href="./src/bdnb_api/resources/donnees/batiment_groupe_dle_gaz_2020.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/batiment_groupe_dle_gaz_2020_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/batiment_groupe_dle_gaz_2020_list_response.py">BatimentGroupeDleGaz2020ListResponse</a></code>

## BatimentGroupe

Types:

```python
from bdnb_api.types.donnees import BatimentGroupeListResponse
```

Methods:

- <code title="get /donnees/batiment_groupe">client.donnees.batiment_groupe.<a href="./src/bdnb_api/resources/donnees/batiment_groupe.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/batiment_groupe_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/batiment_groupe_list_response.py">BatimentGroupeListResponse</a></code>

## RelBatimentGroupeMerimee

Types:

```python
from bdnb_api.types.donnees import RelBatimentGroupeMerimeeListResponse
```

Methods:

- <code title="get /donnees/rel_batiment_groupe_merimee">client.donnees.rel_batiment_groupe_merimee.<a href="./src/bdnb_api/resources/donnees/rel_batiment_groupe_merimee.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/rel_batiment_groupe_merimee_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/rel_batiment_groupe_merimee_list_response.py">RelBatimentGroupeMerimeeListResponse</a></code>

## BatimentGroupeDleElec2020

Types:

```python
from bdnb_api.types.donnees import BatimentGroupeDleElec2020ListResponse
```

Methods:

- <code title="get /donnees/batiment_groupe_dle_elec_2020">client.donnees.batiment_groupe_dle_elec_2020.<a href="./src/bdnb_api/resources/donnees/batiment_groupe_dle_elec_2020.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/batiment_groupe_dle_elec_2020_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/batiment_groupe_dle_elec_2020_list_response.py">BatimentGroupeDleElec2020ListResponse</a></code>

## BatimentGroupeMerimee

Types:

```python
from bdnb_api.types.donnees import BatimentGroupeMerimeeListResponse
```

Methods:

- <code title="get /donnees/batiment_groupe_merimee">client.donnees.batiment_groupe_merimee.<a href="./src/bdnb_api/resources/donnees/batiment_groupe_merimee.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/batiment_groupe_merimee_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/batiment_groupe_merimee_list_response.py">BatimentGroupeMerimeeListResponse</a></code>

## ReferentielAdministratifRegion

Types:

```python
from bdnb_api.types.donnees import ReferentielAdministratifRegionListResponse
```

Methods:

- <code title="get /donnees/referentiel_administratif_region">client.donnees.referentiel_administratif_region.<a href="./src/bdnb_api/resources/donnees/referentiel_administratif_region.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/referentiel_administratif_region_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/referentiel_administratif_region_list_response.py">ReferentielAdministratifRegionListResponse</a></code>

## BatimentGroupeDleReseaux2020

Types:

```python
from bdnb_api.types.donnees import BatimentGroupeDleReseaux2020ListResponse
```

Methods:

- <code title="get /donnees/batiment_groupe_dle_reseaux_2020">client.donnees.batiment_groupe_dle_reseaux_2020.<a href="./src/bdnb_api/resources/donnees/batiment_groupe_dle_reseaux_2020.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/batiment_groupe_dle_reseaux_2020_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/batiment_groupe_dle_reseaux_2020_list_response.py">BatimentGroupeDleReseaux2020ListResponse</a></code>

## Ancqpv

Types:

```python
from bdnb_api.types.donnees import AncqpvListResponse
```

Methods:

- <code title="get /donnees/ancqpv">client.donnees.ancqpv.<a href="./src/bdnb_api/resources/donnees/ancqpv.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/ancqpv_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/ancqpv_list_response.py">AncqpvListResponse</a></code>

## BatimentGroupeAdresse

Types:

```python
from bdnb_api.types.donnees import BatimentGroupeAdresseAPIExpert, BatimentGroupeAdresseListResponse
```

Methods:

- <code title="get /donnees/batiment_groupe_adresse">client.donnees.batiment_groupe_adresse.<a href="./src/bdnb_api/resources/donnees/batiment_groupe_adresse.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/batiment_groupe_adresse_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/batiment_groupe_adresse_list_response.py">BatimentGroupeAdresseListResponse</a></code>

## BatimentGroupeDleGazMultimillesime

Types:

```python
from bdnb_api.types.donnees import (
    BatimentGroupeDleGazMultimillesimeAPIExpert,
    BatimentGroupeDleGazMultimillesimeListResponse,
)
```

Methods:

- <code title="get /donnees/batiment_groupe_dle_gaz_multimillesime">client.donnees.batiment_groupe_dle_gaz_multimillesime.<a href="./src/bdnb_api/resources/donnees/batiment_groupe_dle_gaz_multimillesime.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/batiment_groupe_dle_gaz_multimillesime_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/batiment_groupe_dle_gaz_multimillesime_list_response.py">BatimentGroupeDleGazMultimillesimeListResponse</a></code>

## RelBatimentGroupeParcelle

Types:

```python
from bdnb_api.types.donnees import (
    RelBatimentGroupeParcelleAPIExpert,
    RelBatimentGroupeParcelleListResponse,
)
```

Methods:

- <code title="get /donnees/rel_batiment_groupe_parcelle">client.donnees.rel_batiment_groupe_parcelle.<a href="./src/bdnb_api/resources/donnees/rel_batiment_groupe_parcelle.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/rel_batiment_groupe_parcelle_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/rel_batiment_groupe_parcelle_list_response.py">RelBatimentGroupeParcelleListResponse</a></code>

## BatimentGroupeRadon

Types:

```python
from bdnb_api.types.donnees import BatimentGroupeRadonAPIExpert, BatimentGroupeRadonListResponse
```

Methods:

- <code title="get /donnees/batiment_groupe_radon">client.donnees.batiment_groupe_radon.<a href="./src/bdnb_api/resources/donnees/batiment_groupe_radon.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/batiment_groupe_radon_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/batiment_groupe_radon_list_response.py">BatimentGroupeRadonListResponse</a></code>

## BatimentGroupeDvfOpenRepresentatif

Types:

```python
from bdnb_api.types.donnees import (
    BatimentGroupeDvfOpenRepresentatifAPIExpert,
    BatimentGroupeDvfOpenRepresentatifListResponse,
)
```

Methods:

- <code title="get /donnees/batiment_groupe_dvf_open_representatif">client.donnees.batiment_groupe_dvf_open_representatif.<a href="./src/bdnb_api/resources/donnees/batiment_groupe_dvf_open_representatif.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/batiment_groupe_dvf_open_representatif_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/batiment_groupe_dvf_open_representatif_list_response.py">BatimentGroupeDvfOpenRepresentatifListResponse</a></code>

## BatimentGroupeSimulationsDvf

Types:

```python
from bdnb_api.types.donnees import (
    BatimentGroupeSimulationsDvfAPIExpert,
    BatimentGroupeSimulationsDvfListResponse,
)
```

Methods:

- <code title="get /donnees/batiment_groupe_simulations_dvf">client.donnees.batiment_groupe_simulations_dvf.<a href="./src/bdnb_api/resources/donnees/batiment_groupe_simulations_dvf.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/batiment_groupe_simulations_dvf_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/batiment_groupe_simulations_dvf_list_response.py">BatimentGroupeSimulationsDvfListResponse</a></code>

## BatimentGroupeDpeStatistiqueLogement

Types:

```python
from bdnb_api.types.donnees import (
    BatimentGroupeDpeStatistiqueLogementAPIExpert,
    BatimentGroupeDpeStatistiqueLogementListResponse,
)
```

Methods:

- <code title="get /donnees/batiment_groupe_dpe_statistique_logement">client.donnees.batiment_groupe_dpe_statistique_logement.<a href="./src/bdnb_api/resources/donnees/batiment_groupe_dpe_statistique_logement.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/batiment_groupe_dpe_statistique_logement_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/batiment_groupe_dpe_statistique_logement_list_response.py">BatimentGroupeDpeStatistiqueLogementListResponse</a></code>

## BatimentGroupeComplet

### Bbox

Types:

```python
from bdnb_api.types.donnees.batiment_groupe_complet import BboxListResponse
```

Methods:

- <code title="get /donnees/batiment_groupe_complet/bbox">client.donnees.batiment_groupe_complet.bbox.<a href="./src/bdnb_api/resources/donnees/batiment_groupe_complet/bbox.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/batiment_groupe_complet/bbox_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/batiment_groupe_complet/bbox_list_response.py">BboxListResponse</a></code>

### Polygon

Types:

```python
from bdnb_api.types.donnees.batiment_groupe_complet import PolygonCreateResponse
```

Methods:

- <code title="post /donnees/batiment_groupe_complet/polygon">client.donnees.batiment_groupe_complet.polygon.<a href="./src/bdnb_api/resources/donnees/batiment_groupe_complet/polygon.py">create</a>(\*\*<a href="src/bdnb_api/types/donnees/batiment_groupe_complet/polygon_create_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/batiment_groupe_complet/polygon_create_response.py">PolygonCreateResponse</a></code>

# Metadonnees

## ColonnesSouscription

Types:

```python
from bdnb_api.types.metadonnees import ColonneSouscription, ColonnesSouscriptionListResponse
```

Methods:

- <code title="get /metadonnees/colonne_souscription">client.metadonnees.colonnes_souscription.<a href="./src/bdnb_api/resources/metadonnees/colonnes_souscription.py">list</a>(\*\*<a href="src/bdnb_api/types/metadonnees/colonnes_souscription_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/metadonnees/colonnes_souscription_list_response.py">ColonnesSouscriptionListResponse</a></code>

## Colonnes

Types:

```python
from bdnb_api.types.metadonnees import Colonne, ColonneListResponse
```

Methods:

- <code title="get /metadonnees/colonne">client.metadonnees.colonnes.<a href="./src/bdnb_api/resources/metadonnees/colonnes.py">list</a>(\*\*<a href="src/bdnb_api/types/metadonnees/colonne_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/metadonnees/colonne_list_response.py">ColonneListResponse</a></code>

## MetadonneesComplets

Types:

```python
from bdnb_api.types.metadonnees import MetadonneesComplet, MetadonneesCompletListResponse
```

Methods:

- <code title="get /metadonnees/metadonnees_complet">client.metadonnees.metadonnees_complets.<a href="./src/bdnb_api/resources/metadonnees/metadonnees_complets.py">list</a>(\*\*<a href="src/bdnb_api/types/metadonnees/metadonnees_complet_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/metadonnees/metadonnees_complet_list_response.py">MetadonneesCompletListResponse</a></code>

## RelColonneJeuDeDonnees

Types:

```python
from bdnb_api.types.metadonnees import RelColonneJeuDeDonneeListResponse
```

Methods:

- <code title="get /metadonnees/rel_colonne_jeu_de_donnees">client.metadonnees.rel_colonne_jeu_de_donnees.<a href="./src/bdnb_api/resources/metadonnees/rel_colonne_jeu_de_donnees.py">list</a>(\*\*<a href="src/bdnb_api/types/metadonnees/rel_colonne_jeu_de_donnee_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/metadonnees/rel_colonne_jeu_de_donnee_list_response.py">RelColonneJeuDeDonneeListResponse</a></code>

## JeuDeDonnees

Types:

```python
from bdnb_api.types.metadonnees import JeuDeDonneeListResponse
```

Methods:

- <code title="get /metadonnees/jeu_de_donnees">client.metadonnees.jeu_de_donnees.<a href="./src/bdnb_api/resources/metadonnees/jeu_de_donnees.py">list</a>(\*\*<a href="src/bdnb_api/types/metadonnees/jeu_de_donnee_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/metadonnees/jeu_de_donnee_list_response.py">JeuDeDonneeListResponse</a></code>

# MetaDonnees

## Info

Types:

```python
from bdnb_api.types.meta_donnees import Info, InfoListResponse
```

Methods:

- <code title="get /metadonnees/info">client.meta_donnees.info.<a href="./src/bdnb_api/resources/meta_donnees/info.py">list</a>(\*\*<a href="src/bdnb_api/types/meta_donnees/info_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/meta_donnees/info_list_response.py">InfoListResponse</a></code>

## Table

Types:

```python
from bdnb_api.types.meta_donnees import Table, TableListResponse
```

Methods:

- <code title="get /metadonnees/table">client.meta_donnees.table.<a href="./src/bdnb_api/resources/meta_donnees/table.py">list</a>(\*\*<a href="src/bdnb_api/types/meta_donnees/table_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/meta_donnees/table_list_response.py">TableListResponse</a></code>

## Fournisseur

Types:

```python
from bdnb_api.types.meta_donnees import Fournisseur, FournisseurRetrieveResponse
```

Methods:

- <code title="get /metadonnees/fournisseur">client.meta_donnees.fournisseur.<a href="./src/bdnb_api/resources/meta_donnees/fournisseur.py">retrieve</a>(\*\*<a href="src/bdnb_api/types/meta_donnees/fournisseur_retrieve_params.py">params</a>) -> <a href="./src/bdnb_api/types/meta_donnees/fournisseur_retrieve_response.py">FournisseurRetrieveResponse</a></code>

## ContrainteAcces

Types:

```python
from bdnb_api.types.meta_donnees import ContrainteAcces, ContrainteAcceRetrieveResponse
```

Methods:

- <code title="get /metadonnees/contrainte_acces">client.meta_donnees.contrainte_acces.<a href="./src/bdnb_api/resources/meta_donnees/contrainte_acces.py">retrieve</a>(\*\*<a href="src/bdnb_api/types/meta_donnees/contrainte_acce_retrieve_params.py">params</a>) -> <a href="./src/bdnb_api/types/meta_donnees/contrainte_acce_retrieve_response.py">ContrainteAcceRetrieveResponse</a></code>

## RelColonneJeuDeDonnees

Types:

```python
from bdnb_api.types.meta_donnees import RelColonneJeuDeDonnees
```

## JeuDeDonnees

Types:

```python
from bdnb_api.types.meta_donnees import JeuDeDonnees
```

# Tuiles

## Vectorielles

### Epci

Methods:

- <code title="get /tuiles/epci/{zoom}/{x}/{y}.pbf">client.tuiles.vectorielles.epci.<a href="./src/bdnb_api/resources/tuiles/vectorielles/epci.py">list</a>(y, \*, zoom, x) -> BinaryAPIResponse</code>

### Region

Methods:

- <code title="get /tuiles/region/{zoom}/{x}/{y}.pbf">client.tuiles.vectorielles.region.<a href="./src/bdnb_api/resources/tuiles/vectorielles/region.py">list</a>(y, \*, zoom, x) -> BinaryAPIResponse</code>

### Iris

Methods:

- <code title="get /tuiles/iris/{zoom}/{x}/{y}.pbf">client.tuiles.vectorielles.iris.<a href="./src/bdnb_api/resources/tuiles/vectorielles/iris.py">list</a>(y, \*, zoom, x) -> BinaryAPIResponse</code>

### Departement

Methods:

- <code title="get /tuiles/departement/{zoom}/{x}/{y}.pbf">client.tuiles.vectorielles.departement.<a href="./src/bdnb_api/resources/tuiles/vectorielles/departement.py">list</a>(y, \*, zoom, x) -> BinaryAPIResponse</code>

### BatimentGroupe

Methods:

- <code title="get /tuiles/batiment_groupe/{zoom}/{x}/{y}.pbf">client.tuiles.vectorielles.batiment_groupe.<a href="./src/bdnb_api/resources/tuiles/vectorielles/batiment_groupe.py">list</a>(y, \*, zoom, x) -> BinaryAPIResponse</code>

# TablesBdnb

## BatimentGroupeIndicateurReseauChaudFroid

Types:

```python
from bdnb_api.types.tables_bdnb import BatimentGroupeIndicateurReseauChaudFroidListResponse
```

Methods:

- <code title="get /donnees/batiment_groupe_indicateur_reseau_chaud_froid">client.tables_bdnb.batiment_groupe_indicateur_reseau_chaud_froid.<a href="./src/bdnb_api/resources/tables_bdnb/batiment_groupe_indicateur_reseau_chaud_froid.py">list</a>(\*\*<a href="src/bdnb_api/types/tables_bdnb/batiment_groupe_indicateur_reseau_chaud_froid_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/tables_bdnb/batiment_groupe_indicateur_reseau_chaud_froid_list_response.py">BatimentGroupeIndicateurReseauChaudFroidListResponse</a></code>

## BatimentGroupeDelimitationEnveloppe

Types:

```python
from bdnb_api.types.tables_bdnb import BatimentGroupeDelimitationEnveloppeListResponse
```

Methods:

- <code title="get /donnees/batiment_groupe_delimitation_enveloppe">client.tables_bdnb.batiment_groupe_delimitation_enveloppe.<a href="./src/bdnb_api/resources/tables_bdnb/batiment_groupe_delimitation_enveloppe.py">list</a>(\*\*<a href="src/bdnb_api/types/tables_bdnb/batiment_groupe_delimitation_enveloppe_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/tables_bdnb/batiment_groupe_delimitation_enveloppe_list_response.py">BatimentGroupeDelimitationEnveloppeListResponse</a></code>

## BatimentGroupeSimulationsValeurVerte

Types:

```python
from bdnb_api.types.tables_bdnb import BatimentGroupeSimulationsValeurVerteListResponse
```

Methods:

- <code title="get /donnees/batiment_groupe_simulations_valeur_verte">client.tables_bdnb.batiment_groupe_simulations_valeur_verte.<a href="./src/bdnb_api/resources/tables_bdnb/batiment_groupe_simulations_valeur_verte.py">list</a>(\*\*<a href="src/bdnb_api/types/tables_bdnb/batiment_groupe_simulations_valeur_verte_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/tables_bdnb/batiment_groupe_simulations_valeur_verte_list_response.py">BatimentGroupeSimulationsValeurVerteListResponse</a></code>

## Donnees

### IrisSimulationsValeurVerte

Types:

```python
from bdnb_api.types.tables_bdnb.donnees import IrisSimulationsValeurVerteListResponse
```

Methods:

- <code title="get /donnees/iris_simulations_valeur_verte">client.tables_bdnb.donnees.iris_simulations_valeur_verte.<a href="./src/bdnb_api/resources/tables_bdnb/donnees/iris_simulations_valeur_verte.py">list</a>(\*\*<a href="src/bdnb_api/types/tables_bdnb/donnees/iris_simulations_valeur_verte_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/tables_bdnb/donnees/iris_simulations_valeur_verte_list_response.py">IrisSimulationsValeurVerteListResponse</a></code>

### IrisContexteGeographique

Types:

```python
from bdnb_api.types.tables_bdnb.donnees import IrisContexteGeographiqueListResponse
```

Methods:

- <code title="get /donnees/iris_contexte_geographique">client.tables_bdnb.donnees.iris_contexte_geographique.<a href="./src/bdnb_api/resources/tables_bdnb/donnees/iris_contexte_geographique.py">list</a>(\*\*<a href="src/bdnb_api/types/tables_bdnb/donnees/iris_contexte_geographique_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/tables_bdnb/donnees/iris_contexte_geographique_list_response.py">IrisContexteGeographiqueListResponse</a></code>

### RelBatimentGroupeSirenComplet

Types:

```python
from bdnb_api.types.tables_bdnb.donnees import RelBatimentGroupeSirenCompletListResponse
```

Methods:

- <code title="get /donnees/rel_batiment_groupe_siren_complet">client.tables_bdnb.donnees.rel_batiment_groupe_siren_complet.<a href="./src/bdnb_api/resources/tables_bdnb/donnees/rel_batiment_groupe_siren_complet.py">list</a>(\*\*<a href="src/bdnb_api/types/tables_bdnb/donnees/rel_batiment_groupe_siren_complet_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/tables_bdnb/donnees/rel_batiment_groupe_siren_complet_list_response.py">RelBatimentGroupeSirenCompletListResponse</a></code>

### RelBatimentGroupeSiretComplet

Types:

```python
from bdnb_api.types.tables_bdnb.donnees import RelBatimentGroupeSiretCompletListResponse
```

Methods:

- <code title="get /donnees/rel_batiment_groupe_siret_complet">client.tables_bdnb.donnees.rel_batiment_groupe_siret_complet.<a href="./src/bdnb_api/resources/tables_bdnb/donnees/rel_batiment_groupe_siret_complet.py">list</a>(\*\*<a href="src/bdnb_api/types/tables_bdnb/donnees/rel_batiment_groupe_siret_complet_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/tables_bdnb/donnees/rel_batiment_groupe_siret_complet_list_response.py">RelBatimentGroupeSiretCompletListResponse</a></code>

### BatimentGroupeDleReseauxMultimillesime

Types:

```python
from bdnb_api.types.tables_bdnb.donnees import BatimentGroupeDleReseauxMultimillesimeListResponse
```

Methods:

- <code title="get /donnees/batiment_groupe_dle_reseaux_multimillesime">client.tables_bdnb.donnees.batiment_groupe_dle_reseaux_multimillesime.<a href="./src/bdnb_api/resources/tables_bdnb/donnees/batiment_groupe_dle_reseaux_multimillesime.py">list</a>(\*\*<a href="src/bdnb_api/types/tables_bdnb/donnees/batiment_groupe_dle_reseaux_multimillesime_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/tables_bdnb/donnees/batiment_groupe_dle_reseaux_multimillesime_list_response.py">BatimentGroupeDleReseauxMultimillesimeListResponse</a></code>

### BatimentGroupeRnc

Types:

```python
from bdnb_api.types.tables_bdnb.donnees import BatimentGroupeRncListResponse
```

Methods:

- <code title="get /donnees/batiment_groupe_rnc">client.tables_bdnb.donnees.batiment_groupe_rnc.<a href="./src/bdnb_api/resources/tables_bdnb/donnees/batiment_groupe_rnc.py">list</a>(\*\*<a href="src/bdnb_api/types/tables_bdnb/donnees/batiment_groupe_rnc_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/tables_bdnb/donnees/batiment_groupe_rnc_list_response.py">BatimentGroupeRncListResponse</a></code>

### BatimentGroupeBpe

Types:

```python
from bdnb_api.types.tables_bdnb.donnees import BatimentGroupeBpeListResponse
```

Methods:

- <code title="get /donnees/batiment_groupe_bpe">client.tables_bdnb.donnees.batiment_groupe_bpe.<a href="./src/bdnb_api/resources/tables_bdnb/donnees/batiment_groupe_bpe.py">list</a>(\*\*<a href="src/bdnb_api/types/tables_bdnb/donnees/batiment_groupe_bpe_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/tables_bdnb/donnees/batiment_groupe_bpe_list_response.py">BatimentGroupeBpeListResponse</a></code>

### BatimentGroupeFfoBat

Types:

```python
from bdnb_api.types.tables_bdnb.donnees import BatimentGroupeFfoBatListResponse
```

Methods:

- <code title="get /donnees/batiment_groupe_ffo_bat">client.tables_bdnb.donnees.batiment_groupe_ffo_bat.<a href="./src/bdnb_api/resources/tables_bdnb/donnees/batiment_groupe_ffo_bat.py">list</a>(\*\*<a href="src/bdnb_api/types/tables_bdnb/donnees/batiment_groupe_ffo_bat_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/tables_bdnb/donnees/batiment_groupe_ffo_bat_list_response.py">BatimentGroupeFfoBatListResponse</a></code>

### RelBatimentGroupeRnc

Types:

```python
from bdnb_api.types.tables_bdnb.donnees import RelBatimentGroupeRncListResponse
```

Methods:

- <code title="get /donnees/rel_batiment_groupe_rnc">client.tables_bdnb.donnees.rel_batiment_groupe_rnc.<a href="./src/bdnb_api/resources/tables_bdnb/donnees/rel_batiment_groupe_rnc.py">list</a>(\*\*<a href="src/bdnb_api/types/tables_bdnb/donnees/rel_batiment_groupe_rnc_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/tables_bdnb/donnees/rel_batiment_groupe_rnc_list_response.py">RelBatimentGroupeRncListResponse</a></code>

### BatimentGroupeArgiles

Types:

```python
from bdnb_api.types.tables_bdnb.donnees import BatimentGroupeArgileListResponse
```

Methods:

- <code title="get /donnees/batiment_groupe_argiles">client.tables_bdnb.donnees.batiment_groupe_argiles.<a href="./src/bdnb_api/resources/tables_bdnb/donnees/batiment_groupe_argiles.py">list</a>(\*\*<a href="src/bdnb_api/types/tables_bdnb/donnees/batiment_groupe_argile_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/tables_bdnb/donnees/batiment_groupe_argile_list_response.py">BatimentGroupeArgileListResponse</a></code>

## ExtBatimentGroupeLBdtopoBatCleabs

Types:

```python
from bdnb_api.types.tables_bdnb import (
    ExtBatimentGroupeLBdtopoBatCleabsAPIExpert,
    ExtBatimentGroupeLBdtopoBatCleabListResponse,
)
```

Methods:

- <code title="get /donnees/ext_batiment_groupe_l_bdtopo_bat_cleabs">client.tables_bdnb.ext_batiment_groupe_l_bdtopo_bat_cleabs.<a href="./src/bdnb_api/resources/tables_bdnb/ext_batiment_groupe_l_bdtopo_bat_cleabs.py">list</a>(\*\*<a href="src/bdnb_api/types/tables_bdnb/ext_batiment_groupe_l_bdtopo_bat_cleab_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/tables_bdnb/ext_batiment_groupe_l_bdtopo_bat_cleab_list_response.py">ExtBatimentGroupeLBdtopoBatCleabListResponse</a></code>

## BatimentGroupeHthd

Types:

```python
from bdnb_api.types.tables_bdnb import BatimentGroupeHthdAPIExpert, BatimentGroupeHthdListResponse
```

Methods:

- <code title="get /donnees/batiment_groupe_hthd">client.tables_bdnb.batiment_groupe_hthd.<a href="./src/bdnb_api/resources/tables_bdnb/batiment_groupe_hthd.py">list</a>(\*\*<a href="src/bdnb_api/types/tables_bdnb/batiment_groupe_hthd_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/tables_bdnb/batiment_groupe_hthd_list_response.py">BatimentGroupeHthdListResponse</a></code>

## Proprietaire

Types:

```python
from bdnb_api.types.tables_bdnb import ProprietaireAPIExpert, ProprietaireListResponse
```

Methods:

- <code title="get /donnees/proprietaire">client.tables_bdnb.proprietaire.<a href="./src/bdnb_api/resources/tables_bdnb/proprietaire.py">list</a>(\*\*<a href="src/bdnb_api/types/tables_bdnb/proprietaire_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/tables_bdnb/proprietaire_list_response.py">ProprietaireListResponse</a></code>

## BatimentGroupeBdtopoBat

Types:

```python
from bdnb_api.types.tables_bdnb import (
    BatimentGroupeBdtopoBatAPIExpert,
    BatimentGroupeBdtopoBatListResponse,
)
```

Methods:

- <code title="get /donnees/batiment_groupe_bdtopo_bat">client.tables_bdnb.batiment_groupe_bdtopo_bat.<a href="./src/bdnb_api/resources/tables_bdnb/batiment_groupe_bdtopo_bat.py">list</a>(\*\*<a href="src/bdnb_api/types/tables_bdnb/batiment_groupe_bdtopo_bat_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/tables_bdnb/batiment_groupe_bdtopo_bat_list_response.py">BatimentGroupeBdtopoBatListResponse</a></code>

## RelBatimentGroupeProprietaireSirenOpen

Types:

```python
from bdnb_api.types.tables_bdnb import (
    RelBatimentGroupeProprietaireSirenOpenAPIExpert,
    RelBatimentGroupeProprietaireSirenOpenListResponse,
)
```

Methods:

- <code title="get /donnees/rel_batiment_groupe_proprietaire_siren_open">client.tables_bdnb.rel_batiment_groupe_proprietaire_siren_open.<a href="./src/bdnb_api/resources/tables_bdnb/rel_batiment_groupe_proprietaire_siren_open.py">list</a>(\*\*<a href="src/bdnb_api/types/tables_bdnb/rel_batiment_groupe_proprietaire_siren_open_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/tables_bdnb/rel_batiment_groupe_proprietaire_siren_open_list_response.py">RelBatimentGroupeProprietaireSirenOpenListResponse</a></code>

## BatimentGroupeDleElecMultimillesime

Types:

```python
from bdnb_api.types.tables_bdnb import (
    BatimentGroupeDleElecMultimillesimeAPIExpert,
    BatimentGroupeDleElecMultimillesimeListResponse,
)
```

Methods:

- <code title="get /donnees/batiment_groupe_dle_elec_multimillesime">client.tables_bdnb.batiment_groupe_dle_elec_multimillesime.<a href="./src/bdnb_api/resources/tables_bdnb/batiment_groupe_dle_elec_multimillesime.py">list</a>(\*\*<a href="src/bdnb_api/types/tables_bdnb/batiment_groupe_dle_elec_multimillesime_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/tables_bdnb/batiment_groupe_dle_elec_multimillesime_list_response.py">BatimentGroupeDleElecMultimillesimeListResponse</a></code>

## Adresse

Types:

```python
from bdnb_api.types.tables_bdnb import AdresseAPIExpert, AdresseListResponse
```

Methods:

- <code title="get /donnees/adresse">client.tables_bdnb.adresse.<a href="./src/bdnb_api/resources/tables_bdnb/adresse.py">list</a>(\*\*<a href="src/bdnb_api/types/tables_bdnb/adresse_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/tables_bdnb/adresse_list_response.py">AdresseListResponse</a></code>

## BatimentGroupeWallDict

Types:

```python
from bdnb_api.types.tables_bdnb import (
    BatimentGroupeWallDictAPIExpert,
    BatimentGroupeWallDictListResponse,
)
```

Methods:

- <code title="get /donnees/batiment_groupe_wall_dict">client.tables_bdnb.batiment_groupe_wall_dict.<a href="./src/bdnb_api/resources/tables_bdnb/batiment_groupe_wall_dict.py">list</a>(\*\*<a href="src/bdnb_api/types/tables_bdnb/batiment_groupe_wall_dict_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/tables_bdnb/batiment_groupe_wall_dict_list_response.py">BatimentGroupeWallDictListResponse</a></code>

## ReferentielAdministratif

### Epci

Types:

```python
from bdnb_api.types.tables_bdnb.referentiel_administratif import (
    ReferentielAdministratifEpciAPIExpert,
    EpciListResponse,
)
```

Methods:

- <code title="get /donnees/referentiel_administratif_epci">client.tables_bdnb.referentiel_administratif.epci.<a href="./src/bdnb_api/resources/tables_bdnb/referentiel_administratif/epci.py">list</a>(\*\*<a href="src/bdnb_api/types/tables_bdnb/referentiel_administratif/epci_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/tables_bdnb/referentiel_administratif/epci_list_response.py">EpciListResponse</a></code>

### Departement

Types:

```python
from bdnb_api.types.tables_bdnb.referentiel_administratif import (
    ReferentielAdministratifDepartementAPIExpert,
    DepartementListResponse,
)
```

Methods:

- <code title="get /donnees/referentiel_administratif_departement">client.tables_bdnb.referentiel_administratif.departement.<a href="./src/bdnb_api/resources/tables_bdnb/referentiel_administratif/departement.py">list</a>(\*\*<a href="src/bdnb_api/types/tables_bdnb/referentiel_administratif/departement_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/tables_bdnb/referentiel_administratif/departement_list_response.py">DepartementListResponse</a></code>
