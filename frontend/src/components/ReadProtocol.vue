<template>
  <div class="card card-container" :style="{'background-color': 'transparent !important'}">
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
    this.protocol.id = this.$route.query.id
  },
}
</script>