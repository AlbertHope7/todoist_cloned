from rest_framework import generics

from todos.models import Todo
from .serializers import TodoSerializers
from .permissions import IsAuthorOrReadOnly


class TodoList(generics.ListAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    serializer_class = TodoSerializers

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(author=user)


class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Todo.objects.all()
    serializer_class = TodoSerializers
