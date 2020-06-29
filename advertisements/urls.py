from django.contrib import admin
from django.urls import path
from .views import AdList, AdDetail, SearchResultsView

urlpatterns = [
    path('', AdList.as_view(), name='ad_list'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('<slug:city>/<slug:category>/<int:pk>/', AdDetail.as_view(), name='ad_detail'),
    path('<slug:category>/', AdList.as_view(), name='category_post_list')

]