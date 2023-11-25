from django.db.models import Model

from typing import Type


class UserRouter:
    
    related_apps = {'auth', 'doctors'}
    
    def db_for_read(self, model: Type[Model], **hints) -> str | None:
        # print(f'DEBUG: {model}')
        if model._meta.app_label == 'doctors':
            return 'users'
        return None
    
    def db_for_write(self, model: Type[Model], **hints) -> str | None:
        # print(f'DEBUG: {model}')
        if model._meta.app_label == 'doctors':
            return 'users'
        return None
    
    def allow_relation(self, obj1, obj2, **hints) -> bool | None:
        # print(f'DEBUG: {type(obj1)} {obj1} <-> {type(obj2)} {obj2}')
        if {obj1._meta.app_label, obj2._meta.app_label} == self.related_apps:
            return True
        return None
    
    def allow_migrate(
            self,
            db_label: str, 
            app_label: str, 
            model_name=None, 
            **hints
    ) -> bool | None:
        # print(f'DEBUG: {db_label} {app_label}', end=' ')
        if app_label == 'doctors':
            res = db_label == 'users'
            # print(res)
            return res
        elif db_label == 'users':
            # print(False)
            return False
        # print()
        return None

