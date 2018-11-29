from listings.models import Listing
from django_filters import rest_framework as filters

class ListingFilter(filters.FilterSet):
    """
    querying filters for Listing search
    """
    min_size = filters.NumberFilter(field_name="home_size", lookup_expr='gte')
    max_size = filters.NumberFilter(field_name="home_size", lookup_expr='lte')
    min_sold_price = filters.NumberFilter(field_name="last_sold_price", lookup_expr='gte')
    max_sold_price = filters.NumberFilter(field_name="last_sold_price", lookup_expr='lte')
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')
    min_rent_price = filters.NumberFilter(field_name="rent_price", lookup_expr='gte')
    max_rent_price = filters.NumberFilter(field_name="rent_price", lookup_expr='lte')
    min_property_size = filters.NumberFilter(field_name="property_size", lookup_expr='gte')
    max_property_size = filters.NumberFilter(field_name="property_size", lookup_expr='lte')
    min_rentzestimate_amount = filters.NumberFilter(field_name="rentzestimate_amount", lookup_expr='gte')
    max_rentzestimate_amount = filters.NumberFilter(field_name="rentzestimate_amount", lookup_expr='lte')
    min_tax_value = filters.NumberFilter(field_name="tax_value", lookup_expr='gte')
    max_tax_value = filters.NumberFilter(field_name="tax_value", lookup_expr='lte')
    min_tax_year = filters.NumberFilter(field_name="tax_year", lookup_expr='gte')
    min_year_built = filters.NumberFilter(field_name="year_built", lookup_expr='gte')
    max_year_built = filters.NumberFilter(field_name="year_built", lookup_expr='lte')
    min_zestimate_amount = filters.NumberFilter(field_name="zestimate_amount", lookup_expr='gte')
    max_zestimate_amount = filters.NumberFilter(field_name="zestimate_amount", lookup_expr='lte')
    bedrooms = filters.NumberFilter(field_name="bedrooms")
    min_bedrooms = filters.NumberFilter(field_name="bedrooms", lookup_expr='gte')
    max_bedrooms = filters.NumberFilter(field_name="bedrooms", lookup_expr='lte')
    bathrooms = filters.NumberFilter(field_name="bathrooms")
    min_bathrooms = filters.NumberFilter(field_name="bathrooms", lookup_expr='gte')
    max_bathrooms = filters.NumberFilter(field_name="bathrooms", lookup_expr='lte')
    city = filters.CharFilter(field_name="city", lookup_expr='iexact')
    address = filters.CharFilter(field_name="address", lookup_expr='iexact')
    min_last_sold_date = filters.DateFilter(field_name="last_sold_date", lookup_expr='gte')
    max_last_sold_date = filters.DateFilter(field_name="last_sold_date", lookup_expr='lte')


    class Meta:
        model = Listing
        fields = [
            'address', 'zipcode', 'area_unit', 'home_type', 'link', 'city', 'state', 'bedrooms', 'min_bedrooms', 'max_bedrooms', 'zillow_id', 
            'min_size', 'max_size', 'min_sold_price', 'max_sold_price', 'min_price', 'max_price', 'min_rent_price', 'max_rent_price',
            'min_property_size', 'max_property_size', 'min_rentzestimate_amount', 'max_rentzestimate_amount', 'min_tax_value',
            'max_tax_value', 'min_tax_year', 'min_year_built', 'max_year_built', 'min_zestimate_amount', 'max_zestimate_amount',
            'bathrooms', 'min_bathrooms', 'max_bathrooms'
        ]