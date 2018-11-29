from django.db import models
from decimal import Decimal
from datetime import datetime

class Listing(models.Model):
    """
    model representing a house rental listing

    """
    created = models.DateTimeField(auto_now_add=True)
    area_unit = models.CharField(max_length=10, null=True, default='')
    bathrooms = models.DecimalField(max_digits=4, decimal_places=1, null=True)
    bedrooms = models.PositiveIntegerField(null=True)
    home_size = models.PositiveIntegerField(null=True)
    home_type = models.CharField(max_length=100, null=True, default='')
    last_sold_date = models.DateField(null=True)
    last_sold_price = models.PositiveIntegerField(null=True)
    link = models.CharField(max_length=100, null=True, default='')
    price = models.PositiveIntegerField(null=True)
    property_size = models.PositiveIntegerField(null=True)
    rent_price = models.PositiveIntegerField(null=True)
    rentzestimate_amount = models.PositiveIntegerField(null=True)
    rentzestimate_last_updated = models.DateField(null=True)
    tax_value = models.PositiveIntegerField(null=True)
    tax_year = models.PositiveIntegerField(null=True)
    year_built = models.PositiveIntegerField(null=True)
    zestimate_amount = models.PositiveIntegerField(null=True)
    zestimate_last_updated = models.DateField(null=True)
    zillow_id = models.PositiveIntegerField(null=True)
    address = models.CharField(max_length=100, null=True, default='')
    city = models.CharField(max_length=100, null=True, default='')
    state = models.CharField(max_length=2, null=True, default='')
    zipcode = models.CharField(max_length=10, null=True, default='')

    class Meta:
        ordering = ('created',)

    def from_csv_row(self, headers, row):
        """
        populate a listing object from a csv row
    
        :param headers: array of csv headers
        :param row:     array representing one row of a csv
        :returns self: self
        """

        name_to_value_dict = {key:value for key, value in zip(headers, row)}
        # convert row and headers to dict and set fields
        
        if 'bathrooms' in name_to_value_dict and name_to_value_dict['bathrooms']:
            self.bathrooms = Decimal(name_to_value_dict['bathrooms'])
        if 'bedrooms' in name_to_value_dict and name_to_value_dict['bedrooms']:
            self.bedrooms = int(name_to_value_dict['bedrooms'])
        if 'home_size' in name_to_value_dict and name_to_value_dict['home_size']:
            self.home_size = int(name_to_value_dict['home_size'])
        if 'last_sold_price' in name_to_value_dict and name_to_value_dict['last_sold_price']:
            self.last_sold_price = int(name_to_value_dict['last_sold_price'])
        if 'price' in name_to_value_dict and name_to_value_dict['price']:
            multiplier = name_to_value_dict['price'][-1]
            price = name_to_value_dict['price'][1:-1]
            self.price = int(float(price)* 1000 if multiplier == 'K' else 1000000)
        if 'property_size' in name_to_value_dict and name_to_value_dict['property_size']:
            self.property_size = int(name_to_value_dict['property_size'])
        if 'rent_price' in name_to_value_dict and name_to_value_dict['rent_price']:
            self.rent_price = int(name_to_value_dict['rent_price'])
        if 'rentzestimate_amount' in name_to_value_dict and name_to_value_dict['rentzestimate_amount']:
            self.rentzestimate_amount = int(name_to_value_dict['rentzestimate_amount'])
        if 'tax_value' in name_to_value_dict and name_to_value_dict['tax_value']:
            self.tax_value = int(name_to_value_dict['tax_value'])
        if 'tax_year' in name_to_value_dict and name_to_value_dict['tax_year']:
            self.tax_year = int(name_to_value_dict['tax_year'])
        if 'year_built' in name_to_value_dict and name_to_value_dict['year_built']:
            self.year_built = int(name_to_value_dict['year_built'])
        if 'zestimate_amount' in name_to_value_dict and name_to_value_dict['zestimate_amount']:
            self.zestimate_amount = int(name_to_value_dict['zestimate_amount'])
        if 'zestimate_last_updated' in name_to_value_dict and name_to_value_dict['zestimate_last_updated']:
            self.zestimate_last_updated = datetime.strptime(name_to_value_dict['zestimate_last_updated'], "%m/%d/%Y").date()
        if 'last_sold_date' in name_to_value_dict and name_to_value_dict['last_sold_date']:
            self.last_sold_date = datetime.strptime(name_to_value_dict['last_sold_date'], "%m/%d/%Y").date()
        if 'rentzestimate_last_updated' in name_to_value_dict and name_to_value_dict['rentzestimate_last_updated']:
            self.rentzestimate_last_updated = datetime.strptime(name_to_value_dict['rentzestimate_last_updated'], "%m/%d/%Y").date()
        if 'zillow_id' in name_to_value_dict:
            self.zillow_id = name_to_value_dict['zillow_id']
        if 'address' in name_to_value_dict:
            self.address = name_to_value_dict['address']
        if 'city' in name_to_value_dict:
            self.city = name_to_value_dict['city']
        if 'state' in name_to_value_dict:
            self.state = name_to_value_dict['state']
        if 'zipcode' in name_to_value_dict:
            self.zipcode = name_to_value_dict['zipcode']
        if 'area_unit' in name_to_value_dict:
            self.area_unit = name_to_value_dict['area_unit']
        if 'link' in name_to_value_dict:
            self.link = name_to_value_dict['link']
        if 'home_type' in name_to_value_dict:
            self.home_type = name_to_value_dict['home_type']
    
        return self;
    

