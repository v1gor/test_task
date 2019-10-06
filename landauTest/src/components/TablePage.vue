<template>
  <div >
    <!-- <h1>{{ capital }}</h1> -->
    <table style="text-align: left;">
      <tr>
        <th>Активы</th>
        <!-- <th v-for:balance.id></th>  -->
        <th>date1</th>
        <th>date2</th>
      </tr>
      <tr>
        <td>Денежные средства</td>
        <td><input type="text" name="" value="" v-model="balance.denezhnie_sredstva"></td>
      </tr>
      <tr>
        <td>Финансовые вложения</td>
        <td> <input type="text" name="" value="" v-model="balance.fin_vlozhenie"></td>
      </tr>
      <tr>
        <td>Краткосрочная дебиторская задолженность</td>
        <td> <input type="text" name="" value="" v-model="balance.debit_zadolzhnost"></td>
      </tr>
      <tr>
        <td>Краткосрочные финансовые инвестиции</td>
        <td> <input type="text" name="" value="" v-model="balance.fin_invest"></td>
      </tr>
      <tr>
        <td>Запасы</td>
        <td> <input type="text" name="" value="" v-model="balance.zapas"></td>
      </tr>
      <tr>
        <td>Текущие налоговые активы</td>
        <td> <input type="text" name="" value="" v-model="balance.nalog_active"></td>
      </tr>
      <tr>
        <td>Авансы выданные и расходы буд.периодов</td>
        <td> <input type="text" name="" value="" v-model="balance.avans"></td>
      </tr>
      <tr>
        <td>Прочие текущие активы</td>
        <td> <input type="text" name="" value="" v-model="balance.prochie_current_avtives"></td>
      </tr>
      <tr>
        <td>Всего текущие активы</td>
        <td></td>
      </tr>
      <tr>
        <td>Основные средства</td>
        <td> <input type="text" name="" value="" v-model="balance.osnovine_sredstva"></td>
      </tr>
      <tr>
        <td>Долгосрочные инвестиции</td>
        <td> <input type="text" name="" value="" v-model="balance.long_term_invest"></td>
      </tr>
      <tr>
        <td>Долгосрочная дебиторская задолженность</td>
        <td> <input type="text" name="" value="" v-model="balance.long_term_zadolzhnost"></td>
      </tr>
      <tr>
        <td>Инвестиционная недвижимость</td>
        <td> <input type="text" name="" value="" v-model="balance.invest_nedvizhimost"></td>
      </tr>
      <tr>
        <td>Нематериальные активы</td>
        <td> <input type="text" name="" value="" v-model="balance.nonmaterial_actives"></td>
      </tr>
      <tr>
        <td>Отложенные налоговые активы</td>
        <td> <input type="text" name="" value="" v-model="balance.otlozhennye_nalog_actives"></td>
      </tr>
      <tr>
        <td>Прочие долгосрочные активы</td>
        <td> <input type="text" name="" value="" v-model="balance.prochie_long_term_actives"></td>
      </tr>
      <tr>
        <td>Всего долгосрочные активы</td>
        <td> <input type="text" name="" value="" v-model="balance.all_long_term_actives"></td>
      </tr>
      <tr>
        <td>Всего Активы</td>
        <td> <input type="text" name="" value="" v-model="balance.all_actives"></td>
      </tr>

    </table>

  </div>
</template>

<script>
export default {
  name: 'table-render',
  data () {
    return {
      capital: [],
      balance: []
    }
  },
  created() {
    const Http = new XMLHttpRequest();
    const Http_balance = new XMLHttpRequest();
    const url='http://127.0.0.1:8000/api/capital';
    const url_balance='http://127.0.0.1:8000/api/balance';

    Http.open("GET", url);
    Http.send();

    Http_balance.open("GET", url_balance)
    Http_balance.send()

    Http.onreadystatechange = (e) => {
      var capital_data = JSON.parse(Http.response)
      this.capital = capital_data[0]
      var balance_data = JSON.parse(Http_balance.response)
      this.balance = balance_data[0]
      // document.getElementById("demo").innerHTML = myArr[0];
      // var myArr = JSON.parse(this.responseText);
      // console.log(myArr)
      // this.capital = Http.response
      // type()
    }
  }
}
</script>
