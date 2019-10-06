from django.db import models


class Balance(models.Model):
    denezhnie_sredstva = models.IntegerField()
    fin_vlozhenie = models.IntegerField()
    debit_zadolzhnost =models.IntegerField()
    fin_invest = models.IntegerField()
    zapas = models.IntegerField()
    nalog_active = models.IntegerField()
    avans = models.IntegerField()
    prochie_current_avtives = models.IntegerField()
    all_actives = models.IntegerField()

    osnovine_sredstva = models.IntegerField()
    long_term_invest = models.IntegerField()
    long_term_zadolzhnost = models.IntegerField()
    invest_nedvizhimost =models.IntegerField()
    nonmaterial_actives =models.IntegerField()
    otlozhennye_nalog_actives =models.IntegerField()
    prochie_long_term_actives = models.IntegerField()
    all_long_term_actives = models.IntegerField()
    all_actives = models.IntegerField()


class Capital(models.Model):
    short_time_fin_cap = models.IntegerField()
    obyaz_po_nalogam = models.IntegerField()
    short_time_credit = models.IntegerField()
    obyaz_po_drugim_nalogam = models.IntegerField()
    avans = models.IntegerField()
    prochie_obyaz = models.IntegerField()
    all_current_obyaz = models.IntegerField()

    long_term_fin_obyaz = models.IntegerField()
    long_term_credit = models.IntegerField()
    otlozhennye_nalog_actives = models.IntegerField()
    long_term_zadolzhnost = models.IntegerField()
    otlozhennye_nalog_obyaz = models.IntegerField()
    prochie_long_term_obyaz = models.IntegerField()
    all_long_term_obyaz = models.IntegerField()
    all_obyaz = models.IntegerField()
    ustavni_capital = models.IntegerField()
    neoplacheni_capital = models.IntegerField()
    reserves = models.IntegerField()
    neraspredelennaya_income = models.IntegerField()
    all_capital = models.IntegerField()
    all_obyaz_and_capital = models.IntegerField()
