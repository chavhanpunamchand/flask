import base64

#https://stackabuse.com/encoding-and-decoding-base64-strings-in-python/

#producer --> response madhe thevnyasathi
def encode_image(name):
    with open(name, 'rb') as binary_file:
        binary_file_data = binary_file.read() #binary data
        base64_encoded_data = base64.b64encode(binary_file_data)    # encode - binary--
        base64_message = base64_encoded_data.decode('utf-8') # using utf08 char set
        print(base64_message)
        return base64_message

#101010 --> (@*#$SJ
#consumer side la --> to create file encoded data-->
def decode_image(base64_img):
    base64_img_bytes = base64_img.encode('utf-8')   # conversion-->(@*#$SJ -->101010
    with open('newpencil.png', 'wb') as file_to_save:   # encode- -> write using binary format
        decoded_image_data = base64.decodebytes(base64_img_bytes)
        file_to_save.write(decoded_image_data)


if __name__ == '__main__':
    base64data = encode_image('pencil.png')
    decode_image(base64data)



