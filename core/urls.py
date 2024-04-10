"""
define the url routes of core api
"""
from django.urls import path
from core.api.auth import obtain_jwt_token, refresh_jwt_token, obtain_jwt_token_admin


from core.api.user import follow, unfollow, list_favorite_recent, change_organization

from core.api.image import (IMAGE_API, IMAGE_SET_API)



from core.api.user import get_all_user_info, delete_user, change_user_info



urlpatterns = [

    # user apis
    path('token-auth', obtain_jwt_token),
    path('token-auth/admin', obtain_jwt_token_admin),
    path('token-refresh', refresh_jwt_token),
    path('user/<int:type>/all/<int:page>', get_all_user_info),
    path('user/delete', delete_user),
    path('user/changeinfo', change_user_info),

]
