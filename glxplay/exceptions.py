class FimPlusError(Exception):
    """
    FimPlus exception
    """
    error_code = 0
    desc = 'FimPlusError'

    def __init__(self, desc=None):
        if desc is not None:
            self.desc = '%s' % desc

    def __str__(self):
        return '%s %s' % (self.error_code, self.desc)

class ServiceError(FimPlusError):
    """
    Access info of service
    """

    error_code = 11
    desc = 'ServiceError'

    def __init__(self, desc=None):
        super(ServiceError, self).__init__(desc)

class ServiceNotFound(ServiceError):
    """
    Service information not found
    """

    error_code = 12
    desc = 'ServiceNotFound'

    def __init__(self, desc=None):
        super(ServiceNotFound, self).__init__(desc)

class AccessdbError(FimPlusError):
    """
    Access database error
    """

    error_code = 10
    desc = 'Acessdberror Error'

    def __init__(self, desc=None):
        super(AccessdbError, self).__init__(desc)