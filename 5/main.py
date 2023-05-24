import webapp2

class MainPage(webapp2.RequestHandler):
	def get(self):
		for i in range(11):
			result = "10 x " + str (i) + "=" + str (10*i) + "<br>"
			self.response.write(result)
			
app = webapp2.WSGIApplication([('/', MainPage)], debug = True)
