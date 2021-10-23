from django.db import models
from django.db.models import Model


class Uik(Model):  #Участки
    num_uik = models.IntegerField(
        verbose_name='Номер участка',
        unique=True
    )
    population = models.IntegerField(
        verbose_name='Численность'
    )
    status = models.BooleanField(
        verbose_name='Статус'
    )
    sum_votes = models.IntegerField(
        verbose_name='Общее число голосов'
    )
    sum_numb_votes_fin = models.IntegerField(
        verbose_name='Общее число голосов обработанное'
    )
    presence = models.IntegerField (
        verbose_name='Явка'
    )
    perc_final_bul = models.IntegerField(
        verbose_name='Процент обработанных бюллетеней'
    )
    bad_form = models.IntegerField(
        verbose_name='Общее число испорченных бланков'
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
    info = models.TextField(
        verbose_name='Инфо о кандидате'
    )
    sum_votes = models.IntegerField(
        verbose_name='Общее число голосов'
    )


class Protocol1(Model):
    num_protocol_1 = models.IntegerField(
        verbose_name='Номер протокола 1го типа',
    )
    num_uik = models.IntegerField(
        verbose_name='Номер участка'
    )
    status = models.BooleanField(
        verbose_name='Статус'
    )
    sum_bul = models.IntegerField(
        verbose_name='Число полученных бюллетеней'
    )
    sum_final_bul = models.IntegerField(
        verbose_name='Число обработаных бюллетеней'
    )
    bad_form = models.IntegerField(
        verbose_name='Общее число испорченных бланков'
    )
    transfer_time = models.TimeField(
        verbose_name='Время передачи протокола',
        auto_now=True
    )


class Protocol2(Model):
    num_protocol_2 = models.IntegerField(
        verbose_name='Номер протокола 2го типа',
    )
    num_uik = models.IntegerField(
        verbose_name='Номер участка'
    )
    name = models.CharField(
        verbose_name='ФИО кандидата',
        max_length=200,
    )
    candidate_votes = models.IntegerField(
        verbose_name='Число голосов за кандидата'
    )
    transfer_time = models.TimeField(
        verbose_name='Время передачи протокола',
        auto_now=True
    )


class UikCandidate(Model):
    id_uik = models.OneToOneField(Uik, on_delete=models.CASCADE)
    id_candidate = models.OneToOneField(Candidate, on_delete=models.CASCADE)


class UikProtocol1(Model):
    id_uik = models.OneToOneField(Uik, on_delete=models.CASCADE)
    id_protocol1 = models.OneToOneField(Protocol1, on_delete=models.CASCADE)


class CandidateProtocol2(Model):
    id_candidate = models.OneToOneField(Candidate, on_delete=models.CASCADE)
    id_protocol2 = models.OneToOneField(Protocol2, on_delete=models.CASCADE)















