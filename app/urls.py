"""RoboAdvisor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView

from app.views.view_assetComparisionGraph import assetComparisionGraphDataApi
from app.views.view_assetNews import assetNewsApi
from app.views.view_assetPersonalHolding import assetPersonalHoldingApi
from app.views.view_assetPredictionGraph import assetPredictionGraphDataApi
from app.views.view_assetWaterFall import assetWaterFallApi
from app.views.view_home import home
from app.views.view_navigation import navigationApi
from app.views.view_portfolioComparisionGraph import portfolioComparisionGraphDataApi
from app.views.view_portfolioNews import portfolioNewsApi
from app.views.view_portfolioPersonalHolding import portfolioPersonalHoldingApi
from app.views.view_portfolioPrediction import portfolioPredictionApi
from app.views.view_portfolioPredictionGraph import portfolioPredictionGraphDataApi

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='home'),
    url(r'^getNavigation/', navigationApi, name="getNavigation"),

    # Portfolio
    url(r'^portfolio/getPersonalHolding/', portfolioPersonalHoldingApi, name="getPortfolioPersonalHolding"),
    url(r'^portfolio/getPredictionGraphData/', portfolioPredictionGraphDataApi, name="getPredictionGraphData"),
    url(r'^portfolio/getPrediction/', portfolioPredictionApi, name="getPortfolioPersonalHolding"),
    url(r'^portfolio/getNews/', portfolioNewsApi, name="getNews"),

    # Asset
    url(r'^asset/([A-Z]+-?[A-Z]*)/getPersonalHolding/', assetPersonalHoldingApi,
        name="getPersonalHolding"),
    url(r'^asset/([A-Z]+-?[A-Z]*)/getPredictionGraphData/', assetPredictionGraphDataApi,
        name="getAssetPredictionGraphData"),
    url(r'^asset/([A-Z]+-?[A-Z]*)/getNews/', assetNewsApi, name="getNews"),
    url(r'^asset/([A-Z]+-?[A-Z]*)/getWaterFallData/', assetWaterFallApi, name="getWaterFallData"),

    url(r'^(%s)?$' % '|'.join(['predictions', 'performance', 'predictions/portfolio', 'predictions/asset/([A-Z]+)']),
        TemplateView.as_view(template_name='index.html')),

    # RoboAdvisor Growth
    url(r'^portfolio/getComparisionGraphData/', portfolioComparisionGraphDataApi, name="getComparisionGraphData"),
    url(r'^asset/([A-Z]+-?[A-Z]*)/getComparisionGraphData/', assetComparisionGraphDataApi,
        name="getAssetComparisionGraphData")

]
