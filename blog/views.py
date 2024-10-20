from rest_framework import viewsets, status
from rest_framework.response import Response
from core.CustomPagination import CustomPagination
from core.response import CustomResponse

from .models import *
from .serializers import *


# class BlogPostViewSet(viewsets.ViewSet):
#     def retrieve(self, request, pk=None):
#         try:
#             blog = BlogPost.objects.get(pk=pk)
#             serializer = BlogPostSerializer(blog)
#             return Response({'blog': serializer.data, 'recent_blogs': self.get_recent_blogs()})
#         except BlogPost.DoesNotExist:
#             return Response({'error': 'Blog not found'}, status=status.HTTP_404_NOT_FOUND)


#     def list(self, request):
#         return Response({'recent_blogs': self.get_recent_blogs()})
    

#     def get_recent_blogs(self):
#         recent_blogs = BlogPost.objects.order_by('-published_at')[:3]
#         serializer = RecentBlogSerializer(recent_blogs, many=True)
#         return serializer.data
    
class BlogViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    search_fields = ['title', 'author']
    filterset_fields = ['title', 'content']

    def list(self, request, *args, **kwargs):
        response = CustomResponse()
        queryset = self.filter_queryset(self.get_queryset())
        paginator = CustomPagination()
        paginated_queryset = paginator.paginate_queryset(queryset, request)
        serializer = self.get_serializer(paginated_queryset, many=True)
        response_data = {
            'next_page': paginator.get_next_link(),
            'previous_page': paginator.get_previous_link(),
            'count': paginator.page.paginator.count,
            'results': serializer.data
        }
        return Response(response_data)
