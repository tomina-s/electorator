<template>
  <div class="container" :style="{'background-color': 'transparent !important'}">
    <div class="col-md-12">
      <div class="card card-container" :style="{'background-color': 'transparent !important'}">
          <div
            v-for="(tik) in tiks"
            :key="tik.num_tik"
            class="form-group"
          >
            <router-link
                class="btn btn-light btn-block"
                :to="{ name:'/tik/read', query:{ num_tik: tik.num_tik } }"
            >
                 {{ tik.num_tik }}
            </router-link>
          </div>

          <div class="card-footer pb-0 pt-3 text-center">
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

import TIKService from "../services/tik.service";

export default {
  name: "TIKList",
  data() {
    return {
      page: 1,
      quantity: 0,
      tiks: [],
    }
  },
  mounted() {
    TIKService.GetTIKQuantity()
        .then(r => {
          this.quantity = r.quantity
        })
        .catch(e => {
          console.log(e)
        })
    TIKService.GetTIKList(1)
        .then(r => {
          this.tiks = r
        })
        .catch(e => {
          console.log(e)
        })
  },
  methods: {
    onChangePage(page) {
      TIKService.GetTIKList(page)
          .then(r => {
            this.tiks = r
          })
          .catch(e => {
            console.log(e)
          })
    }
  },
}

</script>