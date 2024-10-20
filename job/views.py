from django.shortcuts import render
from rest_framework import viewsets, status

# from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action, permission_classes
from rest_framework.response import Response
from .models import Jobs
from core.CustomPagination import CustomPagination
from core.response import CustomResponse
from .serializers import *


# Create your views here.
class JobsViewSet(viewsets.ModelViewSet):
    queryset = Jobs.objects.filter(job_status=Jobs.PUBLISHED)
    serializer_class = JobsSerializer
    search_fields = ["country__country", "jobtitle"]
    filterset_fields = ["country"]

    def list(self, request, *args, **kwargs):
        response = CustomResponse()
        queryset = self.filter_queryset(self.get_queryset())
        paginator = CustomPagination()
        paginated_queryset = paginator.paginate_queryset(queryset, request)
        serializer = self.get_serializer(paginated_queryset, many=True)
        response_data = {
            "next_page": paginator.get_next_link(),
            "previous_page": paginator.get_previous_link(),
            "count": paginator.page.paginator.count,
            "results": serializer.data,
        }
        if queryset:
            return Response(
                response.successResponse("data view", response_data),
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                response.errorResponse("No data found"),
                status=status.HTTP_404_NOT_FOUND,
            )

    # @action(detail=True, methods=['post'])
    # # @permission_classes([IsAuthenticated])
    # def apply(self, request, pk=None):
    #     job = self.get_object()
    #     serializer = JobApplicationSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save(job=job)  # Link the application to the logged-in user
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class JobApplicationViewSet(viewsets.ModelViewSet):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer
