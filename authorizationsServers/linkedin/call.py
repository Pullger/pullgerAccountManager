class _Instances():

    @property
    def general(self):
        from ._instances import General
        return General()

    @property
    def sales(self):
        from ._instances import Sales
        return Sales()


instances = _Instances()