from .models import Accounts
from . import structures
from pullgerInternalControl import pIC_pAM
from cryptography.fernet import Fernet
from . import settings


def encrypt_message(msg: str) -> str:
    fernet = Fernet(settings.s_key())
    return fernet.encrypt(msg.encode()).decode()


def decrypt_message(msg: str) -> str:
    fernet = Fernet(settings.s_key())
    return fernet.decrypt(msg.encode()).decode()


def add_account(
        login: str = None,
        password: str = None,
        configuration=None,
        authorization=None,
        **kwargs):
    """
    Add account for authentication in DB

    :param login: Login name of adding account
    :param password: Password name of adding account
    :param kwargs: Declared for call compatibility
    :param authorization:
    :param configuration:
    :return: str: UUID of with element added
    """

    create_parameters = {'configuration': {}}
    # ------------LOGIN------------

    if login is not None:
        create_parameters['login'] = login
    else:
        raise pIC_pAM.api.IncorrectInputData(
            msg="No data login is mandatory kwarg.",
            level=20
        )

    # ----------PASSWORD--------------
    if password is not None:
        create_parameters['password'] = encrypt_message(password)

    # --------AUTHORIZATION----------------
    try:
        if authorization is not None:
            authorization_input_name = str(authorization)
    except BaseException as e:
        pIC_pAM.api.IncorrectInputData(
            msg="Incorrect authorization data",
            level=20,
            exception=e
        )

    from pullgerAccountManager import authorizationsServers

    if authorization_input_name is not None:
        authorization_server = authorizationsServers.functions.getByName(authorization_input_name)

    create_parameters.update({
        'authorization': str(authorization_server)
    })
    # ----------CONFIGURATION--------------
    if configuration is not None:
        create_parameters['configuration'].update(configuration)
    else:
        if password == authorizationsServers.linkedin.instances.general:
            create_parameters['configuration'].update({
                'limitPeopleCircle': 15,
                'limitPeopleMax': 120,
                'limitCompanyCircle': 20,
                'limitCompanyMax': 250,
            })

    return Accounts.putAccount(**create_parameters)


def get_account_list():
    return Accounts.objects.get_account_list()
