from abc import abstractmethod, ABC


class ApplicationServices(ABC):
    @abstractmethod
    def add_entity(self):
        pass

    @abstractmethod
    def remove_entity(self):
        pass

    @abstractmethod
    def update_entity(self):
        pass

    @abstractmethod
    def fetch_entity(self):
        pass

    @abstractmethod
    def fetch_all_entities(self):
        pass

