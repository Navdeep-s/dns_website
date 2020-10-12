
import dns.message,dns.query,dns.flags


def my_dns_query(hostname, query_type, recrusion_desire,server):
		query = dns.message.make_query(hostname,query_type)

		if(not recrusion_desire):
			query.flags ^=dns.flags.RD

		query_response = dns.query.udp(query,server)
		print(query_response)

		# for k in query_response.answer:
		# 	print("........")
		# 	for u in k.items:
		# 		print(u)
		# 	print("........")


		return query_response.to_text()

# my_dns_query("iitjammu.ac.in","CNAME",True,"192.168.43.1")

# Importing flask module in the project is mandatory 
# An object of Flask class is our WSGI application. 
from flask import Flask ,request,render_template

# Flask constructor takes the name of 
# current module (__name__) as argument. 
app = Flask(__name__,template_folder="template") 

# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function. 
@app.route('/') 
# ‘/’ URL is bound with hello_world() function. 
def hello_world(): 
	return 'Hello World'


@app.route("/search")
def search():
	hostname = request.args.get('hostname')
	query_type=request.args.get('query_type')
	recrusion_desire=request.args.get('rd')
	if(recrusion_desire=="1"):
		rd = True
	else:
		rd = False

	server = request.args.get("server")
	return render_template("home.html",answer=my_dns_query(hostname,query_type,rd,server))
	# return "%s!" % my_dns_query(hostname,query_type,rd,server)
# main driver function 
if __name__ == '__main__': 

	# run() method of Flask class runs the application 
	# on the local development server. 
	app.run() 
