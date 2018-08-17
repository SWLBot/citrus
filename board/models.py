from django.db import models

# id field will be automatically generated, which is also the primary key
# of that table

# can add verbose_name to give every column a human-redable name(but English
# or Chinese?)

class User_account(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    authority_level = models.IntegerField(default=0)
    account_status = models.BooleanField(default=False)

class User_profile(models.Model):
    user_id = models.ForeignKey(User_account, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

class Schedule(models.Model):
    sche_type_choices = (
        ('TEXT', '文字'),
        ('IMAGE', '圖片')
    )
    sche_type = models.CharField(max_length=5, choices=sche_type_choices)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    duration = models.IntegerField(default=5)
    count = models.IntegerField(default=0)
    upload_time = models.DateTimeField()
    # related_name: 
    # The name to use for the relation from the related object back to this one.
    # below related_name is from `User_account` to `Schedule`
    upload_user = models.ForeignKey(User_account, 
        on_delete=models.CASCADE, related_name="upload_schedule")
    last_edit_user = models.ForeignKey(User_account, 
        on_delete=models.SET_NULL, null=True, related_name="last_edit_schedule")
