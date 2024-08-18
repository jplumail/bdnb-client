# Shared Types

```python
from bdnb_api.types import (
    BatimentConstructionAPIExpert,
    BatimentGroupeArgilesAPIExpert,
    BatimentGroupeBdtopoEquAPIExpert,
    BatimentGroupeBdtopoZoacAPIExpert,
    BatimentGroupeBpeAPIExpert,
    BatimentGroupeDleElec2020APIExpert,
    BatimentGroupeDleGaz2020APIExpert,
    BatimentGroupeDleReseaux2020APIExpert,
    BatimentGroupeDleReseauxMultimillesimeAPIExpert,
    BatimentGroupeDpeRepresentatifLogementAPIExpert,
    BatimentGroupeDvfOpenStatistiqueAPIExpert,
    BatimentGroupeGeospxAPIExpert,
    BatimentGroupeRncAPIExpert,
    BatimentGroupeSimulationsDpeAPIExpert,
    BatimentGroupeSyntheseEnveloppeAPIExpert,
    RelBatimentConstructionAdresseAPIExpert,
    RelBatimentGroupeAdresseAPIExpert,
    RelBatimentGroupeMerimeeAPIExpert,
    RelBatimentGroupeProprietaireSirenAPIExpert,
    RelBatimentGroupeSirenAPIExpert,
)
```

# Autocompletion

Types:

```python
from bdnb_api.types import AutocompletionEntitesTexteAPIExpert
```

Methods:

