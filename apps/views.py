from django.shortcuts import render

from apps.models import ContactsPage


def index_veiw(request):
    contacts = ContactsPage.objects.all()
    context = {
        'contact': contacts
    }
    return render(request, 'apps/index.html', context)
