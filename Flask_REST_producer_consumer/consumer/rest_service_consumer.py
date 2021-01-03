import requests
from Flask_REST_producer_consumer.consumer.iteminfo import Item
PRODUCT_API_URI = 'http://localhost:5000/api/product/'

def deserialize_into_item(resp):
    return Item(itid=resp.get('product_id'),
                itnm=resp.get('product_name'),
                itqty=resp.get('product_quantity'),
                itpr=resp.get('product_price'),
                itpht=resp.get('product_photo'))

def serialize_item(item):
    return {
            "product_name" : item.itemName ,
            "product_price" : item.itemPrice,
            "product_qty" : item.itemQty,
            "product_photo": item.itemPhoto
        }

class ProductAPIConsumer:

    @staticmethod
    def get_product(pid):
        response = requests.get(PRODUCT_API_URI+str(pid))
        #print(response.json())
        resp = response.json()
        if response.status_code==200 and resp.get('SUCCESS'):
            return deserialize_into_item(resp.get("SUCCESS"))   # PRoduct
        else:
            return resp.get("ERROR")  #str

    @staticmethod
    def get_all_products():
        response = requests.get(PRODUCT_API_URI)
        # print(response.json())
        resp = response.json()
        if response.status_code == 200 and resp.get('SUCCESS'):
             items = resp.get("SUCCESS")
             item_list = []
             for item in items:
                 item_list.append(deserialize_into_item(item))
             return item_list
        else:
            return resp.get("ERROR")

    @staticmethod
    def add_product(item):
        body = serialize_item(item)
        response = requests.post(PRODUCT_API_URI,json=body)
        print(response.json(),response.status_code)
        resp = response.json()
        if response.status_code == 200 and resp.get('SUCCESS'):
           return resp.get("SUCCESS")
        else:
            return resp.get("ERROR")


    @staticmethod
    def delete_product(pid):
        response = requests.delete(PRODUCT_API_URI+str(pid))        #http://localhost:5000/api/product/3
        print(response)
        resp = response.json()
        if response.status_code == 200 and resp.get('SUCCESS'):
            return resp.get("SUCCESS")
        else:
            return resp.get("ERROR")

    @staticmethod
    def update_product(pid,item):
        response= requests.put(PRODUCT_API_URI+str(pid),json=serialize_item(item))
        resp = response.json()
        if response.status_code == 200 and resp.get('SUCCESS'):
            return resp.get("SUCCESS")
        else:
            return resp.get("ERROR")


    @staticmethod
    def add_product_with_photo():       #request.post(uri,files=file,data=)
        pass

if __name__ == '__main__':
    item = Item(itid=222,itnm='xxxxxx',itqty=43,itpr=4394.53)
    ans = ProductAPIConsumer.update_product(8,item)
    print(ans)



class VendorAPIConsumer:  # u are going to write this..
    @staticmethod
    def get_vendor(vid):
        pass

    @staticmethod
    def get_all_vendors():
        pass

    @staticmethod
    def add_vendor(item):
        pass

    @staticmethod
    def delete_vendor(vid):
        pass

    @staticmethod
    def update_vendor(vid, item):
        pass

