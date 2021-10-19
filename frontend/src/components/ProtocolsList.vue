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
            Протокол №{{ protocol.num }}
          </router-link>
        </div>

        <router-link  class="btn btn-primary btn-block" to="/protocol/create" tag="button">Заполнить протокол</router-link>
    </div>
  </div>
</template>

<script>

export default {
  name: "ProtocolList",
  data() {
    return {
      protocols: [],
    }
  },
  computed: {
  },
  created() {
    // TODO запрашивать список протоколов
    this.protocols = [{id: 3, num: "123"}, {id: 32, num: "2"}]
  },
  methods: {
    openProtocol(protocol) {
      console.log(protocol)
      console.log("open protocol")

      this.$router.push(`?id=${protocol}`)
    },
  },
}

</script>