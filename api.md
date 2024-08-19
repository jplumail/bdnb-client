# Autocompletion

Types:

```python
from bdnb_client.types import AutocompletionEntitesTexte, AutocompletionListResponse
```

Methods:

- <code title="get /autocompletion_entites_texte">client.autocompletion.<a href="./src/bdnb_client/resources/autocompletion.py">list</a>(\*\*<a href="src/bdnb_client/types/autocompletion_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/autocompletion_list_response.py">AutocompletionListResponse</a></code>

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
from bdnb_client.types.donnees.batiment_groupe import BatimentGroupeComplet, CompletListResponse
```

Methods:

- <code title="get /donnees/batiment_groupe_complet">client.donnees.batiment_groupe.complet.<a href="./src/bdnb_client/resources/donnees/batiment_groupe/complet/complet.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/batiment_groupe/complet_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/batiment_groupe/complet_list_response.py">CompletListResponse</a></code>

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
from bdnb_client.types.donnees.batiment_groupe import (
    BatimentGroupeBdtopoZoac,
    BdtopoZoacListResponse,
)
```

Methods:

- <code title="get /donnees/batiment_groupe_bdtopo_zoac">client.donnees.batiment_groupe.bdtopo_zoac.<a href="./src/bdnb_client/resources/donnees/batiment_groupe/bdtopo_zoac.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/batiment_groupe/bdtopo_zoac_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/batiment_groupe/bdtopo_zoac_list_response.py">BdtopoZoacListResponse</a></code>

### Geospx

Types:

```python
from bdnb_client.types.donnees.batiment_groupe import BatimentGroupeGeospx, GeospxListResponse
```

Methods:

- <code title="get /donnees/batiment_groupe_geospx">client.donnees.batiment_groupe.geospx.<a href="./src/bdnb_client/resources/donnees/batiment_groupe/geospx.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/batiment_groupe/geospx_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/batiment_groupe/geospx_list_response.py">GeospxListResponse</a></code>

### DvfOpenStatistique

Types:

```python
from bdnb_client.types.donnees.batiment_groupe import (
    BatimentGroupeDvfOpenStatistique,
    DvfOpenStatistiqueListResponse,
)
```

Methods:

- <code title="get /donnees/batiment_groupe_dvf_open_statistique">client.donnees.batiment_groupe.dvf_open_statistique.<a href="./src/bdnb_client/resources/donnees/batiment_groupe/dvf_open_statistique.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/batiment_groupe/dvf_open_statistique_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/batiment_groupe/dvf_open_statistique_list_response.py">DvfOpenStatistiqueListResponse</a></code>

### Qpv

Types:

```python
from bdnb_client.types.donnees.batiment_groupe import BatimentGroupeQpv, QpvListResponse
```

Methods:

- <code title="get /donnees/batiment_groupe_qpv">client.donnees.batiment_groupe.qpv.<a href="./src/bdnb_client/resources/donnees/batiment_groupe/qpv.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/batiment_groupe/qpv_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/batiment_groupe/qpv_list_response.py">QpvListResponse</a></code>

### SyntheseEnveloppe

Types:

```python
from bdnb_client.types.donnees.batiment_groupe import (
    BatimentGroupeSyntheseEnveloppe,
    SyntheseEnveloppeListResponse,
)
```

Methods:

- <code title="get /donnees/batiment_groupe_synthese_enveloppe">client.donnees.batiment_groupe.synthese_enveloppe.<a href="./src/bdnb_client/resources/donnees/batiment_groupe/synthese_enveloppe.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/batiment_groupe/synthese_enveloppe_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/batiment_groupe/synthese_enveloppe_list_response.py">SyntheseEnveloppeListResponse</a></code>

### SimulationsDpe

Types:

```python
from bdnb_client.types.donnees.batiment_groupe import (
    BatimentGroupeSimulationsDpe,
    SimulationsDpeListResponse,
)
```

Methods:

- <code title="get /donnees/batiment_groupe_simulations_dpe">client.donnees.batiment_groupe.simulations_dpe.<a href="./src/bdnb_client/resources/donnees/batiment_groupe/simulations_dpe.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/batiment_groupe/simulations_dpe_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/batiment_groupe/simulations_dpe_list_response.py">SimulationsDpeListResponse</a></code>

### BdtopoEqu

Types:

```python
from bdnb_client.types.donnees.batiment_groupe import BatimentGroupeBdtopoEqu, BdtopoEquListResponse
```

Methods:

- <code title="get /donnees/batiment_groupe_bdtopo_equ">client.donnees.batiment_groupe.bdtopo_equ.<a href="./src/bdnb_client/resources/donnees/batiment_groupe/bdtopo_equ.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/batiment_groupe/bdtopo_equ_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/batiment_groupe/bdtopo_equ_list_response.py">BdtopoEquListResponse</a></code>

### DpeRepresentatifLogement

Types:

```python
from bdnb_client.types.donnees.batiment_groupe import (
    BatimentGroupeDpeRepresentatifLogement,
    DpeRepresentatifLogementListResponse,
)
```

Methods:

- <code title="get /donnees/batiment_groupe_dpe_representatif_logement">client.donnees.batiment_groupe.dpe_representatif_logement.<a href="./src/bdnb_client/resources/donnees/batiment_groupe/dpe_representatif_logement.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/batiment_groupe/dpe_representatif_logement_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/batiment_groupe/dpe_representatif_logement_list_response.py">DpeRepresentatifLogementListResponse</a></code>

### DleGaz2020

Types:

```python
from bdnb_client.types.donnees.batiment_groupe import (
    BatimentGroupeDleGaz2020,
    DleGaz2020ListResponse,
)
```

Methods:

- <code title="get /donnees/batiment_groupe_dle_gaz_2020">client.donnees.batiment_groupe.dle_gaz_2020.<a href="./src/bdnb_client/resources/donnees/batiment_groupe/dle_gaz_2020.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/batiment_groupe/dle_gaz_2020_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/batiment_groupe/dle_gaz_2020_list_response.py">DleGaz2020ListResponse</a></code>

### DleElec2020

Types:

```python
from bdnb_client.types.donnees.batiment_groupe import (
    BatimentGroupeDleElec2020,
    DleElec2020ListResponse,
)
```

Methods:

- <code title="get /donnees/batiment_groupe_dle_elec_2020">client.donnees.batiment_groupe.dle_elec_2020.<a href="./src/bdnb_client/resources/donnees/batiment_groupe/dle_elec_2020.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/batiment_groupe/dle_elec_2020_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/batiment_groupe/dle_elec_2020_list_response.py">DleElec2020ListResponse</a></code>

### Merimee

Types:

```python
from bdnb_client.types.donnees.batiment_groupe import BatimentGroupeMerimee, MerimeeListResponse
```

Methods:

- <code title="get /donnees/batiment_groupe_merimee">client.donnees.batiment_groupe.merimee.<a href="./src/bdnb_client/resources/donnees/batiment_groupe/merimee.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/batiment_groupe/merimee_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/batiment_groupe/merimee_list_response.py">MerimeeListResponse</a></code>

### DleReseaux2020

Types:

```python
from bdnb_client.types.donnees.batiment_groupe import (
    BatimentGroupeDleReseaux2020,
    DleReseaux2020ListResponse,
)
```

Methods:

- <code title="get /donnees/batiment_groupe_dle_reseaux_2020">client.donnees.batiment_groupe.dle_reseaux_2020.<a href="./src/bdnb_client/resources/donnees/batiment_groupe/dle_reseaux_2020.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/batiment_groupe/dle_reseaux_2020_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/batiment_groupe/dle_reseaux_2020_list_response.py">DleReseaux2020ListResponse</a></code>

### Adresse

Types:

```python
from bdnb_client.types.donnees.batiment_groupe import BatimentGroupeAdresse, AdresseListResponse
```

Methods:

- <code title="get /donnees/batiment_groupe_adresse">client.donnees.batiment_groupe.adresse.<a href="./src/bdnb_client/resources/donnees/batiment_groupe/adresse.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/batiment_groupe/adresse_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/batiment_groupe/adresse_list_response.py">AdresseListResponse</a></code>

### DleGazMultimillesime

Types:

```python
from bdnb_client.types.donnees.batiment_groupe import (
    BatimentGroupeDleGazMultimillesime,
    DleGazMultimillesimeListResponse,
)
```

Methods:

- <code title="get /donnees/batiment_groupe_dle_gaz_multimillesime">client.donnees.batiment_groupe.dle_gaz_multimillesime.<a href="./src/bdnb_client/resources/donnees/batiment_groupe/dle_gaz_multimillesime.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/batiment_groupe/dle_gaz_multimillesime_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/batiment_groupe/dle_gaz_multimillesime_list_response.py">DleGazMultimillesimeListResponse</a></code>

### Radon

Types:

```python
from bdnb_client.types.donnees.batiment_groupe import BatimentGroupeRadon, RadonListResponse
```

Methods:

- <code title="get /donnees/batiment_groupe_radon">client.donnees.batiment_groupe.radon.<a href="./src/bdnb_client/resources/donnees/batiment_groupe/radon.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/batiment_groupe/radon_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/batiment_groupe/radon_list_response.py">RadonListResponse</a></code>

### DvfOpenRepresentatif

Types:

```python
from bdnb_client.types.donnees.batiment_groupe import (
    BatimentGroupeDvfOpenRepresentatif,
    DvfOpenRepresentatifListResponse,
)
```

Methods:

- <code title="get /donnees/batiment_groupe_dvf_open_representatif">client.donnees.batiment_groupe.dvf_open_representatif.<a href="./src/bdnb_client/resources/donnees/batiment_groupe/dvf_open_representatif.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/batiment_groupe/dvf_open_representatif_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/batiment_groupe/dvf_open_representatif_list_response.py">DvfOpenRepresentatifListResponse</a></code>

### SimulationsDvf

Types:

```python
from bdnb_client.types.donnees.batiment_groupe import (
    BatimentGroupeSimulationsDvf,
    SimulationsDvfListResponse,
)
```

Methods:

- <code title="get /donnees/batiment_groupe_simulations_dvf">client.donnees.batiment_groupe.simulations_dvf.<a href="./src/bdnb_client/resources/donnees/batiment_groupe/simulations_dvf.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/batiment_groupe/simulations_dvf_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/batiment_groupe/simulations_dvf_list_response.py">SimulationsDvfListResponse</a></code>

### DpeStatistiqueLogement

Types:

```python
from bdnb_client.types.donnees.batiment_groupe import (
    BatimentGroupeDpeStatistiqueLogement,
    DpeStatistiqueLogementListResponse,
)
```

Methods:

- <code title="get /donnees/batiment_groupe_dpe_statistique_logement">client.donnees.batiment_groupe.dpe_statistique_logement.<a href="./src/bdnb_client/resources/donnees/batiment_groupe/dpe_statistique_logement.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/batiment_groupe/dpe_statistique_logement_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/batiment_groupe/dpe_statistique_logement_list_response.py">DpeStatistiqueLogementListResponse</a></code>

### DleReseauxMultimillesime

Types:

```python
from bdnb_client.types.donnees.batiment_groupe import (
    BatimentGroupeDleReseauxMultimillesime,
    DleReseauxMultimillesimeListResponse,
)
```

Methods:

- <code title="get /donnees/batiment_groupe_dle_reseaux_multimillesime">client.donnees.batiment_groupe.dle_reseaux_multimillesime.<a href="./src/bdnb_client/resources/donnees/batiment_groupe/dle_reseaux_multimillesime.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/batiment_groupe/dle_reseaux_multimillesime_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/batiment_groupe/dle_reseaux_multimillesime_list_response.py">DleReseauxMultimillesimeListResponse</a></code>

### Rnc

Types:

```python
from bdnb_client.types.donnees.batiment_groupe import BatimentGroupeRnc, RncListResponse
```

Methods:

- <code title="get /donnees/batiment_groupe_rnc">client.donnees.batiment_groupe.rnc.<a href="./src/bdnb_client/resources/donnees/batiment_groupe/rnc.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/batiment_groupe/rnc_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/batiment_groupe/rnc_list_response.py">RncListResponse</a></code>

### Bpe

Types:

```python
from bdnb_client.types.donnees.batiment_groupe import BatimentGroupeBpe, BpeListResponse
```

Methods:

- <code title="get /donnees/batiment_groupe_bpe">client.donnees.batiment_groupe.bpe.<a href="./src/bdnb_client/resources/donnees/batiment_groupe/bpe.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/batiment_groupe/bpe_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/batiment_groupe/bpe_list_response.py">BpeListResponse</a></code>

### FfoBat

Types:

```python
from bdnb_client.types.donnees.batiment_groupe import BatimentGroupeFfoBat, FfoBatListResponse
```

Methods:

- <code title="get /donnees/batiment_groupe_ffo_bat">client.donnees.batiment_groupe.ffo_bat.<a href="./src/bdnb_client/resources/donnees/batiment_groupe/ffo_bat.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/batiment_groupe/ffo_bat_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/batiment_groupe/ffo_bat_list_response.py">FfoBatListResponse</a></code>

### Argiles

Types:

```python
from bdnb_client.types.donnees.batiment_groupe import BatimentGroupeArgiles, ArgileListResponse
```

Methods:

- <code title="get /donnees/batiment_groupe_argiles">client.donnees.batiment_groupe.argiles.<a href="./src/bdnb_client/resources/donnees/batiment_groupe/argiles.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/batiment_groupe/argile_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/batiment_groupe/argile_list_response.py">ArgileListResponse</a></code>

### Hthd

Types:

```python
from bdnb_client.types.donnees.batiment_groupe import BatimentGroupeHthd, HthdListResponse
```

Methods:

- <code title="get /donnees/batiment_groupe_hthd">client.donnees.batiment_groupe.hthd.<a href="./src/bdnb_client/resources/donnees/batiment_groupe/hthd.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/batiment_groupe/hthd_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/batiment_groupe/hthd_list_response.py">HthdListResponse</a></code>

### BdtopoBat

Types:

```python
from bdnb_client.types.donnees.batiment_groupe import BatimentGroupeBdtopoBat, BdtopoBatListResponse
```

Methods:

- <code title="get /donnees/batiment_groupe_bdtopo_bat">client.donnees.batiment_groupe.bdtopo_bat.<a href="./src/bdnb_client/resources/donnees/batiment_groupe/bdtopo_bat.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/batiment_groupe/bdtopo_bat_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/batiment_groupe/bdtopo_bat_list_response.py">BdtopoBatListResponse</a></code>

### DleElecMultimillesime

Types:

```python
from bdnb_client.types.donnees.batiment_groupe import (
    BatimentGroupeDleElecMultimillesime,
    DleElecMultimillesimeListResponse,
)
```

Methods:

- <code title="get /donnees/batiment_groupe_dle_elec_multimillesime">client.donnees.batiment_groupe.dle_elec_multimillesime.<a href="./src/bdnb_client/resources/donnees/batiment_groupe/dle_elec_multimillesime.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/batiment_groupe/dle_elec_multimillesime_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/batiment_groupe/dle_elec_multimillesime_list_response.py">DleElecMultimillesimeListResponse</a></code>

### WallDict

Types:

```python
from bdnb_client.types.donnees.batiment_groupe import BatimentGroupeWallDict, WallDictListResponse
```

Methods:

- <code title="get /donnees/batiment_groupe_wall_dict">client.donnees.batiment_groupe.wall_dict.<a href="./src/bdnb_client/resources/donnees/batiment_groupe/wall_dict.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/batiment_groupe/wall_dict_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/batiment_groupe/wall_dict_list_response.py">WallDictListResponse</a></code>

### IndicateurReseauChaudFroid

Types:

```python
from bdnb_client.types.donnees.batiment_groupe import (
    BatimentGroupeIndicateurReseauChaudFroid,
    IndicateurReseauChaudFroidListResponse,
)
```

Methods:

- <code title="get /donnees/batiment_groupe_indicateur_reseau_chaud_froid">client.donnees.batiment_groupe.indicateur_reseau_chaud_froid.<a href="./src/bdnb_client/resources/donnees/batiment_groupe/indicateur_reseau_chaud_froid.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/batiment_groupe/indicateur_reseau_chaud_froid_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/batiment_groupe/indicateur_reseau_chaud_froid_list_response.py">IndicateurReseauChaudFroidListResponse</a></code>

### DelimitationEnveloppe

Types:

```python
from bdnb_client.types.donnees.batiment_groupe import (
    BatimentGroupeDelimitationEnveloppe,
    DelimitationEnveloppeListResponse,
)
```

Methods:

- <code title="get /donnees/batiment_groupe_delimitation_enveloppe">client.donnees.batiment_groupe.delimitation_enveloppe.<a href="./src/bdnb_client/resources/donnees/batiment_groupe/delimitation_enveloppe.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/batiment_groupe/delimitation_enveloppe_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/batiment_groupe/delimitation_enveloppe_list_response.py">DelimitationEnveloppeListResponse</a></code>

### SimulationsValeurVerte

Types:

```python
from bdnb_client.types.donnees.batiment_groupe import (
    BatimentGroupeSimulationsValeurVerte,
    SimulationsValeurVerteListResponse,
)
```

Methods:

- <code title="get /donnees/batiment_groupe_simulations_valeur_verte">client.donnees.batiment_groupe.simulations_valeur_verte.<a href="./src/bdnb_client/resources/donnees/batiment_groupe/simulations_valeur_verte.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/batiment_groupe/simulations_valeur_verte_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/batiment_groupe/simulations_valeur_verte_list_response.py">SimulationsValeurVerteListResponse</a></code>

### IrisSimulationsValeurVerte

Types:

```python
from bdnb_client.types.donnees.batiment_groupe import (
    IrisSimulationsValeurVerte,
    IrisSimulationsValeurVerteListResponse,
)
```

Methods:

- <code title="get /donnees/iris_simulations_valeur_verte">client.donnees.batiment_groupe.iris_simulations_valeur_verte.<a href="./src/bdnb_client/resources/donnees/batiment_groupe/iris_simulations_valeur_verte.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/batiment_groupe/iris_simulations_valeur_verte_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/batiment_groupe/iris_simulations_valeur_verte_list_response.py">IrisSimulationsValeurVerteListResponse</a></code>

### IrisContexteGeographique

Types:

```python
from bdnb_client.types.donnees.batiment_groupe import (
    IrisContexteGeographique,
    IrisContexteGeographiqueListResponse,
)
```

Methods:

- <code title="get /donnees/iris_contexte_geographique">client.donnees.batiment_groupe.iris_contexte_geographique.<a href="./src/bdnb_client/resources/donnees/batiment_groupe/iris_contexte_geographique.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/batiment_groupe/iris_contexte_geographique_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/batiment_groupe/iris_contexte_geographique_list_response.py">IrisContexteGeographiqueListResponse</a></code>

## Ancqpv

Types:

```python
from bdnb_client.types.donnees import Ancqpv, AncqpvListResponse
```

Methods:

- <code title="get /donnees/ancqpv">client.donnees.ancqpv.<a href="./src/bdnb_client/resources/donnees/ancqpv.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/ancqpv_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/ancqpv_list_response.py">AncqpvListResponse</a></code>

## Proprietaire

Types:

```python
from bdnb_client.types.donnees import Proprietaire, ProprietaireListResponse
```

Methods:

- <code title="get /donnees/proprietaire">client.donnees.proprietaire.<a href="./src/bdnb_client/resources/donnees/proprietaire.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/proprietaire_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/proprietaire_list_response.py">ProprietaireListResponse</a></code>

## BatimentConstruction

Types:

```python
from bdnb_client.types.donnees import BatimentConstruction, BatimentConstructionListResponse
```

Methods:

- <code title="get /donnees/batiment_construction">client.donnees.batiment_construction.<a href="./src/bdnb_client/resources/donnees/batiment_construction.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/batiment_construction_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/batiment_construction_list_response.py">BatimentConstructionListResponse</a></code>

## Adresse

Types:

```python
from bdnb_client.types.donnees import Adresse, AdresseListResponse
```

Methods:

- <code title="get /donnees/adresse">client.donnees.adresse.<a href="./src/bdnb_client/resources/donnees/adresse.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/adresse_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/adresse_list_response.py">AdresseListResponse</a></code>

## ReferentielAdministratif

### ReferentielAdministratifIris

Types:

```python
from bdnb_client.types.donnees.referentiel_administratif import (
    ReferentielAdministratifIris,
    ReferentielAdministratifIrisListResponse,
)
```

Methods:

- <code title="get /donnees/referentiel_administratif_iris">client.donnees.referentiel_administratif.referentiel_administratif_iris.<a href="./src/bdnb_client/resources/donnees/referentiel_administratif/referentiel_administratif_iris.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/referentiel_administratif/referentiel_administratif_iris_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/referentiel_administratif/referentiel_administratif_iris_list_response.py">ReferentielAdministratifIrisListResponse</a></code>

### Epci

Types:

```python
from bdnb_client.types.donnees.referentiel_administratif import (
    ReferentielAdministratifEpci,
    EpciListResponse,
)
```

Methods:

- <code title="get /donnees/referentiel_administratif_epci">client.donnees.referentiel_administratif.epci.<a href="./src/bdnb_client/resources/donnees/referentiel_administratif/epci.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/referentiel_administratif/epci_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/referentiel_administratif/epci_list_response.py">EpciListResponse</a></code>

### Departement

Types:

```python
from bdnb_client.types.donnees.referentiel_administratif import (
    ReferentielAdministratifDepartement,
    DepartementListResponse,
)
```

Methods:

- <code title="get /donnees/referentiel_administratif_departement">client.donnees.referentiel_administratif.departement.<a href="./src/bdnb_client/resources/donnees/referentiel_administratif/departement.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/referentiel_administratif/departement_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/referentiel_administratif/departement_list_response.py">DepartementListResponse</a></code>

### Region

Types:

```python
from bdnb_client.types.donnees.referentiel_administratif import (
    ReferentielAdministratifRegion,
    RegionListResponse,
)
```

Methods:

- <code title="get /donnees/referentiel_administratif_region">client.donnees.referentiel_administratif.region.<a href="./src/bdnb_client/resources/donnees/referentiel_administratif/region.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/referentiel_administratif/region_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/referentiel_administratif/region_list_response.py">RegionListResponse</a></code>

## Relations

### BatimentConstruction

#### Adresse

Types:

```python
from bdnb_client.types.donnees.relations.batiment_construction import (
    RelBatimentConstructionAdresse,
    AdresseListResponse,
)
```

Methods:

- <code title="get /donnees/rel_batiment_construction_adresse">client.donnees.relations.batiment_construction.adresse.<a href="./src/bdnb_client/resources/donnees/relations/batiment_construction/adresse.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/relations/batiment_construction/adresse_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/relations/batiment_construction/adresse_list_response.py">AdresseListResponse</a></code>

### BatimentGroupe

#### ProprietaireSiren

Types:

```python
from bdnb_client.types.donnees.relations.batiment_groupe import (
    RelBatimentGroupeProprietaireSiren,
    ProprietaireSirenListResponse,
)
```

Methods:

- <code title="get /donnees/rel_batiment_groupe_proprietaire_siren">client.donnees.relations.batiment_groupe.proprietaire_siren.<a href="./src/bdnb_client/resources/donnees/relations/batiment_groupe/proprietaire_siren.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/relations/batiment_groupe/proprietaire_siren_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/relations/batiment_groupe/proprietaire_siren_list_response.py">ProprietaireSirenListResponse</a></code>

#### Qpv

Types:

```python
from bdnb_client.types.donnees.relations.batiment_groupe import (
    RelBatimentGroupeQpv,
    QpvListResponse,
)
```

Methods:

- <code title="get /donnees/rel_batiment_groupe_qpv">client.donnees.relations.batiment_groupe.qpv.<a href="./src/bdnb_client/resources/donnees/relations/batiment_groupe/qpv.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/relations/batiment_groupe/qpv_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/relations/batiment_groupe/qpv_list_response.py">QpvListResponse</a></code>

#### Adresse

Types:

```python
from bdnb_client.types.donnees.relations.batiment_groupe import (
    RelBatimentGroupeAdresse,
    AdresseListResponse,
)
```

Methods:

- <code title="get /donnees/rel_batiment_groupe_adresse">client.donnees.relations.batiment_groupe.adresse.<a href="./src/bdnb_client/resources/donnees/relations/batiment_groupe/adresse.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/relations/batiment_groupe/adresse_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/relations/batiment_groupe/adresse_list_response.py">AdresseListResponse</a></code>

#### Merimee

Types:

```python
from bdnb_client.types.donnees.relations.batiment_groupe import (
    RelBatimentGroupeMerimee,
    MerimeeListResponse,
)
```

Methods:

- <code title="get /donnees/rel_batiment_groupe_merimee">client.donnees.relations.batiment_groupe.merimee.<a href="./src/bdnb_client/resources/donnees/relations/batiment_groupe/merimee.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/relations/batiment_groupe/merimee_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/relations/batiment_groupe/merimee_list_response.py">MerimeeListResponse</a></code>

#### Parcelle

Types:

```python
from bdnb_client.types.donnees.relations.batiment_groupe import (
    RelBatimentGroupeParcelle,
    ParcelleListResponse,
)
```

Methods:

- <code title="get /donnees/rel_batiment_groupe_parcelle">client.donnees.relations.batiment_groupe.parcelle.<a href="./src/bdnb_client/resources/donnees/relations/batiment_groupe/parcelle.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/relations/batiment_groupe/parcelle_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/relations/batiment_groupe/parcelle_list_response.py">ParcelleListResponse</a></code>

#### SirenComplet

Types:

```python
from bdnb_client.types.donnees.relations.batiment_groupe import (
    RelBatimentGroupeSirenComplet,
    SirenCompletListResponse,
)
```

Methods:

- <code title="get /donnees/rel_batiment_groupe_siren_complet">client.donnees.relations.batiment_groupe.siren_complet.<a href="./src/bdnb_client/resources/donnees/relations/batiment_groupe/siren_complet.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/relations/batiment_groupe/siren_complet_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/relations/batiment_groupe/siren_complet_list_response.py">SirenCompletListResponse</a></code>

#### SiretComplet

Types:

```python
from bdnb_client.types.donnees.relations.batiment_groupe import (
    RelBatimentGroupeSiretComplet,
    SiretCompletListResponse,
)
```

Methods:

- <code title="get /donnees/rel_batiment_groupe_siret_complet">client.donnees.relations.batiment_groupe.siret_complet.<a href="./src/bdnb_client/resources/donnees/relations/batiment_groupe/siret_complet.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/relations/batiment_groupe/siret_complet_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/relations/batiment_groupe/siret_complet_list_response.py">SiretCompletListResponse</a></code>

#### Rnc

Types:

```python
from bdnb_client.types.donnees.relations.batiment_groupe import (
    RelBatimentGroupeRnc,
    RncListResponse,
)
```

Methods:

- <code title="get /donnees/rel_batiment_groupe_rnc">client.donnees.relations.batiment_groupe.rnc.<a href="./src/bdnb_client/resources/donnees/relations/batiment_groupe/rnc.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/relations/batiment_groupe/rnc_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/relations/batiment_groupe/rnc_list_response.py">RncListResponse</a></code>

#### ProprietaireSirenOpen

Types:

```python
from bdnb_client.types.donnees.relations.batiment_groupe import (
    RelBatimentGroupeProprietaireSirenOpen,
    ProprietaireSirenOpenListResponse,
)
```

Methods:

- <code title="get /donnees/rel_batiment_groupe_proprietaire_siren_open">client.donnees.relations.batiment_groupe.proprietaire_siren_open.<a href="./src/bdnb_client/resources/donnees/relations/batiment_groupe/proprietaire_siren_open.py">list</a>(\*\*<a href="src/bdnb_client/types/donnees/relations/batiment_groupe/proprietaire_siren_open_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/donnees/relations/batiment_groupe/proprietaire_siren_open_list_response.py">ProprietaireSirenOpenListResponse</a></code>

# Metadonnees

## ColonnesSouscription

Types:

```python
from bdnb_client.types.metadonnees import ColonneSouscription, ColonnesSouscriptionListResponse
```

Methods:

- <code title="get /metadonnees/colonne_souscription">client.metadonnees.colonnes_souscription.<a href="./src/bdnb_client/resources/metadonnees/colonnes_souscription.py">list</a>(\*\*<a href="src/bdnb_client/types/metadonnees/colonnes_souscription_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/metadonnees/colonnes_souscription_list_response.py">ColonnesSouscriptionListResponse</a></code>

## Colonnes

Types:

```python
from bdnb_client.types.metadonnees import Colonne, ColonneListResponse
```

Methods:

- <code title="get /metadonnees/colonne">client.metadonnees.colonnes.<a href="./src/bdnb_client/resources/metadonnees/colonnes.py">list</a>(\*\*<a href="src/bdnb_client/types/metadonnees/colonne_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/metadonnees/colonne_list_response.py">ColonneListResponse</a></code>

## Info

Types:

```python
from bdnb_client.types.metadonnees import Info, InfoListResponse
```

Methods:

- <code title="get /metadonnees/info">client.metadonnees.info.<a href="./src/bdnb_client/resources/metadonnees/info.py">list</a>(\*\*<a href="src/bdnb_client/types/metadonnees/info_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/metadonnees/info_list_response.py">InfoListResponse</a></code>

## Table

Types:

```python
from bdnb_client.types.metadonnees import Table, TableListResponse
```

Methods:

- <code title="get /metadonnees/table">client.metadonnees.table.<a href="./src/bdnb_client/resources/metadonnees/table.py">list</a>(\*\*<a href="src/bdnb_client/types/metadonnees/table_list_params.py">params</a>) -> <a href="./src/bdnb_client/types/metadonnees/table_list_response.py">TableListResponse</a></code>

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
