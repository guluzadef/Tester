# from rest_framework import serializers
# from .models import test
#
#
# class CategorySerializer(serializers.ModelSerializer):
#     courses = serializers.HyperlinkedRelatedField(
#         many=True,
#         read_only=True,
#         view_name='course-detail'
#     )
#
#     class Meta:
#         model = test
#         fields = ('pk', 'name', 'courses',)
