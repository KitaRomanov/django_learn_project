# django_learn_project
Учебный проект сайта магазина по готовому html шаблону






 В файле
 venv/lib/python3.11/site-packages/django/core/serializers/json.py
 
 в функции 
 
 
 def Deserializer(stream_or_string, **options):
    """Deserialize a stream or string of JSON data."""
    if not isinstance(stream_or_string, (bytes, str)):
        stream_or_string = stream_or_string.read()
    if isinstance(stream_or_string, bytes):
        stream_or_string = stream_or_string.decode()
    try:
        objects = json.loads(stream_or_string)
        yield from PythonDeserializer(objects, **options)
    except (GeneratorExit, DeserializationError):
        raise
    except Exception as exc:
        raise DeserializationError() from exc
        
        
        
Необхлдимо указать кодировку UTF-16
stream_or_string = stream_or_string.decode('UTF-16')

И тогда фикстуры удачно загрузятся в БД

Данная проблема изначально возникла из-за виндовс и пока еще не исправлена.

