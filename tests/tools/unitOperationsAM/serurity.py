from django.test import TestCase


class Test001EncryptingPassword(TestCase):
    def test_000_generate_key(self):
        from pullgerAccountManager import settings

        s_key = settings.s_key()
        self.assertEqual(len(s_key), 44, 'Incorrect secret key')

    def test_001_encrypt_decrypt_message(self):
        from pullgerAccountManager import apiAM

        testMessage = '!@~34t #$%^&*e()-+=_st'
        eMessage = apiAM.encrypt_message(testMessage)
        self.assertNotEqual(testMessage, eMessage, 'Not encrypt.')
        dMessage = apiAM.decrypt_message(eMessage)
        self.assertEqual(dMessage, testMessage, 'Incorrect description')
