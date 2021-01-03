

class Item:

    def __init__(self,itid,itnm,itqty,itpr,itpht='NA'):
        self.itemId = itid
        self.itemName = itnm
        self.itemQty = itqty
        self.itemPrice= itpr
        self.itemPhoto = itpht

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f'''
            Item Id : {self.itemId}  Item Name : {self.itemName}     
            Item Qty : {self.itemQty}  Item Price : {self.itemPrice}     
        '''

    @staticmethod
    def get_dummy():
        return Item(0,'',0,0.0,'')
