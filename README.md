# Literumilo - A spell checker and morphological analyzer for Esperanto.

This program analyzes individual Esperanto words, or an entire file of Esperanto text.

## Requirements

Literumilo was developed and tested on Python 3.7 .

## Usage

To run literumilo from the command line, type the word or file to analyze after the program name. For example,
to analyze the word 'kafejo', run the command:

$ `python3 literumilo.py kafejo`

The program will print out the word 'kafejo', divided into morphemes, and a check mark:

`kaf.ej.o ✓`

If the word is misspelled, for example 'kafeyo', the program will print an X: `✘kafeyo`

To check the spelling in a file, eg. 'likaono.txt', enter the command:

$ `python3 literumilo.py likaono.txt`

Literumilo will print a list of unknown words to standard out:

Lycaon  
mezgrandajnd  
habitatoj  
pictus  
Canis  
kanisedo  
jdaroj  

Literumilo has a morphological analysis option: -m. Run the command as below:

$ `python3 literumilo.py -m likaono.txt`

The program will output the text to standard out, with known Esperanto words divided into morphemes. For example:

Ĝi est.as unik.a kanisedo, nom.e la unu.nur.a speci.o en la genr.o likaon.o. Ĝi est.as plej proksim.e rilat.a al la genr.o Canis, kvankam ĝi ne pov.as inter.re.produkt.iĝ.i kun ili. Ĝi est.as frukt.o.don.a re.produkt.ul.o, kun grand.aj jdaroj de ĝis 19 likaon.id.oj, kaj pov.as re.produkt.iĝ.i je iu ajn epok.o de la jar.o. La re.produkt.ad.o est.as kutim.e lim.ig.it.a al la alf.a par.o.

## Tests

To run unit tests, run the following command:

$ `python3 -m unittest tests/test_literumilo.py`

The output should be:

```
..
----------------------------------------------------------------------
Ran 2 tests in 0.002s

OK
```

## Developer

Literumilo was developed by Cleve (Klivo) Lendon.

## Contact

To contact the developer, send email to indriko@yahoo.com . Preferred languages are English and Esperanto. Comments, suggestions and criticism are welcomed.

## History

First release, May 2020.

## License

Literumilo is free software. It is distributed free of charge, without conditions, and without guarantees. You may use, modify and distribute it as you wish. There is no need to ask for permission. If you use Literumilo's code in your own project, and publish it, I request only that you acknowledge the source.
