from pullgerInternalControl.pullgerAccountManager import authorizationServer as Exceptions


def getByName(inAuthorisation: str):
    splittedAuthorisation = inAuthorisation.split('.')
    if len(splittedAuthorisation) == 2:
        if splittedAuthorisation[0].upper() == "LINKEDIN":
            if splittedAuthorisation[1].upper() == "GENERAL":
                from . import linkedin
                return linkedin.instances.general
            elif splittedAuthorisation[1].upper() == "SALES":
                from . import linkedin
                return linkedin.instances.sales
            else:
                raise Exceptions.IncorrectInputData(
                    f'Unlisted authorisation type name: [{splittedAuthorisation[1]}]',
                    level=20
                    )
        else:
            raise Exceptions.IncorrectInputData(f'Unlisted authorisation server name: [{splittedAuthorisation[0]}]',
                                                level=20
                                                )
    else:
        raise Exceptions.IncorrectInputData(f'Incorect authorisation server name: [{inAuthorisation}]',
                                            level=20
                                            )