<template>
  <div class="col-md-12">
    <div class="card card-container">
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

        <router-link  class="btn btn-primary btn-block" to="/protocol/create" tag="button">Заполнить протокол</router-link>
    </div>
  </div>
</template>

<script>
import ProtocolService from "../services/protocol.service"

export default {
  name: "ProtocolList",
  data() {
    return {
      protocols: [],
    }
  },
  computed: {
  },
  mounted() {
    const uik_id = this.$route.params.id
    ProtocolService.GetProtocolSecondList(uik_id, 1)
        .then(r => {
          console.log(r)
          this.protocols = r
        })
        .catch(e => {
          console.log(e)
        })
  },
  created() {
  },
  methods: {
  },
}

</script>