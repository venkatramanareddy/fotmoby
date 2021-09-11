import requests

baseUrl="https://www.fotmob.com"
baseUrl = baseUrl;
matchesUrl = baseUrl + "/matches?";
leaguesUrl = baseUrl + "/leagues?";
teamsUrl = baseUrl + "/teams?";
playerUrl = baseUrl + "/playerData?";
matchDetailsUrl = baseUrl + "/matchDetails?";
searchUrl = baseUrl + "/searchapi/";
cache = {}
suppress_cache=False
    
def getLeague(id="47", tab="overview", type="league", timeZone="America/New_York"):
    url = leaguesUrl + 'id=%s&tab=%s&type=%s&timeZone=%s'%(id,tab,type,timeZone)
    return pullResponse(url)

def getTeam(id="47", tab="overview", type="league", timeZone="America/New_York"):
    url = leaguesUrl + 'id=%s&tab=%s&type=%s&timeZone=%s'%(id,tab,type,timeZone)
    return pullResponse(url)

def pullResponse(url):
    print("pulling data from ", url)
    if suppress_cache or url not in cache:
        # Make actual API call
        r = requests.get(url)
        cache[url] = r
    return cache[url]  

