from data_structures.network_collection import NetworkCollection
import unittest

class TestRemoveInvalidRecords(unittest.TestCase):
    def test_remove(self):

        networks = ["192.168.10.0/24", "192.168.20.0/24", "192.168.30.0/24", "172.16.0.0/16", "10.0.0.0/8",
                    "192.168.203.0/24"]
        test_entry_list = [
          {
            "address": "192.168.203.20",
            "available": True,
            "last_used": "30/01/20 17:00:00"
          },
            {
                "address": "0.0.0.0",
                "available": True,
                "last_used": "30/01/20 17:00:00"
            },
            {
                "address": "apa_calda",
                "available": True,
                "last_used": "30/01/20 17:00:00"
            },
          {
            "address": "192.168.203.21",
            "available": False,
            "last_used": "30/01/20 17:00:00"
          },
          {
            "address": "192.168.203.19",
            "available": False,
            "last_used": "30/01/20 17:00:00"
          },
          {
            "address": "192.168.0.0",
            "available": True,
            "last_used": "30/01/20 17:00:00"
          }
        ]
        valid_output = [{
            "address": "192.168.203.20",
            "available": True,
            "last_used": "30/01/20 17:00:00"
          },
            {
                "address": "192.168.203.21",
                "available": False,
                "last_used": "30/01/20 17:00:00"
            },
            {
                "address": "192.168.203.19",
                "available": False,
                "last_used": "30/01/20 17:00:00"
            }

        ]
        actual_output = []
        for nw in networks:
            self.nw_obj = NetworkCollection(nw, test_entry_list)
            actual_output.append(self.nw_obj.remove_invalid_records())
        #obtain a flat list from a list of lists
        flat_list = [item for sublist in actual_output for item in sublist]
        self.assertEqual(flat_list, valid_output)
