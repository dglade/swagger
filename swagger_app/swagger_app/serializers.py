from rest_framework import serializers
from swagger_app.models import Plot, Plant, Harvest


class PlotSerializer(serializers.ModelSerializer):

    class Meta:
        model = Plot
        fields = ('plot_number', 'x_coord', 'y_coord')

#    def create(self, validated_data):
#        plants_data = validated_data.pop('plants')
#        plot = Plot.objects.create(**validated_data)
#        for plant_data in plants_data:
#            Plant.objects.create(plot=plot, **plant_data)
#        return plot


class PlantSerializer(serializers.ModelSerializer):
    plot = serializers.PrimaryKeyRelatedField(many=False, read_only=False, queryset=Plot.objects.all(), allow_null=False)

    class Meta:
        model = Plant
        fields = ('name', 'zone', 'plot')

#    def create(self, validated_data):
#        harvests_data = validated_data.pop('harvests')
#        plant = Plant.objects.create(**validated_data)
#        for harvest_data in harvests_data:
#            Harvest.objects.create(plant=plant, **harvest_data)


class HarvestSerializer(serializers.ModelSerializer):
    plant = serializers.PrimaryKeyRelatedField(many=False, read_only=False, queryset=Plant.objects.all(), allow_null=False)

    class Meta:
        model = Harvest
        fields = ('harvest_date', 'amount', 'plant')

