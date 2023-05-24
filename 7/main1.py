import webapp2
import urllib
import json
from google.appengine.ext.webapp import template

class MainPage(webapp2.RequestHandler):
	def get(self):
		temp = {}
		path = "/home/prathamesh/CCL/7/templates/index.html"
		self.response.write(template.render(path,temp))
	
	def post(self):
		pincode = self.request.get('pincode')
		url = "https://api.postalpincode.in/pincode/" + pincode
		data = urllib.urlopen(url).read()
		data = json.loads(data)
		status = data[0]["Status"]
		
		if status == "Success":
			name = data[0]["PostOffice"][0]["Name"]
			region = data[0]["PostOffice"][0]["Region"]
			temp = {"name": name, "region": region}
			path = "/home/prathamesh/CCL/7/templates/result.html"
			
		if status == "Error":
			temp = {"data":data}
			path = "/home/prathamesh/CCL/7/templates/error.html"
		
		self.response.write(template.render(path,temp))
			
app = webapp2.WSGIApplication([('/', MainPage)],debug = True)			
