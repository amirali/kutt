# Kutt cli

![](https://img.shields.io/pypi/v/kutt)

⚠️ This repo will be archived until further notice.  
Long story short, I had some ideas about contributing to kutt itself and update this repo as it goes on. But for the past months, I could find the time nor energy to do it. If you are willing to maintain this repo, contact me via [email](mailto:amiralinull+kutt@gmail.com) to discuss the ideas and transfer the ownership.

- [CLI](https://github.com/amirali/kutt#cli)
- [library](https://github.com/amirali/kutt#lib)

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
