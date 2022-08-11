from django.views import View

from mainapp.models import Profile
from order.models import Basket


class BasketMixin(View):

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            profile = Profile.objects.filter(user=request.user).first()
            if not profile:
                profile = Profile.objects.create(
                    user=request.user
                )
            basket = Basket.objects.filter(owner=profile, in_order=False).first()
            if not basket:
                basket = Basket.objects.create(owner=profile)
        else:
            basket = Basket.objects.filter(for_anonymous_user=True).first()
            if not basket:
                basket = Basket.objects.create(for_anonymous_user=True)

        self.basket = basket
        return super().dispatch(request, *args, **kwargs)
