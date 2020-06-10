# VerdeQueTeQuieroVerde

## Documentacion Django: [Django](https://docs.djangoproject.com/es/3.0/intro/tutorial01/)

## Dependencias del proyecto:

- *python3*
- *pip3*
- *python3-dev*
- *libpq-dev*
- *venv* (Virtual environment recomendado)
## Instalar dependencias de Python con:

`pip3 install -r requirements.txt`

## Metodologia de desarrollo:

- Feature branch desde Master
- Test Driven Development (TDD)
- Code Review antes de mergear a Master
- Cada push a Master se despliega automaticamente

### Comandos utiles para el desarrollo

#### Run server
`bash runserver.sh`

#### Create migrations
`python3 manage.py createmigrations`

#### Correr migraciones
`bash migrate.sh`

#### Correr test unitarios
`bash test.sh`

#### Correr test de solo una aplicacion Django (para minimizar el tiempo)
`python manage.py test Djangoapplication`
