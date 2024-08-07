# your_app/middleware.py

from django.utils.deprecation import MiddlewareMixin
from django.conf import settings

class AdminSessionMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path.startswith('/admin'):
            request.session.save()
            request.session = request.session.__class__(session_key=request.COOKIES.get('sessionid_admin'))
            request.session_cookie_name = settings.ADMIN_SESSION_COOKIE_NAME
        else:
            request.session_cookie_name = settings.SESSION_COOKIE_NAME
