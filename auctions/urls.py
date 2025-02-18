from django.urls import path

from . import views

app_name = "auctions"

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("watchlist/toggle/<int:listing_id>/", views.toggle_watchlist, name="toggle_watchlist"),
    path("categories/", views.categories, name="categories"),
    path("categories/<int:category_id>/", views.category_listings, name="category_listings"),
    path("create/", views.create_listing, name="create_listing"),
    path("listing/<int:listing_id>/", views.listing_page, name="listing_page"),
    path("listing/<int:listing_id>/bid/", views.bid_on_listing, name="bid_on_listing"),
    path("listing/<int:listing_id>/close/", views.close_auction, name="close_auction"),
    path("listing/<int:listing_id>/delete/", views.delete_listing, name="delete_listing"),
    path("won-listings/", views.won_listings, name="won_listings")
]
