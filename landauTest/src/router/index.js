import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import TablePage from '@/components/TablePage'
import FileSender from '@/components/FileSender'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/table',
      name: 'table-render',
      component: TablePage
    },
    {
      path: '/',
      name: 'FileSender',
      component: FileSender
    }
  ]
})
