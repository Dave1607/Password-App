from flask import Flask
from flask import jsonify,request
from password_protocols import generate_password,valid_password
from cryptography import hash_password,check_password

app = Flask(__name__)

#the api call create a new strong password 
@app.route("/")
def get_password():
    new_password = generate_password()
    return jsonify({'password':new_password})

#api call to encrypt password using  sha256 algorithm
@app.route("/encrypt/", methods=['POST'])
def encrypt_password():
    data = request.get_json()
    if 'password' in data:
        password = data['password']
        encrypted_password = hash_password(password)
        return jsonify({'encrypted_password': encrypted_password})
    else:
        return jsonify({'error': 'Password not provided'}), 400

#this api call checks  the strength of a given password
@app.route("/validate",methods=['POST'])
def check_valid_password():
    data = request.get_json()
    if "password" in data:
        password = data["password"]
        valid_check = valid_password(password)
        return jsonify({'valid':valid_check})
    else:
        return jsonify({"Error":"No Password Provided"}), 400
    
#api call to check if the entered password is valid or not
#the stored password should be the stored hashed password
#always store the hashed password to your database
@app.route("/match/",methods = ["POST"])
def  check_match_password():
    data = request.get_json()
    if  "stored_password" and "provided_password" in data:
        stored_password = data["stored_password"]
        provided_password = data["provided_password"]
        match_check = check_password(stored_password,provided_password)
        return jsonify({
            "match_check": match_check
            })
    else:
        return jsonify({
            "Error":"Both Stored Password and Provided Password must be given"
        }), 400

if  __name__ == "__main__":
    app.run(debug = False)