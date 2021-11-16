<template>
<div class ="block">
  <div class="container" :style="{'background-color': 'transparent !important'}">
        <div v-if="tiks.length > 0" class="display-3 text-center text-white font-weight-bold">
          <div>
            {{ tiks[0].num_tik }}
          </div>
        </div>
    <div class="text-white">
      <div class="col-12" v-if="tiks.length > 0">
        <div class="row display-4">
          <div class="col-10 text-left">
            Явка в 12:00 составила
          </div>
          <div class="col-2 text-right">
              {{Math.round((tiks[0].presence / tiks[0].population * 100 + Number.EPSILON) * 100) / 100}}%
          </div>
        </div>
        <div class="row display-4" v-if="tiks.length > 1">
          <div class="col-10 text-left">
            Явка в 15:00 составила
          </div>
          <div class="col-2 text-right">
              {{Math.round((tiks[1].presence / tiks[1].population * 100 + Number.EPSILON) * 100) / 100}}%
          </div>
        </div>
        <div class="row display-4" v-if="tiks.length > 2" >
          <div class="col-10 text-left">
            Явка в 18:00 составила
          </div>
          <div class="col-2 text-right">
              {{Math.round((tiks[2].presence / tiks[2].population * 100 + Number.EPSILON) * 100) / 100}}%
          </div>
        </div>
        <div class="row display-4" v-for="(candidate, i) in candidates" :key="i">
          <div class="col-10 text-left">
            {{candidate.name}}
          </div>
          <div class="col-2 text-right">
              {{candidate.sum_votes}}
          </div>
        </div>
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
<style>
.block {
    display: flex;
    align-items: center;
    justify-content: center;
}
</style>