from django.http import HttpResponse


def home(request):
    return HttpResponse('<html><body>olá Django!</body></html>', content_type='text/html')
