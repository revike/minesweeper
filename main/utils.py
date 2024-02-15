from rest_framework import views, exceptions


def custom_exception_handler(exc, context):
    """Custom exception handler"""
    response = views.exception_handler(exc, context)
    if isinstance(exc, exceptions.ValidationError):
        error = 'ошибка'
        if len(response.data) > 0:
            error = f'{response.data[0]}'
        custom_response_data = {'error': error}
        response.data = custom_response_data
    return response
