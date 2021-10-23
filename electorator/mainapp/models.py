from django.db import models
from django.db.models import Model


class Uik(Model):  # Участки
    num_uik = models.IntegerField(
        verbose_name='Номер участка',
        unique=True
    )
    num_tik = models.CharField(
        verbose_name='Номер ТИК',
        max_length=200
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
    presence = models.IntegerField(
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
    party = models.CharField(
        verbose_name='Партия',
        max_length=200
    )
    info = models.TextField(
        verbose_name='Инфо о кандидате'
    )
    sum_votes = models.IntegerField(
        verbose_name='Общее число голосов'
    )
    photo = models.ImageField(
        verbose_name='Фото',
        upload_to='media/'
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
        verbose_name='Номер протокола 2го типа'
    )
    num_uik = models.IntegerField(
        verbose_name='Номер участка'
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
    id_uik = models.OneToOneField(Uik, on_delete=models.CASCADE)
    id_candidate = models.OneToOneField(Candidate, on_delete=models.CASCADE)


class UikProtocol1(Model):
    id_uik = models.OneToOneField(Uik, on_delete=models.CASCADE)
    id_protocol1 = models.OneToOneField(Protocol1, on_delete=models.CASCADE)


#class Users(Model):
#    name = models.CharField(
#        verbose_name='Имя пользователя',
#        max_length=200
#    )
#    password = models.CharField(
#        verbose_name='Пароль',
#        max_length=200
#    )
#    num_uik = models.ForeignKey(Uik, on_delete=models.CASCADE)

