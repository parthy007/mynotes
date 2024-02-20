from rest_framework.response import Response
from .models import Note
from .serializers import NoteSerializers


def getNotesList(request):
    notes = Note.objects.all().order_by('-updated')
    serializer = NoteSerializers(notes, many=True)
    return Response(serializer.data)


def getNoteDetail(request, rid):
    notes = Note.objects.get(id=rid)
    serializer = NoteSerializers(notes, many=False)
    return Response(serializer.data)


def createNote(request):
    data = request.data
    note = Note.objects.create(
        body=data['body']
    )
    serializer = NoteSerializers(note, many=False)
    return Response(serializer.data)

def updateNote(request, rid):
    data = request.data
    note = Note.objects.get(id=rid)
    serializer = NoteSerializers(instance=note, data=data)

    if serializer.is_valid():
        serializer.save()

    return serializer.data


def deleteNote(request, rid):
    note = Note.objects.get(id=rid)
    note.delete()
    return Response('Note was deleted!')