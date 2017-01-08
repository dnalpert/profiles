# profiles
Django profile for each user

Project/urls.py

    from profiles import views as profile_views
    
    url(r'^$', profile_views.index, name='index'),
    url(r'^profile/(?P<username>\w+)/$', profile_views.UserProfile, name='profile'),
    url(r'^edit_profile/$', profile_views.EditUserProfile, name='edit_profile'),
    
