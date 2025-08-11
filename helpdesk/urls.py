from django.contrib.auth import views as auth_views
from django.urls import path

from helpdesk.views import ticket_views, kb_views


urlpatterns = [
    
	path('', ticket_views.index, name='index'),

	path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
	path('accounts/logout/', auth_views.LogoutView.as_view(next_page='/accounts/login/'), name='logout'),

	path('tickets/', ticket_views.ticket_list, name='ticket_list'),
	path('tickets/novo/', ticket_views.ticket_create, name='ticket_create'),
	path('tickets/<int:ticket_id>/', ticket_views.ticket_detail, name='ticket_detail'),

	path('kb/', kb_views.artigo_list, name='artigo_list'),
	path('kb/<int:artigo_id>/', kb_views.artigo_detail, name='artigo_detail'),

]
