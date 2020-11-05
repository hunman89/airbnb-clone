from django.contrib import admin
from django.utils.html import mark_safe
from . import models


@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """ Item Admin Definition"""

    list_display = (
        "name",
        "used_by",
    )

    def used_by(self, object):
        return object.rooms.count()


class PhotoInline(admin.TabularInline):

    model = models.Photo


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """ Room Admin Definition"""

    inlines = (PhotoInline,)

    fieldsets = (
        (
            "Basic Info",
            {
                "fields": (
                    "name",
                    "description",
                    "city",
                    "country",
                    "address",
                    "price",
                    "room_type",
                )
            },
        ),
        ("Times", {"fields": ("check_in", "check_out", "instant_book")}),
        ("Spaces", {"fields": ("guests", "beds", "bedrooms", "bath")}),
        (
            "More About the Space",
            {
                "classes": ("collapse",),
                "fields": ("amenity", "facility", "houserule"),
            },
        ),
        ("Last Details", {"fields": ("host",)}),
    )

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "guests",
        "beds",
        "bedrooms",
        "bath",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
        "count_photos",
        "total_rating",
    )

    list_filter = (
        "instant_book",
        "host__superhost",
        "room_type",
        "amenity",
        "facility",
        "houserule",
        "city",
        "country",
    )

    raw_id_fields = ("host",)

    search_fields = ("city", "host__username")

    ordering = (
        "name",
        "price",
    )

    filter_horizontal = (
        "amenity",
        "facility",
        "houserule",
    )

    #    def save_model(self, request, obj, form, change):
    #       print(obj, change, form)
    #      super().save_model(request, obj, form, change)

    def count_amenities(self, object):
        return object.amenity.count()

    def count_photos(self, object):
        return object.photos.count()

    count_photos.short_description = "Photo Count"


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """ Phot Admin Definition """

    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, object):
        return mark_safe(f'<img width="50px" src="{object.file.url}" />')

    get_thumbnail.short_description = "Thumbnail"
