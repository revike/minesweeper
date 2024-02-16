from rest_framework import views, exceptions


def custom_exception_handler(exc, context):
    """Custom exception handler"""
    response = views.exception_handler(exc, context)
    if isinstance(exc, exceptions.ValidationError):
        error = 'Произошла непредвиденная ошибка'
        if len(response.data) > 0:
            if isinstance(response.data, list):
               error = f'{response.data[0]}'
            elif isinstance(response.data, dict):
                error = 'ошибка разбора входных данных'
        custom_response_data = {'error': error}
        response.data = custom_response_data
    return response
