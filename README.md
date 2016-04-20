# RnaCancerClassifier

## Files

 * [classifier.py](./classifier.py) contains the main functions:
   * **csv2asp** converts a csv data file into a [Potassco](http://potassco.sourceforge.net) ASP file for the construction of a classifier
   * **gateinputs2pdf** generates a graph-based drawing of a classifier
   * **gateinputs2function** used internally by _check\_classifier_
   * **check\_classifier** checks whether a given classifier is consistent with a given data file
 
 * [toy_data.csv](./toy_data.csv) an example of input data  
 * [toy_settings.py](./toy_settings.py) an example of parameters settings
 

## Example input data
A data file is a 0-1 matrix that contains miRNA expression profiles and whether the tissue is healthy or cancerous.
An example is [toy_data.csv](./toy_data.csv):

```
ID, Annots, g1, g2, g3
1,  0,      1,  1,  1
2,  0,      0,  0,  1
3,  1,      0,  1,  0
```
 * `ID` is the row index
 * `Annots` denotes whether the tissue is _healthy_ by `0` or _cancerous_ by `1`
 * `g1, g2, ...` denotes the expression of a miRNA is _low_ by `0` or _high_ by `1`
 

## Example of parameter settings
A settings file calls functions of [classifier.py](./classifier.py) contains the input parameters 
