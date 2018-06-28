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
    if request.GET.get('code'):
        if request.GET.get('state') and request.session.get('state'):
            if request.GET['state'] == request.session['state']:
                bnet = BattleNetOAuth2(region='us')
                data = bnet.retrieve_access_token(request.GET['code'])
                if data.get('access_token'):
                    code = data['access_token']
                    bnet = BattleNetOAuth2(region='us', scope='wow.profile', access_token=code)
                    status, profile = bnet.get_profile()
                    if status == 200:
                        characters = []
                        for character in profile['characters']:
                            if character['level'] > 90:
                                characters.append(character)
                        return render(request, 'characters.html', {'characters': characters})
    return HttpResponse('error')
