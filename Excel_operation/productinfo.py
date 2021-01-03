

class Product:

    def __init__(self,pid,pnm,prc,pqty,pcat):
        self.prodId = pid
        self.prodName  = pnm
        self.prodPrice = prc
        self.prodQty = pqty
        self.prodCategory = pcat

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f'''
            Product Id : {self.prodId},
            Product Name : {self.prodName},
            Product Qty : {self.prodQty},
            Product Price : {self.prodPrice},
            Product Category : {self.prodCategory}
        '''

    def __eq__(self, other):
        return self.prodId == other.prodId

    




