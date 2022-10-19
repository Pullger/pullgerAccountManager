from abc import ABC, abstractmethod

class AuthorizationStrucruABC(ABC):
    __slots__ =('_authorizationsServers', '_authorizationType')
    @abstractmethod
    def getDomain(self):
        pass

    def __str__(self):
        return f'{self._authorizationsServers}.{self._authorizationType}'