from pullgerAccountManager import models as pullgerAM_MODEL

def addLinkedinAccount():
    accauntDICT ={
        'login': 'developer.sphere@outlook.com',
        'password': 'nkValm76Ys8c6SSwk2Ci',
        'limitPeopleCircle': 15,
        'limitPeopleMax': 120,
        'limitCompanyCircle': 20,
        'limitCompanyMax': 250,
    }

    pullgerAM_MODEL.Accounts.putAccount(**accauntDICT)