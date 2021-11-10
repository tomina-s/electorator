<template>
  <div class="container" :style="{'background-color': 'transparent !important'}">
    <div class="col-md-12">
      <div class="card card-container" :style="{'background-color': 'transparent !important'}">
        <router-link v-if="isUIK" class="btn btn-primary btn-block" tag="button"
          :to="{
            name: protocols.length === 0 ? 'timer' :
              (protocols.length > 0 && protocols.length < 4) ? 'turnout' : 'createProtocol',
              query:{ protocolNum: protocols.length + 1 }
          }"
        >Заполнить протокол</router-link>

        <div v-for="protocol in protocols" :key="protocol.id" class="card card-container">
          <router-link
            class="btn btn-outline-secondary btn-block"
            :to="{
              name: protocol.num_protocol_1 === 1 ? 'timer' :
                (protocol.num_protocol_1 > 1 && protocol.num_protocol_1 < 5) ? 'turnout' : 'createProtocol',
                query:{ protocolNum: protocol.num_protocol_1, uik_id: uik_id }
              }"
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
import {getUIKPermission} from "../services/common.service";

export default {
  name: "ProtocolList",
  computed: {
    isUIK() {
      return this.$store.state.auth.account && this.$store.state.auth.account.role === "УИК"
    },
  },
  data() {
    let perm = this.$route.query.uik_id
    if (!perm) {
      perm = getUIKPermission()
    }

    if (!perm) {
      return
    }

    return {
      uik_id: perm,
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