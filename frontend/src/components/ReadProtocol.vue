
</template>

<script>

export default {
  name: "ReadProtocol",
  data() {
    return {
      protocol: {
        id: 33,
        candidates: [
          {
            id: 1,
            name: "huvalk"
          },
          {
            id: 2,
            name: "huvalk2"
          }
        ]
      },
    }
  },
  created() {
    // TODO запрос к протоколу
    console.log("request for protocol: ", this.$route.params)
    this.protocol.id = this.$route.params.id
  },
}
</script>