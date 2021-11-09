<template>
  <button
      :disabled="true"
    class="btn btn-light btn-block"
    @click="$router.push({ name:namePrev, query:{ protocolNum:  protocolNum - 1 } })"
  >
    Предыдущий протокол
  </button>
  <button
      :disabled="protocolNum >= 5 || !done"
    class="btn btn-light btn-block"
    @click="$router.push({ name:nameNext, query:{ protocolNum:  protocolNum + 1 } })"
  >
    Следующий протокол
  </button>
</template>

<script>

export default {
  name: "Switcher",
  props: {
    protocolNum: Number,
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
        nameNext = "turnout"
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