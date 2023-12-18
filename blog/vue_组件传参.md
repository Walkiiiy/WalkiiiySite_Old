## vue组件传参
* 父组件向子组件传参：使用 Props 传递数据

    在子组件中声明 Props：
    在子组件中，你需要使用 props 选项来声明你期望从父组件接收的数据。
``` js
<script>
export default {
  props: ['message']
}
</script>
```
在父组件中传递数据：
在父组件的模板中，将数据作为属性传递给子组件。
``` js

    <template>
      <ChildComponent :message="parentMessage" />
    </template>

    <script>
    import ChildComponent from './ChildComponent.vue';

    export default {
      components: {
        ChildComponent
      },
      data() {
        return {
          parentMessage: 'Hello from Parent'
        }
      }
    }
    </script>
```

* 子组件向父组件传参：使用 Emit 发送事件

    在子组件中触发事件：
    当某个事件（如用户操作）发生时，子组件可以使用 $emit 方法发送一个自定义事件。
``` js
<template>
  <button @click="sendEvent">Click me</button>
</template>

<script>
export default {
  methods: {
    sendEvent() {
      this.$emit('childEvent', 'Data from Child');
    }
  }
}
</script>
```
在父组件中监听事件：
父组件在使用子组件的地方监听这个事件，并定义一个方法来处理这个事件。

``` js

    <template>
      <ChildComponent @childEvent="handleEvent" />
    </template>

    <script>
    import ChildComponent from './ChildComponent.vue';

    export default {
      components: {
        ChildComponent
      },
      methods: {
        handleEvent(data) {
          console.log('Event received:', data);
        }
      }
    }
    </script>
```
这两种方式是Vue中组件通信的基础，可以根据具体的应用场景灵活选择使用。