from flask import Flask, render_template, request, send_file
import requests,json,pprint
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    name = None
    return render_template('index.html', name=name)

@app.route('/upc', methods=['POST'])
def upc_retrieve():
	if 'productId' in request.form:
		productId = request.form['productId']
	res = requests.get("https://svcs.ebay.com/services/search/FindingService/v1?OPERATION-NAME=findItemsByProduct&SERVICE-VERSION=1.0.0&SECURITY-APPNAME=ThejassK-ProRetri-PRD-47141958a-32e1cf44&RESPONSE-DATA-FORMAT=JSON&REST-PAYLOAD&productId.@type=UPC&productId="+productId)
	json_pretty = pprint.pformat(json.loads(res.text))
	json_pretty = json_pretty.replace("u'","'")
	file = open("templates/output.json","w")
	file.write(json_pretty)
	return send_file('templates/output.json',attachment_filename='output.json')  # render_template('output.json')

if __name__ == '__main__':
    app.run(debug=True)

