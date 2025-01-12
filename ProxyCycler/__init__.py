class ProxyCycler:
    def __init__(self, proxies: List[Optional] = None):
        self.proxies = set(proxies) if proxies else set()
        self.current_proxy = proxies[0]

    def cycle_proxies(self):
        if len(self.proxies) == 0:
            raise AttributeError("No proxies supplied. Cannot cycle.")
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

    def add_proxy(self, proxy: str):
        self.proxies.add(proxy)

    def create_proxy_dict(self, keys: Optional[List] = None):
        if keys is None:
            return {
                "http": self.current_proxy,
                "https": self.current_proxy,
            }
        else:
            return {key: self.current_proxy for key in keys}
