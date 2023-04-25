from cdtool.models import Service, ActiveServiceOnEnv
from django.db import DatabaseError as DatabaseErrorDjango
from glxplay.exceptions import ServiceNotFound, AccessdbError
class ServiceDb():
    def __init__(self):
        pass

    @staticmethod
    def get_service_info(name):
        try:
            result = Service.objects.filter(cd_name=name)
            if result.exists():
                return result[0]
            else:
                raise ServiceNotFound(desc='Service %s not found' % name)
        except DatabaseErrorDjango as ex:
            raise AccessdbError(ex)
        
    @staticmethod
    def get_service_list():

        try:
            return Service.objects.all()
        except DatabaseErrorDjango as ex:
            raise AccessdbError(ex)
        
    @staticmethod
    def get_service_name_list():

        try:
            return Service.objects.all().values('name')
        except DatabaseErrorDjango as ex:
            raise AccessdbError(ex)
        
class ServiceOnEnvDb():
    def __init__(self):
        pass

    @staticmethod
    def get_list_service_name_active_on_env(env):
        try:
            return ActiveServiceOnEnv.objects.filter(env=env, active=True).values('service__name')

        except DatabaseErrorDjango as ex:
            raise AccessdbError(ex)