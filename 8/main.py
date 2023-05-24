import webapp2
import urllib
import json
from google.appengine.ext.webapp import template

class MainPage(webapp2.RequestHandler):
    def get(self):
        temp={}
        path="/home/prathamesh/CCL/8/templates/index.html"
        self.response.write(template.render(path,temp))
   
    def post(self):
        lat = self.request.get("lat")
        longi = self.request.get("long")
        url = 'https://api.open-meteo.com/v1/forecast?latitude={}&longitude={}&current_weather=true'.format(lat,longi)
        data = urllib.urlopen(url).read()
        data = json.loads(data)
        
        if "Error" in data:
            temp={"data":data['reason']}
            path="/home/prathamesh/CCL/8/templates/error.html"
        else:
            temperature1=data["current_weather"]["temperature"]
            windspeed1 = data["current_weather"]["windspeed"]
            temp = {"temperature1":temperature1,"windspeed":windspeed1}
            path="/home/prathamesh/CCL/8/templates/result.html"
        self.response.write(template.render(path,temp))
        
app = webapp2.WSGIApplication([('/',MainPage)], debug=True)
