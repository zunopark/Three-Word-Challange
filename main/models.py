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
        ('Afghanistan', '아프가니스탄'),
        ('Albania', '알바니아'),
        ('Algeria', '알제리아'),
        ('Andorra', '안도라')
    )
# Angola
# Antigua and Barbuda
# Argentina
# Armenia
# Australia
# Austria
# Azerbaijan
# Bahamas
# Bahrain
# Bangladesh
# Barbados
# Belarus
# Belgium
# Belize
# Benin
# Bhutan
# Bolivia
# Bosnia and Herzegovina
# Botswana
# Brazil
# Brunei
# Bulgaria
# Burkina Faso
# Burundi
# Cabo Verde
# Cambodia
# Cameroon
# Canada
# Central African Republic (CAR)
# Chad
# Chile
# China
# Colombia
# Comoros
# Congo, Democratic Republic of the
# Congo, Republic of the
# Costa Rica
# Cote d'Ivoire
# Croatia
# Cuba
# Cyprus
# Czechia
# Denmark
# Djibouti
# Dominica
# Dominican Republic
# Ecuador
# Egypt
# El Salvador
# Equatorial Guinea
# Eritrea
# Estonia
# Eswatini
# Ethiopia
# Fiji
# Finland
# France
# Gabon
# Gambia
# Georgia
# Germany
# Ghana
# Greece
# Grenada
# Guatemala
# Guinea
# Guinea-Bissau
# Guyana
# Haiti
# Honduras
# Hungary
# Iceland
# India
# Indonesia
# Iran
# Iraq
# Ireland
# Israel
# Italy
# Jamaica
# Japan
# Jordan
# Kazakhstan
# Kenya
# Kiribati
# Kosovo
# Kuwait
# Kyrgyzstan
# Laos
# Latvia
# Lebanon
# Lesotho
# Liberia
# Libya
# Liechtenstein
# Lithuania
# Luxembourg
# Madagascar
# Malawi
# Malaysia
# Maldives
# Mali
# Malta
# Marshall Islands
# Mauritania
# Mauritius
# Mexico
# Micronesia
# Moldova
# Monaco
# Mongolia
# Montenegro
# Morocco
# Mozambique
# Myanmar
# Namibia
# Nauru
# Nepal
# Netherlands
# New Zealand
# Nicaragua
# Niger
# Nigeria
# North Korea
# North Macedonia (formerly Macedonia)
# Norway
# Oman
# Pakistan
# Palau
# Palestine
# Panama
# Papua New Guinea
# Paraguay
# Peru
# Philippines
# Poland
# Portugal
# Qatar
# Romania
# Russia
# Rwanda
# Saint Kitts and Nevis
# Saint Lucia
# Saint Vincent and the Grenadines
# Samoa
# San Marino
# Sao Tome and Principe
# Saudi Arabia
# Senegal
# Serbia
# Seychelles
# Sierra Leone
# Singapore
# Slovakia
# Slovenia
# Solomon Islands
# Somalia
# South Africa
# South Korea
# South Sudan
# Spain
# Sri Lanka
# Sudan
# Suriname
# Sweden
# Switzerland
# Syria
# Taiwan
# Tajikistan
# Tanzania
# Thailand
# Timor-Leste
# Togo
# Tonga
# Trinidad and Tobago
# Tunisia
# Turkey
# Turkmenistan
# Tuvalu
# Uganda
# Ukraine
# United Arab Emirates (UAE)
# United Kingdom (UK)
# United States of America (USA)
# Uruguay
# Uzbekistan
# Vanuatu
# Vatican City (Holy See)
# Venezuela
# Vietnam
# Yemen
# Zambia
# Zimbabwe

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