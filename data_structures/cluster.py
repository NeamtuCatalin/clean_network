class Cluster:
    def __init__(self, name, network_list, security_level):
        """
        Constructor for Cluster data structure.

        self.name -> str
        self.security_level -> int
        self.networks -> list(NetworkCollection)
        """

        self.name = str(name)
        self.networks = network_list
        self.security_level = int(security_level)


