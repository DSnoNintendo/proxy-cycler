from typing import Optional, List


class ProxyCycler:
    def __init__(self, proxies: List[Optional] = None, keys: List[Optional] = None):
        self.proxies = set(proxies) if proxies else set()
        self.current_proxy = proxies[0]
        if not keys:
            self.keys = ["http", "https"]
        else:
            self.keys = keys

    def cycle_proxies(self):
        if len(self.proxies) == 0:
            raise ValueError("No proxies supplied. Cannot cycle.")
        if len(self.proxies) == 1:
            self.current_proxy = self.proxies.pop()
            self.proxies.add(self.current_proxy)

        if self.proxy_cycle == self.proxies:
            self.proxy_cycle = set()
            self.current_proxy = None
            for proxy in self.proxies:
                if proxy != self.current_proxy:
                    self.current_proxy = proxy
        else:
            for proxy in self.proxies:
                if proxy not in self.proxy_cycle:
                    self.current_proxy = proxy

        return self.create_proxy_dict()

    def add_proxy(self, proxy: str):
        self.proxies.add(proxy)

    def create_proxy_dict(self):
        return {key: self.current_proxy for key in self.keys}
