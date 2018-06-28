from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

from battlenet.oauth2 import BattleNetOAuth2


# Create your views here.
def bnet_login(request):
    bnet = BattleNetOAuth2(region='us')
    url, state = bnet.get_authorization_url()
    # save state somewhere for checking the redirect response against
    request.session['state'] = state
    return HttpResponseRedirect(url)

def oauth(request):
    print(request)
    # store the code and login() user
    return HttpResponse('worked?')
