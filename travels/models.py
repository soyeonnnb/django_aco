from django.db import models

# Create your models here.
class Travel(models.Model):

    """Travel Model Definition 여행지 모델"""

    name = models.CharField(max_length=100)  # 이름
    start_date = models.DateField()  # 여행 시작 날짜
    end_date = models.DateField()  # 여행 종료 날짜
    created_at = models.DateField(auto_now_add=True)  # 생성 날짜
    updated_at = models.DateField(auto_now=True)  # 수정 날짜
    color = models.CharField(max_length=20)  # 고유색


class Place(models.Model):

    """Place Model Definition 여행장소 모델"""

    travel = models.ForeignKey(
        Travel, on_delete=models.CASCADE, related_name="place"
    )  # 여행
    name = models.CharField(max_length=100)  # 장소명
    day = models.IntegerField()  # 장소 여행 날짜
    order = models.IntegerField()  # 장소 방문 순서
    latitude = models.FloatField()  # 위도(x)
    longitude = models.FloatField()  # 경도(y)
    created_at = models.DateField(auto_now_add=True)  # 생성 날짜
    updated_at = models.DateField(auto_now=True)  # 수정 날짜


class Lodging(models.Model):

    """Lodging Model Definition 숙소 모델"""

    travel = models.ForeignKey(
        Travel, on_delete=models.CASCADE, related_name="lodging"
    )  # 여행
    name = models.CharField(max_length=100)  # 숙소명
    latitude = models.FloatField()  # 위도(x)
    longitude = models.FloatField()  # 경도(y)
    created_at = models.DateField(auto_now_add=True)  # 생성 날짜
    updated_at = models.DateField(auto_now=True)  # 수정 날짜
