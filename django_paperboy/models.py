from django.db import models
from math import floor


class Paperboy(models.Model):
    name = models.CharField(max_length=255)
    experience = models.IntegerField()
    earnings = models.FloatField()

    def __str__(self):
        return "This paperboy is named {}. He has delivered {} papers and earned ${:.2f}.".format(self.name, self.experience, self.earnings)

    def quota(self):
        return floor(self.experience * 0.5 + 50)

    def report(self):
        return "Look at me! I'm {} and I've delivered {} papers so far. They've paid me ${:.2f} for this, can you believe it?!".format(self.name, self.experience, self.earnings)

    @classmethod
    def total_delivered(cls):
        total = 0
        paperboys = cls.objects.all()
        for boy in paperboys:
            total += boy.experience
        return total

    @classmethod
    def total_earned(cls):
        total = 0
        paperboys = cls.objects.all()
        for boy in paperboys:
            total += boy.earnings
        return total

    def deliver(self, start_address, end_address):
        start = min(start_address, end_address)
        end = max(start_address, end_address)
        total_houses = end - start + 1
        curr_quota = self.quota()
        if total_houses == curr_quota:
            earned = (0.25 * total_houses)
        elif total_houses < curr_quota:
            earned = (0.25 * total_houses) - 2
        elif total_houses > curr_quota:
            earned = (0.25 * curr_quota) + (0.50 * (total_houses-curr_quota))
        self.experience += total_houses
        self.earnings += earned
        self.save()
        return earned
