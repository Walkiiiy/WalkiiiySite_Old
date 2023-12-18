## vue_watch
* 一般监视
``` js
<template>
  <!-- 模板内容 -->
</template>

<script>
export default {
  data() {
    return {
      watchedData: ''
    }
  },
  watch: {
    // 监视数据属性 'watchedData'
    watchedData(newVal, oldVal) {
      console.log(`值从 ${oldVal} 变为 ${newVal}`);
    }
  }
}
</script>
```
* 有时，你可能希望在 watch 设置时立即执行一次。可以通过设置 immediate 选项实现：
``` js
watch: {
  watchedData: {
    handler(newVal, oldVal) {
      console.log(`watchedData 变化了，新值为 ${newVal}`);
    },
    immediate: true
  }
}
```
* watch的过度使用可能会造成性能问题