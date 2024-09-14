# notes/views.py
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Note
from .serializers import NoteSerializer
import markdown
import language_tool_python
from django.shortcuts import render, get_object_or_404

# notes/views.py

def note_list(request):
    notes = Note.objects.all()
    return render(request, 'notes/note_list.html', {'notes': notes})

def note_detail(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    return render(request, 'notes/note_detail.html', {'note': note})


@api_view(['POST'])
def save_note(request):
    serializer = NoteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Note saved successfully!'})
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def list_notes(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def check_grammar(request):
    tool = language_tool_python.LanguageTool('en-US')
    markdown_text = request.data.get('content')
    if markdown_text:
        matches = tool.check(markdown_text)
        return Response({'grammar_issues': [str(match) for match in matches]})
    return Response({'error': 'No content provided'}, status=400)

@api_view(['GET'])
def render_markdown_to_html(request, note_id):
    try:
        note = Note.objects.get(id=note_id)
        html_content = markdown.markdown(note.content)
        return Response({'html': html_content})
    except Note.DoesNotExist:
        return Response({'error': 'Note not found'}, status=404)


