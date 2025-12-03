from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import date

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')

        # Users
        users = [
            User(name='Peter Parker', email='peter@marvel.com', team='Marvel', is_superhero=True),
            User(name='Tony Stark', email='tony@marvel.com', team='Marvel', is_superhero=True),
            User(name='Bruce Wayne', email='bruce@dc.com', team='DC', is_superhero=True),
            User(name='Clark Kent', email='clark@dc.com', team='DC', is_superhero=True),
        ]
        for user in users:
            user.save()

        # Activities
        Activity.objects.create(user='Peter Parker', type='Running', duration=30, points=10, date=date.today())
        Activity.objects.create(user='Tony Stark', type='Cycling', duration=45, points=15, date=date.today())
        Activity.objects.create(user='Bruce Wayne', type='Swimming', duration=60, points=20, date=date.today())
        Activity.objects.create(user='Clark Kent', type='Strength', duration=40, points=12, date=date.today())

        # Leaderboard
        Leaderboard.objects.create(team='Marvel', points=25, rank=1)
        Leaderboard.objects.create(team='DC', points=32, rank=1)

        # Workouts
        Workout.objects.create(name='Pushups', description='Upper body', difficulty='Easy')
        Workout.objects.create(name='Sprints', description='Cardio', difficulty='Medium')
        Workout.objects.create(name='Deadlift', description='Strength', difficulty='Hard')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
