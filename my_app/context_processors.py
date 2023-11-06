from my_app.models import MAINDETAILS

def context_view(request):
    detail = MAINDETAILS.objects.last()
    return {"detail":detail}