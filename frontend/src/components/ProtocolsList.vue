<template>
  <div class="col-md-12">
    <div class="card card-container">
        <router-link  class="btn btn-primary btn-block" to="/protocol/create" tag="button">Заполнить протокол</router-link>

          <div v-for="protocol in protocols" :key="protocol.id" class="card card-container">
            <div class="form-group">
              Протокол №{{ protocol.id }}
            </div>
            <div class="form-group">
              Номер УИК: {{ protocol.num_uik }}
            </div>
            <div class="form-group">
              Участок {{ protocol.status ? 'открыт' : 'закрыт' }}
            </div>
            <div class="form-group">
              Проголосовало: {{ protocol.sum_bul }}
            </div>
            <div class="form-group">
              Бюллетеней испорчено: {{ protocol.bad_form }}
            </div>
            <div v-for="(candidate) in protocol.candidates"
                 :key="candidate.id"
                 class="form-group">
              {{ candidate.name }}:
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
    console.log(this.uik_id)
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