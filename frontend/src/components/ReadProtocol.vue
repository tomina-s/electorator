<template>
  <div class="card card-container">
    <div class="form-group">
      Протокол №{{protocol.id}}
    </div>
    <div class="form-group">
      Номер УИК:
    </div>
    <div class="form-group">
      Участок открыт:
    </div>
    <div class="form-group">
      Проголосовало:
    </div>
    <div class="form-group">
      Бюллетеней испорчено:
    </div>
    <div v-for="(candidate) in protocol.candidates"
         :key="candidate.id"
         class="form-group">
      {{ candidate.name }}:
    </div>
  </div>
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