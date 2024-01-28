from flask import Flask, render_template
app = Flask(__name__)

# Home page with a cat image
@app.route('/')
def home():
    return render_template('pycamp.html')

@app.route('/hello')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    # IP Address and Port
    ip_address = '127.0.0.1'
    port = 5000
    app.run(host=ip_address, port=port, debug=True)