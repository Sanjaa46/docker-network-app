from flask import Flask
import os

app = Flask(__name__)
file_path = '/data/messages.txt'

@app.route('/')
def write_message():
	with open(file_path, 'a') as f:
		f.write('Hello from conatinaer!\n')
	return 'message written!\n'

@app.route('/read')
def read_messages():
	if os.path.exists(file_path):
		with open(file_path) as f:
			return f.read()
	else:
		return 'No messages yet.'

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
