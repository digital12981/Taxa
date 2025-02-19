import pkg_resources
import os

def generate_requirements():
    packages = [
        'flask-migrate',
        'flask-weasyprint',
        'flask-sqlalchemy',
        'trafilatura',
        'weasyprint',
        'flask-login',
        'flask',
        'requests',
        'gevent',
        'email-validator',
        'gunicorn',
        'flask-wtf',
        'flask-caching',
        'psycopg2-binary'
    ]
    
    with open('requirements.txt', 'w') as f:
        for package in packages:
            try:
                version = pkg_resources.get_distribution(package).version
                f.write(f"{package}=={version}\n")
            except:
                f.write(f"{package}\n")

if __name__ == "__main__":
    generate_requirements()
