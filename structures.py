import logging
from abc import ABC, abstractmethod
from pullgerInternalControl import pIC_pAM


class authorizationStrucruABC(ABC):
    __slots__ = ('_authorizationsServers', '_authorizationType')

    @abstractmethod
    def getDomain(self):
        pass


class AuthorizationsServers:
    __slots__ = ()

    @staticmethod
    def getByName(inAuthorisationServer:str):
        if inAuthorisationServer.upper() == "LINKEDIN":
            return AuthorizationsServers.linkedin()
        else:
            raise pIC_pAM.structures.IncorrectInputData(
                f'Unknown authorization server: {inAuthorisationServer}',
                level=40
            )

    class linkedin():
        __slots__ = ()

        def __str__(self):
            return 'linkedin'

        def getByName(self, authorizationType):
            if authorizationType.upper() == "GENERAL":
                return self.general
            elif authorizationType.upper() == "SALES":
                return self.sales
            else:
                raise pIC_pAM.structures.IncorrectInputData(
                    f'Unknown authorization type: {authorizationType}',
                    level=40
                )
            pass

        @classmethod
        def getDefault(cls):
            return cls.general()

        class general(authorizationStrucruABC):
            @property
            def fullName(self):
                return self._authorizationsServers + ('' if self._authorizationType == '' else '_' + self._authorizationType)

            def __init__(self):
                self._authorizationsServers = 'linkedin'
                self._authorizationType = ''

            def __str__(self):
                return self._authorizationType

            def getDomain(self):
                from pullgerDomain.com.linkedin.port import port
                return port.Domain

        class sales(general):
            def __init__(self):
                super().__init__()
                self._authorizationType = 'sales'