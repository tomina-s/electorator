<template>
  <div class="col-md-12">
    <div class="card card-container">
        <router-link  class="btn btn-primary btn-block" to="/protocol/create" tag="button">Заполнить протокол</router-link>

        <div
          v-for="(protocol) in protocols"
          :key="protocol.id"
          class="form-group"
        >
          <router-link
              class="btn btn-outline-secondary btn-block"
              :to="{ name:'/protocol/read', params:{ id:  protocol.id } }"
          >
            Протокол №{{ protocol.id }}
          </router-link>
        </div>

        <div class="card-footer pb-0 pt-3">
          <!--TODO для тестов маленькие страницы -->
          <pagination
              v-model="page"
              :records="numberOfProtocols"
              :per-page="10"
              :options='{
                chunk: 4,
                texts: {count: "", first: "", last: ""}
              }'
              @paginate="onChangePage"
          />
        </div>
    </div>
  </div>
</template>

<script>
import ProtocolService from "../services/protocol.service"

export default {
  name: "ProtocolList",
  data() {
    return {
      page: 1,
      uik_id: this.$route.params.uik_id,
      numberOfProtocols: 0,
      protocols: [],
    }
  },
  computed: {
  },
  mounted() {
    ProtocolService.GetProtocolFirstQuantity(this.uik_id, 1)
        .then(r => {
          this.numberOfProtocols = r.quantity
        })
        .catch(e => {
          console.log(e)
        })
    ProtocolService.GetProtocolFirstList(this.uik_id, 1)
        .then(r => {
          this.protocols = r
        })
        .catch(e => {
          console.log(e)
        })
  },
  created() {
  },
  methods: {
    onChangePage(p) {
    ProtocolService.GetProtocolFirstList(this.uik_id, p)
        .then(r => {
          console.log('updateProtocols')
          this.protocols = r
        })
        .catch(e => {
          console.log(e)
        })
    }
  },
}

</script>