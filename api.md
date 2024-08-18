# Autocompletion

Types:

```python
from bdnb_api.types import AutocompletionEntitesTexte
```

Methods:

- <code title="get /autocompletion_entites_texte">client.autocompletion.<a href="./src/bdnb_api/resources/autocompletion.py">list</a>(\*\*<a href="src/bdnb_api/types/autocompletion_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/autocompletion_entites_texte.py">SyncDefault[AutocompletionEntitesTexte]</a></code>

# Stats

## BatimentGroupes

Types:

```python
from bdnb_api.types.stats import BatimentGroupeJsonStats
```

Methods:

- <code title="get /stats/batiment_groupe">client.stats.batiment_groupes.<a href="./src/bdnb_api/resources/stats/batiment_groupes.py">list</a>(\*\*<a href="src/bdnb_api/types/stats/batiment_groupe_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/stats/batiment_groupe_json_stats.py">BatimentGroupeJsonStats</a></code>

# Donnees

## BatimentGroupeComplet

Types:

```python
from bdnb_api.types.donnees import BatimentGroupeComplet
```

Methods:

- <code title="get /donnees/batiment_groupe_complet">client.donnees.batiment_groupe_complet.<a href="./src/bdnb_api/resources/donnees/batiment_groupe_complet/batiment_groupe_complet.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/batiment_groupe_complet_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/batiment_groupe_complet/batiment_groupe_complet.py">SyncDefault[BatimentGroupeComplet]</a></code>

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

## BatimentConstruction

Types:

```python
from bdnb_api.types.donnees import BatimentConstruction
```

Methods:

- <code title="get /donnees/batiment_construction">client.donnees.batiment_construction.<a href="./src/bdnb_api/resources/donnees/batiment_construction.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/batiment_construction_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/batiment_construction.py">SyncDefault[BatimentConstruction]</a></code>

## BatimentGroupeBdtopoZoac

Types:

```python
from bdnb_api.types.donnees import BatimentGroupeBdtopoZoac
```

Methods:

- <code title="get /donnees/batiment_groupe_bdtopo_zoac">client.donnees.batiment_groupe_bdtopo_zoac.<a href="./src/bdnb_api/resources/donnees/batiment_groupe_bdtopo_zoac.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/batiment_groupe_bdtopo_zoac_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/batiment_groupe_bdtopo_zoac.py">SyncDefault[BatimentGroupeBdtopoZoac]</a></code>

## BatimentGroupeGeospx

Types:

```python
from bdnb_api.types.donnees import BatimentGroupeGeospx
```

Methods:

- <code title="get /donnees/batiment_groupe_geospx">client.donnees.batiment_groupe_geospx.<a href="./src/bdnb_api/resources/donnees/batiment_groupe_geospx.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/batiment_groupe_geospx_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/batiment_groupe_geospx.py">SyncDefault[BatimentGroupeGeospx]</a></code>

## RelBatimentGroupeProprietaireSiren

Types:

```python
from bdnb_api.types.donnees import RelBatimentGroupeProprietaireSiren
```

Methods:

- <code title="get /donnees/rel_batiment_groupe_proprietaire_siren">client.donnees.rel_batiment_groupe_proprietaire_siren.<a href="./src/bdnb_api/resources/donnees/rel_batiment_groupe_proprietaire_siren.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/rel_batiment_groupe_proprietaire_siren_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/rel_batiment_groupe_proprietaire_siren.py">SyncDefault[RelBatimentGroupeProprietaireSiren]</a></code>

## BatimentGroupeDvfOpenStatistique

Types:

```python
from bdnb_api.types.donnees import BatimentGroupeDvfOpenStatistique
```

Methods:

- <code title="get /donnees/batiment_groupe_dvf_open_statistique">client.donnees.batiment_groupe_dvf_open_statistique.<a href="./src/bdnb_api/resources/donnees/batiment_groupe_dvf_open_statistique.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/batiment_groupe_dvf_open_statistique_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/batiment_groupe_dvf_open_statistique.py">SyncDefault[BatimentGroupeDvfOpenStatistique]</a></code>

## RelBatimentGroupeQpv

Types:

```python
from bdnb_api.types.donnees import RelBatimentGroupeQpv
```

Methods:

- <code title="get /donnees/rel_batiment_groupe_qpv">client.donnees.rel_batiment_groupe_qpv.<a href="./src/bdnb_api/resources/donnees/rel_batiment_groupe_qpv.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/rel_batiment_groupe_qpv_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/rel_batiment_groupe_qpv.py">SyncDefault[RelBatimentGroupeQpv]</a></code>

## BatimentGroupeQpv

Types:

```python
from bdnb_api.types.donnees import BatimentGroupeQpv
```

Methods:

- <code title="get /donnees/batiment_groupe_qpv">client.donnees.batiment_groupe_qpv.<a href="./src/bdnb_api/resources/donnees/batiment_groupe_qpv.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/batiment_groupe_qpv_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/batiment_groupe_qpv.py">SyncDefault[BatimentGroupeQpv]</a></code>

## RelBatimentConstructionAdresse

Types:

```python
from bdnb_api.types.donnees import RelBatimentConstructionAdresse
```

Methods:

- <code title="get /donnees/rel_batiment_construction_adresse">client.donnees.rel_batiment_construction_adresse.<a href="./src/bdnb_api/resources/donnees/rel_batiment_construction_adresse.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/rel_batiment_construction_adresse_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/rel_batiment_construction_adresse.py">SyncDefault[RelBatimentConstructionAdresse]</a></code>

## RelBatimentGroupeAdresse

Types:

```python
from bdnb_api.types.donnees import RelBatimentGroupeAdresse
```

Methods:

- <code title="get /donnees/rel_batiment_groupe_adresse">client.donnees.rel_batiment_groupe_adresse.<a href="./src/bdnb_api/resources/donnees/rel_batiment_groupe_adresse.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/rel_batiment_groupe_adresse_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/rel_batiment_groupe_adresse.py">SyncDefault[RelBatimentGroupeAdresse]</a></code>

## BatimentGroupeSyntheseEnveloppe

Types:

```python
from bdnb_api.types.donnees import BatimentGroupeSyntheseEnveloppe
```

Methods:

- <code title="get /donnees/batiment_groupe_synthese_enveloppe">client.donnees.batiment_groupe_synthese_enveloppe.<a href="./src/bdnb_api/resources/donnees/batiment_groupe_synthese_enveloppe.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/batiment_groupe_synthese_enveloppe_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/batiment_groupe_synthese_enveloppe.py">SyncDefault[BatimentGroupeSyntheseEnveloppe]</a></code>

## BatimentGroupeSimulationsDpe

Types:

```python
from bdnb_api.types.donnees import BatimentGroupeSimulationsDpe
```

Methods:

- <code title="get /donnees/batiment_groupe_simulations_dpe">client.donnees.batiment_groupe_simulations_dpe.<a href="./src/bdnb_api/resources/donnees/batiment_groupe_simulations_dpe.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/batiment_groupe_simulations_dpe_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/batiment_groupe_simulations_dpe.py">SyncDefault[BatimentGroupeSimulationsDpe]</a></code>

## BatimentGroupeBdtopoEqu

Types:

```python
from bdnb_api.types.donnees import BatimentGroupeBdtopoEqu
```

Methods:

- <code title="get /donnees/batiment_groupe_bdtopo_equ">client.donnees.batiment_groupe_bdtopo_equ.<a href="./src/bdnb_api/resources/donnees/batiment_groupe_bdtopo_equ.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/batiment_groupe_bdtopo_equ_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/batiment_groupe_bdtopo_equ.py">SyncDefault[BatimentGroupeBdtopoEqu]</a></code>

## BatimentGroupeDpeRepresentatifLogement

Types:

```python
from bdnb_api.types.donnees import BatimentGroupeDpeRepresentatifLogement
```

Methods:

- <code title="get /donnees/batiment_groupe_dpe_representatif_logement">client.donnees.batiment_groupe_dpe_representatif_logement.<a href="./src/bdnb_api/resources/donnees/batiment_groupe_dpe_representatif_logement.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/batiment_groupe_dpe_representatif_logement_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/batiment_groupe_dpe_representatif_logement.py">SyncDefault[BatimentGroupeDpeRepresentatifLogement]</a></code>

## BatimentGroupeDleGaz2020

Types:

```python
from bdnb_api.types.donnees import BatimentGroupeDleGaz2020
```

Methods:

- <code title="get /donnees/batiment_groupe_dle_gaz_2020">client.donnees.batiment_groupe_dle_gaz_2020.<a href="./src/bdnb_api/resources/donnees/batiment_groupe_dle_gaz_2020.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/batiment_groupe_dle_gaz_2020_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/batiment_groupe_dle_gaz_2020.py">SyncDefault[BatimentGroupeDleGaz2020]</a></code>

## BatimentGroupe

Types:

```python
from bdnb_api.types.donnees import BatimentGroupe
```

Methods:

- <code title="get /donnees/batiment_groupe">client.donnees.batiment_groupe.<a href="./src/bdnb_api/resources/donnees/batiment_groupe.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/batiment_groupe_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/batiment_groupe.py">SyncDefault[BatimentGroupe]</a></code>

## RelBatimentGroupeMerimee

Types:

```python
from bdnb_api.types.donnees import RelBatimentGroupeMerimee
```

Methods:

- <code title="get /donnees/rel_batiment_groupe_merimee">client.donnees.rel_batiment_groupe_merimee.<a href="./src/bdnb_api/resources/donnees/rel_batiment_groupe_merimee.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/rel_batiment_groupe_merimee_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/rel_batiment_groupe_merimee.py">SyncDefault[RelBatimentGroupeMerimee]</a></code>

## BatimentGroupeDleElec2020

Types:

```python
from bdnb_api.types.donnees import BatimentGroupeDleElec2020
```

Methods:

- <code title="get /donnees/batiment_groupe_dle_elec_2020">client.donnees.batiment_groupe_dle_elec_2020.<a href="./src/bdnb_api/resources/donnees/batiment_groupe_dle_elec_2020.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/batiment_groupe_dle_elec_2020_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/batiment_groupe_dle_elec_2020.py">SyncDefault[BatimentGroupeDleElec2020]</a></code>

## BatimentGroupeMerimee

Types:

```python
from bdnb_api.types.donnees import BatimentGroupeMerimee
```

Methods:

- <code title="get /donnees/batiment_groupe_merimee">client.donnees.batiment_groupe_merimee.<a href="./src/bdnb_api/resources/donnees/batiment_groupe_merimee.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/batiment_groupe_merimee_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/batiment_groupe_merimee.py">SyncDefault[BatimentGroupeMerimee]</a></code>

## BatimentGroupeDleReseaux2020

Types:

```python
from bdnb_api.types.donnees import BatimentGroupeDleReseaux2020
```

Methods:

- <code title="get /donnees/batiment_groupe_dle_reseaux_2020">client.donnees.batiment_groupe_dle_reseaux_2020.<a href="./src/bdnb_api/resources/donnees/batiment_groupe_dle_reseaux_2020.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/batiment_groupe_dle_reseaux_2020_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/batiment_groupe_dle_reseaux_2020.py">SyncDefault[BatimentGroupeDleReseaux2020]</a></code>

## Ancqpv

Types:

```python
from bdnb_api.types.donnees import Ancqpv
```

Methods:

- <code title="get /donnees/ancqpv">client.donnees.ancqpv.<a href="./src/bdnb_api/resources/donnees/ancqpv.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/ancqpv_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/ancqpv.py">SyncDefault[Ancqpv]</a></code>

## BatimentGroupeAdresse

Types:

```python
from bdnb_api.types.donnees import BatimentGroupeAdresse
```

Methods:

- <code title="get /donnees/batiment_groupe_adresse">client.donnees.batiment_groupe_adresse.<a href="./src/bdnb_api/resources/donnees/batiment_groupe_adresse.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/batiment_groupe_adresse_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/batiment_groupe_adresse.py">SyncDefault[BatimentGroupeAdresse]</a></code>

## BatimentGroupeDleGazMultimillesime

Types:

```python
from bdnb_api.types.donnees import BatimentGroupeDleGazMultimillesime
```

Methods:

- <code title="get /donnees/batiment_groupe_dle_gaz_multimillesime">client.donnees.batiment_groupe_dle_gaz_multimillesime.<a href="./src/bdnb_api/resources/donnees/batiment_groupe_dle_gaz_multimillesime.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/batiment_groupe_dle_gaz_multimillesime_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/batiment_groupe_dle_gaz_multimillesime.py">SyncDefault[BatimentGroupeDleGazMultimillesime]</a></code>

## RelBatimentGroupeParcelle

Types:

```python
from bdnb_api.types.donnees import RelBatimentGroupeParcelle
```

Methods:

- <code title="get /donnees/rel_batiment_groupe_parcelle">client.donnees.rel_batiment_groupe_parcelle.<a href="./src/bdnb_api/resources/donnees/rel_batiment_groupe_parcelle.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/rel_batiment_groupe_parcelle_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/rel_batiment_groupe_parcelle.py">SyncDefault[RelBatimentGroupeParcelle]</a></code>

## BatimentGroupeRadon

Types:

```python
from bdnb_api.types.donnees import BatimentGroupeRadon
```

Methods:

- <code title="get /donnees/batiment_groupe_radon">client.donnees.batiment_groupe_radon.<a href="./src/bdnb_api/resources/donnees/batiment_groupe_radon.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/batiment_groupe_radon_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/batiment_groupe_radon.py">SyncDefault[BatimentGroupeRadon]</a></code>

## BatimentGroupeDvfOpenRepresentatif

Types:

```python
from bdnb_api.types.donnees import BatimentGroupeDvfOpenRepresentatif
```

Methods:

- <code title="get /donnees/batiment_groupe_dvf_open_representatif">client.donnees.batiment_groupe_dvf_open_representatif.<a href="./src/bdnb_api/resources/donnees/batiment_groupe_dvf_open_representatif.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/batiment_groupe_dvf_open_representatif_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/batiment_groupe_dvf_open_representatif.py">SyncDefault[BatimentGroupeDvfOpenRepresentatif]</a></code>

## BatimentGroupeSimulationsDvf

Types:

```python
from bdnb_api.types.donnees import BatimentGroupeSimulationsDvf
```

Methods:

- <code title="get /donnees/batiment_groupe_simulations_dvf">client.donnees.batiment_groupe_simulations_dvf.<a href="./src/bdnb_api/resources/donnees/batiment_groupe_simulations_dvf.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/batiment_groupe_simulations_dvf_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/batiment_groupe_simulations_dvf.py">SyncDefault[BatimentGroupeSimulationsDvf]</a></code>

## BatimentGroupeDpeStatistiqueLogement

Types:

```python
from bdnb_api.types.donnees import BatimentGroupeDpeStatistiqueLogement
```

Methods:

- <code title="get /donnees/batiment_groupe_dpe_statistique_logement">client.donnees.batiment_groupe_dpe_statistique_logement.<a href="./src/bdnb_api/resources/donnees/batiment_groupe_dpe_statistique_logement.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/batiment_groupe_dpe_statistique_logement_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/batiment_groupe_dpe_statistique_logement.py">SyncDefault[BatimentGroupeDpeStatistiqueLogement]</a></code>

## IrisSimulationsValeurVerte

Types:

```python
from bdnb_api.types.donnees import IrisSimulationsValeurVerte
```

Methods:

- <code title="get /donnees/iris_simulations_valeur_verte">client.donnees.iris_simulations_valeur_verte.<a href="./src/bdnb_api/resources/donnees/iris_simulations_valeur_verte.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/iris_simulations_valeur_verte_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/iris_simulations_valeur_verte.py">SyncDefault[IrisSimulationsValeurVerte]</a></code>

## IrisContexteGeographique

Types:

```python
from bdnb_api.types.donnees import IrisContexteGeographique
```

Methods:

- <code title="get /donnees/iris_contexte_geographique">client.donnees.iris_contexte_geographique.<a href="./src/bdnb_api/resources/donnees/iris_contexte_geographique.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/iris_contexte_geographique_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/iris_contexte_geographique.py">SyncDefault[IrisContexteGeographique]</a></code>

## RelBatimentGroupeSirenComplet

Types:

```python
from bdnb_api.types.donnees import RelBatimentGroupeSirenComplet
```

Methods:

- <code title="get /donnees/rel_batiment_groupe_siren_complet">client.donnees.rel_batiment_groupe_siren_complet.<a href="./src/bdnb_api/resources/donnees/rel_batiment_groupe_siren_complet.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/rel_batiment_groupe_siren_complet_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/rel_batiment_groupe_siren_complet.py">SyncDefault[RelBatimentGroupeSirenComplet]</a></code>

## RelBatimentGroupeSiretComplet

Types:

```python
from bdnb_api.types.donnees import RelBatimentGroupeSiretComplet
```

Methods:

- <code title="get /donnees/rel_batiment_groupe_siret_complet">client.donnees.rel_batiment_groupe_siret_complet.<a href="./src/bdnb_api/resources/donnees/rel_batiment_groupe_siret_complet.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/rel_batiment_groupe_siret_complet_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/rel_batiment_groupe_siret_complet.py">SyncDefault[RelBatimentGroupeSiretComplet]</a></code>

## BatimentGroupeDleReseauxMultimillesime

Types:

```python
from bdnb_api.types.donnees import BatimentGroupeDleReseauxMultimillesime
```

Methods:

- <code title="get /donnees/batiment_groupe_dle_reseaux_multimillesime">client.donnees.batiment_groupe_dle_reseaux_multimillesime.<a href="./src/bdnb_api/resources/donnees/batiment_groupe_dle_reseaux_multimillesime.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/batiment_groupe_dle_reseaux_multimillesime_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/batiment_groupe_dle_reseaux_multimillesime.py">SyncDefault[BatimentGroupeDleReseauxMultimillesime]</a></code>

## BatimentGroupeRnc

Types:

```python
from bdnb_api.types.donnees import BatimentGroupeRnc
```

Methods:

- <code title="get /donnees/batiment_groupe_rnc">client.donnees.batiment_groupe_rnc.<a href="./src/bdnb_api/resources/donnees/batiment_groupe_rnc.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/batiment_groupe_rnc_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/batiment_groupe_rnc.py">SyncDefault[BatimentGroupeRnc]</a></code>

## BatimentGroupeBpe

Types:

```python
from bdnb_api.types.donnees import BatimentGroupeBpe
```

Methods:

- <code title="get /donnees/batiment_groupe_bpe">client.donnees.batiment_groupe_bpe.<a href="./src/bdnb_api/resources/donnees/batiment_groupe_bpe.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/batiment_groupe_bpe_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/batiment_groupe_bpe.py">SyncDefault[BatimentGroupeBpe]</a></code>

## BatimentGroupeFfoBat

Types:

```python
from bdnb_api.types.donnees import BatimentGroupeFfoBat
```

Methods:

- <code title="get /donnees/batiment_groupe_ffo_bat">client.donnees.batiment_groupe_ffo_bat.<a href="./src/bdnb_api/resources/donnees/batiment_groupe_ffo_bat.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/batiment_groupe_ffo_bat_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/batiment_groupe_ffo_bat.py">SyncDefault[BatimentGroupeFfoBat]</a></code>

## RelBatimentGroupeRnc

Types:

```python
from bdnb_api.types.donnees import RelBatimentGroupeRnc
```

Methods:

- <code title="get /donnees/rel_batiment_groupe_rnc">client.donnees.rel_batiment_groupe_rnc.<a href="./src/bdnb_api/resources/donnees/rel_batiment_groupe_rnc.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/rel_batiment_groupe_rnc_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/rel_batiment_groupe_rnc.py">SyncDefault[RelBatimentGroupeRnc]</a></code>

## BatimentGroupeArgiles

Types:

```python
from bdnb_api.types.donnees import BatimentGroupeArgiles
```

Methods:

- <code title="get /donnees/batiment_groupe_argiles">client.donnees.batiment_groupe_argiles.<a href="./src/bdnb_api/resources/donnees/batiment_groupe_argiles.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/batiment_groupe_argile_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/batiment_groupe_argiles.py">SyncDefault[BatimentGroupeArgiles]</a></code>

## BatimentGroupeHthd

Types:

```python
from bdnb_api.types.donnees import BatimentGroupeHthd
```

Methods:

- <code title="get /donnees/batiment_groupe_hthd">client.donnees.batiment_groupe_hthd.<a href="./src/bdnb_api/resources/donnees/batiment_groupe_hthd.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/batiment_groupe_hthd_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/batiment_groupe_hthd.py">SyncDefault[BatimentGroupeHthd]</a></code>

## Proprietaire

Types:

```python
from bdnb_api.types.donnees import Proprietaire
```

Methods:

- <code title="get /donnees/proprietaire">client.donnees.proprietaire.<a href="./src/bdnb_api/resources/donnees/proprietaire.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/proprietaire_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/proprietaire.py">SyncDefault[Proprietaire]</a></code>

## BatimentGroupeBdtopoBat

Types:

```python
from bdnb_api.types.donnees import BatimentGroupeBdtopoBat
```

Methods:

- <code title="get /donnees/batiment_groupe_bdtopo_bat">client.donnees.batiment_groupe_bdtopo_bat.<a href="./src/bdnb_api/resources/donnees/batiment_groupe_bdtopo_bat.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/batiment_groupe_bdtopo_bat_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/batiment_groupe_bdtopo_bat.py">SyncDefault[BatimentGroupeBdtopoBat]</a></code>

## RelBatimentGroupeProprietaireSirenOpen

Types:

```python
from bdnb_api.types.donnees import RelBatimentGroupeProprietaireSirenOpen
```

Methods:

- <code title="get /donnees/rel_batiment_groupe_proprietaire_siren_open">client.donnees.rel_batiment_groupe_proprietaire_siren_open.<a href="./src/bdnb_api/resources/donnees/rel_batiment_groupe_proprietaire_siren_open.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/rel_batiment_groupe_proprietaire_siren_open_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/rel_batiment_groupe_proprietaire_siren_open.py">SyncDefault[RelBatimentGroupeProprietaireSirenOpen]</a></code>

## BatimentGroupeDleElecMultimillesime

Types:

```python
from bdnb_api.types.donnees import BatimentGroupeDleElecMultimillesime
```

Methods:

- <code title="get /donnees/batiment_groupe_dle_elec_multimillesime">client.donnees.batiment_groupe_dle_elec_multimillesime.<a href="./src/bdnb_api/resources/donnees/batiment_groupe_dle_elec_multimillesime.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/batiment_groupe_dle_elec_multimillesime_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/batiment_groupe_dle_elec_multimillesime.py">SyncDefault[BatimentGroupeDleElecMultimillesime]</a></code>

## Adresse

Types:

```python
from bdnb_api.types.donnees import Adresse
```

Methods:

- <code title="get /donnees/adresse">client.donnees.adresse.<a href="./src/bdnb_api/resources/donnees/adresse.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/adresse_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/adresse.py">SyncDefault[Adresse]</a></code>

## BatimentGroupeWallDict

Types:

```python
from bdnb_api.types.donnees import BatimentGroupeWallDict
```

Methods:

- <code title="get /donnees/batiment_groupe_wall_dict">client.donnees.batiment_groupe_wall_dict.<a href="./src/bdnb_api/resources/donnees/batiment_groupe_wall_dict.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/batiment_groupe_wall_dict_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/batiment_groupe_wall_dict.py">SyncDefault[BatimentGroupeWallDict]</a></code>

## BatimentGroupeIndicateurReseauChaudFroid

Types:

```python
from bdnb_api.types.donnees import BatimentGroupeIndicateurReseauChaudFroid
```

Methods:

- <code title="get /donnees/batiment_groupe_indicateur_reseau_chaud_froid">client.donnees.batiment_groupe_indicateur_reseau_chaud_froid.<a href="./src/bdnb_api/resources/donnees/batiment_groupe_indicateur_reseau_chaud_froid.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/batiment_groupe_indicateur_reseau_chaud_froid_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/batiment_groupe_indicateur_reseau_chaud_froid.py">SyncDefault[BatimentGroupeIndicateurReseauChaudFroid]</a></code>

## BatimentGroupeDelimitationEnveloppe

Types:

```python
from bdnb_api.types.donnees import BatimentGroupeDelimitationEnveloppe
```

Methods:

- <code title="get /donnees/batiment_groupe_delimitation_enveloppe">client.donnees.batiment_groupe_delimitation_enveloppe.<a href="./src/bdnb_api/resources/donnees/batiment_groupe_delimitation_enveloppe.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/batiment_groupe_delimitation_enveloppe_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/batiment_groupe_delimitation_enveloppe.py">SyncDefault[BatimentGroupeDelimitationEnveloppe]</a></code>

## BatimentGroupeSimulationsValeurVerte

Types:

```python
from bdnb_api.types.donnees import BatimentGroupeSimulationsValeurVerte
```

Methods:

- <code title="get /donnees/batiment_groupe_simulations_valeur_verte">client.donnees.batiment_groupe_simulations_valeur_verte.<a href="./src/bdnb_api/resources/donnees/batiment_groupe_simulations_valeur_verte.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/batiment_groupe_simulations_valeur_verte_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/batiment_groupe_simulations_valeur_verte.py">SyncDefault[BatimentGroupeSimulationsValeurVerte]</a></code>

## ReferentielAdministratif

### ReferentielAdministratifIris

Types:

```python
from bdnb_api.types.donnees.referentiel_administratif import ReferentielAdministratifIris
```

Methods:

- <code title="get /donnees/referentiel_administratif_iris">client.donnees.referentiel_administratif.referentiel_administratif_iris.<a href="./src/bdnb_api/resources/donnees/referentiel_administratif/referentiel_administratif_iris.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/referentiel_administratif/referentiel_administratif_iris_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/referentiel_administratif/referentiel_administratif_iris.py">SyncDefault[ReferentielAdministratifIris]</a></code>

### Epci

Types:

```python
from bdnb_api.types.donnees.referentiel_administratif import ReferentielAdministratifEpci
```

Methods:

- <code title="get /donnees/referentiel_administratif_epci">client.donnees.referentiel_administratif.epci.<a href="./src/bdnb_api/resources/donnees/referentiel_administratif/epci.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/referentiel_administratif/epci_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/referentiel_administratif/referentiel_administratif_epci.py">SyncDefault[ReferentielAdministratifEpci]</a></code>

### Departement

Types:

```python
from bdnb_api.types.donnees.referentiel_administratif import ReferentielAdministratifDepartement
```

Methods:

- <code title="get /donnees/referentiel_administratif_departement">client.donnees.referentiel_administratif.departement.<a href="./src/bdnb_api/resources/donnees/referentiel_administratif/departement.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/referentiel_administratif/departement_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/referentiel_administratif/referentiel_administratif_departement.py">SyncDefault[ReferentielAdministratifDepartement]</a></code>

### Region

Types:

```python
from bdnb_api.types.donnees.referentiel_administratif import ReferentielAdministratifRegion
```

Methods:

- <code title="get /donnees/referentiel_administratif_region">client.donnees.referentiel_administratif.region.<a href="./src/bdnb_api/resources/donnees/referentiel_administratif/region.py">list</a>(\*\*<a href="src/bdnb_api/types/donnees/referentiel_administratif/region_list_params.py">params</a>) -> <a href="./src/bdnb_api/types/donnees/referentiel_administratif/referentiel_administratif_region.py">SyncDefault[ReferentielAdministratifRegion]</a></code>

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
