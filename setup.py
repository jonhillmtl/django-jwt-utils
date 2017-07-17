from distutils.core import setup

setup(name='django-jwt-utils',
      version='0.1',
      description='Useful functions for Django and JSON Web Tokens',
      author='Jon Hill',
      author_email='jon@jonhill.ca',
      url='https://github.com/jonhillmtl/django-jwt-utils',
      license='MIT',
      packages = ['django_jwt_utils'],
      install_requires=[
          "jwcrypto",
          "django",
          "pytest"
      ],
)
