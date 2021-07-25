from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

class SnippetSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    title=serializers.CharField(required=False, allow_blank=True, max_length=100)
    code=serializers.CharField(style={'base_templete':'textarea.html'})
    linenos=serializers.BooleanField(required=False)
    style=serializers.ChoiceField(choices=STYLE_CHOICES)

    def create(self, validation_data):
        return Snippets.object.create(**validation_data)

    def update(instance, validation_data):
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance
