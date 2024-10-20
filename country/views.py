from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from core.CustomPagination import CustomPagination
from core.response import CustomResponse
from .serializers import *
from .models import *


# Create your views here.
class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    search_fields = ['country']
    # def list (self, request, *args, **kwargs):
    #     response = CustomResponse()
    #     queryset = self.filter_queryset(self.get_queryset())
    #     paginator = CustomPagination()
    #     paginated_queryset = paginator.paginate_queryset(queryset, request)
    #     serializer = self.get_serializer(paginated_queryset, many=True)
    #     response_data = {
    #         'next_page': paginator.get_next_link(),
    #         'previous_page': paginator.get_previous_link(),
    #         'count': paginator.page.paginator.count,
    #         'results': serializer.data
    #     }
    #     if queryset:
    #         return Response(response.successResponse('data view', response_data), status=status.HTTP_200_OK)
    #     else:
    #         return Response(response.errorResponse('No data found'), status=status.HTTP_404_NOT_FOUND)

