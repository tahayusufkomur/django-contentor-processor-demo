from contentor_video_processor.models import ContentorVideoField, ContentorVideoModel
from django.db import models

class Video(ContentorVideoModel):
    name = models.CharField(max_length=50)
    video = ContentorVideoField(
        null=True,
        blank=True,
        upload_to="videos/original/",
    )