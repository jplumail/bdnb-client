# Autocompletion

Types:

```python
from bdnb_client.types import AutocompletionEntitesTexte
```

Methods:

- <code title="get /autocompletion_entites_texte">client.autocompletion.<a href="./src/bdnb_client/resources/autocompletion.py">list</a>(\*\*<a href="src/bdnb_client/types/autocompletion_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/autocompletion_entites_texte.py">SyncDefault[AutocompletionEntitesTexte]</a></code>

# Stats

## BatimentGroupe

Types:

```python
from bdnb_client.types.stats import BatimentGroupeJsonStats
```

Methods:

- <code title="get /stats/batiment_groupe">client.stats.batiment_groupe.<a href="./src/bdnb_client/resources/stats/batiment_groupe.py">list</a>(\*\*<a href="src/bdnb_client/types/stats/batiment_groupe_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/stats/batiment_groupe_json_stats.py">BatimentGroupeJsonStats</a></code>

# Donnees

## BatimentGroupe

Types:

```python
from bdnb_client.types.donnees import BatimentGroupe
```

Methods:

- <code title="get /donnees/batiment_groupe">client.donnees.batiment_groupe.<a href="./src/bdnb_client/resources/donnees/batiment_groupe/batiment_groupe.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/batiment_groupe_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/batiment_groupe/batiment_groupe.py">SyncDefault[BatimentGroupe]</a></code>

### Complet

Types:

```python
from bdnb_client.types.donnees.batiment_groupe import BatimentGroupeComplet
```

Methods:

- <code title="get /donnees/batiment_groupe_complet">client.donnees.batiment_groupe.complet.<a href="./src/bdnb_client/resources/donnees/batiment_groupe/complet/complet.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/batiment_groupe/complet_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/batiment_groupe/batiment_groupe_complet.py">SyncDefault[BatimentGroupeComplet]</a></code>

#### Bbox

Types:

```python
from bdnb_client.types.donnees.batiment_groupe.complet import BboxListResponse
```

Methods:

- <code title="get /donnees/batiment_groupe_complet/bbox">client.donnees.batiment_groupe.complet.bbox.<a href="./src/bdnb_client/resources/donnees/batiment_groupe/complet/bbox.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/batiment_groupe/complet/bbox_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/batiment_groupe/complet/bbox_list_response.py">BboxListResponse</a></code>

#### Polygon

Types:

```python
from bdnb_client.types.donnees.batiment_groupe.complet import PolygonListResponse
```

Methods:

- <code title="post /donnees/batiment_groupe_complet/polygon">client.donnees.batiment_groupe.complet.polygon.<a href="./src/bdnb_client/resources/donnees/batiment_groupe/complet/polygon.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/batiment_groupe/complet/polygon_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/batiment_groupe/complet/polygon_list_response.py">PolygonListResponse</a></code>

### BdtopoZoac

Types:

```python
from bdnb_client.types.donnees.batiment_groupe import BatimentGroupeBdtopoZoac
```

Methods:

- <code title="get /donnees/batiment_groupe_bdtopo_zoac">client.donnees.batiment_groupe.bdtopo_zoac.<a href="./src/bdnb_client/resources/donnees/batiment_groupe/bdtopo_zoac.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/batiment_groupe/bdtopo_zoac_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/batiment_groupe/batiment_groupe_bdtopo_zoac.py">SyncDefault[BatimentGroupeBdtopoZoac]</a></code>

### Geospx

Types:

```python
from bdnb_client.types.donnees.batiment_groupe import BatimentGroupeGeospx
```

Methods:

- <code title="get /donnees/batiment_groupe_geospx">client.donnees.batiment_groupe.geospx.<a href="./src/bdnb_client/resources/donnees/batiment_groupe/geospx.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/batiment_groupe/geospx_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/batiment_groupe/batiment_groupe_geospx.py">SyncDefault[BatimentGroupeGeospx]</a></code>

### DvfOpenStatistique

Types:

```python
from bdnb_client.types.donnees.batiment_groupe import BatimentGroupeDvfOpenStatistique
```

Methods:

- <code title="get /donnees/batiment_groupe_dvf_open_statistique">client.donnees.batiment_groupe.dvf_open_statistique.<a href="./src/bdnb_client/resources/donnees/batiment_groupe/dvf_open_statistique.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/batiment_groupe/dvf_open_statistique_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/batiment_groupe/batiment_groupe_dvf_open_statistique.py">SyncDefault[BatimentGroupeDvfOpenStatistique]</a></code>

### Qpv

Types:

```python
from bdnb_client.types.donnees.batiment_groupe import BatimentGroupeQpv
```

Methods:

- <code title="get /donnees/batiment_groupe_qpv">client.donnees.batiment_groupe.qpv.<a href="./src/bdnb_client/resources/donnees/batiment_groupe/qpv.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/batiment_groupe/qpv_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/batiment_groupe/batiment_groupe_qpv.py">SyncDefault[BatimentGroupeQpv]</a></code>

### SyntheseEnveloppe

Types:

```python
from bdnb_client.types.donnees.batiment_groupe import BatimentGroupeSyntheseEnveloppe
```

Methods:

- <code title="get /donnees/batiment_groupe_synthese_enveloppe">client.donnees.batiment_groupe.synthese_enveloppe.<a href="./src/bdnb_client/resources/donnees/batiment_groupe/synthese_enveloppe.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/batiment_groupe/synthese_enveloppe_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/batiment_groupe/batiment_groupe_synthese_enveloppe.py">SyncDefault[BatimentGroupeSyntheseEnveloppe]</a></code>

### SimulationsDpe

Types:

```python
from bdnb_client.types.donnees.batiment_groupe import BatimentGroupeSimulationsDpe
```

Methods:

- <code title="get /donnees/batiment_groupe_simulations_dpe">client.donnees.batiment_groupe.simulations_dpe.<a href="./src/bdnb_client/resources/donnees/batiment_groupe/simulations_dpe.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/batiment_groupe/simulations_dpe_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/batiment_groupe/batiment_groupe_simulations_dpe.py">SyncDefault[BatimentGroupeSimulationsDpe]</a></code>

### BdtopoEqu

Types:

```python
from bdnb_client.types.donnees.batiment_groupe import BatimentGroupeBdtopoEqu
```

Methods:

- <code title="get /donnees/batiment_groupe_bdtopo_equ">client.donnees.batiment_groupe.bdtopo_equ.<a href="./src/bdnb_client/resources/donnees/batiment_groupe/bdtopo_equ.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/batiment_groupe/bdtopo_equ_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/batiment_groupe/batiment_groupe_bdtopo_equ.py">SyncDefault[BatimentGroupeBdtopoEqu]</a></code>

### DpeRepresentatifLogement

Types:

```python
from bdnb_client.types.donnees.batiment_groupe import BatimentGroupeDpeRepresentatifLogement
```

Methods:

- <code title="get /donnees/batiment_groupe_dpe_representatif_logement">client.donnees.batiment_groupe.dpe_representatif_logement.<a href="./src/bdnb_client/resources/donnees/batiment_groupe/dpe_representatif_logement.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/batiment_groupe/dpe_representatif_logement_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/batiment_groupe/batiment_groupe_dpe_representatif_logement.py">SyncDefault[BatimentGroupeDpeRepresentatifLogement]</a></code>

### DleGaz2020

Types:

```python
from bdnb_client.types.donnees.batiment_groupe import BatimentGroupeDleGaz2020
```

Methods:

- <code title="get /donnees/batiment_groupe_dle_gaz_2020">client.donnees.batiment_groupe.dle_gaz_2020.<a href="./src/bdnb_client/resources/donnees/batiment_groupe/dle_gaz_2020.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/batiment_groupe/dle_gaz_2020_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/batiment_groupe/batiment_groupe_dle_gaz_2020.py">SyncDefault[BatimentGroupeDleGaz2020]</a></code>

### DleElec2020

Types:

```python
from bdnb_client.types.donnees.batiment_groupe import BatimentGroupeDleElec2020
```

Methods:

- <code title="get /donnees/batiment_groupe_dle_elec_2020">client.donnees.batiment_groupe.dle_elec_2020.<a href="./src/bdnb_client/resources/donnees/batiment_groupe/dle_elec_2020.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/batiment_groupe/dle_elec_2020_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/batiment_groupe/batiment_groupe_dle_elec_2020.py">SyncDefault[BatimentGroupeDleElec2020]</a></code>

### Merimee

Types:

```python
from bdnb_client.types.donnees.batiment_groupe import BatimentGroupeMerimee
```

Methods:

- <code title="get /donnees/batiment_groupe_merimee">client.donnees.batiment_groupe.merimee.<a href="./src/bdnb_client/resources/donnees/batiment_groupe/merimee.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/batiment_groupe/merimee_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/batiment_groupe/batiment_groupe_merimee.py">SyncDefault[BatimentGroupeMerimee]</a></code>

### DleReseaux2020

Types:

```python
from bdnb_client.types.donnees.batiment_groupe import BatimentGroupeDleReseaux2020
```

Methods:

- <code title="get /donnees/batiment_groupe_dle_reseaux_2020">client.donnees.batiment_groupe.dle_reseaux_2020.<a href="./src/bdnb_client/resources/donnees/batiment_groupe/dle_reseaux_2020.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/batiment_groupe/dle_reseaux_2020_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/batiment_groupe/batiment_groupe_dle_reseaux_2020.py">SyncDefault[BatimentGroupeDleReseaux2020]</a></code>

### Adresse

Types:

```python
from bdnb_client.types.donnees.batiment_groupe import BatimentGroupeAdresse
```

Methods:

- <code title="get /donnees/batiment_groupe_adresse">client.donnees.batiment_groupe.adresse.<a href="./src/bdnb_client/resources/donnees/batiment_groupe/adresse.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/batiment_groupe/adresse_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/batiment_groupe/batiment_groupe_adresse.py">SyncDefault[BatimentGroupeAdresse]</a></code>

### DleGazMultimillesime

Types:

```python
from bdnb_client.types.donnees.batiment_groupe import BatimentGroupeDleGazMultimillesime
```

Methods:

- <code title="get /donnees/batiment_groupe_dle_gaz_multimillesime">client.donnees.batiment_groupe.dle_gaz_multimillesime.<a href="./src/bdnb_client/resources/donnees/batiment_groupe/dle_gaz_multimillesime.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/batiment_groupe/dle_gaz_multimillesime_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/batiment_groupe/batiment_groupe_dle_gaz_multimillesime.py">SyncDefault[BatimentGroupeDleGazMultimillesime]</a></code>

### Radon

Types:

```python
from bdnb_client.types.donnees.batiment_groupe import BatimentGroupeRadon
```

Methods:

- <code title="get /donnees/batiment_groupe_radon">client.donnees.batiment_groupe.radon.<a href="./src/bdnb_client/resources/donnees/batiment_groupe/radon.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/batiment_groupe/radon_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/batiment_groupe/batiment_groupe_radon.py">SyncDefault[BatimentGroupeRadon]</a></code>

### DvfOpenRepresentatif

Types:

```python
from bdnb_client.types.donnees.batiment_groupe import BatimentGroupeDvfOpenRepresentatif
```

Methods:

- <code title="get /donnees/batiment_groupe_dvf_open_representatif">client.donnees.batiment_groupe.dvf_open_representatif.<a href="./src/bdnb_client/resources/donnees/batiment_groupe/dvf_open_representatif.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/batiment_groupe/dvf_open_representatif_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/batiment_groupe/batiment_groupe_dvf_open_representatif.py">SyncDefault[BatimentGroupeDvfOpenRepresentatif]</a></code>

### SimulationsDvf

Types:

```python
from bdnb_client.types.donnees.batiment_groupe import BatimentGroupeSimulationsDvf
```

Methods:

- <code title="get /donnees/batiment_groupe_simulations_dvf">client.donnees.batiment_groupe.simulations_dvf.<a href="./src/bdnb_client/resources/donnees/batiment_groupe/simulations_dvf.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/batiment_groupe/simulations_dvf_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/batiment_groupe/batiment_groupe_simulations_dvf.py">SyncDefault[BatimentGroupeSimulationsDvf]</a></code>

### DpeStatistiqueLogement

Types:

```python
from bdnb_client.types.donnees.batiment_groupe import BatimentGroupeDpeStatistiqueLogement
```

Methods:

- <code title="get /donnees/batiment_groupe_dpe_statistique_logement">client.donnees.batiment_groupe.dpe_statistique_logement.<a href="./src/bdnb_client/resources/donnees/batiment_groupe/dpe_statistique_logement.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/batiment_groupe/dpe_statistique_logement_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/batiment_groupe/batiment_groupe_dpe_statistique_logement.py">SyncDefault[BatimentGroupeDpeStatistiqueLogement]</a></code>

### DleReseauxMultimillesime

Types:

```python
from bdnb_client.types.donnees.batiment_groupe import BatimentGroupeDleReseauxMultimillesime
```

Methods:

- <code title="get /donnees/batiment_groupe_dle_reseaux_multimillesime">client.donnees.batiment_groupe.dle_reseaux_multimillesime.<a href="./src/bdnb_client/resources/donnees/batiment_groupe/dle_reseaux_multimillesime.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/batiment_groupe/dle_reseaux_multimillesime_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/batiment_groupe/batiment_groupe_dle_reseaux_multimillesime.py">SyncDefault[BatimentGroupeDleReseauxMultimillesime]</a></code>

### Rnc

Types:

```python
from bdnb_client.types.donnees.batiment_groupe import BatimentGroupeRnc
```

Methods:

- <code title="get /donnees/batiment_groupe_rnc">client.donnees.batiment_groupe.rnc.<a href="./src/bdnb_client/resources/donnees/batiment_groupe/rnc.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/batiment_groupe/rnc_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/batiment_groupe/batiment_groupe_rnc.py">SyncDefault[BatimentGroupeRnc]</a></code>

### Bpe

Types:

```python
from bdnb_client.types.donnees.batiment_groupe import BatimentGroupeBpe
```

Methods:

- <code title="get /donnees/batiment_groupe_bpe">client.donnees.batiment_groupe.bpe.<a href="./src/bdnb_client/resources/donnees/batiment_groupe/bpe.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/batiment_groupe/bpe_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/batiment_groupe/batiment_groupe_bpe.py">SyncDefault[BatimentGroupeBpe]</a></code>

### FfoBat

Types:

```python
from bdnb_client.types.donnees.batiment_groupe import BatimentGroupeFfoBat
```

Methods:

- <code title="get /donnees/batiment_groupe_ffo_bat">client.donnees.batiment_groupe.ffo_bat.<a href="./src/bdnb_client/resources/donnees/batiment_groupe/ffo_bat.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/batiment_groupe/ffo_bat_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/batiment_groupe/batiment_groupe_ffo_bat.py">SyncDefault[BatimentGroupeFfoBat]</a></code>

### Argiles

Types:

```python
from bdnb_client.types.donnees.batiment_groupe import BatimentGroupeArgiles
```

Methods:

- <code title="get /donnees/batiment_groupe_argiles">client.donnees.batiment_groupe.argiles.<a href="./src/bdnb_client/resources/donnees/batiment_groupe/argiles.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/batiment_groupe/argile_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/batiment_groupe/batiment_groupe_argiles.py">SyncDefault[BatimentGroupeArgiles]</a></code>

### Hthd

Types:

```python
from bdnb_client.types.donnees.batiment_groupe import BatimentGroupeHthd
```

Methods:

- <code title="get /donnees/batiment_groupe_hthd">client.donnees.batiment_groupe.hthd.<a href="./src/bdnb_client/resources/donnees/batiment_groupe/hthd.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/batiment_groupe/hthd_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/batiment_groupe/batiment_groupe_hthd.py">SyncDefault[BatimentGroupeHthd]</a></code>

### BdtopoBat

Types:

```python
from bdnb_client.types.donnees.batiment_groupe import BatimentGroupeBdtopoBat
```

Methods:

- <code title="get /donnees/batiment_groupe_bdtopo_bat">client.donnees.batiment_groupe.bdtopo_bat.<a href="./src/bdnb_client/resources/donnees/batiment_groupe/bdtopo_bat.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/batiment_groupe/bdtopo_bat_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/batiment_groupe/batiment_groupe_bdtopo_bat.py">SyncDefault[BatimentGroupeBdtopoBat]</a></code>

### DleElecMultimillesime

Types:

```python
from bdnb_client.types.donnees.batiment_groupe import BatimentGroupeDleElecMultimillesime
```

Methods:

- <code title="get /donnees/batiment_groupe_dle_elec_multimillesime">client.donnees.batiment_groupe.dle_elec_multimillesime.<a href="./src/bdnb_client/resources/donnees/batiment_groupe/dle_elec_multimillesime.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/batiment_groupe/dle_elec_multimillesime_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/batiment_groupe/batiment_groupe_dle_elec_multimillesime.py">SyncDefault[BatimentGroupeDleElecMultimillesime]</a></code>

### WallDict

Types:

```python
from bdnb_client.types.donnees.batiment_groupe import BatimentGroupeWallDict
```

Methods:

- <code title="get /donnees/batiment_groupe_wall_dict">client.donnees.batiment_groupe.wall_dict.<a href="./src/bdnb_client/resources/donnees/batiment_groupe/wall_dict.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/batiment_groupe/wall_dict_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/batiment_groupe/batiment_groupe_wall_dict.py">SyncDefault[BatimentGroupeWallDict]</a></code>

### IndicateurReseauChaudFroid

Types:

```python
from bdnb_client.types.donnees.batiment_groupe import BatimentGroupeIndicateurReseauChaudFroid
```

Methods:

- <code title="get /donnees/batiment_groupe_indicateur_reseau_chaud_froid">client.donnees.batiment_groupe.indicateur_reseau_chaud_froid.<a href="./src/bdnb_client/resources/donnees/batiment_groupe/indicateur_reseau_chaud_froid.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/batiment_groupe/indicateur_reseau_chaud_froid_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/batiment_groupe/batiment_groupe_indicateur_reseau_chaud_froid.py">SyncDefault[BatimentGroupeIndicateurReseauChaudFroid]</a></code>

### DelimitationEnveloppe

Types:

```python
from bdnb_client.types.donnees.batiment_groupe import BatimentGroupeDelimitationEnveloppe
```

Methods:

- <code title="get /donnees/batiment_groupe_delimitation_enveloppe">client.donnees.batiment_groupe.delimitation_enveloppe.<a href="./src/bdnb_client/resources/donnees/batiment_groupe/delimitation_enveloppe.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/batiment_groupe/delimitation_enveloppe_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/batiment_groupe/batiment_groupe_delimitation_enveloppe.py">SyncDefault[BatimentGroupeDelimitationEnveloppe]</a></code>

### SimulationsValeurVerte

Types:

```python
from bdnb_client.types.donnees.batiment_groupe import BatimentGroupeSimulationsValeurVerte
```

Methods:

- <code title="get /donnees/batiment_groupe_simulations_valeur_verte">client.donnees.batiment_groupe.simulations_valeur_verte.<a href="./src/bdnb_client/resources/donnees/batiment_groupe/simulations_valeur_verte.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/batiment_groupe/simulations_valeur_verte_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/batiment_groupe/batiment_groupe_simulations_valeur_verte.py">SyncDefault[BatimentGroupeSimulationsValeurVerte]</a></code>

### IrisSimulationsValeurVerte

Types:

```python
from bdnb_client.types.donnees.batiment_groupe import IrisSimulationsValeurVerte
```

Methods:

- <code title="get /donnees/iris_simulations_valeur_verte">client.donnees.batiment_groupe.iris_simulations_valeur_verte.<a href="./src/bdnb_client/resources/donnees/batiment_groupe/iris_simulations_valeur_verte.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/batiment_groupe/iris_simulations_valeur_verte_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/batiment_groupe/iris_simulations_valeur_verte.py">SyncDefault[IrisSimulationsValeurVerte]</a></code>

### IrisContexteGeographique

Types:

```python
from bdnb_client.types.donnees.batiment_groupe import IrisContexteGeographique
```

Methods:

- <code title="get /donnees/iris_contexte_geographique">client.donnees.batiment_groupe.iris_contexte_geographique.<a href="./src/bdnb_client/resources/donnees/batiment_groupe/iris_contexte_geographique.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/batiment_groupe/iris_contexte_geographique_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/batiment_groupe/iris_contexte_geographique.py">SyncDefault[IrisContexteGeographique]</a></code>

## Ancqpv

Types:

```python
from bdnb_client.types.donnees import Ancqpv
```

Methods:

- <code title="get /donnees/ancqpv">client.donnees.ancqpv.<a href="./src/bdnb_client/resources/donnees/ancqpv.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/ancqpv_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/ancqpv.py">SyncDefault[Ancqpv]</a></code>

## Proprietaire

Types:

```python
from bdnb_client.types.donnees import Proprietaire
```

Methods:

- <code title="get /donnees/proprietaire">client.donnees.proprietaire.<a href="./src/bdnb_client/resources/donnees/proprietaire.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/proprietaire_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/proprietaire.py">SyncDefault[Proprietaire]</a></code>

## BatimentConstruction

Types:

```python
from bdnb_client.types.donnees import BatimentConstruction
```

Methods:

- <code title="get /donnees/batiment_construction">client.donnees.batiment_construction.<a href="./src/bdnb_client/resources/donnees/batiment_construction.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/batiment_construction_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/batiment_construction.py">SyncDefault[BatimentConstruction]</a></code>

## Adresse

Types:

```python
from bdnb_client.types.donnees import Adresse
```

Methods:

- <code title="get /donnees/adresse">client.donnees.adresse.<a href="./src/bdnb_client/resources/donnees/adresse.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/adresse_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/adresse.py">SyncDefault[Adresse]</a></code>

## ReferentielAdministratif

### ReferentielAdministratifIris

Types:

```python
from bdnb_client.types.donnees.referentiel_administratif import ReferentielAdministratifIris
```

Methods:

- <code title="get /donnees/referentiel_administratif_iris">client.donnees.referentiel_administratif.referentiel_administratif_iris.<a href="./src/bdnb_client/resources/donnees/referentiel_administratif/referentiel_administratif_iris.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/referentiel_administratif/referentiel_administratif_iris_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/referentiel_administratif/referentiel_administratif_iris.py">SyncDefault[ReferentielAdministratifIris]</a></code>

### Epci

Types:

```python
from bdnb_client.types.donnees.referentiel_administratif import ReferentielAdministratifEpci
```

Methods:

- <code title="get /donnees/referentiel_administratif_epci">client.donnees.referentiel_administratif.epci.<a href="./src/bdnb_client/resources/donnees/referentiel_administratif/epci.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/referentiel_administratif/epci_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/referentiel_administratif/referentiel_administratif_epci.py">SyncDefault[ReferentielAdministratifEpci]</a></code>

### Departement

Types:

```python
from bdnb_client.types.donnees.referentiel_administratif import ReferentielAdministratifDepartement
```

Methods:

- <code title="get /donnees/referentiel_administratif_departement">client.donnees.referentiel_administratif.departement.<a href="./src/bdnb_client/resources/donnees/referentiel_administratif/departement.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/referentiel_administratif/departement_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/referentiel_administratif/referentiel_administratif_departement.py">SyncDefault[ReferentielAdministratifDepartement]</a></code>

### Region

Types:

```python
from bdnb_client.types.donnees.referentiel_administratif import ReferentielAdministratifRegion
```

Methods:

- <code title="get /donnees/referentiel_administratif_region">client.donnees.referentiel_administratif.region.<a href="./src/bdnb_client/resources/donnees/referentiel_administratif/region.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/referentiel_administratif/region_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/referentiel_administratif/referentiel_administratif_region.py">SyncDefault[ReferentielAdministratifRegion]</a></code>

## Relations

### BatimentConstruction

#### Adresse

Types:

```python
from bdnb_client.types.donnees.relations.batiment_construction import RelBatimentConstructionAdresse
```

Methods:

- <code title="get /donnees/rel_batiment_construction_adresse">client.donnees.relations.batiment_construction.adresse.<a href="./src/bdnb_client/resources/donnees/relations/batiment_construction/adresse.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/relations/batiment_construction/adresse_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/relations/batiment_construction/rel_batiment_construction_adresse.py">SyncDefault[RelBatimentConstructionAdresse]</a></code>

### BatimentGroupe

#### ProprietaireSiren

Types:

```python
from bdnb_client.types.donnees.relations.batiment_groupe import RelBatimentGroupeProprietaireSiren
```

Methods:

- <code title="get /donnees/rel_batiment_groupe_proprietaire_siren">client.donnees.relations.batiment_groupe.proprietaire_siren.<a href="./src/bdnb_client/resources/donnees/relations/batiment_groupe/proprietaire_siren.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/relations/batiment_groupe/proprietaire_siren_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/relations/batiment_groupe/rel_batiment_groupe_proprietaire_siren.py">SyncDefault[RelBatimentGroupeProprietaireSiren]</a></code>

#### Qpv

Types:

```python
from bdnb_client.types.donnees.relations.batiment_groupe import RelBatimentGroupeQpv
```

Methods:

- <code title="get /donnees/rel_batiment_groupe_qpv">client.donnees.relations.batiment_groupe.qpv.<a href="./src/bdnb_client/resources/donnees/relations/batiment_groupe/qpv.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/relations/batiment_groupe/qpv_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/relations/batiment_groupe/rel_batiment_groupe_qpv.py">SyncDefault[RelBatimentGroupeQpv]</a></code>

#### Adresse

Types:

```python
from bdnb_client.types.donnees.relations.batiment_groupe import RelBatimentGroupeAdresse
```

Methods:

- <code title="get /donnees/rel_batiment_groupe_adresse">client.donnees.relations.batiment_groupe.adresse.<a href="./src/bdnb_client/resources/donnees/relations/batiment_groupe/adresse.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/relations/batiment_groupe/adresse_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/relations/batiment_groupe/rel_batiment_groupe_adresse.py">SyncDefault[RelBatimentGroupeAdresse]</a></code>

#### Merimee

Types:

```python
from bdnb_client.types.donnees.relations.batiment_groupe import RelBatimentGroupeMerimee
```

Methods:

- <code title="get /donnees/rel_batiment_groupe_merimee">client.donnees.relations.batiment_groupe.merimee.<a href="./src/bdnb_client/resources/donnees/relations/batiment_groupe/merimee.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/relations/batiment_groupe/merimee_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/relations/batiment_groupe/rel_batiment_groupe_merimee.py">SyncDefault[RelBatimentGroupeMerimee]</a></code>

#### Parcelle

Types:

```python
from bdnb_client.types.donnees.relations.batiment_groupe import RelBatimentGroupeParcelle
```

Methods:

- <code title="get /donnees/rel_batiment_groupe_parcelle">client.donnees.relations.batiment_groupe.parcelle.<a href="./src/bdnb_client/resources/donnees/relations/batiment_groupe/parcelle.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/relations/batiment_groupe/parcelle_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/relations/batiment_groupe/rel_batiment_groupe_parcelle.py">SyncDefault[RelBatimentGroupeParcelle]</a></code>

#### SirenComplet

Types:

```python
from bdnb_client.types.donnees.relations.batiment_groupe import RelBatimentGroupeSirenComplet
```

Methods:

- <code title="get /donnees/rel_batiment_groupe_siren_complet">client.donnees.relations.batiment_groupe.siren_complet.<a href="./src/bdnb_client/resources/donnees/relations/batiment_groupe/siren_complet.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/relations/batiment_groupe/siren_complet_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/relations/batiment_groupe/rel_batiment_groupe_siren_complet.py">SyncDefault[RelBatimentGroupeSirenComplet]</a></code>

#### SiretComplet

Types:

```python
from bdnb_client.types.donnees.relations.batiment_groupe import RelBatimentGroupeSiretComplet
```

Methods:

- <code title="get /donnees/rel_batiment_groupe_siret_complet">client.donnees.relations.batiment_groupe.siret_complet.<a href="./src/bdnb_client/resources/donnees/relations/batiment_groupe/siret_complet.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/relations/batiment_groupe/siret_complet_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/relations/batiment_groupe/rel_batiment_groupe_siret_complet.py">SyncDefault[RelBatimentGroupeSiretComplet]</a></code>

#### Rnc

Types:

```python
from bdnb_client.types.donnees.relations.batiment_groupe import RelBatimentGroupeRnc
```

Methods:

- <code title="get /donnees/rel_batiment_groupe_rnc">client.donnees.relations.batiment_groupe.rnc.<a href="./src/bdnb_client/resources/donnees/relations/batiment_groupe/rnc.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/relations/batiment_groupe/rnc_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/relations/batiment_groupe/rel_batiment_groupe_rnc.py">SyncDefault[RelBatimentGroupeRnc]</a></code>

#### ProprietaireSirenOpen

Types:

```python
from bdnb_client.types.donnees.relations.batiment_groupe import (
    RelBatimentGroupeProprietaireSirenOpen,
)
```

Methods:

- <code title="get /donnees/rel_batiment_groupe_proprietaire_siren_open">client.donnees.relations.batiment_groupe.proprietaire_siren_open.<a href="./src/bdnb_client/resources/donnees/relations/batiment_groupe/proprietaire_siren_open.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/relations/batiment_groupe/proprietaire_siren_open_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/relations/batiment_groupe/rel_batiment_groupe_proprietaire_siren_open.py">SyncDefault[RelBatimentGroupeProprietaireSirenOpen]</a></code>

# Metadonnees

## ColonnesSouscription

Types:

```python
from bdnb_client.types.metadonnees import ColonneSouscription
```

Methods:

- <code title="get /metadonnees/colonne_souscription">client.metadonnees.colonnes_souscription.<a href="./src/bdnb_client/resources/metadonnees/colonnes_souscription.py">list</a>(\*\*<a href="src/bdnb_client/types/metadonnees/colonnes_souscription_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/metadonnees/colonne_souscription.py">SyncDefault[ColonneSouscription]</a></code>

## Colonnes

Types:

```python
from bdnb_client.types.metadonnees import Colonne
```

Methods:

- <code title="get /metadonnees/colonne">client.metadonnees.colonnes.<a href="./src/bdnb_client/resources/metadonnees/colonnes.py">list</a>(\*\*<a href="src/bdnb_client/types/metadonnees/colonne_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/metadonnees/colonne.py">SyncDefault[Colonne]</a></code>

## Info

Types:

```python
from bdnb_client.types.metadonnees import Info
```

Methods:

- <code title="get /metadonnees/info">client.metadonnees.info.<a href="./src/bdnb_client/resources/metadonnees/info.py">list</a>(\*\*<a href="src/bdnb_client/types/metadonnees/info_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/metadonnees/info.py">SyncDefault[Info]</a></code>

## Table

Types:

```python
from bdnb_client.types.metadonnees import Table
```

Methods:

- <code title="get /metadonnees/table">client.metadonnees.table.<a href="./src/bdnb_client/resources/metadonnees/table.py">list</a>(\*\*<a href="src/bdnb_client/types/metadonnees/table_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/metadonnees/table.py">SyncDefault[Table]</a></code>

# Tuiles

## Vectorielles

### Epci

Methods:

- <code title="get /tuiles/epci/{zoom}/{x}/{y}.pbf">client.tuiles.vectorielles.epci.<a href="./src/bdnb_client/resources/tuiles/vectorielles/epci.py">list</a>(y, \*, zoom, x) -> BinaryAPIResponse</code>

### Region

Methods:

- <code title="get /tuiles/region/{zoom}/{x}/{y}.pbf">client.tuiles.vectorielles.region.<a href="./src/bdnb_client/resources/tuiles/vectorielles/region.py">list</a>(y, \*, zoom, x) -> BinaryAPIResponse</code>

### Iris

Methods:

- <code title="get /tuiles/iris/{zoom}/{x}/{y}.pbf">client.tuiles.vectorielles.iris.<a href="./src/bdnb_client/resources/tuiles/vectorielles/iris.py">list</a>(y, \*, zoom, x) -> BinaryAPIResponse</code>

### Departement

Methods:

- <code title="get /tuiles/departement/{zoom}/{x}/{y}.pbf">client.tuiles.vectorielles.departement.<a href="./src/bdnb_client/resources/tuiles/vectorielles/departement.py">list</a>(y, \*, zoom, x) -> BinaryAPIResponse</code>

### BatimentGroupe

Methods:

- <code title="get /tuiles/batiment_groupe/{zoom}/{x}/{y}.pbf">client.tuiles.vectorielles.batiment_groupe.<a href="./src/bdnb_client/resources/tuiles/vectorielles/batiment_groupe.py">list</a>(y, \*, zoom, x) -> BinaryAPIResponse</code>
