from django.urls import path
from cart.views import add_to_cart
from .views import (
    EventDetailView,
    EventListView,
    EventCreateView,
    EventUpdateView,
    EventDeleteView,
)

app_name = "event"

urlpatterns = [
    path("events/", EventListView.as_view(), name="browse_events"),
    path("new/", EventCreateView.as_view(), name="create_event"),
    path("<int:pk>/", EventDetailView.as_view(), name="detail"),
    path("<int:pk>/edit/", EventUpdateView.as_view(), name="edit_event"),
    path("<int:pk>/delete/", EventDeleteView.as_view(), name="delete_event"),
    path("<int:event_id>/add-to-cart/", add_to_cart, name="add_to_cart"),
]
