import logging
from abc import ABC, abstractmethod
from pullgerAccountManager import exceptions

class authorizationStrucruABC(ABC):
    @abstractmethod
    def getDomain(self):
        pass

class authorizationsServers():
    __slots__ = ()

    @staticmethod
    def getByNames(rootServerName):
        if rootServerName.upper() == "LINKEDIN":
            return authorizationsServers.linkedin()
        else:
            raise exceptions.structures(
                f'Unknown authorization server: {rootServerName}',
                level=40
            )

    class linkedin():
        __slots__ = ()

        def __new__(cls):
            return cls.general()


        class general(authorizationStrucruABC):
            __slots__ = ('_rootName', '_currentName')

            @property
            def fullName(self):
                return self._rootName + ('' if self._currentName == '' else '_' + self._currentName)

            def __init__(self):
                self._rootName = 'linkedin'
                self._currentName = ''

            def __str__(self):
                return self.fullName

            def getDomain(self):
                from pyPullgerDomain.com.linkedin.port import port
                return port.Domain

        class sales(general):
            __slots__ = ()

            def __init__(self):
                super().__init__()
                self._currentName = 'sales'
                pass


