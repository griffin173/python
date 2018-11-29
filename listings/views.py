from listings.models import Listing
from listings.serializers import ListingSerializer
from listings.filters import ListingFilter
from rest_framework import generics, views
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.parsers import FileUploadParser
from django_filters import rest_framework as filters
from io import TextIOWrapper
import csv

class ListingList(generics.ListCreateAPIView):
    """
    API endpoint for querying/creating Listings, get, post
    """
    serializer_class = ListingSerializer
    queryset = Listing.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ListingFilter

class ListingDetail(generics.RetrieveUpdateAPIView):
    """
    API endpoint for a single listing, get, put, and patch

    """
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

class ImportView(views.APIView):

    parser_classes = (FileUploadParser,)

    def post(self, request, filename, format=None):
        """
        accepts a CSV file and translates each row into a Listing and saves it

        """
        file_obj = request.data['file']
        text = TextIOWrapper(request.FILES['file'].file, encoding='utf-8 ', errors='replace')
        csv_reader = csv.reader(text, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                headers = row
                line_count += 1
            else:
                listing = Listing()
                listing.from_csv_row(headers,row)
                
                listing.save();
                line_count += 1
        return Response(status=200)