from pullgerInternalControl.pullgerAccountManager import authorizationServer as Exceptions


def getByName(authorizationType):
    if authorizationType.upper() == "GENERAL":
        from .. import linkedin
        return linkedin.instances.general
    elif authorizationType.upper() == "SALES":
        from .. import linkedin
        return linkedin.instances.sales
    else:
        raise Exceptions.structures.IncorrectInputData(
            f'Unknown authorization type: {authorizationType}',
            level=40
        )