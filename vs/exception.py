from rest_framework.views import exception_handler
import sys, traceback
from rest_framework.response import Response
from rest_framework import status

def custom_exception_handler(exc):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc)

    # Now add the HTTP status code to the response.
    if response is not None:
        response.data['status_code'] = response.status_code
    else:
        type, value, tb = sys.exc_info()
        return Response({'error': True, 'content': traceback.format_exception(type, value, tb)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return response