from flask import Flask, request, render_template
from flask_googlemaps import GoogleMaps
app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")

#@app.route("/post", methods=['GET', 'POST'])
#def post():
#        return "Method used: %s" % request.method
        
	
if __name__ == '__main__':

# you can also pass the key here if you prefer
	GoogleMaps(app, key="AIzaSyCuzw014n-d0tt-VOQeyJ7mId-GDXerV8g")
	app.run(debug=True)
