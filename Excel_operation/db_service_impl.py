
CREATE_TABLE = '''
    create table prodinfo(
		prod_id int,
		prod_name varchar(30),
		prod_qty  int,
		prod_price float,
		prod_cat varchar(30),
		primary key(prod_id)
	)
'''
INSERT_PRODUCT = "insert into prodinfo values({},'{}',{},{},'{}')"
DELETE_PRODUCT = "delete from prodinfo where prod_id={}"
UPDATE_PRODUCT = "update prodinfo set prod_name = '{}', prod_qty = {}, prod_price={},prod_cat='{}' where prod_id={}"
FETCH_ALL_PRODUCT = 'select * from prodinfo'
FETCH_SINGLE_PRODUCT = 'select * from prodinfo where prod_id={}'
FETCH_ALL_PRODUCT_CAT = "select * from prodinfo where prod_cat = '{}' "
MAX_PRICE_QUERY = "select max(prod_price) from prodinfo"

from Excel_operation.services import PersistServices
from Excel_operation.productinfo import Product
import pymysql

def getconnection(): # to connect with database
    return pymysql.connect(host='localhost', user='root', password='root',database='proddb', port=3306)


def execute_crud_queries(sql):
    try:
        conn = getconnection()  # connection with db --
        cursor = conn.cursor()  # communication channel--
        cursor.execute(sql)
        conn.commit()
    except :
        pass
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

class MySqlDbServiceImpl(PersistServices):
    
    def add_product(self, prod):
        if type(prod) == Product:
            if type(prod.prodId) == int and prod.prodId > 0:
                if self.get_product(prod.prodId):  # product or None
                    print('Given Product Already Exist into Excel sheet --Duplicate Product')
                else:
                    execute_crud_queries(INSERT_PRODUCT.format(prod.prodId,prod.prodName,prod.prodQty,prod.prodPrice,prod.prodCategory))
                    #write_data_into_excel(excelProductList)  # sync up -- memory data with--excelsheet..
                    print('Product Added Successfully....!')
            else:
                print('Invalid Product Id...Cannot add product into inventory')
        else:
            print('Invalid Product Type.!')

    def get_product(self, prId):  # product or None
        conn = getconnection()
        cursor = conn.cursor()
        cursor.execute(FETCH_SINGLE_PRODUCT.format(prId))
        prod = cursor.fetchone()
        print('Product Info -->',prod)
        return prod


    def get_all_products(self):  # read from excelsheet-->
        conn = getconnection()
        cursor = conn.cursor()
        cursor.execute(FETCH_ALL_PRODUCT)  # all -->
        print(cursor.fetchall())    # result --> entire result will be given
        print(cursor.fetchone())    # one by one- -> single
        print(cursor.fetchmany(5))  # only first 5-->

    def update_product(self, prId, prod):
        dbprod = self.get_product(prId)
        if dbprod:
            execute_crud_queries(UPDATE_PRODUCT.format(prod.prodName,prod.prodQty,prod.prodPrice,prod.prodCategory,prod.prodId))
            print('Product Record Updated..!')
        else:
            print('No product with given id -- so cannot update..!')


    def remove_product(self, prId):
        dbprod = self.get_product(prId)
        if dbprod:
            execute_crud_queries(DELETE_PRODUCT.format(prId))
            print('Product Record Updated..!')
        else:
            print('No product with given id -- so cannot update..!')


    def get_products_by_category(self, cate):
        conn = getconnection()
        cursor = conn.cursor()
        cursor.execute(FETCH_ALL_PRODUCT_CAT.format(cate))
        print(cursor.fetchall())


    def get_max_product_price(self):
        conn = getconnection()
        cursor = conn.cursor()
        cursor.execute(MAX_PRICE_QUERY)
        print(cursor.fetchone())

    def create_table(self):
        execute_crud_queries(CREATE_TABLE)

if __name__ == '__main__':
    dbservice = MySqlDbServiceImpl()
    #dbservice.create_table()
    prod4 = Product(pid=101, pnm='Mobile', prc=2932.3, pqty=3, pcat='D')
    #dbservice.add_product(prod4)
    #dbservice.get_product(101)
    #dbservice.update_product(101,prod4)
    #dbservice.get_products_by_category('A')
    dbservice.get_max_product_price()