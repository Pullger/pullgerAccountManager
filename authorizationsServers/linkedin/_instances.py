from ..glob import AuthorizationStrucruABC as _AuthorizationStrucruABC


class General(_AuthorizationStrucruABC):
    def __init__(self):
        self._authorizationsServers = 'linkedin'
        self._authorizationType = 'general'

    def get_domain(self):
        from pullgerDomain.com.linkedin.port import port
        return port.Domain


class Sales(General):
    def __init__(self):
        super().__init__()
        self._authorizationType = 'sales'