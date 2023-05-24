import webapp2
class MainPage(webapp2.RequestHandler) :
	def get(self):
		for i in range(10):
			self.response.out.write("Prathamesh 607 IT<br>")
app=webapp2.WSGIApplication([('/',MainPage)],debug=True)
