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
    password="OPTIONAL password",
    customurl="OPTIONAL customurl",
    domain="OPTIONAL custom domain",
    reuse=True, # OPTIONAL
    host_url="OPTIONAL host url")

# For delete a URL
kutt.delete(API, "URL or ID", host_url="OPTIONAL host url")

# Get urls list
links = kutt.links(API, host_url="OPTIONAL host url")
```
