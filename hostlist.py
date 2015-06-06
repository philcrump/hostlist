import csv
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    with open('/var/lib/misc/dnsmasq.leases', 'rb') as leasesFile:
        leasesReader = csv.reader(leasesFile, delimiter=' ')
	return render_template('default.html', leases=leasesReader)

if __name__ == "__main__":
    #app.debug = True
    app.run('0.0.0.0',80)
