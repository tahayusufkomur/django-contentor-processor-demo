from django.contrib import admin

from home.models import Video


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ("name", "status_table", "video")
    search_fields = ("name",)
    list_filter = ("name",)
    list_per_page = 10

    def status_table(self, obj):
        return obj.get_video_resolution_table_html()