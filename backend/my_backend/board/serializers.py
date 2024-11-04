from rest_framework import serializers
from board.entity.models import Board
class BoardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Board
        fields = ['boardId', 'title', 'writer', 'content', 'regDate', 'updDate'] # 문자 틀리면 에러남
        read_only_fields = ['regDate', 'updDate']