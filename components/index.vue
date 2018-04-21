<template>
  <component :is="name"></component>
</template>
<script>
  module.exports = {
    props: ['type'],
    computed: {
      name() {
        return `feather-${this.type}`
      }
    }
  }
</script>
// tabler icon style
<style lang="scss" scoped>
$icon-color: #2c3e50;;
.icon {
	text-align: center;
	display: flex;
	align-items: center;
	justify-content: center;
	svg {
		font-size: 0.875rem;
		stroke: $icon-color;
	}
}
</style>
