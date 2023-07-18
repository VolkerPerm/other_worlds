import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Worlds


# class WorldsModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content


class WorldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worlds
        fields = ('__all__')


    # def create(self, validated_data):
    #     return Worlds.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.content = validated_data.get('content', instance.content)
    #     instance.time_update = validated_data.get('time_update', instance.time_update)
    #     instance.is_publisher = validated_data.get('is_publisher', instance.is_publisher)
    #     instance.cat_id = validated_data.get('cat_id', instance.cat_id)
    #     instance.save()
    #     return instance



# def encode():
#     model = WorldsModel('Civ', 'Content: Civ')
#     model_sr = WorldsSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
#
#
# def decode():
#     stream = io.BytesIO(b'{"title": "Civ", "content": "Civ"}')
#     data = JSONParser().parse(stream)
#     serializer = WorldsSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)
