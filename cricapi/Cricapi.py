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

# https://cricapi.com/api/fantasySummary?apikey=yiPB2mqlqdNnPa57Vs8P8S74DXk1&unique_id=1034809
# https://cricapi.com/api/fantasySquad?apikey=yiPB2mqlqdNnPa57Vs8P8S74DXk1&unique_id=1034809
# https://cricapi.com/api/playerFinder?apikey=yiPB2mqlqdNnPa57Vs8P8S74DXk1&name=Tendulkar

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


# https://cricapi.com/api/matches?apikey=yiPB2mqlqdNnPa57Vs8P8S74DXk1
# https://cricapi.com/api/cricket?apikey=yiPB2mqlqdNnPa57Vs8P8S74DXk1
# https://cricapi.com/api/cricketScore?apikey=yiPB2mqlqdNnPa57Vs8P8S74DXk1&unique_id=1034809
# https://cricapi.com/api/matchCalendar?apikey=yiPB2mqlqdNnPa57Vs8P8S74DXk1
# https://cricapi.com/api/playerStats?apikey=yiPB2mqlqdNnPa57Vs8P8S74DXk1&pid=35320
# https://cricapi.com/api/fantasySummary?apikey=yiPB2mqlqdNnPa57Vs8P8S74DXk1&unique_id=1034809
# https://cricapi.com/api/fantasySquad?apikey=yiPB2mqlqdNnPa57Vs8P8S74DXk1&unique_id=1034809
# https://cricapi.com/api/playerFinder?apikey=yiPB2mqlqdNnPa57Vs8P8S74DXk1&name=Tendulkar

#             
# # importing the requests library 
# import requests 

# # api-endpoint 
# URL = "http://maps.googleapis.com/maps/api/geocode/json"

# # location given here 
# location = "delhi technological university"

# # defining a params dict for the parameters to be sent to the API 
# PARAMS = {'address':location} 

# # sending get request and saving the response as response object 
# r = requests.get(url = URL, params = PARAMS) 

# # extracting data in json format 
# data = r.json() 


# # extracting latitude, longitude and formatted address 
# # of the first matching location 
# latitude = data['results'][0]['geometry']['location']['lat'] 
# longitude = data['results'][0]['geometry']['location']['lng'] 
# formatted_address = data['results'][0]['formatted_address'] 

# # printing the output 
# print("Latitude:%s\nLongitude:%s\nFormatted Address:%s"
# 	%(latitude, longitude,formatted_address)) 

api = Cricapi("yiPB2mqlqdNnPa57Vs8P8S74DXk1")
# matches = api.matches()
# cricket = api.cricket()
# matchCalendar = api.matchCalendar()
params = {'unique_id':1034809, 'name':'sachin'}
# params = {'pid':35320}
cricketScore = api.playerFinder(params)
print(cricketScore)