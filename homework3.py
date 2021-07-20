import requests
import json
class citylist(object):
    def __init__(self):
        url = "https://chxin.neocities.org/weather.json"
        r = requests.get(url)
        w = json.loads(r.content)
        self.w=w["weather"]
        self.i=w["weather"][0]
        self.n=0
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.n >=len(self.w):
            raise StopIteration()
        else :
            self.i=self.w[self.n]
            self.n =self.n+1;
        return self.i


obj=citylist()
for item in obj:
    print("城市:"+item["city"]+" 最低温度:"+str(item["mintmp"])+" 最高温度:"+str(item["maxtmp"])+" 天气:"+item["weather"])
