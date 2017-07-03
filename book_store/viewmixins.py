from django.contrib.auth.decorators import login_required
from django.views.generic import base
from django.utils.decorators import method_decorator


class LoginRequiredMixin(base.View):
    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(
            request, *args, **kwargs)