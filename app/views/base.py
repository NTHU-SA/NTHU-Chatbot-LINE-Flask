from app import app

@app.route('/', methods=['GET'])
def home():
    return "Hi there, this is NTHU LINE Flask"

@app.route('/ping', methods=['GET'])
def ping():
    return "Hi there, this is NTHU LINE Flask"