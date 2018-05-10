from django.shortcuts import redirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse


def login_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.session.has_key('islogin'):
            request.session['url_path'] = ''
            return view_func(request, *args, **kwargs)
        else:
            return redirect(reverse('user:login'))

    return wrapper
