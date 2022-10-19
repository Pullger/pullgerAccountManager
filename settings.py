def s_key():
    try:
        from . import settings_s_key
        return settings_s_key.S_KEY
    except BaseException:
        import os
        from cryptography.fernet import Fernet

        S_DIR = os.path.abspath(os.path.dirname(__file__))
        S_FILE = os.path.join(S_DIR, 'settings_s_key.py')

        secret_key_file = open(S_FILE, "w")


        secret_key = 'S_KEY = ' + str(Fernet.generate_key()) + '\n'
        secret_key_file.write(secret_key)
        secret_key_file.close()

        from . import settings_s_key
        return settings_s_key.S_KEY