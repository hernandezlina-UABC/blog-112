from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    PostDraftListView,
    PostArchivedListView,
    PostView
)

urlpatterns = [
    path("list/", PostListView.as_view(), name= "post_list"),
    path("list/draft/", PostDraftListView.as_view(), name= "post_drafts"),
    path("list/archived/", PostArchivedListView.as_view(), name= "post_archived"),
    path("<int:pk>/", PostView.as_view(), name= "post_detail"),
    path("new/", PostCreateView.as_view(), name= "post_new"),
    path("edit/<int:pk>/", PostUpdateView.as_view(), name= "post_edit"),
    path("delete/<int:pk>/", PostDeleteView.as_view(), name= "post_delete"),
]

"""
PostUpdateView:
UPDATE Post
SET title = "", subtitle = "", body = ""
WHERE id=?



PostDeleteView:
DELETE FROM post WHERE id = ?
"""

