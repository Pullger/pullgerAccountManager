from pullgerAccountManager.tests.tools import dataTemplatesAM
from django.test import TestCase
from pullgerAccountManager import apiAM
from pullgerAccountManager import authorizationsServers


def add_account_for_linkedin(self: TestCase) -> None:
    accArg = {}

    account_structure = dataTemplatesAM.LinkedInAccount()
    account_structure['authorization'] = str(authorizationsServers.linkedin.instances.general)
    accArg.update(account_structure)

    account_config = {'configuration': dataTemplatesAM.LinkedInConfiguration()}
    accArg.update(account_config)

    uuidAccount = apiAM.add_account(**accArg)

    accList = apiAM.get_account_list()
    for curAcc in accList:
        self.assertEqual(uuidAccount, curAcc.uuid, "Incorrect uuid save")

        for key, value in account_structure.items():
            if key == 'password':
                self.assertEqual(apiAM.decrypt_message(getattr(curAcc, key)), value, 'Incorrect password description.')
            else:
                self.assertEqual(getattr(curAcc, key), value, 'Incorrect data save on property {key}')
