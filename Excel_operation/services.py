from abc import ABC,abstractmethod

class PersistServices(ABC):

    @abstractmethod
    def add_product(self,prod):
        pass

    @abstractmethod
    def get_product(self,prId):
        pass

    @abstractmethod
    def get_all_products(self):
        pass

    @abstractmethod
    def update_product(self,prId,prod):
        pass

    @abstractmethod
    def remove_product(self,prId):
        pass

    @abstractmethod
    def get_products_by_category(self,cate):
        pass

    @abstractmethod
    def get_max_product_price(self):
        pass
