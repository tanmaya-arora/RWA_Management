from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from .models import City, Committee, Country, Society, State, Package, Package_Category, Cart, Event 
from marketing.models import Campaign
from user_management.models import Owner, Tenant, FamilyMember
from support.models import Ticket
from reporting.models import ProductStock, SaleHistory
from internal.models import Order

class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = '__all__'


class CommitteeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Committee
        fields = '__all__'


class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = '__all__'


class CampaignSerializer(serializers.ModelSerializer):

    class Meta:
        model = Campaign
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class FamilyMemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = FamilyMember
        fields = '__all__'


class MemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = Owner
        fields = '__all__'

class TenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        fields = '__all__'
    

class SocietySerializer(serializers.ModelSerializer):

    class Meta:
        model = Society
        fields = '__all__'


class StateSerializer(serializers.ModelSerializer):

    class Meta:
        model = State
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    # name = serializers.SerializerMethodField(read_only=True)
    # _id = serializers.SerializerMethodField(read_only=True)
    # is_admin = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = '__all__'

    # def get_is_admin(self, obj):
    #     return obj.is_staff

    # def get__id(self, obj):  # double underscore, because i use '_id' in models
    #     return obj.id

    # def get_name(self, obj):
    #     name = obj.first_name
    #     if name == '':
    #         name = obj.email
    #     return name
    

class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', '_id', 'username',
                  'email', 'name', 'is_admin', 'token', 'is_verified']

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)


class PackageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Package
        fields = '__all__'


class PackageCategoriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Package_Category
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = '__all__'

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductStock
        fields = '__all__'

class SaleHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleHistory
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'