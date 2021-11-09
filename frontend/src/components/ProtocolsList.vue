<template>
  <div class="container" :style="{'background-color': 'transparent !important'}">
    <div class="col-md-12">
      <div class="card card-container" :style="{'background-color': 'transparent !important'}">
          <router-link  class="btn btn-primary btn-block" to="/protocol/create" tag="button">Заполнить протокол</router-link>

            <div v-for="protocol in protocols" :key="protocol.id" class="card card-container">
              <router-link
                  class="btn btn-outline-secondary btn-block"
                  :to="{ name:'/protocol/read', query:{ protocol_id:  protocol.id } }"
              >
                Протокол №{{ protocol.num_protocol_1 }}
              </router-link>
            </div>
      </div>
    </div>
  </div>
</template>

<script>
import ProtocolService from "../services/protocol.service"

export default {
  name: "ProtocolList",
  data() {
    console.log(this.$route.query.uik_id)
    return {
      uik_id: this.$route.query.uik_id,
      protocols: [],
    }
  },
  mounted() {
    ProtocolService.GetProtocolFirstList(this.uik_id, 1)
        .then(r => {
          this.protocols = r
        })
        .catch(e => {
          console.log(e)
        })
  },
  methods: {
  },
}

</script>