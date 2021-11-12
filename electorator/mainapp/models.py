from datetime import datetime

from django.db import models
from django.db.models import Model


class Tik(Model):
    num_tik = models.CharField(
        verbose_name='Номер ТИК',
        max_length=200,
        default='0'
    )
    population = models.IntegerField(
        verbose_name='Численность',
        default=0
    )
    open_uik = models.IntegerField(
        verbose_name='Число открытых участков',
        default=0
    )
    sum_votes = models.IntegerField(
        verbose_name='Общее число голосов',
        default=0
    )
    sum_numb_votes_fin = models.IntegerField(
        verbose_name='Общее число бюллетеней обработанное',
        default=0
    )
    presence = models.IntegerField(
        verbose_name='Явка',
        default=0
    )
    perc_final_bul = models.IntegerField(
        verbose_name='Процент обработанных бюллетеней',
        default=0
    )
    bad_form = models.IntegerField(
        verbose_name='Общее число испорченных бланков',
        default=0
    )
    update_time = models.TimeField(
        verbose_name='Время последнего изменени',
        auto_now=True
    )


class Uik(Model):
    num_uik = models.IntegerField(
        verbose_name='Номер участка',
        unique=True
    )
    num_tik = models.CharField(
        verbose_name='Номер ТИК',
        max_length=200,
        default='0'
    )
    population = models.IntegerField(
        verbose_name='Численность'
    )
    status = models.BooleanField(
        verbose_name='Статус'
    )
    sum_votes = models.IntegerField(
        verbose_name='Общее число голосов',
        default=0
    )
    sum_numb_votes_fin = models.IntegerField(
        verbose_name='Общее число голосов обработанное',
        default=0
    )
    presence = models.IntegerField(
        verbose_name='Явка',
        default=0
    )
    perc_final_bul = models.IntegerField(
        verbose_name='Процент обработанных бюллетеней',
        default=0
    )
    bad_form = models.IntegerField(
        verbose_name='Общее число испорченных бланков',
        default=0
    )
    update_time = models.TimeField(
        verbose_name='Время последнего изменени',
        auto_now=True
    )



class Candidate(Model):
    name = models.CharField(
        verbose_name='ФИО кандидата',
        max_length=200,
        unique=True
    )
    party = models.CharField(
        verbose_name='Партия',
        max_length=200
    )
    info = models.TextField(
        verbose_name='Инфо о кандидате'
    )
    sum_votes = models.IntegerField(
        verbose_name='Общее число голосов',
        default=0
    )
    photo = models.ImageField(
        verbose_name='Фото',
        upload_to='media/'
    )
    birthday = models.DateField(
        verbose_name='Дата рождения',
        blank=True,
        default=datetime.now()
    )
    birthday_place=models.CharField(
        verbose_name='Место рождения',
        max_length=100,
        blank=True

    )
    education=models.CharField(
        verbose_name='Образование',
        max_length=200,
        blank=True
    )
    work=models.CharField(
        verbose_name='Место работы',
        max_length=200,
        blank=True
    )
    position=models.CharField(
        verbose_name='Должность',
        max_length=200,
        blank=True
    )
    polit_position=models.CharField(
        verbose_name='Политическая дожность',
        max_length=200,
        blank=True
    )


class Protocol1(Model):
    num_protocol_1 = models.IntegerField(
        verbose_name='Номер протокола 1го типа',
        default=0
    )
    num_uik = models.ForeignKey(
        Uik,
        verbose_name='Номер участка',
        on_delete=models.CASCADE
    )
    status = models.BooleanField(
        verbose_name='Статус',
        default=False
    )
    sum_bul = models.IntegerField(
        verbose_name='Число полученных бюллетеней',
        default=0
    )
    sum_final_bul = models.IntegerField(
        verbose_name='Число обработаных бюллетеней',
        default=0
    )
    bad_form = models.IntegerField(
        verbose_name='Общее число испорченных бланков',
        default=0
    )
    transfer_time = models.TimeField(
        verbose_name='Время передачи протокола',
        auto_now=True
    )


class Protocol2(Model):
    num_protocol_2 = models.IntegerField(
        verbose_name='Номер протокола 2го типа',
        default=0
    )
    num_uik = models.ForeignKey(
        Uik,
        verbose_name='Номер участка',
        on_delete=models.CASCADE
    )
    name = models.ForeignKey(
        Candidate, on_delete=models.CASCADE
    )
    candidate_votes = models.IntegerField(
        verbose_name='Число голосов за кандидата'
    )
    transfer_time = models.TimeField(
        verbose_name='Время передачи протокола',
        auto_now=True
    )


class UikCandidate(Model):
    id_uik = models.ForeignKey(Uik, on_delete=models.CASCADE)
    id_candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)


class UikProtocol1(Model):
    id_uik = models.ForeignKey(Uik, on_delete=models.CASCADE)
    id_protocol1 = models.ForeignKey(Protocol1, on_delete=models.CASCADE)
