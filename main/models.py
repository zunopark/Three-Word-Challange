from django.db import models

class PageCounter(models.Model):
    objects = models.Manager()
    count = models.IntegerField(verbose_name="방문자수")


# 나라별 검색 및 총 좋아요 랭킹
class Nation(models.Model):
    nation_list = (
        ('Afghanistan', '아프가니스탄'),
        ('Albania', '알바니아'),
        ('Algeria', '알제리아'),
        ('Andorra', '안도라'),
        ('Angola', '앙골라'),
        ('Antigua and Barbuda', '안티구아 앤 발부다'),
        ('Argentina', '아르헨티나'),
        ('Armenia', '알메니아'),
        ('Australia', '호주'),
        ('Azerbaijan', '아제르바이젠'),
        ('Bahamas', '바하마스'),
        ('Bahrain', '바레인'),
        ('Bangladesh', '방글라데시'),
        ('Barbados', '바르바도'),
        ('Belarus', '벨라루스'),
        ('Belgium', '벨기에'),
        ('Belize', '베리즈'),
        ('Benin', '베닌'),
        ('Bhutan', '부탄'),
        ('Bolivia', '볼리비아'),
        ('Bosnia and Herzegovina', '보스니아 헤르체코비나'),
        ('Botswana', '보츠와나'),
        ('Brazil', '브라질'),
        ('Brunei', '브루네이'),
        ('Bulgaria', '불가리아'),
        ('Burkina Faso', '브루키나 파소'),
        ('Burundi', '부룬다이'),
        ('Cabo Verde', '카보 베르드'),
        ('Cambodia', '캄보디아'),
        ('Cameroon', '카메룬'),
        ('Canada', '캐나다'),
        ('Central African Republic (CAR)', '중앙 아프리카 공화국'),
        ('Chad', '차드'),
        ('Chile', '칠레'),
        ('China', '중국'),
        ('Colombia', '콜롬비아'),
        ('Comoros', '코모로스'),
        ('Congo, Democratic Republic of the', '콩고민주공화국'),
        ('Costa Rica', '코스타리카'),
        ("Cote d'Ivoire", '코트디부아르'),
        ('Croatia', '크로아티아'),
        ('Cuba', '쿠바'),
        ('Cyprus', '싸이프러스'),
        ('Czechia', '체코'),
        ('Denmark', '덴마크'),
        ('Djibouti', '지부티'),
        ('Dominica', '도미니카'),
        ('Dominican Republic', '도미니카 공화국'),
        ('Ecuador', '에콰도르'),
        ('Egypt', '이집트'),
        ('El Salvador', '엘 살바도르'),
        ('Equatorial Guinea', '적도 기니'),
        ('Eritrea', '에르트레아'),
        ('Estonia', '에스토니아'),
        ('Eswatini', '에스와티니'),
        ('Ethiopia', '에티오피아'),
        ('Fiji', '피지'),
        ('Finland', '핀란드'),
        ('France', '프랑스'),
        ('Gabon', '가봉'),
        ('Gambia', '감비아'),
        ('Georgia', '조지아'),
        ('Germany', '독일'),
        ('Ghana', '가나'),
        ('Greece', '그리스'),
        ('Grenada', '그레나다'),
        ('Guatemala', '과테말라'),
        ('Guinea', '기니'),
        ('Guinea-Bissau', '기니비사우'),
        ('Guyana', '구야나'),
        ('Haiti', '하이티'),
        ('Honduras', '온두라스'),
        ('Hungary', '헝가리'),
        ('Iceland', '아이스란드'),
        ('India', '인도'),
        ('Indonesia', '인도네시아'),
        ('Iran', '이란'),
        ('Iraq', '이라크'),
        ('Ireland', '아일랜드'),
        ('Israel', '이스라엘'),
        ('Italy', '이탈리아'),
        ('Jamaica', '자메이카'),
        ('Japan', '일본'),
        ('Jordan', '요르단'),
        ('Kazakhstan', '카자흐스탄'),
        ('Kenya', '케냐'),
        ('Kiribati', '키리바티'),
        ('Kosovo', '코소보'),
        ('Kuwait', '쿠웨이트'),
        ('Kyrgyzstan', '키르기스탄'),
        ('Laos', '라오스'),
        ('Latvia', '라트비아'),
        ('Lebanon', '레바논'),
        ('Lesotho', '레소토'),
        ('Liberia', '라이베리아'),
        ('Libya', '리비야'),
        ('Liechtenstein', '리히텐슈타인'),
        ('Lithuania', '리투아니아'),
        ('Luxembourg', '룩셈부르그'),
        ('Madagascar', '마다가스카르'),
        ('Malawi', '말라위'),
        ('Malaysia', '말레이시아'),
        ('Maldives', '말디브'),
        ('Mali', '말리'),
        ('Malta', '말타'),
        ('Marshall Islands', '마쉘 섬'),
        ('Mauritania', '마리타니아'),
        ('Mauritius', '마리티우스'),
        ('Mexico', '멕시코'),
        ('Micronesia', '미크로네시아'),
        ('Moldova', '몰도바'),
        ('Monaco', '모나코'),
        ('Mongolia', '몽골'),
        ('Montenegro', '몬테네그로'),
        ('Morocco', '모로코'),
        ('Mozambique', '모잠비크'),
        ('Myanmar', '마이안마르'),
        ('Namibia', '나미비아'),
        ('Nauru', '나우루'),
        ('Nepal', '네팔'),
        ('Netherlands', '네덜란드'),
        ('New Zealand', '뉴질랜드'),
        ('Nicaragua', '니카라구아'),
        ('Niger', '니게르'),
        ('Nigeria', '나이지리아'),
        ('North Korea', '북한'),
        ('North Macedonia', '북마케도니아'),
        ('Norway', '노르웨이'),
        ('Oman', '오만'),
        ('Pakistan', '파키스탄'),
        ('Palau', '팔라우'),
        ('Palestine', '팔레스타인'),
        ('Panama', '파나마'),
        ('Papua New Guinea', '파푸아 뉴기니'),
        ('Paraguay', '파라과이'),
        ('Peru', '페루'),
        ('Philippines', '필리핀'),
        ('Poland', '폴란드'),
        ('Portugal', '포르투갈'),
        ('Qatar', '카타르'),
        ('Romania', '루마니아'),
        ('Russia', '러시아'),
        ('Rwanda', '르완다'),
        ('Saint Kitts and Nevis', 'Saint Kitts and Nevis'),
        ('Saint Lucia', '세인트 루시아'),
        ('Saint Vincent and the Grenadines', 'Saint Vincent and the Grenadines'),
        ('Samoa', '사모아'),
        ('San Marino', '산 마리노'),
        ('Sao Tome and Principe', 'Sao Tome and Principe'),
        ('Saudi Arabia', '사우디 아라비아'),
        ('Senegal', '세네갈'),
        ('Serbia', '세르비아'),
        ('Seychelles', 'Seychelles'),
        ('Sierra Leone', 'Sierra Leone'),
        ('Singapore', '싱가포르'),
        ('Slovakia', '슬로바키아'),
        ('Slovenia', '슬로베니아'),
        ('Solomon Islands', '솔로몬 섬'),
        ('Somalia', '소말리아'),
        ('South Africa', '남아프리카'),
        ('South Korea', '한국'),
        ('South Sudan', '남수단'),
        ('Spain', '스페인'),
        ('Sri Lanka', '스리랑카'),
        ('Sudan', '수단'),
        ('Suriname', '수리남'),
        ('Sweden', '스웨덴'),
        ('Switzerland', '스위스랜드'),
        ('Syria', '시리아'),
        ('Taiwan', '대만'),
        ('Tajikistan', '타지키스탄'),
        ('Tanzania', '탄자니아'),
        ('Thailand', '태국'),
        ('Timor-Leste', '티모르 레스트'),
        ('Togo', '토고'),
        ('Tonga', '통가'),
        ('Trinidad and Tobago', '트리니다드 토바고'),
        ('Tunisia', '튀니시아'),
        ('Turkey', '터키'),
        ('Turkmenistan', '투르크메니스탄'),
        ('Tuvalu', '투발루'),
        ('Uganda', '우간다'),
        ('Ukraine', '우크라이나'),
        ('United Arab Emirates (UAE)', '아랍에미리트'),
        ('United Kingdom (UK)', '영국'),
        ('United States of America', '미국'),
        ('Uruguay', '우루과이'),
        ('Uzbekistan', '우즈베키스탄'),
        ('Vanuatu', '바누아투'),
        ('Vatican City', '바티칸'),
        ('Venezuela', '베네수엘라'),
        ('Vietnam', '베트남'),
        ('Yemen', '예맨'),
        ('Zambia', '잠비아'),
        ('Zimbabwe', '짐바브웨')
    )

    objects = models.Manager()
    name = models.CharField(max_length=100, choices=nation_list)

    # 나라 국기
    image = models.ImageField()

    # 국가 별 총 좋아요 수
    sum_of_like = models.IntegerField(default=0)

    # 총 post 개수
    total_post = models.IntegerField(default=0)

    # 총 포인트
    nation_point = models.IntegerField(default=0)

    def __str__(self):
        return self.name


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

    # 다른 제시어 표시 변수
    is_show = models.BooleanField(verbose_name="다른 제시어 표시 변수, 건드리지 말자", null=False, default=False)

    # 홈 화면 고정 변수
    today = models.BooleanField(verbose_name="오늘만 보이게 하려면 체크", null=False, default=False)

    # 제시어 제출 날짜
    release_date = models.DateTimeField()

    # 1,2,3 위의 국가
    first_nation = models.ForeignKey(Nation, on_delete=models.CASCADE, related_name="첫번째")
    second_nation = models.ForeignKey(Nation, on_delete=models.CASCADE, related_name="두번째")
    third_nation = models.ForeignKey(Nation, on_delete=models.CASCADE, related_name="세번째")


    def __str__(self):
        return self.name


class Post(models.Model):
    objects = models.Manager()
    keyword = models.ForeignKey(Keyword, on_delete=models.CASCADE)
    nation = models.ForeignKey(Nation, on_delete=models.CASCADE)

    nation_name = models.CharField(max_length=100, null=False)

    first = models.CharField(max_length=100, null=False)
    second = models.CharField(max_length=100, null=False)
    third = models.CharField(max_length=100, null=False)

    trans_1 = models.CharField(max_length=100, default="")
    trans_2 = models.CharField(max_length=100, default="")
    trans_3 = models.CharField(max_length=100, default="")

    nickname = models.CharField(max_length=100, null=False)
    
    # 날짜 시간까지
    release_date = models.DateTimeField(auto_now_add=True)

    # 각 게시글 당 좋아요 수
    num_of_like = models.IntegerField(default=0)


    # 각각의 번역
    is_trans = models.BooleanField(default=False)

    def __str__(self):
        return self.keyword.name