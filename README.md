# Literumilo - A spell checker and morphological analyzer for Esperanto.

Literumilo checks the spelling of Esperanto words, and divides them into morphemes. For example, 'miskomprenita' is divided as 'mis.kompren.it.a'.

Literumilo can analyze individual Esperanto words, or an entire file of Esperanto text.

## Requirements

Literumilo was developed and tested on Python 3.7 .

## Links

Github: [https://github.com/Indrikoterio/literumilo-python](https://github.com/Indrikoterio/literumilo-python)

PyPi: [https://pypi.org/project/literumilo/1.0.8/](https://pypi.org/project/literumilo/1.0.8/)

## Installation

This works for me:

```
$ python3 -m pip install literumilo
```

## Usage

### Importing

In your Python program, you can import the module simply as shown here:

```
import literumilo
```

Using the above method, literumilo's functions must be prefixed with the package name, as below:

```
result = literumilo.check_word("ĉirkaŭiris")
```

Alternatively, you can import the function names directly:

```
from literumilo import x_to_accent
from literumilo import check_word
from literumilo import analyze_string
from literumilo import analyze_file
```

The code samples below assume that the second method has been used:

### x\_to\_accent

This function converts from the 'x method' to Unicode accented letters. For example, the following line:

```
print(x_to_accent("cxirkaux"))
```

prints out `ĉirkaŭ`.

### check_word

The function check_word checks the spelling of an Esperanto word, and divides it into morphemes, if it is valid. It returns a class, AnalysisResult, with two attributes, 'word' and 'valid' (valid is boolean). For example:

```
result = check_word("ĉirkaŭiris")
if result.valid:
    print("OK> {}".format(result.word))
else:
    print("Bad> {}".format(result.word))
```

The above code will print out `OK> ĉirkaŭ.ir.is`.

### analyze_string

This function has two modes, morpheme mode and spell checker mode. The first parameter is the string to analyze. The second is the mode. When the mode is True, analyze_string will divide every Esperanto word in the string into morphemes, and return the new string. For example:

```
TEXT = "Birdoj (Aves) estas klaso de vertebruloj kun ĉirkaŭ 9 ĝis 10 mil vivantaj specioj."
result = analyze_string(TEXT, True)
print(result)
```

The above will print out

```
Bird.oj (Aves) est.as klas.o de vertebr.ul.oj kun ĉirkaŭ 9 ĝis 10 mil viv.ant.aj speci.oj
```

When the morpheme mode is False, analyze_string outputs a list of unknown words. This code,

```
TEXT = "Birdoj (Aves) estas klaso de vertebruloj kun ĉirkaŭ 9 ĝis 10 mil vivantaj specioj."
result = analyze_string(TEXT, False)
print(result)
```

will print out:

```
Aves
```

### analyze_file

The function analyze\_file simply reads a file into a string, and calls analyze\_string. For example:

```
result = analyze_file(file_path, True)
print(result)
```

The second parameter is the mode - the same as analyze_string's mode parameter.

## Developer

Literumilo was developed by Cleve (Klivo) Lendon.

## Contact

To contact the developer, send email to indriko@yahoo.com . Preferred languages are English and Esperanto. Comments, suggestions and criticism are welcomed.

## History

First release, May 2020.

## License

Literumilo is free software. It is distributed free of charge, without conditions, and without guarantees. You may use, modify and distribute it as you wish. There is no need to ask for permission. If you use Literumilo's code in your own project, and publish it, I request only that you acknowledge the source.
