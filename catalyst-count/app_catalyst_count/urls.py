from django.urls import path,include
from .import views


urlpatterns = [
   path("signup/",views.RegisterView,name="register"),
   path('insert/',views.InsertData,name='insert'),
   path('showpage/',views.ShowPage,name='show_users'),
   path("", views.UserLoginForm, name='login'),
   path('user_login/', views.UserLogin, name='user_login'),
   path('upload_data/', views.UploadData, name='upload_data'),
   path('upload_chunked/', views.MyChunkedUploadView.as_view(), name='my_upload_view'),

   path('query_builder/',views.QueryBuilder,name='query_builder'),
   path('users/',views.Users,name='users'),
   path('logout/',views.Logout,name='logout'),

]
