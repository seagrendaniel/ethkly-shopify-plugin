from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from shopify_auth.decorators import login_required
from django.http import HttpResponseRedirect
# Create your views here.
from flask import Flask, render_template, request, redirect, Response, session
import os
import requests
import json
import uuid
import shopify
 
HOST = '7b3ce72e.ngrok.io'
SHOPIFY_APP_API_KEY = os.environ['SHOPIFY_APP_API_KEY']
SHOPIFY_APP_API_SECRET = os.environ['SHOPIFY_APP_API_SECRET']
CALLBACK_URL = 'http://' + HOST + '/install'
SCOPE = 'read_products, read_collection_listings'

def home(request, *args, **kwargs):
    return render(request, 'home.html')

def install(request):
    if request.GET.get('shop'):
        shop = request.GET.get('shop')
    else: 
        return Response(response='Error: parameter shop not found', status=500)
    auth_url = 'https://{0}/admin/oauth/authorize?client_id={1}&scope={2}&redirect_uri={3}'.format(
        shop, SHOPIFY_APP_API_KEY, SCOPE, os.environ['REDIRECT_URI']
    )
    print('Debug - auth URL: ', auth_url)
    return HttpResponseRedirect(auth_url)


# @app.route('/connect', methods=['GET'])
def connect(request):
    if request.GET.get("shop"):
        params = {
            "client_id": SHOPIFY_APP_API_KEY,
            "client_secret": SHOPIFY_APP_API_SECRET,
            "code": request.GET.get("code")
        }
        resp = requests.post(
            "https://{0}/admin/oauth/access_token".format(
                request.GET.get("shop")
            ),
            data=params
        )
        if 200 == resp.status_code:
            resp_json = json.loads(resp.text)

            access_token = resp_json.get("access_token")
            shop = request.GET.get("shop")

            return render(request, 'welcome.html')
        else:
            print ("Failed to get access token: ", resp.status_code, resp.text)
            return render(request, 'error.html')
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)





