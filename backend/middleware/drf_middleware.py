import logging
import uuid

from django.utils.deprecation import MiddlewareMixin
from django.conf import settings

# Get an instance of a logger
_logger = logging.getLogger('djangofile')

def wrap_streaming_content(content):
    for chunk in content:
        yield chunk

class LogRestMiddleware(MiddlewareMixin):
    """Middleware to log every request/response.
    Is not triggered when the request/response is managed using the cache
    """

    def _log_request(self, request):
        """Log the request"""
        user = str(getattr(request, 'user', ''))
        method = str(getattr(request, 'method', '')).upper()
        request_path = str(getattr(request, 'path', ''))
        remote_addr = request.META["REMOTE_ADDR"]

        token= str(getattr(request.META, 'HTTP_AUTHORIZATION', ''))
        token = f'{token[:15]}.........{token[-10:]}' if token else ''
        _logger.debug(f'req: [{method}] [{request_path}] ({user}) [{remote_addr}] [{self.uuid}] [{token}]')

    def _log_response(self, request, response):
        """Log the response using values from the request"""
        user = str(getattr(request, 'user', ''))
        method = str(getattr(request, 'method', '')).upper()
        status_code = str(getattr(response, 'status_code', ''))
        status_text = str(getattr(response, 'status_text', ''))
        request_path = str(getattr(request, 'path', ''))
        content = str(response.content)

        _logger.debug(f'res: [{method}] [{request_path}] ({user}) [{self.uuid}]- {status_code}, {status_text} {content}')

    def process_response(self, request, response):
        """Method call when the middleware is used in the `MIDDLEWARE_CLASSES` option in the settings. Django < 1.10"""
        self._log_request(request)
        self._log_response(request, response)
        return response

    def __call__(self, request):
        """Method call when the middleware is used in the `MIDDLEWARE` option in the settings (Django >= 1.10)"""
        if 'api/' in request.path:
            # seta um identificador
            self.uuid =  uuid.uuid4()
            self._log_request(request)
            response = self.get_response(request)
            self._log_response(request, response)
            return response

        return self.get_response(request)
