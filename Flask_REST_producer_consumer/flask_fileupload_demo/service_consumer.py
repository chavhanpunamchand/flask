import requests

FILE_PATH = 'D:\\python_work\\flask_projects\\flask_service_impl\\flask_fileupload_demo\\'
def post_data():
    file = {"file1" : open('yogy.png','rb')}
    response = requests.post('http://localhost:5001/producer/',
                             files=file,
                             data={"name":"yogy"})
    print(response.json())

import base64

def get_data():
    response = requests.get('http://localhost:5001/producer/')
    encodeddata = response.json().get("data")
    decode_image(encodeddata)


def decode_image(base64_img):           #consumer la
    base64_img_bytes = base64_img.encode('utf-8')
    with open('yogesh_consumer.png', 'wb') as file_to_save:
        decoded_image_data = base64.decodebytes(base64_img_bytes)
        file_to_save.write(decoded_image_data)

if __name__ == '__main__':
    #post_data()
    get_data()