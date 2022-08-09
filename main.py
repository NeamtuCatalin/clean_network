from data_structures.datacenter import Datacenter
from data_structures.network_collection import NetworkCollection
from data_structures.cluster import Cluster
from data_structures.entry import Entry
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

URL = "http://www.mocky.io/v2/5e539b332e00007c002dacbe"


def get_data(url, max_retries=5, delay_between_retries=1):
    """
    Fetch the data from http://www.mocky.io/v2/5e539b332e00007c002dacbe
    and return it as a JSON object.
​
    Args:
        url (str): The url to be fetched.
        max_retries (int): Number of retries.
        delay_between_retries (int): Delay between retries in seconds.
    Returns:
        data (dict)
    """
    import requests
    from requests.adapters import HTTPAdapter
    from urllib3.util.retry import Retry

    session = requests.Session()
    retry = Retry(connect=max_retries, backoff_factor=delay_between_retries)
    # https://urllib3.readthedocs.io/en/stable/reference/urllib3.util.html
    adapter = HTTPAdapter(max_retries=retry)
    '''
    The built-in HTTP Adapter for urllib3.

    Provides a general-case interface for Requests sessions to contact HTTP and HTTPS urls by implementing 
    the Transport Adapter interface. This class will usually be created by the Session class under the covers.

    Parameters:
    * pool_connections – The number of urllib3 connection pools to cache. 
    * pool_maxsize – The maximum number of connections to save in the pool. 
    * max_retries(int) – The maximum number of retries each connection should attempt. 
    Note, this applies only to failed DNS lookups, socket connections and connection timeouts, 
    never to requests where data has made it to the server. 
    '''
    session.mount('http://', adapter)
    session.mount('https://', adapter)

    return session.get(url).json()


def main():
    """
    Main entry to our program.
    """
    data = get_data(URL)

    if not data:
        raise ValueError('No data to process')
    #e.g for key : Berlin, Paris
    #e.g for value : {'BER-1': {'security_level': 1'}...}
    datacenters = [
        Datacenter(key, value)
        for key, value in data.items()
    ]
    clean_DC(data, datacenters)

def clean_DC(data, datacenters):
    '''

    Args:
        param: datacenter list of objects
        data: data json untouched

    Returns: DC cleaned out

    '''

    # datacenter will be the obj for datacenter class
    for datacenter in datacenters:
        ok_clusters = datacenter.remove_invalid_clusters()
        for cluster_name in ok_clusters:
            cluster = Cluster(cluster_name,
                              data[datacenter.name][cluster_name]['networks'],
                              data[datacenter.name][cluster_name]['security_level'])
            for k,v in cluster.networks.items():
                network = NetworkCollection(k,v)
                ok_networks = network.remove_invalid_records()
                results = {datacenter.name: {cluster.name:{'security_level':cluster.security_level, 'networks':{k:ok_networks}}}}
                #It will print all the ok clusters for each network they have
                print(results)

if __name__ == '__main__':
    main()
