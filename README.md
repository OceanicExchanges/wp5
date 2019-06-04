# Using word vector models to trace conceptual change over time

Here, we provide scripts that have been created to trace concepts across different time spans. These scripts require that embeddings are available through the [ShiCo](https://github.com/NLeSC/ShiCo) backend.


## Scripts:

- extract_words.py: script to generate table of times and words and shows the similarity scores for each word in the given time span


### extract_words.py

This script extracts words from ShiCo backend and shows all words in the column and presents the similarity score:

```
python3 extract_words.py backend query_term min_count show_every_x translate merge_words
```

with:

-  backend: URL of the backend 
- query_term: term that is searched
- min_count: minimum occurrence of term in all models
- show_every_x: stepwise for the selected time spans (e.g. for German only models are availble for every two years, thus a value of 2 should be selected)
- translate: name of the dictionary. The file contains the word in the language of the model followed by the word in e.g. English
- mapping of writing variation, e.g.: death:deat,deah column:colum,colunn

__Example:__

```
python3 extract_words.py http://193.167.189.229/shico-settings-swe/ sjukdom 0 2 ../data/dict.sw sjukdom:sjuldom,fjukdom,sjnkdom,sjutdom,fjuldom,fjutdom,slutdom,fjufbom  afled:aflidit,alled,aflcd,asted,afledo,afied långvarig:längwarig,långvari
```

__Output of Example (excerpt):__

```
http://193.167.189.229/shico-settings-swe//track/sjukdom?aggWFParam=1&aggWeighFunction=Gaussian&aggWordsPerYear=5&aggYearsInInterval=5&algorithm=Non-adaptive&boostMethod=Sum+similarity&doCleaning=No&endKey=&forwards=Forward&maxRelatedTerms=10&maxTerms=15&minSim=0.1&startKey=&wordBoost=1
	disease	breast disease	died	mental disease	trouble	eye disease	crying	epidemic	fever	long-standing	still	cold	death-struggle	epidemic	peaceful	fever	stomach disease	disease	long-standing	suffering	insanity	heart suffering	passed away	contagious	tyfus	disease	lung disease	appendicitis	neuropathy	deafness	purulent	pneumonia	tuberculosis	plague	paralysis	sepsis	overstrain	infirmity	calm	UNKNOWN	caught	UNKNOWN	recovered	wound	influenza	UNKNOWN
year	sjukdom(199)	bröstsjukdom(59)	afled(45)	sinnessjukdom(40)	åkomma(31)	ögonsjukdom(29)	långvarig(22)	tärande(20)	farsot(20)	febersjukdom(16)	stilla(14)	förkylning(14)	dödskamp(13)	epidemi(11)	fridfullt(10)	feber(10)	magsjukdom(10)	ohälsa(9)	langwarig(7)	lidande(7)	sinnesrubbning(6)	hjärtlidande(5)	afsomnade(4)	smittosam(4)	tyfus(4)	sjukdomen(4)	lungsjukdom(4)	blindtarmsinflammation(3)	nervsjukdom(3)	döfhet(3)	varig(2)	lunginflammation(2)	lungsot(2)	plågor(2)	förlamning(2)	blodförgiftning(2)	öfveransträngning(2)	ålderdomssvaghet(2)	lugnt(1)	häftig(1)	påkommen(1)	iråkad(1)	tillfrisknat(1)	blessyr(1)	influensa(1)	insjuknande(1)
1840_1850	0.0000	0.6719	0.5729	0.0000	0.0000	0.0000	0.6622	0.7434	0.0000	0.0000	0.6518	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.6381	0.0000	0.0000	0.0000	0.5463	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.5476	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000
1842_1852	0.6771	0.6756	0.5504	0.0000	0.0000	0.0000	0.6315	0.7259	0.0000	0.0000	0.6210	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.6151	0.0000	0.0000	0.0000	0.5361	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000
1844_1854	0.6579	0.6867	0.5601	0.0000	0.0000	0.0000	0.6035	0.7007	0.0000	0.0000	0.5699	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.5834	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000
1846_1856	0.6585	0.6918	0.5467	0.0000	0.0000	0.0000	0.5906	0.7005	0.0000	0.6010	0.5340	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.5339	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000
1848_1858	0.5939	0.7124	0.5452	0.0000	0.0000	0.0000	0.5766	0.6815	0.0000	0.5617	0.5374	0.0000	0.0000	0.0000	0.5702	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000
1850_1860	0.6266	0.7051	0.5402	0.0000	0.0000	0.0000	0.5440	0.6969	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.5602	0.5508	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000
1852_1862	0.0000	0.6807	0.5526	0.0000	0.0000	0.0000	0.5183	0.6951	0.0000	0.5264	0.5373	0.0000	0.0000	0.0000	0.5892	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.5299	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000
1854_1864	0.0000	0.6726	0.5251	0.0000	0.0000	0.0000	0.5114	0.6603	0.0000	0.0000	0.5122	0.0000	0.0000	0.0000	0.5453	0.5438	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.5127	0.0000	0.0000	0.0000	0.0000	0.0000
1856_1866	0.0000	0.6528	0.5297	0.0000	0.0000	0.0000	0.0000	0.6161	0.5231	0.0000	0.0000	0.5181	0.0000	0.0000	0.5132	0.5427	0.0000	0.0000	0.0000	0.5352	0.0000	0.0000	0.0000	0.5199	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.5134	0.0000	0.0000	0.0000
1858_1868	0.6470	0.6323	0.0000	0.0000	0.0000	0.0000	0.0000	0.5498	0.5923	0.5778	0.0000	0.0000	0.0000	0.5539	0.0000	0.6083	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.0000	0.00
```

## Dataset:

Translations:

Categories:


## ShiCo backends:

| Modelname | Frontend | Backend |
|-----------|----------|---------|
| Finnish  | http://www.comhis.fi/shico_fin | http://195.148.30.187/shico-settings-fin/ |
| German SBB| http://shico-sbb.ims.uni-stuttgart.de/| http://shico-sbb.ims.uni-stuttgart.de/backend/|
| German Europeana| http://shico-europeana.ims.uni-stuttgart.de/ | http://shico-europeana.ims.uni-stuttgart.de/backend/|
| German Chronicling America| http://shico-ca.ims.uni-stuttgart.de/  | http://shico-ca.ims.uni-stuttgart.de/backend/|
| Swedish | http://www.comhis.fi/shico_swe | http://193.167.189.229/shico-settings-swe/  |
| Times | https://shico-times-2.hum.uu.nl/  | https://shico-times-2.hum.uu.nl/api/ |


## Publication:

to appear
