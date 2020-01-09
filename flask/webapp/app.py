# https://projects.raspberrypi.org/en/projects/python-web-server-with-flask/4
#from flask import Flask
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/docs')
def docs():
    return 'docs'

'''@app.route('/')
def index():
    return 'Hello world'*/
'''
    
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    #app.run(debug=True, host='0.0.0.0')
    app.run(host='0.0.0.0', port=80)
