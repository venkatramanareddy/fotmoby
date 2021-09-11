import requests

class FotMob:
    def __init__(self, suppress_cache=False):
        self.baseUrl="https://www.fotmob.com"
        baseUrl = self.baseUrl;
        self.matchesUrl = baseUrl + "/matches?";
        self.leaguesUrl = baseUrl + "/leagues?";
        self.teamsUrl = baseUrl + "/teams?";
        self.playerUrl = baseUrl + "/playerData?";
        self.matchDetailsUrl = baseUrl + "/matchDetails?";
        self.searchUrl = baseUrl + "/searchapi/";
        self.cache = {}
        self.suppress_cache=suppress_cache
    
    def getLeague(self, id="47", tab="overview", type="league", timeZone="America/New_York"):
        url = self.leaguesUrl + 'id=%s&tab=%s&type=%s&timeZone=%s'%(id,tab,type,timeZone)
        return self.pullResponse(url)
    
    def getTeam(self, id="47", tab="overview", type="league", timeZone="America/New_York"):
        url = self.leaguesUrl + 'id=%s&tab=%s&type=%s&timeZone=%s'%(id,tab,type,timeZone)
        return self.pullResponse(url)

    def pullResponse(self, url):
        print("pulling data from ", url)
        if self.suppress_cache or url not in self.cache:
            # Make actual API call
            r = requests.get(url)
            self.cache[url] = r
        return self.cache[url]  

