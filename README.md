# DataTools

Collection of tools to quickly process data in some different formats.

## Requirements

The ``requirements.txt`` specifies a list of requirements for **all**
the script. If you just need to use some, you'll probably don't need
all the dependencies.

However, usually it won't harm to install them anyways.

To install:

```console
virtualenv .venv
source .venv/bin/activate

pip install -r requirements.txt
```


## The tools

### charset_convert.py

Convert a file from a charset to another.

Example usage (convert a file from latin-1 to utf-8):

```
cat input_file.txt | python charset_convert.py latin-1 utf-8 > output_file.txt
```

### xpath.py

Perform an XPATH query on a XML file.

Example usage:

```
cat input.xml | python xpath.py 'dct:title'
```

**Warning:** the output depends on the xpath query itself, and it is **not** guaranteed to be valid XML
(eg. if selecting ``text()`` or a bunch of nodes)
