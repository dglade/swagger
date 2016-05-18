from django.db import models


class Plot(models.Model):
    x_coord = models.IntegerField()
    y_coord = models.IntegerField()
    plot_number = models.IntegerField()

#    def __str__(self):
#        return 'Plot %(plot)s - (%(x)s, %(y)s)' % {'plot': self.plot_number,
#                                                  'x': self.x_coord,
#                                                  'y': self.y_coord}


class Plant(models.Model):
    name = models.CharField(max_length=30)
    zone = models.IntegerField()
    plot = models.ForeignKey(Plot,
                             on_delete=models.CASCADE,
                             related_name='plant')

    def __str__(self):
        return '%(name)s' % {'name': self.name}


class Harvest(models.Model):
    harvest_date = models.DateField()
    amount = models.IntegerField()
    plant = models.ForeignKey(Plant,
                              on_delete=models.CASCADE,
                              related_name='harvests')

#    def __str__(self):
#        return '%(date)s - amount %(amount)s' % {'date': self.harvest_date,
#                                                 'amount': self.amount}


