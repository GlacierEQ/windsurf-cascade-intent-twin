import unittest
from src.impact_assurance import ImpactVector,assess
class ImpactAssuranceTests(unittest.TestCase):
 def test_contained_change_scores_higher(self):
  low=assess(ImpactVector(8,8,2,8,8,8,8)); high=assess(ImpactVector(8,8,10,8,8,8,8)); self.assertGreater(low["score"],high["score"])
 def test_invalid_refuses(self):
  with self.assertRaises(ValueError): ImpactVector(11,1,1,1,1,1,1)
