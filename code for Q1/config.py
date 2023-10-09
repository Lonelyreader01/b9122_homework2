class Config:
    def __init__(self, config_data):
        self.config_data = config_data

    def __getattr__(self, name):
        if name in self.config_data:
            value = self.config_data[name]
            if isinstance(value, dict):
                return Config(value)
            return value
        else:
            raise AttributeError(f"'Config' object has no attribute '{name}'")
        
    # def __getitem__(self, key):
    #     if key in self.config_data:
    #         value = self.config_data[key]
    #         if isinstance(value, dict):
    #             return Config(value)
    #         return value
    #     else:
    #         raise KeyError(f"'Config' object has no key '{key}'")



config_data = {
    'United_Nations': {
        'seed_url': ["https://press.un.org/en"],
        'init_url': "https://press.un.org",
        'relative_anchor_tag': '<a href="/en/press-release" hreflang="en">Press Release</a>',
        'MAX_LENGTH': 13,
        'path': '1'
    },
    'European_Parliament': {
        'seed_url': [f'https://www.europarl.europa.eu/news/en/press-room/page/{i}' for i in range(100)],
        'init_url': "https://www.europarl.europa.eu",
        'relative_anchor_tag': '<span class="ep_name">Plenary session</span>',
        'MAX_LENGTH': 13,
        'path': '2'
    }
}

configs = Config(config_data)
