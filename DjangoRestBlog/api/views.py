from api.models import Posts
from rest_framework.generics import (
    ListAPIView, RetrieveAPIView
)
from .serializers import (PostListSerializer)


class HomeAPIView(ListAPIView):
    """
        List of all data.
    """
    queryset = Posts.objects.all()
    serializer_class = PostListSerializer


class DetailAPIView(RetrieveAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostListSerializer
    lookup_field = 'slug'
