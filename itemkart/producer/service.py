from abc import ABC , abstractmethod


class ApplicationServices(ABC) :

    @abstractmethod
    def add_entity(self , item) :
        pass

    @abstractmethod
    def remove_entity(self , itemid) :
        pass

    @abstractmethod
    def update_entity(self , item , itemid) :
        pass

    @abstractmethod
    def fetch_entity(self , item) :
        pass

    @abstractmethod
    def fetch_all_entities(self) :
        pass

    @abstractmethod
    def get_entity_as_per_cat(self , cat) :
        pass
