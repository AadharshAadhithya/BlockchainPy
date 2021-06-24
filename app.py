from Blockchain import Blockchain
from flask import Flask,jsonify,request,url_for,redirect,Response
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

blockchain = Blockchain(1)
@app.route('/')
def init():

	return redirect(url_for('chain'))

@app.route('/chain')
def chain():
	resp = blockchain.jsonifyBlockchain()
	print(resp[0])

	return jsonify(chain=blockchain.jsonifyBlockchain())


@app.route('/mine',methods=['POST'])
def mineblock():
	if request.method=='POST':
		data = request.get_json()
		data = data['data']
		blockchain.addBlock(data)
    
	return redirect(url_for('chain'))




if __name__=='__main__':
	app.run()