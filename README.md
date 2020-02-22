# Kutt cli

- [CLI](https://github.com/realamirali/kutt-cli#cli)
- [library](https://github.com/realamirali/kutt-cli#lib)

## CLI

Signup in kutt.it and in setting menu generate an API Key and run `kutt config-api`

(plz use python 3 for install and run kutt)
```
> pip install kutt
```

```
  > kutt --help

  Usage: kutt [OPTIONS] COMMAND [ARGS]...

  Submit(options):
      -c, --customurl STRING          Custom ID for custom URL
      -p, --password STRING           Password for the URL
      -r, --reuse                     Return last object of target if exists
  Submit(example):
      > kutt submit -c '[CUSTOM]' -p '[PASSWORD]' -r "[URL]"
  Delete(example):
      > kutt delete [URL/ID]
  List(example):
      > kutt list

  Options:
  --help  Show this message and exit.

  Commands:
  delete  Delete a shorted link (Give me url id or url shorted)
  list    List of last 5 URL objects.
  submit  Submit a new short URL
```

# lib

use kutt in your code in this sul:  
```python
from kutt import kutt

API = "YOUR_API_KEY"

# For submit a new URL
# obj variable has url object data (read the https://github.com/thedevs-network/kutt#api document)
obj = kutt.submit(API, "URL", password="OPTIONAL password", customurl="OPTIONAL customurl", reuse=True) # reuse, customurl and password are OPTIONAL

# For delete a URL
kutt.delete(API, "URL or ID")

# Get urls list
links = kutt.links(API)
```
