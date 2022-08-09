import re

class Datacenter:
    def __init__(self, name, cluster_list):
        """
        Constructor for Datacenter data structure.
        self.name -> str
        self.clusters -> list(Cluster)
        """
        #Berlin, Paris
        self.name = str(name)
        self.clusters = list(cluster_list)

    def remove_invalid_clusters(self):
        """
        Removes invalid objects from the clusters list.
        """
        first_letters = (self.name[:3]).upper()
        checked_clusters = []
        #always check de keys from json, the one with the datacenter names
        for i in self.clusters:
            #['BER-1', 'BER-203', 'BER-4000', 'TEST-1']
            result = re.search('(.*?)-(\d+)', i)
            if (result.group(1) == first_letters) and (len(result.group(2))<=3):
                checked_clusters.append(i)
        return checked_clusters






