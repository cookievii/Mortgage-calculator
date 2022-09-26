from api.views import OfferViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("offer", OfferViewSet, basename="offer")
