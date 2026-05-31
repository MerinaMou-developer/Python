from rest_framework import serializers

# serializers
class BookingSerializers(serializers.serializer):
    guests=serializers.IntegerField()
    def validate_guest(self,value):
        if value<=0:
            raise serializers.ValidationError("Guests must be greater than 0")
        
        return value


# Model serializers
class BookingSerializers(serializers.ModelSerializer):
    class Meta:
        model=Booking
        fileds=['guests','check_in','check_out','room']

    # filed level validation

    def validate_guests(self,value):
        if value<=0:
            raise serializers.ValidationError("Guests must be greater than 0")
        
        return value
    
    # multiple filed validation

    def validate(self,data):
        if data["check_in"]>=data["check_out"]:
            raise serializers.ValidationError("check-in must be before checkout")
        
        return data