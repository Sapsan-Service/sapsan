from django.shortcuts import render


def index_account(request):
    return render(request, 'account/index_account.html')
