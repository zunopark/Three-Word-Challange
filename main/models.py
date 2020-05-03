from django.db import models


# 학습 추천을 위한 한국어 제시어.
class Keyword(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=50)
    translation = models.CharField(max_length=50)
    pronunciation = models.CharField(max_length=50)

    # write할때 제시어 설명
    explanation = models.CharField(max_length=100)

    # 제시어 별 총 좋아요 수
    sum_of_like = models.IntegerField(default=0)

    # 하루에 하나만 뽑기 위해
    is_show = models.BooleanField(verbose_name="오늘 표시할 것인가", null=False, default=False)

    # 제시어 제출 날짜
    release_date = models.DateTimeField()

    def __str__(self):
        return self.name


# 나라별 검색 및 총 좋아요 랭킹 구현 위해서.
class Nation(models.Model):
    nation_list = (
        ('한국', 'Korea'),
        ('일본', 'Japan'),
        ('중국', 'China'),
    )
    objects = models.Manager()
    name = models.CharField(max_length=100, choices=nation_list)

    # 나라 국기
    image = models.ImageField()

    # 국가 별 총 좋아요 수
    sum_of_like = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Post(models.Model):
    objects = models.Manager()
    keyword = models.ForeignKey(Keyword, on_delete=models.CASCADE)
    nation = models.ForeignKey(Nation, on_delete=models.CASCADE)

    first = models.CharField(max_length=100, null=False)
    first_translation = models.TextField(null=True, default="")
    second = models.CharField(max_length=100, null=False)
    second_translation = models.TextField(null=True, default="")
    third = models.CharField(max_length=100, null=False)
    third_translation = models.TextField(null=True, default="")
    
    # 날짜 시간까지
    release_date = models.DateTimeField(auto_now_add=True)

    # 각 게시글 당 좋아요 수
    num_of_like = models.IntegerField(default=0)

    def __str__(self):
        return self.keyword.name