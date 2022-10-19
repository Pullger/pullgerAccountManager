from django.test import TestCase
from django.apps import apps
from pullgerAccountManager import api
from . import dataTemplate

class UnitOperations():
    @staticmethod
    def AddAccount(self):
        accArg = {}

        from pullgerAccountManager.authorizationsServers.linkedin import instances
        from pullgerAccountManager import api

        accountStructure = dataTemplate.LinkedInAccount()
        accountStructure['authorization'] = str(instances.general)
        accArg.update(accountStructure)

        accountConfig = {}
        accountConfig['configuration'] = dataTemplate.LinkedInConfiguration()
        accArg.update(accountConfig)

        uuidAccount = api.addAccount(**accArg)

        accList = api.getAccountList()
        for curAcc in accList:
            self.assertEqual(uuidAccount, curAcc.uuid, "Incorrect uuid save")

            for key, value in accountStructure.items():
                if key == 'password':
                    self.assertEqual(api.decripteMessage(getattr(curAcc, key)), value, 'Incorrect password description.')
                else:
                    self.assertEqual(getattr(curAcc, key), value, 'Incorrect data save on property {key}')


class Test_000_Encripting(TestCase):
    def test_000_GenerateKey(self):
        from pullgerAccountManager import settings

        s_key = settings.s_key()
        self.assertEqual(len(s_key), 44, 'Incorrect secret key')

    def test_001_EncrypteDecrypteMessage(self):
        from .. import api

        testMessage = '!@~34t #$%^&*e()-+=_st';
        eMessage = api.encrypteMessage(testMessage)
        self.assertNotEqual(testMessage, eMessage, 'Not encrypte.')
        dMessage = api.decripteMessage(eMessage)
        self.assertEqual(dMessage, testMessage, 'Incorrect decription')

class Test_001_API(TestCase):
    def test_001_AddAccount(self):
        UnitOperations.AddAccount(self)