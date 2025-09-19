from django.core.exceptions import PermissionDenied
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

def group_required(*group_names):
    def decorator(view_class):
        @method_decorator(login_required, name='dispatch')
        @method_decorator(_check_groups(group_names), name='dispatch')
        class Wrapped(view_class):
            pass
        return Wrapped
    return decorator

def _check_groups(group_names):
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                raise PermissionDenied
            user_groups = set(request.user.groups.values_list('name', flat=True))
            if any(g in user_groups for g in group_names):
                return view_func(request, *args, **kwargs)
            raise PermissionDenied
        return _wrapped_view
    return decorator
