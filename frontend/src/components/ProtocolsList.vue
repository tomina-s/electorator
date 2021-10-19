<template>
  <div class="col-md-12">
    <div class="card card-container">
      <Form @submit="openProtocol" :validation-schema="schema">
        <div
          v-for="(protocol) in protocols"
          :key="protocol.id"
          class="form-group"
        >
          <button class="btn btn-outline-secondary btn-block" v-on:click="openProtocol(protocol.id)">{{ protocol.num }}</button>
        </div>

        <router-link  class="btn btn-primary btn-block" to="/protocol/create" tag="button">Заполнить протокол</router-link>
      </Form>
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

      this.$router.push(`/protocol/read?id=${protocol.id}`)
    },
  },
}

</script>