- <code title="get /autocompletion_entites_texte">client.autocompletion.<a href="./src/bdnb_api/resources/autocompletion.py">list</a>(\*\*<a href="src/bdnb_api/types/autocompletion_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/autocompletion_entites_texte_api_expert.py">SyncDefault[AutocompletionEntitesTexteAPIExpert]</a></code>

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
from bdnb_api.types import (
    AncqpvAPIExpert,
    BatimentGroupeAPIExpert,
    BatimentGroupeFfoBatAPIExpert,
    BatimentGroupeMerimeeAPIExpert,
    BatimentGroupeQpvAPIExpert,
    IrisContexteGeographiqueAPIExpert,
    IrisSimulationsValeurVerteAPIExpert,
    RelBatimentGroupeQpvAPIExpert,
    RelBatimentGroupeRncAPIExpert,
    RelBatimentGroupeSiretCompletAPIExpert,
)
```

## BatimentGroupeComplet

Types:

```python
from bdnb_api.types.donnees import BatimentGroupeCompletAPIExpert
```

Methods:

- <code title="get /donnees/batiment_groupe_complet">client.donnees.batiment_groupe_complet.<a href="./src/bdnb_api/resources/donnees/batiment_groupe_complet/batiment_groupe_complet.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/batiment_groupe_complet_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/batiment_groupe_complet_api_expert.py">SyncDefault[BatimentGroupeCompletAPIExpert]</a></code>

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
from bdnb_api.types.donnees.batiment_groupe_complet import PolygonListResponse
```

Methods:

- <code title="post /donnees/batiment_groupe_complet/polygon">client.donnees.batiment_groupe_complet.polygon.<a href="./src/bdnb_api/resources/donnees/batiment_groupe_complet/polygon.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/batiment_groupe_complet/polygon_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/batiment_groupe_complet/polygon_list_response.py">PolygonListResponse</a></code>

## BatimentsConstruction

Methods:

- <code title="get /donnees/batiment_construction">client.donnees.batiments_construction.<a href="./src/bdnb_api/resources/donnees/batiments_construction.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/batiments_construction_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/shared/batiment_construction_api_expert.py">SyncDefault[BatimentConstructionAPIExpert]</a></code>

## BatimentGroupeBdtopoZoac

Methods:

- <code title="get /donnees/batiment_groupe_bdtopo_zoac">client.donnees.batiment_groupe_bdtopo_zoac.<a href="./src/bdnb_api/resources/donnees/batiment_groupe_bdtopo_zoac.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/batiment_groupe_bdtopo_zoac_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/shared/batiment_groupe_bdtopo_zoac_api_expert.py">SyncDefault[BatimentGroupeBdtopoZoacAPIExpert]</a></code>

## BatimentGroupeGeospx

Methods:

- <code title="get /donnees/batiment_groupe_geospx">client.donnees.batiment_groupe_geospx.<a href="./src/bdnb_api/resources/donnees/batiment_groupe_geospx.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/batiment_groupe_geospx_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/shared/batiment_groupe_geospx_api_expert.py">SyncDefault[BatimentGroupeGeospxAPIExpert]</a></code>

## RelBatimentGroupeProprietaireSiren

Methods:

- <code title="get /donnees/rel_batiment_groupe_proprietaire_siren">client.donnees.rel_batiment_groupe_proprietaire_siren.<a href="./src/bdnb_api/resources/donnees/rel_batiment_groupe_proprietaire_siren.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/rel_batiment_groupe_proprietaire_siren_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/shared/rel_batiment_groupe_proprietaire_siren_api_expert.py">SyncDefault[RelBatimentGroupeProprietaireSirenAPIExpert]</a></code>

## BatimentGroupeDvfOpenStatistique

Methods:

- <code title="get /donnees/batiment_groupe_dvf_open_statistique">client.donnees.batiment_groupe_dvf_open_statistique.<a href="./src/bdnb_api/resources/donnees/batiment_groupe_dvf_open_statistique.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/batiment_groupe_dvf_open_statistique_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/shared/batiment_groupe_dvf_open_statistique_api_expert.py">SyncDefault[BatimentGroupeDvfOpenStatistiqueAPIExpert]</a></code>

## RelBatimentGroupeQpv

Methods:

- <code title="get /donnees/rel_batiment_groupe_qpv">client.donnees.rel_batiment_groupe_qpv.<a href="./src/bdnb_api/resources/donnees/rel_batiment_groupe_qpv.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/rel_batiment_groupe_qpv_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/rel_batiment_groupe_qpv_api_expert.py">SyncDefault[RelBatimentGroupeQpvAPIExpert]</a></code>

## BatimentGroupeQpv

Methods:

- <code title="get /donnees/batiment_groupe_qpv">client.donnees.batiment_groupe_qpv.<a href="./src/bdnb_api/resources/donnees/batiment_groupe_qpv.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/batiment_groupe_qpv_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/batiment_groupe_qpv_api_expert.py">SyncDefault[BatimentGroupeQpvAPIExpert]</a></code>

## RelBatimentConstructionAdresse

Methods:

- <code title="get /donnees/rel_batiment_construction_adresse">client.donnees.rel_batiment_construction_adresse.<a href="./src/bdnb_api/resources/donnees/rel_batiment_construction_adresse.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/rel_batiment_construction_adresse_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/shared/rel_batiment_construction_adresse_api_expert.py">SyncDefault[RelBatimentConstructionAdresseAPIExpert]</a></code>

## RelBatimentGroupeAdresse

Methods:

- <code title="get /donnees/rel_batiment_groupe_adresse">client.donnees.rel_batiment_groupe_adresse.<a href="./src/bdnb_api/resources/donnees/rel_batiment_groupe_adresse.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/rel_batiment_groupe_adresse_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/shared/rel_batiment_groupe_adresse_api_expert.py">SyncDefault[RelBatimentGroupeAdresseAPIExpert]</a></code>

## BatimentGroupeSyntheseEnveloppe

Methods:

- <code title="get /donnees/batiment_groupe_synthese_enveloppe">client.donnees.batiment_groupe_synthese_enveloppe.<a href="./src/bdnb_api/resources/donnees/batiment_groupe_synthese_enveloppe.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/batiment_groupe_synthese_enveloppe_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/shared/batiment_groupe_synthese_enveloppe_api_expert.py">SyncDefault[BatimentGroupeSyntheseEnveloppeAPIExpert]</a></code>

## BatimentGroupeSimulationsDpe

Methods:

- <code title="get /donnees/batiment_groupe_simulations_dpe">client.donnees.batiment_groupe_simulations_dpe.<a href="./src/bdnb_api/resources/donnees/batiment_groupe_simulations_dpe.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/batiment_groupe_simulations_dpe_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/shared/batiment_groupe_simulations_dpe_api_expert.py">SyncDefault[BatimentGroupeSimulationsDpeAPIExpert]</a></code>

## BatimentGroupeBdtopoEqu

Methods:

- <code title="get /donnees/batiment_groupe_bdtopo_equ">client.donnees.batiment_groupe_bdtopo_equ.<a href="./src/bdnb_api/resources/donnees/batiment_groupe_bdtopo_equ.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/batiment_groupe_bdtopo_equ_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/shared/batiment_groupe_bdtopo_equ_api_expert.py">SyncDefault[BatimentGroupeBdtopoEquAPIExpert]</a></code>

## BatimentGroupeDpeRepresentatifLogement

Methods:

- <code title="get /donnees/batiment_groupe_dpe_representatif_logement">client.donnees.batiment_groupe_dpe_representatif_logement.<a href="./src/bdnb_api/resources/donnees/batiment_groupe_dpe_representatif_logement.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/batiment_groupe_dpe_representatif_logement_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/shared/batiment_groupe_dpe_representatif_logement_api_expert.py">SyncDefault[BatimentGroupeDpeRepresentatifLogementAPIExpert]</a></code>

## BatimentGroupeDleGaz2020

Methods:

- <code title="get /donnees/batiment_groupe_dle_gaz_2020">client.donnees.batiment_groupe_dle_gaz_2020.<a href="./src/bdnb_api/resources/donnees/batiment_groupe_dle_gaz_2020.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/batiment_groupe_dle_gaz_2020_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/shared/batiment_groupe_dle_gaz_2020_api_expert.py">SyncDefault[BatimentGroupeDleGaz2020APIExpert]</a></code>

## BatimentGroupe

Methods:

- <code title="get /donnees/batiment_groupe">client.donnees.batiment_groupe.<a href="./src/bdnb_api/resources/donnees/batiment_groupe.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/batiment_groupe_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/batiment_groupe_api_expert.py">SyncDefault[BatimentGroupeAPIExpert]</a></code>

## RelBatimentGroupeMerimee

Methods:

- <code title="get /donnees/rel_batiment_groupe_merimee">client.donnees.rel_batiment_groupe_merimee.<a href="./src/bdnb_api/resources/donnees/rel_batiment_groupe_merimee.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/rel_batiment_groupe_merimee_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/shared/rel_batiment_groupe_merimee_api_expert.py">SyncDefault[RelBatimentGroupeMerimeeAPIExpert]</a></code>

## BatimentGroupeDleElec2020

Methods:

- <code title="get /donnees/batiment_groupe_dle_elec_2020">client.donnees.batiment_groupe_dle_elec_2020.<a href="./src/bdnb_api/resources/donnees/batiment_groupe_dle_elec_2020.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/batiment_groupe_dle_elec_2020_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/shared/batiment_groupe_dle_elec_2020_api_expert.py">SyncDefault[BatimentGroupeDleElec2020APIExpert]</a></code>

## BatimentGroupeMerimee

Methods:

- <code title="get /donnees/batiment_groupe_merimee">client.donnees.batiment_groupe_merimee.<a href="./src/bdnb_api/resources/donnees/batiment_groupe_merimee.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/batiment_groupe_merimee_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/batiment_groupe_merimee_api_expert.py">SyncDefault[BatimentGroupeMerimeeAPIExpert]</a></code>

## BatimentGroupeDleReseaux2020

Methods:

- <code title="get /donnees/batiment_groupe_dle_reseaux_2020">client.donnees.batiment_groupe_dle_reseaux_2020.<a href="./src/bdnb_api/resources/donnees/batiment_groupe_dle_reseaux_2020.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/batiment_groupe_dle_reseaux_2020_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/shared/batiment_groupe_dle_reseaux_2020_api_expert.py">SyncDefault[BatimentGroupeDleReseaux2020APIExpert]</a></code>

## Ancqpv

Methods:

- <code title="get /donnees/ancqpv">client.donnees.ancqpv.<a href="./src/bdnb_api/resources/donnees/ancqpv.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/ancqpv_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/ancqpv_api_expert.py">SyncDefault[AncqpvAPIExpert]</a></code>

## BatimentGroupeAdresse

Types:

```python
from bdnb_api.types.donnees import BatimentGroupeAdresseAPIExpert
```

Methods:

- <code title="get /donnees/batiment_groupe_adresse">client.donnees.batiment_groupe_adresse.<a href="./src/bdnb_api/resources/donnees/batiment_groupe_adresse.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/batiment_groupe_adresse_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/batiment_groupe_adresse_api_expert.py">SyncDefault[BatimentGroupeAdresseAPIExpert]</a></code>

## BatimentGroupeDleGazMultimillesime

Types:

```python
from bdnb_api.types.donnees import BatimentGroupeDleGazMultimillesimeAPIExpert
```

Methods:

- <code title="get /donnees/batiment_groupe_dle_gaz_multimillesime">client.donnees.batiment_groupe_dle_gaz_multimillesime.<a href="./src/bdnb_api/resources/donnees/batiment_groupe_dle_gaz_multimillesime.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/batiment_groupe_dle_gaz_multimillesime_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/batiment_groupe_dle_gaz_multimillesime_api_expert.py">SyncDefault[BatimentGroupeDleGazMultimillesimeAPIExpert]</a></code>

## RelBatimentGroupeParcelle

Types:

```python
from bdnb_api.types.donnees import RelBatimentGroupeParcelleAPIExpert
```

Methods:

- <code title="get /donnees/rel_batiment_groupe_parcelle">client.donnees.rel_batiment_groupe_parcelle.<a href="./src/bdnb_api/resources/donnees/rel_batiment_groupe_parcelle.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/rel_batiment_groupe_parcelle_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/rel_batiment_groupe_parcelle_api_expert.py">SyncDefault[RelBatimentGroupeParcelleAPIExpert]</a></code>

## BatimentGroupeRadon

Types:

```python
from bdnb_api.types.donnees import BatimentGroupeRadonAPIExpert
```

Methods:

- <code title="get /donnees/batiment_groupe_radon">client.donnees.batiment_groupe_radon.<a href="./src/bdnb_api/resources/donnees/batiment_groupe_radon.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/batiment_groupe_radon_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/batiment_groupe_radon_api_expert.py">SyncDefault[BatimentGroupeRadonAPIExpert]</a></code>

## BatimentGroupeDvfOpenRepresentatif

Types:

```python
from bdnb_api.types.donnees import BatimentGroupeDvfOpenRepresentatifAPIExpert
```

Methods:

- <code title="get /donnees/batiment_groupe_dvf_open_representatif">client.donnees.batiment_groupe_dvf_open_representatif.<a href="./src/bdnb_api/resources/donnees/batiment_groupe_dvf_open_representatif.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/batiment_groupe_dvf_open_representatif_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/batiment_groupe_dvf_open_representatif_api_expert.py">SyncDefault[BatimentGroupeDvfOpenRepresentatifAPIExpert]</a></code>

## BatimentGroupeSimulationsDvf

Types:

```python
from bdnb_api.types.donnees import BatimentGroupeSimulationsDvfAPIExpert
```

Methods:

- <code title="get /donnees/batiment_groupe_simulations_dvf">client.donnees.batiment_groupe_simulations_dvf.<a href="./src/bdnb_api/resources/donnees/batiment_groupe_simulations_dvf.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/batiment_groupe_simulations_dvf_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/batiment_groupe_simulations_dvf_api_expert.py">SyncDefault[BatimentGroupeSimulationsDvfAPIExpert]</a></code>

## BatimentGroupeDpeStatistiqueLogement

Types:

```python
from bdnb_api.types.donnees import BatimentGroupeDpeStatistiqueLogementAPIExpert
```

Methods:

- <code title="get /donnees/batiment_groupe_dpe_statistique_logement">client.donnees.batiment_groupe_dpe_statistique_logement.<a href="./src/bdnb_api/resources/donnees/batiment_groupe_dpe_statistique_logement.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/batiment_groupe_dpe_statistique_logement_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/batiment_groupe_dpe_statistique_logement_api_expert.py">SyncDefault[BatimentGroupeDpeStatistiqueLogementAPIExpert]</a></code>

## IrisSimulationsValeurVerte

Methods:

- <code title="get /donnees/iris_simulations_valeur_verte">client.donnees.iris_simulations_valeur_verte.<a href="./src/bdnb_api/resources/donnees/iris_simulations_valeur_verte.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/iris_simulations_valeur_verte_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/iris_simulations_valeur_verte_api_expert.py">SyncDefault[IrisSimulationsValeurVerteAPIExpert]</a></code>

## IrisContexteGeographique

Methods:

- <code title="get /donnees/iris_contexte_geographique">client.donnees.iris_contexte_geographique.<a href="./src/bdnb_api/resources/donnees/iris_contexte_geographique.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/iris_contexte_geographique_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/iris_contexte_geographique_api_expert.py">SyncDefault[IrisContexteGeographiqueAPIExpert]</a></code>

## RelBatimentGroupeSirenComplet

Methods:

- <code title="get /donnees/rel_batiment_groupe_siren_complet">client.donnees.rel_batiment_groupe_siren_complet.<a href="./src/bdnb_api/resources/donnees/rel_batiment_groupe_siren_complet.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/rel_batiment_groupe_siren_complet_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/shared/rel_batiment_groupe_siren_api_expert.py">SyncDefault[RelBatimentGroupeSirenAPIExpert]</a></code>

## RelBatimentGroupeSiretComplet

Methods:

- <code title="get /donnees/rel_batiment_groupe_siret_complet">client.donnees.rel_batiment_groupe_siret_complet.<a href="./src/bdnb_api/resources/donnees/rel_batiment_groupe_siret_complet.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/rel_batiment_groupe_siret_complet_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/rel_batiment_groupe_siret_complet_api_expert.py">SyncDefault[RelBatimentGroupeSiretCompletAPIExpert]</a></code>

## BatimentGroupeDleReseauxMultimillesime

Methods:

- <code title="get /donnees/batiment_groupe_dle_reseaux_multimillesime">client.donnees.batiment_groupe_dle_reseaux_multimillesime.<a href="./src/bdnb_api/resources/donnees/batiment_groupe_dle_reseaux_multimillesime.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/batiment_groupe_dle_reseaux_multimillesime_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/shared/batiment_groupe_dle_reseaux_multimillesime_api_expert.py">SyncDefault[BatimentGroupeDleReseauxMultimillesimeAPIExpert]</a></code>

## BatimentGroupeRnc

Methods:

- <code title="get /donnees/batiment_groupe_rnc">client.donnees.batiment_groupe_rnc.<a href="./src/bdnb_api/resources/donnees/batiment_groupe_rnc.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/batiment_groupe_rnc_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/shared/batiment_groupe_rnc_api_expert.py">SyncDefault[BatimentGroupeRncAPIExpert]</a></code>

## BatimentGroupeBpe

Methods:

- <code title="get /donnees/batiment_groupe_bpe">client.donnees.batiment_groupe_bpe.<a href="./src/bdnb_api/resources/donnees/batiment_groupe_bpe.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/batiment_groupe_bpe_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/shared/batiment_groupe_bpe_api_expert.py">SyncDefault[BatimentGroupeBpeAPIExpert]</a></code>

## BatimentGroupeFfoBat

Methods:

- <code title="get /donnees/batiment_groupe_ffo_bat">client.donnees.batiment_groupe_ffo_bat.<a href="./src/bdnb_api/resources/donnees/batiment_groupe_ffo_bat.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/batiment_groupe_ffo_bat_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/batiment_groupe_ffo_bat_api_expert.py">SyncDefault[BatimentGroupeFfoBatAPIExpert]</a></code>

## RelBatimentGroupeRnc

Methods:

- <code title="get /donnees/rel_batiment_groupe_rnc">client.donnees.rel_batiment_groupe_rnc.<a href="./src/bdnb_api/resources/donnees/rel_batiment_groupe_rnc.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/rel_batiment_groupe_rnc_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/rel_batiment_groupe_rnc_api_expert.py">SyncDefault[RelBatimentGroupeRncAPIExpert]</a></code>

## BatimentGroupeArgiles

Methods:

- <code title="get /donnees/batiment_groupe_argiles">client.donnees.batiment_groupe_argiles.<a href="./src/bdnb_api/resources/donnees/batiment_groupe_argiles.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/batiment_groupe_argile_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/shared/batiment_groupe_argiles_api_expert.py">SyncDefault[BatimentGroupeArgilesAPIExpert]</a></code>

## BatimentGroupeHthd

Types:

```python
from bdnb_api.types.donnees import BatimentGroupeHthdAPIExpert
```

Methods:

- <code title="get /donnees/batiment_groupe_hthd">client.donnees.batiment_groupe_hthd.<a href="./src/bdnb_api/resources/donnees/batiment_groupe_hthd.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/batiment_groupe_hthd_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/batiment_groupe_hthd_api_expert.py">SyncDefault[BatimentGroupeHthdAPIExpert]</a></code>

## Proprietaire

Types:

```python
from bdnb_api.types.donnees import ProprietaireAPIExpert
```

Methods:

- <code title="get /donnees/proprietaire">client.donnees.proprietaire.<a href="./src/bdnb_api/resources/donnees/proprietaire.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/proprietaire_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/proprietaire_api_expert.py">SyncDefault[ProprietaireAPIExpert]</a></code>

## BatimentGroupeBdtopoBat

Types:

```python
from bdnb_api.types.donnees import BatimentGroupeBdtopoBatAPIExpert
```

Methods:

- <code title="get /donnees/batiment_groupe_bdtopo_bat">client.donnees.batiment_groupe_bdtopo_bat.<a href="./src/bdnb_api/resources/donnees/batiment_groupe_bdtopo_bat.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/batiment_groupe_bdtopo_bat_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/batiment_groupe_bdtopo_bat_api_expert.py">SyncDefault[BatimentGroupeBdtopoBatAPIExpert]</a></code>

## RelBatimentGroupeProprietaireSirenOpen

Types:

```python
from bdnb_api.types.donnees import RelBatimentGroupeProprietaireSirenOpenAPIExpert
```

Methods:

- <code title="get /donnees/rel_batiment_groupe_proprietaire_siren_open">client.donnees.rel_batiment_groupe_proprietaire_siren_open.<a href="./src/bdnb_api/resources/donnees/rel_batiment_groupe_proprietaire_siren_open.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/rel_batiment_groupe_proprietaire_siren_open_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/rel_batiment_groupe_proprietaire_siren_openapi_expert.py">SyncDefault[RelBatimentGroupeProprietaireSirenOpenAPIExpert]</a></code>

## BatimentGroupeDleElecMultimillesime

Types:

```python
from bdnb_api.types.donnees import BatimentGroupeDleElecMultimillesimeAPIExpert
```

Methods:

- <code title="get /donnees/batiment_groupe_dle_elec_multimillesime">client.donnees.batiment_groupe_dle_elec_multimillesime.<a href="./src/bdnb_api/resources/donnees/batiment_groupe_dle_elec_multimillesime.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/batiment_groupe_dle_elec_multimillesime_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/batiment_groupe_dle_elec_multimillesime_api_expert.py">SyncDefault[BatimentGroupeDleElecMultimillesimeAPIExpert]</a></code>

## Adresse

Types:

```python
from bdnb_api.types.donnees import AdresseAPIExpert
```

Methods:

- <code title="get /donnees/adresse">client.donnees.adresse.<a href="./src/bdnb_api/resources/donnees/adresse.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/adresse_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/adresse_api_expert.py">SyncDefault[AdresseAPIExpert]</a></code>

## BatimentGroupeWallDict

Types:

```python
from bdnb_api.types.donnees import BatimentGroupeWallDictAPIExpert
```

Methods:

- <code title="get /donnees/batiment_groupe_wall_dict">client.donnees.batiment_groupe_wall_dict.<a href="./src/bdnb_api/resources/donnees/batiment_groupe_wall_dict.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/batiment_groupe_wall_dict_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/batiment_groupe_wall_dict_api_expert.py">SyncDefault[BatimentGroupeWallDictAPIExpert]</a></code>

## BatimentGroupeIndicateurReseauChaudFroid

Types:

```python
from bdnb_api.types.donnees import BatimentGroupeIndicateurReseauChaudFroidAPIExpert
```

Methods:

- <code title="get /donnees/batiment_groupe_indicateur_reseau_chaud_froid">client.donnees.batiment_groupe_indicateur_reseau_chaud_froid.<a href="./src/bdnb_api/resources/donnees/batiment_groupe_indicateur_reseau_chaud_froid.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/batiment_groupe_indicateur_reseau_chaud_froid_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/batiment_groupe_indicateur_reseau_chaud_froid_api_expert.py">SyncDefault[BatimentGroupeIndicateurReseauChaudFroidAPIExpert]</a></code>

## BatimentGroupeDelimitationEnveloppe

Types:

```python
from bdnb_api.types.donnees import BatimentGroupeDelimitationEnveloppeAPIExpert
```

Methods:

- <code title="get /donnees/batiment_groupe_delimitation_enveloppe">client.donnees.batiment_groupe_delimitation_enveloppe.<a href="./src/bdnb_api/resources/donnees/batiment_groupe_delimitation_enveloppe.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/batiment_groupe_delimitation_enveloppe_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/batiment_groupe_delimitation_enveloppe_api_expert.py">SyncDefault[BatimentGroupeDelimitationEnveloppeAPIExpert]</a></code>

## BatimentGroupeSimulationsValeurVerte

Types:

```python
from bdnb_api.types.donnees import BatimentGroupeSimulationsValeurVerteAPIExpert
```

Methods:

- <code title="get /donnees/batiment_groupe_simulations_valeur_verte">client.donnees.batiment_groupe_simulations_valeur_verte.<a href="./src/bdnb_api/resources/donnees/batiment_groupe_simulations_valeur_verte.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/batiment_groupe_simulations_valeur_verte_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/batiment_groupe_simulations_valeur_verte_api_expert.py">SyncDefault[BatimentGroupeSimulationsValeurVerteAPIExpert]</a></code>

## ReferentielAdministratif

### ReferentielAdministratifIris

Types:

```python
from bdnb_api.types.donnees.referentiel_administratif import ReferentielAdministratifIrisAPIExpert
```

Methods:

- <code title="get /donnees/referentiel_administratif_iris">client.donnees.referentiel_administratif.referentiel_administratif_iris.<a href="./src/bdnb_api/resources/donnees/referentiel_administratif/referentiel_administratif_iris.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/referentiel_administratif/referentiel_administratif_iris_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/referentiel_administratif/referentiel_administratif_iris_api_expert.py">SyncDefault[ReferentielAdministratifIrisAPIExpert]</a></code>

### Epci

Types:

```python
from bdnb_api.types.donnees.referentiel_administratif import ReferentielAdministratifEpciAPIExpert
```

Methods:

- <code title="get /donnees/referentiel_administratif_epci">client.donnees.referentiel_administratif.epci.<a href="./src/bdnb_api/resources/donnees/referentiel_administratif/epci.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/referentiel_administratif/epci_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/referentiel_administratif/referentiel_administratif_epci_api_expert.py">SyncDefault[ReferentielAdministratifEpciAPIExpert]</a></code>

### Departement

Types:

```python
from bdnb_api.types.donnees.referentiel_administratif import (
    ReferentielAdministratifDepartementAPIExpert,
)
```

Methods:

- <code title="get /donnees/referentiel_administratif_departement">client.donnees.referentiel_administratif.departement.<a href="./src/bdnb_api/resources/donnees/referentiel_administratif/departement.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/referentiel_administratif/departement_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/referentiel_administratif/referentiel_administratif_departement_api_expert.py">SyncDefault[ReferentielAdministratifDepartementAPIExpert]</a></code>

### Region

Types:

```python
from bdnb_api.types.donnees.referentiel_administratif import ReferentielAdministratifRegionAPIExpert
```

Methods:

- <code title="get /donnees/referentiel_administratif_region">client.donnees.referentiel_administratif.region.<a href="./src/bdnb_api/resources/donnees/referentiel_administratif/region.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/referentiel_administratif/region_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/referentiel_administratif/referentiel_administratif_region_api_expert.py">SyncDefault[ReferentielAdministratifRegionAPIExpert]</a></code>

# Metadonnees

## ColonnesSouscription

Types:

```python
from bdnb_api.types.metadonnees import ColonneSouscription
```

Methods:

- <code title="get /metadonnees/colonne_souscription">client.metadonnees.colonnes_souscription.<a href="./src/bdnb_api/resources/metadonnees/colonnes_souscription.py">list</a>(\*\*<a href="src/bdnb_api/types/metadonnees/colonnes_souscription_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/metadonnees/colonne_souscription.py">SyncDefault[ColonneSouscription]</a></code>

## Colonnes

Types:

```python
from bdnb_api.types.metadonnees import Colonne
```

Methods:

- <code title="get /metadonnees/colonne">client.metadonnees.colonnes.<a href="./src/bdnb_api/resources/metadonnees/colonnes.py">list</a>(\*\*<a href="src/bdnb_api/types/metadonnees/colonne_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/metadonnees/colonne.py">SyncDefault[Colonne]</a></code>

## MetadonneesComplets

Types:

```python
from bdnb_api.types.metadonnees import MetadonneesComplet
```

Methods:

- <code title="get /metadonnees/metadonnees_complet">client.metadonnees.metadonnees_complets.<a href="./src/bdnb_api/resources/metadonnees/metadonnees_complets.py">list</a>(\*\*<a href="src/bdnb_api/types/metadonnees/metadonnees_complet_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/metadonnees/metadonnees_complet.py">SyncDefault[MetadonneesComplet]</a></code>

## Info

Types:

```python
from bdnb_api.types.metadonnees import Info
```

Methods:

- <code title="get /metadonnees/info">client.metadonnees.info.<a href="./src/bdnb_api/resources/metadonnees/info.py">list</a>(\*\*<a href="src/bdnb_api/types/metadonnees/info_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/metadonnees/info.py">SyncDefault[Info]</a></code>

## Table

Types:

```python
from bdnb_api.types.metadonnees import Table
```

Methods:

- <code title="get /metadonnees/table">client.metadonnees.table.<a href="./src/bdnb_api/resources/metadonnees/table.py">list</a>(\*\*<a href="src/bdnb_api/types/metadonnees/table_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/metadonnees/table.py">SyncDefault[Table]</a></code>

## RelColonneJeuDeDonnees

Types:

```python
from bdnb_api.types.metadonnees import RelColonneJeuDeDonnees
```

Methods:

- <code title="get /metadonnees/rel_colonne_jeu_de_donnees">client.metadonnees.rel_colonne_jeu_de_donnees.<a href="./src/bdnb_api/resources/metadonnees/rel_colonne_jeu_de_donnees.py">list</a>(\*\*<a href="src/bdnb_api/types/metadonnees/rel_colonne_jeu_de_donnee_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/metadonnees/rel_colonne_jeu_de_donnees.py">SyncDefault[RelColonneJeuDeDonnees]</a></code>

## JeuDeDonnees

Types:

```python
from bdnb_api.types.metadonnees import JeuDeDonnees
```

Methods:

- <code title="get /metadonnees/jeu_de_donnees">client.metadonnees.jeu_de_donnees.<a href="./src/bdnb_api/resources/metadonnees/jeu_de_donnees.py">list</a>(\*\*<a href="src/bdnb_api/types/metadonnees/jeu_de_donnee_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/metadonnees/jeu_de_donnees.py">SyncDefault[JeuDeDonnees]</a></code>

## Fournisseur

Types:

```python
from bdnb_api.types.metadonnees import Fournisseur, FournisseurRetrieveResponse
```

Methods:

- <code title="get /metadonnees/fournisseur">client.metadonnees.fournisseur.<a href="./src/bdnb_api/resources/metadonnees/fournisseur.py">retrieve</a>(\*\*<a href="src/bdnb_api/types/metadonnees/fournisseur_retrieve_params.py">params</a>) -> <a href="./src/bdnb_api/types/metadonnees/fournisseur_retrieve_response.py">FournisseurRetrieveResponse</a></code>

## ContrainteAcces

Types:

```python
from bdnb_api.types.metadonnees import ContrainteAcces, ContrainteAcceRetrieveResponse
```

Methods:

- <code title="get /metadonnees/contrainte_acces">client.metadonnees.contrainte_acces.<a href="./src/bdnb_api/resources/metadonnees/contrainte_acces.py">retrieve</a>(\*\*<a href="src/bdnb_api/types/metadonnees/contrainte_acce_retrieve_params.py">params</a>) -> <a href="./src/bdnb_api/types/metadonnees/contrainte_acce_retrieve_response.py">ContrainteAcceRetrieveResponse</a></code>

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
