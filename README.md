# ProxyCycler
A simple tool for using a collection of proxies with the Python requests library


# Setup

```python    
from proxy-cycler import ProxyCycler
import requests

proxy_cycler = ProxyCycler( 
                    # Add list of proxy URLS                  
                    proxies=["socks5://user:pass@proxyurl.1:1080"],
)

# Add proxy dynamically
proxy_cycler.add_proxy("socks5://user:pass@proxyurl.2:1080")

while True:
    try:
        # each request will use a proxy different from the last
        r = requests.get("google.com",
                         proxies=proxy_cycler.cycle_proxies())
        if r.status_code == 200:
            break
    except requests.exceptions.RequestException:
        pass
```


## Non-HTTP Proxies
Without configuring the ```key ``` member variable of ```ProxyCycler``` the dictionary returned by ```cycle_proxies``` only configures ```http``` and `https` proxies.

```python
proxy_cycler = ProxyCycler(  # Add list of proxy URLS 
                    proxies=["socks5://user:pass@proxyurl.1:1080"]
                    # Include support for ftp and smtp proxies
                    keys=["http", "https", "ftp", "smtp"])
```
