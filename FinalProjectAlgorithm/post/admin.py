from django.contrib import admin
from post.models import *


admin.site.register(CategoryPost)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(MySubscription)
admin.site.register(BlockedUser)