<template>
  <div class="container" :style="{'background-color': 'transparent !important'}">
    <div class="col-md-12 text-white">
      <div v-if="tiks.length > 0" class="card card-container text-center" :style="{'background-color': 'transparent !important'}">
        <div class="form-group">
          {{ tiks[0].num_tik }}
        </div>
        <div class="form-group">
          Явка в 12:00 составила {{Math.round((tiks[0].presence / tiks[0].population * 100 + Number.EPSILON) * 100) / 100}}%
        </div>
        <div v-if="tiks.length > 1" class="form-group">
          Явка в 15:00 составила {{Math.round((tiks[1].presence / tiks[1].population * 100 + Number.EPSILON) * 100) / 100}}%
        </div>
        <div v-if="tiks.length > 2" class="form-group">
          Явка в 18:00 составила {{Math.round((tiks[2].presence / tiks[2].population * 100 + Number.EPSILON) * 100) / 100}}%
        </div>
        <div v-for="(candidate, i) in candidates" :key="i" class="form-group">
          {{candidate.name}} {{candidate.sum_votes}}
        </div>
      </div>
    </div>
  </div>
</template>

<script>

import TIKService from "../services/tik.service";

export default {
  name: "ReadProtocol",
  mounted() {
    TIKService.GetTIK(this.$route.query.num_tik)
      .then(r => {
        this.tiks = r
      })
      .catch(e => {
        console.log(e)
      })
    TIKService.GetTIKCandidates(this.$route.query.num_tik)
      .then(r => {
        this.candidates = r
      })
      .catch(e => {
        console.log(e)
      })
  },
  data() {
    return {
      num_tik: "",
      tiks: [],
      candidates: []
    }
  },
}
</script>