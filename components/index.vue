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
.icon {
	text-align: center;
	display: flex;
	align-items: center;
	justify-content: center;
	margin-right: .25rem;
	line-height: 1;
	width: 0.875rem;
	vertical-align: baseline;
	svg {
		font-size: 0.875rem;
   		display: inline-block;
	}
}
</style>
