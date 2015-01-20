DEBUG = True

# Make these unique, and don't share it with anybody.
SECRET_KEY = "f72bd952-6085-46b1-96e6-1ed93302051ded8160ec-8f0b-4194-a838-3a68ee86225ec28c1da6-a495-476a-acfb-a122e43aa0c9"
NEVERCACHE_KEY = "f16a66bd-ef4d-4b13-a4a4-6d8370c192ecf18efe6a-89f5-4e6f-8393-ec9ccace8414bd9dd4df-ce07-4d8a-a0c4-34271767cc4e"

DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.sqlite3",
        # DB name or path to database file if using sqlite3.
        "NAME": "dev.db",
        # Not used with sqlite3.
        "USER": "",
        # Not used with sqlite3.
        "PASSWORD": "",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "",
    }
}
