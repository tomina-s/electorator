<template>
  <div class="container" :style="{'background-color': 'transparent !important'}">
    <div class="col-md-12">
      <div class="card card-container" :style="{'background-color': 'transparent !important'}">
          <div
            v-for="(uik) in uiks"
            :key="uik.id"
            class="form-group"
          >
            <router-link
                class="btn btn-outline-secondary btn-block"
                :to="{ name:'/protocols', query:{ uik_id:  uik.id } }"
            >
                 УИК №{{ uik.num_uik }}
            </router-link>
          </div>

          <div class="card-footer pb-0 pt-3">
            <pagination
                v-model="page"
                :records="quantity"
                :per-page="10"
                :options='{ texts: {count: "", first: "", last: ""} }'
                @paginate="onChangePage"
            />
          </div>
      </div>
    </div>
  </div>
</template>

<script>

import UIKService from "../services/uik.service";

export default {
  name: "UIKList",
  data() {
    return {
      page: 1,
      quantity: 0,
      uiks: [],
    }
  },
  mounted() {
    UIKService.GetUIKQuantity()
        .then(r => {
          this.quantity = r.quantity
        })
        .catch(e => {
          console.log(e)
        })
    UIKService.GetUIKList(1)
        .then(r => {
          this.uiks = r
        })
        .catch(e => {
          console.log(e)
        })
  },
  methods: {
    onChangePage(page) {
      UIKService.GetUIKList(page)
          .then(r => {
            this.uiks = r
          })
          .catch(e => {
            console.log(e)
          })
    }
  },
}

</script>