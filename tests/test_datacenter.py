from data_structures.datacenter import Datacenter
import unittest

class TestRemoveInvalidClusters(unittest.TestCase):
    def test_remove(self):

        test_locations = ["Ploiesti", "Pitesti", "Bucuresti", "Ferentari", "Berceni", True, "Becali"]
        test_cluster_list = ["PLO-300", "PiT-200", "BUC-4562", "FERE-1", "BERC-2"]
        valid_output = ["PLO-300"]
        actual_output = []
        for location in test_locations:
            self.datacenter_obj = Datacenter(location, test_cluster_list)
            actual_output.append(self.datacenter_obj.remove_invalid_clusters())
        #obtain a flat list from a list of lists
        flat_list = [item for sublist in actual_output for item in sublist]
        self.assertEqual(flat_list, valid_output)
