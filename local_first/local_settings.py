DEBUG = True
ALLOWED_HOSTS = ['*']

from integration_utils.bitrix24.local_settings_class import LocalSettingsClass

TINKOFF_API_KEY = 'your-api-key'
ENDPOINT_TINKOFF = 'your-secret-key'
API_KEY_TINKOFF = 'your-api-key'
SECRET_KEY_TINKOFF = 'your-secret-key'

OPEN_AI_API_KEY = 'your-api-key'

NGROK_URL = 'https://d0abfd39f460.ngrok-free.app'

APP_SETTINGS = LocalSettingsClass(
    portal_domain='b24-68oetn.bitrix24.ru',
    app_domain='127.0.0.1:8000',
    app_name='local_first',
    salt='wefiewofioiI(IF(Eufrew8fju8ewfjhwkefjlewfjlJFKjewubhybfwybgybHBGYBGF',
    secret_key='wefewfkji4834gudrj.kjh237tgofhfjekewf.kjewkfjeiwfjeiwjfijewf',
    application_bitrix_client_id='local.686e7db2524e05.77730538',
    application_bitrix_client_secret='wMh8M2SuKSLrQaiS0TAELhApSglyLxAWgtOgsvuSZzkPmhCJzh',
    application_index_path='/',
)

DOMAIN = "56218ef983f3-8301993767665431593.ngrok-free.app"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'localbitrix',
        'USER': 'postgres',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': '5432',
    },
}