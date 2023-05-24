import webapp2
class MainPage(webapp2.RequestHandler):
	def get(self):
		for i in range(11):
			result = "5 x" + str (i) + "=" + str (5*i) + "<br>"
			self.response.write(result)
			
app = webapp2.WSGIApplication([('/', MainPage)], debug = True)
