from rest_framework.serializers import ModelSerializer
from .models import Note

class NoteSerializers(ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'
        #fields = ['body','updated','created']