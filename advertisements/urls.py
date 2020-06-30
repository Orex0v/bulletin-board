from django.contrib import admin
from django.urls import path
from .views import AdList, AdDetail, SearchResultsView, UserAdList, NewPostView, EditPost

urlpatterns = [
    path('', AdList.as_view(), name='home'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('<slug:city>/<slug:category>/<int:pk>/', AdDetail.as_view(), name='ad_detail'),
    path('category/<slug:category>/', AdList.as_view(), name='category_post_list'),
    path('profile/', UserAdList.as_view(), name='user_post_list'),
    path('additem/', NewPostView.as_view(), name='additem'),
    path('edit/<int:pk>/', EditPost.as_view(), name='edit_post')

]