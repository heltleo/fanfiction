from backend.settings import *
import dj_database_url

DATABASES['default'] = dj_database_url.config()

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

DEBUG = config('DEBUG', cast=bool)

# email admin

SERVER_EMAIL = config('ADMIN_EMAIL')

ADMINS = [
  (config('ADMIN_NAME'), config('ADMIN_EMAIL')),
]

ALLOWED_HOSTS = ['*',]

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

# Media storages

AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}

DEFAULT_FILE_STORAGE = 'backend.storage_backends.MediaStorage'
