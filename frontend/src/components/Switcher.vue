<template>
  <button
      :disabled="protocolNum < 2"
    class="btn btn-light btn-block"
    @click="$router.push({ name:namePrev, query:{ protocolNum:  protocolNum - 1, uik_id: uik_id } })"
  >
    Предыдущий протокол
  </button>
  <button
      :disabled="protocolNum >= 5 || !done"
    class="btn btn-light btn-block"
    @click="$router.push({ name:nameNext, query:{ protocolNum:  protocolNum + 1, uik_id: uik_id } })"
  >
    Следующий протокол
  </button>
</template>

<script>

export default {
  name: "Switcher",
  props: {
    uik_id: Number,
    protocolNum: String,
    done: Boolean
  },
  data() {
    console.log("switcher", this.done, this.protocolNum)
    let nameNext = ""
    let namePrev = ""
    switch (this.protocolNum) {
      case 1:
        nameNext = "turnout"
        namePrev = ""
        break
      case 2:
        nameNext = "turnout"
        namePrev = "timer"
        break
      case 3:
        nameNext = "turnout"
        namePrev = "turnout"
        break
      case 4:
        nameNext = "createProtocol"
        namePrev = "turnout"
        break
      case 5:
        nameNext = ""
        namePrev = "turnout"
        break
    }
    return {
      nameNext: nameNext,
      namePrev: namePrev,
    }
  },
}
</script>