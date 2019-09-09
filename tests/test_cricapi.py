import os
import unittest
from cricapi import Cricapi

# Import API keys from environment variables
api_key_name = "CRICAPI_API_KEY"
api_key = os.environ.get(api_key_name, None)
assert api_key is not None, "Must declare environment variable: {key_name}".format(
    key_name=api_key_name)
api = Cricapi(api_key)

class TestAPI(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n---------------------\nSetting up {} tests...\n".format("Cricapi"))
        cls.auth = api_key
        cls.api = api
        cls.match_id = "1152849"
        cls.player_id = 52812
        cls.player_name = "Viv Richards"

    def test_matches(self):
        """Test the matches endpoint"""
        msg = "Reponse to matches endpoint did not return a dict"
        response = self.api.matches()
        self.assertIsInstance(response, dict, msg)

    def test_cricket(self):
        """Test the cricket endpoint"""
        msg = "Reponse to cricket endpoint did not return a dict"
        response = self.api.cricket()
        self.assertIsInstance(response, dict, msg)

    def test_matchCalendar(self):
        """Test the matchCalendar endpoint"""
        msg = "Reponse to matchCalendar endpoint did not return a dict"
        response = self.api.matchCalendar()
        self.assertIsInstance(response, dict, msg)

    def test_cricketScore(self):
        """Test the cricketScore endpoint"""
        msg = "Reponse to cricketScore endpoint did not return a dict"
        params = {'unique_id' : self.match_id}
        response = self.api.cricketScore(params)
        self.assertIsInstance(response, dict, msg)

    def test_playerStats(self):
        """Test the playerStats endpoint"""
        msg = "Reponse to playerStats endpoint did not return a dict"
        params = {'pid' : self.player_id}
        response = self.api.playerStats(params)
        self.assertIsInstance(response, dict, msg)

    def test_fantasySummary(self):
        """Test the fantasySummary endpoint"""
        msg = "Reponse to fantasySummary endpoint did not return a dict"
        params = {'unique_id' : self.match_id}
        response = self.api.fantasySummary(params)
        self.assertIsInstance(response, dict, msg)

    def test_fantasySquad(self):
        """Test the fantasySquad endpoint"""
        msg = "Reponse to fantasySquad endpoint did not return a dict"
        params = {'unique_id' : self.match_id}
        response = self.api.fantasySquad(params)
        self.assertIsInstance(response, dict, msg)

    def test_playerFinder(self):
        """Test the playerFinder endpoint"""
        msg = "Reponse to playerFinder endpoint did not return a dict"
        params = {"name" : self.player_name}
        response = self.api.playerFinder(params)
        self.assertIsInstance(response, dict, msg)





