import requests
import json

class Cricapi(object): 
    def __init__(self,apikey):
        self._apikey = apikey
        self._url = "https://cricapi.com/api"

    def matches(self):
        """ returns matches data"""
        URL = self._get_url("matches",{})
        r = requests.get(url = URL)
        data =  r.json()
        return data

    def cricket(self):
        """ returns cricket data"""
        URL = self._get_url("cricket",{})
        r = requests.get(url = URL)
        data =  r.json()
        return data

    def matchCalendar(self):
        """ returns matchCalendar data"""
        URL = self._get_url("matchCalendar",{})
        r = requests.get(url = URL)
        data =  r.json()
        return data

    def cricketScore(self,params):
        """ returns cricketScore data"""
        URL = self._get_url("cricketScore",params)
        r = requests.get(url = URL)
        data =  r.json()
        return data

    def playerStats(self,params):
        """ returns playerStats data"""
        URL = self._get_url("playerStats",params)
        r = requests.get(url = URL)
        data =  r.json()
        return data

    def fantasySummary(self,params):
        """ returns fantasySummary data"""
        URL = self._get_url("fantasySummary",params)
        r = requests.get(url = URL)
        data =  r.json()
        return data

    def fantasySquad(self,params):
        """ returns fantasySquad data"""
        URL = self._get_url("fantasySquad",params)
        r = requests.get(url = URL)
        data =  r.json()
        return data

    def playerFinder(self,params):
        """ returns playerFinder data"""
        URL = self._get_url("playerFinder",params)
        r = requests.get(url = URL)
        data =  r.json()
        return data

    def _get_url(self,type, params):
        if type == "matches":    
            return "{0}/matches?apikey={1}".format(self._url,self._apikey)
        elif type == "cricket":
            return "{0}/cricket?apikey={1}".format(self._url,self._apikey)
        elif type == "matchCalendar":
            return "{0}/matchCalendar?apikey={1}".format(self._url,self._apikey)
        elif type == "cricketScore":
            return "{0}/cricketScore?apikey={1}&unique_id={2}".format(self._url,self._apikey,params["unique_id"])    
        elif type == "playerStats":
            return "{0}/playerStats?apikey={1}&pid={2}".format(self._url,self._apikey,params["pid"])
        elif type == "fantasySummary":
            return "{0}/fantasySummary?apikey={1}&unique_id={2}".format(self._url,self._apikey,params["unique_id"])                                    
        elif type == "fantasySquad":
            return "{0}/fantasySquad?apikey={1}&unique_id={2}".format(self._url,self._apikey,params["unique_id"])
        elif type == "playerFinder":
            return "{0}/playerFinder?apikey={1}&name={2}".format(self._url,self._apikey,params["name"]) 
