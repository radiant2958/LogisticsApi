# from django.db.models.signals import post_migrate
# from django.dispatch import receiver
# from django.conf import settings
# import os

# @receiver(post_migrate)
# def populate_models(sender, **kwargs):
#     from logistics.models import Initialization, Location
#     from logistics.management.commands.utils import load_data_from_csv, create_vehicles_with_random_location

#     app_label = sender.label
#     if app_label == 'logistics':
#         try:
#             init, created = Initialization.objects.get_or_create(id=1)
#             if not init.data_loaded:
#                 file_path = os.path.join(settings.BASE_DIR, 'uszips.csv')
#                 load_data_from_csv(file_path)
#                 init.data_loaded = True
#                 init.save()

#             if not init.vehicles_created:
#                 create_vehicles_with_random_location(20)
#                 init.vehicles_created = True
#                 init.save()
#         except Exception as e:
#             print("Error populating models:", e)
