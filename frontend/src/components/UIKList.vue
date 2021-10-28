<template>
  <div class="col-md-12">
    <div class="card card-container">
        <div
          v-for="(uik) in pageOfItems"
          :key="uik"
          class="form-group"
        >
          <router-link
              class="btn btn-outline-secondary btn-block"
              :to="{ name:'/protocols', params:{ id:  uik } }"
          >
               УИК №{{ uik }}
          </router-link>
        </div>

        <div class="card-footer pb-0 pt-3">
          <pagination
              v-model="page"
              :records="uiks.length"
              :per-page="10"
              :options='{ texts: {count: "", first: "", last: ""} }'
              @paginate="onChangePage"
          />
        </div>
    </div>
  </div>
</template>

<script>

import {getPermissions} from "../services/common.service";

export default {
  name: "UIKList",
  data() {
    const uiks = getPermissions().sort()
    const firstPage = uiks.slice(0, uiks.length < 10 ? uiks.length : 10)

    return {
      page: 1,
      uiks: uiks,
      pageOfItems: firstPage,
    }
  },
  computed: {
  },
  created() {
  },
  methods: {
    onChangePage(page) {
      this.pageOfItems = this.uiks.slice((page - 1) * 10, page * 10)
    }
  },
}

</script>