# About
This repository contains tools for creating and analyzing concordances derived from the Digital Corpus of the European Parliament.

The scripts enable one to create sentence-aligned corpora (e.g., tab-delimited documents giving the English and German versions of a document or set of documents line by line) for all the language pairs for which European Parliament translations exist. One can then create a concordance by scanning the corpus for certain terms in one or both of the languages and then identify matches to be investigated in more detail.

The intended user is a (computational) linguist, translator, or researcher investigating the way language and translation are used in the EU, especially with regards to the fact that so many documents are translated and the fact that there is no single official language or version—technically, there are no translations and each version is an original.

The `ladder2text.py` and `languagepair.py` scripts are originally provided by the EU for the DCEP project and are available under the EUPL license. Some changes have and will be made to add or improve functionality. More information about the DCEP project is available here: [https://ec.europa.eu/jrc/en/language-technologies/dcep](https://ec.europa.eu/jrc/en/language-technologies/dcep) and here: [http://optima.jrc.it/Resources/DCEP-2013/DCEP-Download-Page.html](http://optima.jrc.it/Resources/DCEP-2013/DCEP-Download-Page.html).

## Usage
Instructions for downloading and building a corpus are available on the [DCEP download page](http://optima.jrc.it/Resources/DCEP-2013/DCEP-Download-Page.html). The instructions are a bit difficult to follow and I will be adding streamlined instructions later. The DCEP scripts (`languagepairs.py` and `ladder2text.py`) are written for Python 2.7

Once you have created a corpus, you can create a concordance by running `create_concordance.py` (written for Python 3, should work with Python 2.7) and following the prompts. The current version requires that you enter a term for each language. Opting to allow alternate endings is recommended.

After creating a concordance, you can grade it, i.e., verify which results are interesting for your query and which are just coincidental occurences of the two words used to create the concordance, by running `grade_concordance.py`. If the amount of context for a given abbreviated result is not enough to make an evaluation, select `u` to see the full result.