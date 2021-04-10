from flask import Flask, request, make_response, render_template

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
	files = [file[1] for file in request.files.lists()]
	for file in files[0]:
		file.save(f'./uploads/{file.filename}')
	return ('success', 200)
