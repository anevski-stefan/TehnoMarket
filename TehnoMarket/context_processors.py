from django.contrib.auth import get_user_model
from TehnoMarket.models import CustomUser

def user_role(request):
    role = None
    if request.user.is_authenticated:
        try:
            user = get_user_model().objects.get(pk=request.user.pk)
            cuser = CustomUser.objects.get(user=user)
            if str(cuser.role).lower() == "продавач":
                role = "Продавач"
        except CustomUser.DoesNotExist:
            role = None
    return {'user_role': role}
