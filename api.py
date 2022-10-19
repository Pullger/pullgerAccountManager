from .models import Accounts
from . import structures
from pullgerInternalControl import pIC_pAM


def encrypteMessage(inMessage):
    from cryptography.fernet import Fernet
    from . import settings

    fernet = Fernet(settings.s_key())
    return fernet.encrypt(inMessage.encode()).decode()


def decripteMessage(inMessage):
    from cryptography.fernet import Fernet
    from . import settings

    fernet = Fernet(settings.s_key())
    return fernet.decrypt(inMessage.encode()).decode()


def addAccount(**kwargs):
    '''

    :param kwargs:
    :return: str: UUID of with element aded
    '''

    CreatigParameters = { 'configuration': {}}
    # ------------LOGIN------------

    if 'login' in kwargs:
        CreatigParameters['login'] = kwargs['login']
    else:
        raise pIC_pAM.api.IncorrectInputData("No data login is mandatory kwarg.",
                                                level=20
                                                )
    # --------AUTHORIZATION----------------
    try:
        if 'authorization' in kwargs:
            authorization_InputName = str(kwargs['authorization'])
    except BaseException as e:
        pIC_pAM.api.IncorrectInputData("Incorrect authorization data",
                                          level=20,
                                          exception=e
                                          )

    from pullgerAccountManager import authorizationsServers

    if authorization_InputName != None:
        authorization = authorizationsServers.functions.getByName(authorization_InputName)

    CreatigParameters.update({
        'authorization': str(authorization)
    })
    # ----------CONFIGURATION--------------
    if 'configuration' in kwargs:
        CreatigParameters['configuration'].update(kwargs['configuration'])
    else:
        if authorization == authorizationsServers.linkedin.instances.general:
            CreatigParameters['configuration'].update({
                'limitPeopleCircle': 15,
                'limitPeopleMax': 120,
                'limitCompanyCircle': 20,
                'limitCompanyMax': 250,
            })
    # ----------PASSWORD--------------
    if 'password' in kwargs:
        CreatigParameters['password'] = encrypteMessage(kwargs['password'])

    return Accounts.putAccount(**CreatigParameters)


def getAccount():
    pass


def getAccountList():
    return Accounts.objects.getAccountList()
