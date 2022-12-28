*.pyc
*~
__pycache__
venv
db.sqlite3
/static
.DS_Store
.idea
local_settings.py
from django.contrib import admin

from .models import Post, Comment


admin.site.register(Post)
admin.site.register(Comment)