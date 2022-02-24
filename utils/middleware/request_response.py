import binascii
import json
from django.utils.deprecation import MiddlewareMixin

from utils.AES256 import AES256


class EncryptDecryptMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        super().__init__(get_response)
        self.get_response = get_response
        self.encrypted = False

    def __call__(self, request):
        request = self.get_response(request)
        return request

    def process_view(self, request, view_func, *view_args, **view_kwargs):
        request_data = getattr(request, '_body', request.body)
        request_data = json.loads(request_data or '{}')
        self.encrypted = request_data.get('encrypted', False)
        if self.encrypted:
            ciphertext = binascii.unhexlify(request_data.get('data'))
            request._body = AES256().decrypt(ciphertext)
        else:
            request._body = json.dumps(request_data.get('data')).encode('utf-8')
        return None

    def process_template_response(self, request, response):
        data = response.data
        if self.encrypted:
            ciphertext = AES256().encrypt(json.dumps(data))
            response.data = dict(data=ciphertext, encrypted=self.encrypted)
        else:
            response.data = dict(data=data, encrypted=self.encrypted)
        return response

