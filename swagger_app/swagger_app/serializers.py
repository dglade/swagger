from rest_framework import serializers
from swagger_app.models import Plot, Plant, Harvest


class PlotSerializer(serializers.Serializer):
    x_coord = serializers.IntegerField()
    y_coord = serializers.IntegerField()
    plot_number = serializers.IntegerField()

    def create(self, validated_data):
        plot = Plot.objects.update_or_create(**validated_data)[0]
        return plot

    def update(self, instance, validated_data):
        instance.x_coord = validated_data.get('x_coord',
                                              instance.x_coord)
        instance.y_coord = validated_data.get('y_coord',
                                              instance.y_coord)
        instance.plot_number = validated_data.get('plot_number',
                                                  instance.plot_number)
        instance.save()
        return instance


class PlantSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    zone = serializers.IntegerField()
    plot = PlotSerializer()

    def create(self, validated_data):
        plot_data = validated_data.pop('plot')
        plot = Plot.objects.update_or_create(**plot_data)[0]
        plant = Plant.objects.update_or_create(plot=plot,
                                               **validated_data)[0]
        return plant

    def update(self, instance, validated_data):
        plot_data = validated_data.pop('plot')
        plot = instance.plot

        instance.name = validated_data.get('name',
                                           instance.name)
        instance.zone = validated_data.get('zone',
                                           instance.zone)
        instance.save()

        plot.x_coord = plot_data.get('x_coord', plot.x_coord)
        plot.y_coord = plot_data.get('y_coord', plot.y_coord)
        plot.plot_number = plot_data.get('plot_number',
                                         plot.plot_number)
        plot.save()
        return instance


class HarvestSerializer(serializers.Serializer):
    harvest_date = serializers.DateField()
    amount = serializers.IntegerField()
    plant = PlantSerializer()

    class __meta__:
        depth = 2


    def create(self, validated_data):
        plant_data = validated_data.pop('plant')
        plot_data = plant_data.pop('plot')
        plot = Plot.objects.update_or_create(**plot_data)[0]
        plant = Plant.objects.update_or_create(plot=plot, **plant_data)[0]
        harvest = Harvest.objects.update_or_create(plant=plant,
                                                   **validated_data)[0]
        return harvest

    def update(self, instance, validated_data):
        plant_data = validated_data.pop('plant')
        plot_data = plant_data.pop('plot')
        plant = instance.plant
        plot = plant.plot

        instance.harvest_date = validated_data.get('harvest_date',
                                                   instance.harvest_date)
        instance.amount = validated_data.get('amount',
                                             instance.amount)
        instance.save()

        plant.name = plant_data.get('name', plant.name)
        plant.zone = plant_data.get('zone', plant.zone)
        plant.save()

        plot.x_coord = plot_data.get('x_coord', plot.x_coord)
        plot.y_coord = plot_data.get('y_coord', plot.y_coord)
        plot.plot_number = plot_data.get('plot_number',
                                         plot.plot_number)
        plot.save()
        return instance

