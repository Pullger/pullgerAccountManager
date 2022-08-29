from ..exceptions import General as RootGeneral

class General(RootGeneral):
    def __init__(self, message, **kwargs):
        from pullgerSquirrel.exceptions import updateLoggerNameInKWARGS
        updateLoggerNameInKWARGS('structures', kwargs)

        super().__init__(message, **kwargs)