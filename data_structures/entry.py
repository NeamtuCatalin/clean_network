import ipaddress
from datetime import datetime
class Entry:
    def __init__(self, address, available, last_used):
        """
        Constructor for Entry data structure.

        self.address -> str
        self.available -> bool
        self.last_used -> datetime
        """


        self.address = ipaddress.IPv4Address(address)
        self.available = bool(available)
        #problema la datetime cu prelucratul formatului
        self.las_used = last_used




