from flask import Flask, request, make_response, render_template
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
	if request.method != 'GET':
		return ('method not supported', 405)
	return render_template('index.html')

@app.route('/api/save/files', methods=['POST'])
def save_files():
	if request.method != 'POST':
		return ('method not supported', 405)
	json_request = request.get_json()
	print(json_request)
	print(request.files)
	return ('success', 200)
	# f = request.files['the_file']
 #  f.save('/var/www/uploads/uploaded_file.txt')
