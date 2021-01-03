from flask import Flask,request

app = Flask(__name__)

import base64
import json
from flask import jsonify
@app.route('/producer/')  #http://localhost:5000/producer/      get
def get_data():
    with open('D:\\python_work\\flask_projects\\flask_service_impl\\rest\\yogesh_server.png','rb') as binary_file:
        binary_file_data = binary_file.read()  # binary
        base64_encoded_data = base64.b64encode(binary_file_data) #encode-->
        base64_message = base64_encoded_data.decode('utf-8')
        print('ENDATA :',base64_message)
        return jsonify({"data":base64_message})
    '''
    with open('D:\\python_work\\flask_projects\\flask_service_impl\\rest\\aa.png','rb') as image:
        encodingimage = base64.b64encode(image.read())
        return jsonify(encodingimage)
    '''


@app.route("/producer/",methods = ['POST']) #http://localhost:5000/producer/ -post
def persist_data():
   # x = request.get_json()  # NO
   # y = request.files['file1']  #yES
   # z = request.content
    #a = request.values
    #b = request.form  #
    #print(x)
    #print(y)
   # print(z)
    #print(a)
    #print(b)
    file = request.files['file1']#FILE GET
    file.save("yogy_server.png")
    data = request.form
    print(data)
    return {"success" : "Invoked.."}



if __name__ == '__main__':
    app.run(debug=True,port=5001)