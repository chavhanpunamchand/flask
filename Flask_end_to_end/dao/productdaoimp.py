from Flask_end_to_end.configurations.db_config import get_connection
from Flask_end_to_end.configurations.orm_config import db
from Flask_end_to_end.models.productinfo import *
from functools import reduce


class ProductDAOORMImpl:
    def add_product(self,prod):
        # conn=get_connection()
        # channel=conn.cursor()
        # channel.execute('')
        if type(self.get_product(prod.pid))==Product:
            return self.update_product(prod)
        else:
            try:
                db.session.add(prod)
                db.session.commit()
                return "Product record added sucesfully"
            except:
                return "Problem in product add"


    def get_product(self,prid):
        try:
            prod=Product.query.filter_by(pid=prid).first()
            if prod:
                return prod
        except:
            return "problem in fetch product"
        return "No product available for given ID"


    def get_all_product(self):
        prodlist=Product.query.all()
        prodlist.reverse()
        return prodlist


    def delete_product(self,prid):
        prod=self.get_product(prid)
        if type(prod)==Product:
            db.session.delete(prod)
            db.session.commit()
            return "Product removed"
        else:
            return prod +", cannot update"

    def update_product(self,user_given_prod):
        prid=user_given_prod.pid
        prod=self.get_product(prid)
        if type(prod)==Product:
            prod.name=user_given_prod.name
            prod.qty=user_given_prod.qty
            prod.price=user_given_prod.price
            prod.cat=user_given_prod.cat
            prod.vendor=user_given_prod.vendor
            db.session.commit()
            return "product updated successfully"
        else:
            return prod +", cannot update"

    def total_inventory_invesment(self):
        prods=self.get_all_product()
        if prods:
             finalans=reduce(lambda p1,p2:p1.price+p2.price if type(p1)==Product else p1+p2.price )
             return finalans


# import sys
# if __name__ == '__main__':
    # p1=ProductDAOORMImpl()
    # p1.update_product(101,Product(name = 'TTT', qty = 50, price = 765, cat = 'Cloth'))
    # print(get_all_product())
    # print(get_product(1022))
    # sys.exit(0)
    # for item in range(1,10):
    #     pr2 =Product(pid=106+item,name = 'yyyy', qty = 20, price = 800, cat = 'Sport', vendor = 'Reebok')
    #     add_product(pr2)