from django.db import models

class reservation_list(models.Model):
    name = models.CharField(max_length=32)
    company = models.CharField(max_length=32)
    phone = models.CharField(max_length=32)
    QQ = models.CharField(max_length=32)
    WeChat = models.CharField(max_length=32)
    address = models.CharField(max_length=32)
    time = models.CharField(max_length=32)
    service = models.CharField(max_length=32)
    os_version = models.CharField(max_length=32)
    formating = models.CharField(max_length=32)
    software = models.CharField(max_length=32)
    update = models.CharField(max_length=32)

class register_list(models.Model):
    s_id = models.CharField(max_length=32)
    name = models.CharField(max_length=32)
    college = models.CharField(max_length=32)  # 学院
    campus = models.CharField(max_length=32)   # 校区
    received_list = models.CharField(max_length=32)


class seekHelp_list(models.Model):
    s_id = models.CharField(max_length=32)
    version = models.CharField(max_length=32)  # 0/1/2,表示帖子还是评论，还是评论的回复
    content = models.CharField(max_length=32)
    discuss_list = models.CharField(max_length=32)


class watchHour_list(models.Model):
    s_id_list = models.CharField(max_length=32)
    odd_or_even = models.CharField(max_length=32)  # 单双周
    week = models.CharField(max_length=32)  # 星期几
    time_slot = models.CharField(max_length=32)  # 时间段

