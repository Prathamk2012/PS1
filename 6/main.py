import webapp2
class MainPage(webapp2.RequestHandler):
	def get(self):
		n=8
		fib_num = [0,1]
		for i in range(2,n):
			next = fib_num[-1] + fib_num[-2]
			fib_num.append(next)
			
		self.response.write('<br>'.join(str (num) for num in fib_num))
app = webapp2.WSGIApplication([('/',MainPage)],debug = True)
