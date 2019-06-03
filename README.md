# Using word vector models to trace conceptual change over time



## Scripts:

### extract_words.py

This script extracts words from ShiCo backend and shows all words in the column and presents the similarity score:

'''
python3 extract_words.py backend query_term min_count show_every_x translate merge_words
'''

with:

-  backend: URL of the backend 
- query_term: term that is searched
- min_count: minimum occurrence of term in all models
- show_every_x: stepwise for the selected time spans (e.g. for German only models are availble for every two years, thus a value of 2 should be selected)
- translate: name of the dictionary. The file contains the word in the language of the model followed by the word in e.g. English
- mapping of writing variation, e.g.: death:deat,deah column:colum,colunn

__Example:__

'''
python3 extract_words.py http://193.167.189.229/shico-settings-swe/ sjukdom 0 2 dict.sw sjukdom:sjuldom,fjukdom,sjnkdom,sjutdom,fjuldom,fjutdom,slutdom,fjufbom  afled:aflidit,alled,aflcd,asted,afledo,afied långvarig:längwarig,långvari
'''

## Dataset:

Translations:

Categories:


## ShiCo backends:

| Modelname | Frontend | Backend |
|-----------|----------|---------|
| Swedish | http://www.comhis.fi/shico_swe | http://193.167.189.229/shico-settings-swe/  |
| German SBB| http://shico-sbb.ims.uni-stuttgart.de/| http://shico-sbb.ims.uni-stuttgart.de/backend/|
| German Europeana| http://shico-europeana.ims.uni-stuttgart.de/ | http://shico-europeana.ims.uni-stuttgart.de/backend/|
| German Chronicling America| http://shico-ca.ims.uni-stuttgart.de/  | http://shico-ca.ims.uni-stuttgart.de/backend/|
| Finnish  | http://www.comhis.fi/shico_fin | http://195.148.30.187/shico-settings-fin/ |
| Times | https://shico-times-2.hum.uu.nl/  | https://shico-times-2.hum.uu.nl/api/ |


## Publication:

to appear
