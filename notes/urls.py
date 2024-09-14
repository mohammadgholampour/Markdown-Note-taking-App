# notes/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('notes/', views.note_list, name='notes_list'),
    path('notes/<int:note_id>/', views.note_detail, name='note_detail'),
    path('notes/save/', views.save_note, name='save_note'),
    path('notes/check-grammar/', views.check_grammar, name='check_grammar'),
    path('notes/render/<int:note_id>/', views.render_markdown_to_html, name='render_markdown_to_html'),
]
