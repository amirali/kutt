# Kutt cli

- [CLI](https://github.com/realamirali/kutt-cli#cli)
- [library](https://github.com/realamirali/kutt-cli#lib)

## CLI

Signup in kutt.it and in setting menu generate an API Key and run `kutt config help`

```
> pip install kutt
```
Type `kutt [COMMAND] --help` for get help

# lib

use kutt in your code in this sul:  
```python
from kutt import kutt

API = "YOUR_API_KEY"

# For submit a new URL
# obj variable has url object data (read the https://github.com/thedevs-network/kutt#api document)
obj = kutt.submit(
    API,
    "URL",
    description="OPTIONAL description",
    expire_in="OPTIONAL expire time",
    password="OPTIONAL password",
    customurl="OPTIONAL customurl",
    description="OPTIONAL desciption",
    domain="OPTIONAL custom domain",
    reuse=True, # OPTIONAL
    )

# For delete a URL
kutt.delete(API, "ID")


# update a URL 
kutt.update(API, "ID", "URL", "address", description="OPTIONAL description", expire_in="OPTIONAL expire time")


# Get urls list
links = kutt.links(API, limit=10, skip=0)

# Get url stats
stats = kutt.stats(API, "ID")
```
