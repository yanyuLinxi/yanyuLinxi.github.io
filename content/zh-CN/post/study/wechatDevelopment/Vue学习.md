---
title: "Vue学习"
date: 2021-09-08T17:00:28+08:00
tags : [
   "wechat开发"
]
categories : [
   "学习"
]
series : []
aliases : []
draft: false
---

# 其他
1. 使用Vscode写html，一个！号后可以选择模板。
2. 引入Vue框架
   1. ```<script src="https://unpkg.com/vue@next"></script>```
3. 练手：
   1. https://gitee.com/panjiachen/vue-admin-template

# 基础

## 创建实例, 支持链式。返回同一个实例。

```javascript
Vue.createAPP({})
    .component("")
    .directive
```
## 挂载到组件

```javascript
const app = Vue.createAPP()
const vm = app.mount("#app")

// app 是dom 元素id号. 与id绑定。class是样式。
// 与大多数应用方法不同的是，mount 不返回应用本身。相反，它返回的是根组件实例k。现在理解为返回实例。

//应该等app所有都建立完成后，再进行绑定到html的组件上。
```

## 钩子

```javascript
// 存在一些生命周期的钩子是可以绑定在Vue上的
Vue.createApp({
    data(){
        return {count: 1}
    },
    created(){
        console.log('count is: ' + this.count)  // "count is 1"  创建时调用
    }
    // 其他的还有 mounted updated unmounted等等
})
```

data是一个函数是返回这个对象的所有预先声明的变量

data 返回一个字典，字典所以用 :

## 插值，文本
```javascript
<span> Message:{{msg}}</span>
// span 中放内容会实时更新
<span v-once> 这个里面放的内容不会更新</span>
<p>Using v-html directive: <span v-html="rawHtml"></span></p>  //这样才能放置html内容
//其中javascript脚本中，data[rawHtml]可以赋值为一段html。v-html后面跟的是data id。
```

## Attribute
```javascript
//可以绑定属性
// 绑定属性前，前面一个没有引号，后面的有引号。
<div v-bind:id="dynamicId"></div>
//赋值dynamicId在data内可以更改id这个值，如果绑定的是null 或者undefined 则不会包含该attribute。
<button v-bind:disabled="isButtonDisabled">按钮</button>
//如果 isButtonDisabled 的值是 truthy[1]，那么 disabled attribute 将被包含在内。如果该值是一个空字符串，它也会被包括在内，与 <button disabled=""> 保持一致。对于其他 falsy[2] 的值，该 attribute 将被省略
```
```html
<!-- html中的{{}} 可以填入data property 或者methods名。如{{name()}}。 同样的可以由v-bind:title="name()"这样子-->

```


## 使用javascript表达式
```js
{{ number + 1 }}

{{ ok ? 'YES' : 'NO' }}

{{ message.split('').reverse().join('') }}

<div v-bind:id="'list-' + id"></div>
//以上都是ok的。表明可以进行简单的运算
<!--  这是语句，不是表达式：-->
{{ var a = 1 }}

<!-- 流控制也不会生效，请使用三元表达式 -->
{{ if (ok) { return message } }}

```


## 指令。指令 (Directives) 是带有 v- 前缀的特殊 attribute。指令 attribute 的值预期是单个 JavaScript 表达式 (v-for 和 v-on 是例外情况，稍后我们再讨论)。指令的职责是，当表达式的值改变时，将其产生的连带影响，响应式地作用于 DOM。

```html
<p v-if="seen">现在你看到我了</p>
<!-- 这里，v-if 指令将根据表达式 seen 的值的真假来插入/移除 <p> 元素。 -->

<!-- 一些指令能够接收一个“参数”，在指令名称之后以冒号表示。例如，v-bind 指令可以用于响应式地更新 HTML attribute：-->
<a v-bind:href="url"> ... </a>
<!-- 在这里 href 是参数，告知 v-bind 指令将该元素的 href attribute 与表达式 url 的值绑定。-->


<!-- 动态参数  也可以在指令参数中使用 JavaScript 表达式，方法是用方括号括起来： -->
<a v-bind:[attributeName]="url"> ... </a>
<!-- 如果data property中存在attributeName，其值为 "href"，那么这个绑定将等价于 v-bind:href -->


<!-- 修饰符 (modifier) 是以半角句号 . 指明的特殊后缀，用于指出一个指令应该以特殊方式绑定。例如，.prevent 修饰符告诉 v-on 指令对于触发的事件调用 event. preventDefault() -->
<form v-on:submit.prevent="onSubmit">...</form>
```

## 缩写
```html
<!-- 完整语法 -->
<a v-bind:href="url"> ... </a>

<!-- v-bind 缩写 -->
<a :href="url">
<!-- 动态参数的缩写 -->
<a :[key]="url"> ... </a>

<!-- 完整语法 -->
<a v-on:click="doSomething"> ... </a>

<!-- 缩写 -->
<a @click="doSomething"> ... </a>

<!-- 动态参数的缩写 (2.6.0+) -->
<a @[event]="doSomething"> ... </a>
```

## 注意
```html
<!-- 动态参数表达式有一些语法约束，因为某些字符，如空格和引号，放在 HTML attribute 名里是无效的。例如： -->
<!-- 这会触发一个编译警告 -->
<a v-bind:['foo' + bar]="value"> ... </a>

<!-- 在 DOM 中使用模板时 (直接在一个 HTML 文件里撰写模板)，还需要避免使用大写字符来命名键名，因为浏览器会把 attribute 名全部强制转为小写： -->
<!--
在 DOM 中使用模板时这段代码会被转换为 `v-bind:[someattr]`。
除非在实例中有一个名为“someattr”的 property，否则代码不会工作。
-->
<a v-bind:[someAttr]="value"> ... </a>
<!-- 所有attribute都是小写 -->

```

## Data property
组件的 data 选项是一个函数。Vue 在创建新组件实例的过程中调用此函数。它应该返回一个对象，然后 Vue 会通过响应性系统将其包裹起来，并以 $data 的形式存储在组
```js
const app = Vue.createApp({
  data() {
    return { count: 4 }
  }
})

const vm = app.mount('#app')
//  vm变量表示的就是应用实例， 先这么理解把
console.log(vm.$data.count) // => 4
console.log(vm.count)       // => 4
// 这些实例 property 仅在实例首次创建时被添加，所以你需要确保它们都在 data 函数返回的对象中。必要时，要对尚未提供所需值的 property 使用 null、undefined 或其他占位的值。
// 直接将不包含在 data 中的新 property 添加到组件实例是可行的。但由于该 property 不在背后的响应式 $data 对象内，所以 Vue
// vm.data是响应式的。
```

## methods
这里是methods。打错一个字都不行!!!

我们用 methods 选项向组件实例添加方法，它应该是一个包含所需方法的对象：
```js
const app = Vue.createApp({
  data() {
    return { count: 4 }
  },
  methods: {
    increment() {
      // `this` 指向该组件实例
      this.count++
    }
  }
})

const vm = app.mount('#app')

console.log(vm.count) // => 4

vm.increment()

console.log(vm.count) // => 5
```

```html
<!-- 这些 methods 和组件实例的其它所有 property 一样可以在组件的模板中被访问。在模板中，它们通常被当做事件监听使用： -->
<button @click="increment">Up vote</button>
```

## 函数防抖：将几次操作合并为一此操作进行。 ... 函数节流：使得一定时间内只触发一次函数。

这里稍微没看懂。后面再看。

## 侦听器 watch。可以侦测属性变换。
watch 会监听属性是否发生变化。发生变化后执行某种操作。最好还是使用计算属性。能用计算属性就别用侦听器。
watch顾名思义就是监听变量值的变化。
```html
<div id="watch-example">
  <p>
    Ask a yes/no question:
    <input v-model="question" />
  </p>
  <p>{{ answer }}</p>
</div>

```

```js
<script src="https://cdn.jsdelivr.net/npm/axios@0.12.0/dist/axios.min.js"></script>
<script>
  const watchExampleVM = Vue.createApp({
    data() {
      return {
        question: '',
        answer: 'Questions usually contain a question mark. ;-)'
      }
    },
    watch: {
      // whenever question changes, this function will run
      question(newQuestion, oldQuestion) {
        if (newQuestion.indexOf('?') > -1) {
          this.getAnswer()
        }
      }
    },
    methods: {
      getAnswer() {
        this.answer = 'Thinking...'
        axios
          .get('https://yesno.wtf/api')
          .then(response => {
            this.answer = response.data.answer
          })
          .catch(error => {
            this.answer = 'Error! Could not reach the API. ' + error
          })
      }
    }
  }).mount('#watch-example')
</script>


```

##  v-model
```js
// 你可以用 v-model 指令在表单 <input>、<textarea> 及 <select> 元素上创建双向数据绑定。如：
<input v-model="question" />
// v-model 会忽略所有表单元素的 value、checked、selected attribute 的初始值而总是将当前活动实例的数据作为数据来源。你应该通过 JavaScript 在组件的 data 选项中声明初始值。
// v-model 绑定的输入表单会始终将数据与Vue实例中的数据。
<input v-model="message" placeholder="edit me" />
<p>Message is: {{ message }}</p>
```

## class 和style绑定。样式绑定

对象语法：
{string: js_var_name}
意思是js_var_name是truty的时候，string才存在。

数据类型：变量要么是对象，要么是字典形式的对象，即active 或者 {active:isActive}

```html
<div
  class="static"
  :class="{ active: isActive, 'text-danger': hasError }"
></div>
```
```js

data() {
  return {
    isActive: true,
    hasError: false
  }
}
```
```html
<!-- 渲染结果： -->
<div class="static active"></div>
```

绑定的数据对象不必内联定义在模板里：
```html
<div :class="classObject"></div>

data() {
  return {
    classObject: {
      active: true,
      'text-danger': false
    }
  }
}

// 或者用计算属性
data() {
  return {
    isActive: true,
    error: null
  }
},
computed: {
  classObject() {
    return {
      active: this.isActive && !this.error,
      'text-danger': this.error && this.error.type === 'fatal'
    }
  }
}
```

##  使用数组
```html
<div :class="[activeClass, errorClass]"></div>
```
```js
data() {
  return {
    activeClass: 'active',
    errorClass: 'text-danger'
  }
}
```

记住html 的 id位置输送的进去的都是变量名。html中的vue变量用{{}}取值。用""将变量包裹起来。

数组语法和对象语法可以嵌套：
```html
<div :class="[{active:isActive}, errorClass]"></div>
```

## 条件渲染

v-if 指令用于条件性地渲染一块内容。这块内容只会在指令的表达式返回 truthy 值的时候被渲染。
```html
<h1 v-if="awesome">Vue is awesome!</h1>
<h1 v-else>Oh no 😢</h1>
```
在 <template> 元素上使用 v-if 条件渲染分组
<template> 可以作为常见分组包裹在最外层

因为 v-if 是一个指令，所以必须将它添加到一个元素上。但是如果想切换多个元素呢？此时可以把一个 <template> 元素当做不可见的包裹元素，并在上面使用 v-if。最终的渲染结果将不包含 <template> 元素。
```html
<template v-if="ok">
  <h1>Title</h1>
  <p>Paragraph 1</p>
  <p>Paragraph 2</p>
</template>
```
你可以使用 v-else 指令来表示 v-if 的“else 块”：
```html
<div v-if="Math.random() > 0.5">
  Now you see me
</div>
<div v-else>
  Now you don't
</div>

v-else-if，顾名思义，充当 v-if 的“else-if 块”，并且可以连续使用：
<div v-if="type === 'A'">
  A
</div>
<div v-else-if="type === 'B'">
  B
</div>
<div v-else-if="type === 'C'">
  C
</div>
<div v-else>
  Not A/B/C
</div>
<!-- v-else 元素必须紧跟在带 v-if 或者 v-else-if 的元素的后面，否则它将不会被识别。 -->
```

v-show 另一个用于条件性展示元素的选项是 v-show 指令。用法大致一样：
```html
<h1 v-show="ok">Hello!</h1>
<!-- 不同的是带有 v-show 的元素始终会被渲染并保留在 DOM 中。v-show 只是简单地切换元素的 CSS property display。 -->
```
注意，v-show 不支持 <template> 元素，也不支持 v-else。


v-if 是“真正”的条件渲染，因为它会确保在切换过程中，条件块内的事件监听器和子组件适当地被销毁和重建。

v-if 也是惰性的：如果在初始渲染时条件为假，则什么也不做——直到条件第一次变为真时，才会开始渲染条件块。

相比之下，v-show 就简单得多——不管初始条件是什么，元素总是会被渲染，并且只是简单地基于 CSS 进行切换。

一般来说，v-if 有更高的切换开销，而 v-show 有更高的初始渲染开销。因此，如果需要非常频繁地切换，则使用 v-show 较好；如果在运行时条件很少改变，则使用 v-if 较好。

切换少量：if。切换多次 show.

不推荐同时使用 v-if 和 v-for

当 v-if 与 v-for 一起使用时，v-if 具有比 v-for 更高的优先级

## v-for
v-for 指令需要使用 item in items 形式的特殊语法，其中 items 是源数据数组，而 item 则是被迭代的数组元素的
```html
<ul id="array-rendering">
  <li v-for="item in items">
    {{ item.message }}
    <!-- 使用.访问属性 -->
  </li>
</ul>
```
```js
Vue.createApp({
  data() {
    return {
      items: [{ message: 'Foo' }, { message: 'Bar' }]
    }
  }
}).mount('#array-rendering')
```
在 v-for 块中，我们可以访问所有父作用域的 property。即和当前list  property同一作用域的property

v-for 还支持一个可选的第二个参数，即当前项的索引。

list使用[{},{}]这样的语法。

{{}}只支持访问一个变量。

当访问对象的时候，可以for (value, name,  index) in object

当访问list的时候 可以 for (value, index) in list

列表可以添加value, index。访问字典对象时，可以value, name, index

```html
<ul id="array-with-index">
  <li v-for="(item, index) in items">
    {{ parentMessage }} - {{ index }} - {{ item.message }}
  </li>
</ul>
```

```js
Vue.createApp({
  data() {
    return {
      parentMessage: 'Parent',
      items: [{ message: 'Foo' }, { message: 'Bar' }]
    }
  }
}).mount('#array-with-index')
```

在使用for时使用key。它在更新时，不移动dom元素，而是更新dom的内容。

嵌套循环可以实时获取父作用域的变量。但要求有上下级关系。如嵌套的<div>.或者<ul><li></li></ul>等。


v-for 也可以接受整数。在这种情况下，它会把模板重复对应次数
```html
<div id="range" class="demo">
  <span v-for="n in 10" :key="n">{{ n }} </span>
</div>

```

类似于 v-if，你也可以利用带有 v-for 的 <template> 来循环渲染一段包含多个元素的内容。比如：

```html
<ul>
  <template v-for="item in items" :key="item.msg">
    <li>{{ item.msg }}</li>
    <li class="divider" role="presentation"></li>
  </template>
</ul>
```

当 Vue 正在更新使用 v-for 渲染的元素列表时，它默认使用“就地更新”的策略。如果数据项的顺序被改变，Vue 将不会移动 DOM 元素来匹配数据项的顺序，而是就地更新每个元素，并且确保它们在每个索引位置正确渲染。

这个默认的模式是高效的，但是只适用于不依赖子组件状态或临时 DOM 状态 (例如：表单输入值) 的列表渲染输出。

为了给 Vue 一个提示，以便它能跟踪每个节点的身份，从而重用和重新排序现有元素，你需要为每项提供一个唯一 key attribute：
```html
<div v-for="item in items" :key="item.id">
  <!-- content -->
</div>
```
## 数组操作和渲染相关

### 部分方法替换原list

push()
pop()
shift()
unshift()
splice()
sort()
reverse()

### 部分方法返回新数组

如 filter()、concat() 和 slice()


example1.items = example1.items.filter(item => item.message.match(/Foo/))

可以用计算属性 或者methods来帮助进行排序什么的。

## 事件处理
然而许多事件处理逻辑会更为复杂，所以直接把 JavaScript 代码写在 v-on 指令中是不可行的。因此 v-on 还可以接收一个需要调用的方法名称。
除了直接绑定到一个方法，也可以在内联 JavaScript 语句中调用方法：
```html
<div id="inline-handler">
  <button @click="say('hi')">Say hi</button>
  <button @click="say('what')">Say what</button>
</div>
Vue.createApp({
  methods: {
    say(message) {
      alert(message)
    }
  }
}).mount('#inline-handler')

有时也需要在内联语句处理器中访问原始的 DOM 事件。可以用特殊变量 $event 把它传入方法：
<button @click="warn('Form cannot be submitted yet.', $event)">
  Submit
</button>

事件处理程序中可以有多个方法，这些方法由逗号运算符分隔：
<!-- 这两个 one() 和 two() 将执行按钮点击事件 -->
<button @click="one($event), two($event)">
  Submit
</button>
```
## 事件修饰符
在事件处理程序中调用 event.preventDefault() 或 event.stopPropagation() 是非常常见的需求。尽管我们可以在方法中轻松实现这点，但更好的方式是：方法只有纯粹的数据逻辑，而不是去处理 DOM 事件细节。

为了解决这个问题，Vue.js 为 v-on 提供了事件修饰符。之前提过，修饰符是由点开头的指令后缀来表示的。

.stop
.prevent
.capture
.self
.once
.passive
```html
<!-- 阻止单击事件继续传播 -->
<a @click.stop="doThis"></a>

<!-- 提交事件不再重载页面 -->
<form @submit.prevent="onSubmit"></form>

<!-- 修饰符可以串联 -->
<a @click.stop.prevent="doThat"></a>

<!-- 只有修饰符 -->
<form @submit.prevent></form>

<!-- 添加事件监听器时使用事件捕获模式 -->
<!-- 即内部元素触发的事件先在此处理，然后才交由内部元素进行处理 -->
<div @click.capture="doThis">...</div>

<!-- 只当在 event.target 是当前元素自身时触发处理函数 -->
<!-- 即事件不是从内部元素触发的 -->
<div @click.self="doThat">...</div>
使用修饰符时，顺序很重要；相应的代码会以同样的顺序产生。因此，用 v-on:click.prevent.self 会阻止所有的点击，而 v-on:click.self.prevent 只会阻止对元素自身的点击
```


## 按键修饰符
在监听键盘事件时，我们经常需要检查详细的按键。Vue 允许为 v-on 或者 @ 在监听键盘事件时添加按键修饰符：
<!-- 只有在 `key` 是 `Enter` 时调用 `vm.submit()` -->
<input @keyup.enter="submit" />

可以用如下修饰符来实现仅在按下相应按键时才触发鼠标或键盘事件的监听器。
.ctrl
.alt
.shift
.meta
<!-- Alt + Enter -->
<input @keyup.alt.enter="clear" />

<!-- Ctrl + Click -->
<div @click.ctrl="doSomething">Do something</div>

.exact 修饰符允许你控制由精确的系统修饰符组合触发的事件。

.left
.right
.middle
这些修饰符会限制处理函数仅响应特定的鼠标按钮

## 表单输入绑定

v-model 会忽略所有表单元素的 value、checked、selected attribute 的初始值而总是将当前活动实例的数据作为数据来源。你应该通过 JavaScript 在组件的 data 选项中声明初始值。

v-model 在内部为不同的输入元素使用不同的 property 并抛出不同的事件：

text 和 textarea 元素使用 value property 和 input 事件；
checkbox 和 radio 使用 checked property 和 change 事件；
select 字段将 value 作为 prop 并将 change 作为事件。

使用v-model来将输出绑定数据。v-model后跟着就是data名称。

多个复选框，绑定到同一个数组：
```html

<div id="v-model-multiple-checkboxes">
  <input type="checkbox" id="jack" value="Jack" v-model="checkedNames" />
  <label for="jack">Jack</label>
  <input type="checkbox" id="john" value="John" v-model="checkedNames" />
  <label for="john">John</label>
  <input type="checkbox" id="mike" value="Mike" v-model="checkedNames" />
  <label for="mike">Mike</label>
  <br />
  <span>Checked names: {{ checkedNames }}</span>
</div>
```

for 属性规定 label 与哪个表单元素绑定。
这个不是vue规定的，是html规定的。注意不是v-for


但是有时我们可能想把值绑定到当前活动实例的一个动态 property 上，这时可以用 v-bind 实现，此外，使用 v-bind 可以将输入值绑定到非字符串
```html
<select v-model="selected">
  <!-- 内联对象字面量 -->
  <option :value="{ number: 123 }">123</option>
</select>
// 当被选中时
typeof vm.selected // => 'object'
vm.selected.number // => 123
```

## 组件基础
```js
const app = Vue.createApp({})

// 定义一个名为 button-counter 的新全局组件
app.component('button-counter', {
  data() {
    return {
      count: 0
    }
  },
  template: `
    <button @click="count++">
      You clicked me {{ count }} times.
    </button>`
})

组件是带有名称的可复用实例，在这个例子中是 <button-counter>。我们可以把这个组件作为一个根实例中的自定义元素来使用：
<div id="components-demo">
  <button-counter></button-counter>
</div>
app.mount('#components-demo')

component拥有自己的data域。注意这个data域是子data域。同为template的子域是无法访问的。

```

### 通过prop 向子组件传递数据

Prop 是你可以在组件上注册的一些自定义 attribute。为了给博文组件传递一个标题，我们可以用 props 选项将其包含在该组件可接受的 prop 列表中：

这里props就是一个预先申明你会传入哪些参数，所以template可以使用哪些参数。

props 传入的值并不是从父类继承的。是在创建组件的时候集成的。即<component :value="adsf">这个时候传入value 用props接收。

整个步骤是什么？
父级：Vue 初始app
子级： html 组件 和 定义的component。component就是定义一段可复用的html。它应该是独立于实例的。所以它不访问实例内容。但是被实例mount的html是可以访问实例的。所以通过被mount的html访问实例。然后传值给component。

component的html 可以通过<slot :item="item">来绑定属性到slot上。然后在html上就可以通过v-slot:slotName="variableName" 来访问。

总的来说component是一个独立出来的component html， 和创建的实例隔离开来，互不相访问。但是 实例可以和挂载的html互相访问。html可以使用该实例的component来访问其变量。并通过slot互相交互。component的目的就是复用。

template和组件配合使用分发插槽等。

### $emit
组件的作用就是来可复用。所以html理论上不能访问组件的变量。应该由组件内部自己显示变量。

数据流向，是从父html单向流向子组件的。子组件不应该修改父html的值。

javascript传值都是传引用。所以值会引发连串修改。


子组件使用props来接收父组件的传值。
子组件使用\$emit向父组件来发送值，父组件通过子组件的\$emit来监听传值。

子组件 @click=$emit('functionName', args)

父组件 @functionName="balabala"

这个意思是子组件点击的时候发送functionName。
父组件接收functionName后执行balabala
父组件可以通过$event来访问这个参数。或者将这个参数原封不动传给balabala。

注意emit出去的需要用 字符串符号括起来。它发射的是字符串。

然后发射的只能是小写字母。html不区分大小写。Vue区分。

子组件传出单个参数时：
// 子组件
this.$emit('test',this.param)
// 父组件
@test='test($event,userDefined)'

子组件传出多个参数时：
// 子组件
this.$emit('test',this.param1，this.param2, this.param3)
// 父组件 arguments 是以数组的形式传入
@test='test(arguments,userDefined)'

// 父组件
@test='test($event,userDefined)'  //userDefined 为父组件的附加对象/参数
常写成
@test='test' 这个时候$event默认传参了。

当执行函数时，没有参数时，$event参数默认在第一个。
当有多个参数时，$event需要显示传参。位置随意。

$emit 传出参数的也可以进行验证。

### 插槽

<slot></slot> 在template可以使用插槽来代替html 插槽中的内容。

但是注意，子作用域可以访问父作用域。
父作用域先渲染。
子作用域后渲染。
父级模板里的所有内容都是在父级作用域中编译的；子模板里的所有内容都是在子作用域中编译的。
子作用域的内容不可以互相访问。

<slot>中的内容，如果html的template中有内容会替换，没内容会保留这里的内容。</slot>

<template> 作为vue的基本模板。大多数的内容都可以放在template上。但少数如v-slot不能放在template上。</template>

<slot name="定义name" :item="绑定item到子作用域上的值">

<template v-slot:"定义的name"="一个对象用来接收item的值">   这样html可以操控布局应该怎样呈现数据。也可以访问子组件定义的值。

### 在组件上使用v-model

v-model是vue的语法

正常  <input v-model="searchText" >
详细 <input :value="searchText" @input="searchText=$event.target.value">
在组件上 <component :model-value="searchText"  @update:model-value="searchText=$event">

v-###:asdf  使用v开头的都是vue的语法。后面跟着的asdf都不用引号的。

### 动态组件

组件命了名后，如果有组件需要切换的话
<component :is="componentNameSwitch" class="tab"></div>
来切换

<keep-alive>组件可以包裹信息，不让他消失。

### 与Dom兼容关系

<table>
<tr is="vue:blog-post"></tr>
</table>
由于table内允许的只能是tr标签。所以这里通过is来让component显示出来，此时加上vue:前缀。

当你用驼峰大小写的时候，在html 属性上，因为不区分大小写，所以驼峰大小写会被解释为带一个横线

建议直接使用kebab-case 来定义组件名称。就是全部小写带横线。

### 局部注册

使用对象实例来注册局部组件。

## props

prop可以预先声明接受的值的类型。还可以进行预先的验证。
类型检查：
String
Number
Boolean
Array
Object
Date
Function
Symbol

这个类型检查可python不同。python类型检查错了也行，但这里必须检查正确才行。

## provide

这里provide :{}
和provide(){return{}}有什么区别？
感觉是一样的。直觉告诉我，一个是属性，一个是函数。
感觉真的要学javascript啊。=》javascript找不到答案。

这个provide 和 inject 并非是响应式的。

使用vue.computed(()=>)来响应式更改值。


## 没读懂

### 异步组件
### 非Prop的Attribute
### 模板引用
# API
## 计算属性
```html
<div id="computed-basics">
  <p>Has published books:</p>
  <span>{{ publishedBooksMessage }}</span>
</div>
<script>
Vue.createApp({
  data() {
    return {
      author: {
        name: 'John Doe',
        books: [
          'Vue 2 - Advanced Guide',
          'Vue 3 - Basic Guide',
          'Vue 4 - The Mystery'
        ]
      }
    }
  },
  computed: {
    // 计算属性的 getter
    publishedBooksMessage() {  // 这里的函数名就是data 的property了。
      // `this` 指向 vm 实例
      return this.author.books.length > 0 ? 'Yes' : 'No'
    }
  }
}).mount('#computed-basics')

//通过computed来计算得到data 的 property，函数名就是property，记住它是个函数，处于data层

// 你可能已经注意到我们可以通过在表达式中调用方法来达到同样的效果：
methods: {
  calculateBooksMessage() {
    return this.author.books.length > 0 ? 'Yes' : 'No'
  }
}
// 我们可以将同一函数定义为一个方法而不是一个计算属性。两种方式的最终结果确实是完全相同的。然而，不同的是计算属性是基于它们的响应依赖关系缓存的。计算属性只在相关响应式依赖发生改变时它们才会重新求值。这就意味着只要 author.books 还没有发生改变，多次访问 publishedBookMessage 计算属性会立即返回之前的计算结果，而不必再次执行函数。

//计算属性默认只有 getter，不过在需要时你也可以提供一个 setter：

computed: {
  fullName: {
    // getter
    get() {
      return this.firstName + ' ' + this.lastName
    },
    // setter
    set(newValue) {
      const names = newValue.split(' ')
      this.firstName = names[0]
      this.lastName = names[names.length - 1]
    }
  }
}
// 现在再运行 vm.fullName = 'John Doe' 时，setter 会被调用，vm.firstName 和 vm.lastName 也会相应地被更新
// get是从需要的值到最终值。
// set是从最终值到初始值的改变。
// fullname是data property
</script>

```

# 补充知识

## axios

```html
<script src="https://cdn.jsdelivr.net/npm/axios@0.12.0/dist/axios.min.js"></script>
```

```js

//  引入axios

// 发送 POST 请求
axios({
  method: 'post',
  url: '/user/12345',
  data: {
    firstName: 'Fred',
    lastName: 'Flintstone'
  }
});

// 请求响应的处理在 then 和 catch 回调中，请求正常会进入 then ，请求异常则会进 catch
axios({
  method: 'post',
  url: '/user/12345',
  data: {
    firstName: 'Fred',
    lastName: 'Flintstone'
  }
}).then(res => {
    consloe.log(res)
}).catch(err => {
    console.log(err)
})


// 通过 axios 发出的请求的响应结果中， axios 会加入一些字段，如下
{
  // `data` 由服务器提供的响应
  data: {},
  // `status` 来自服务器响应的 HTTP 状态码
  status: 200,
  // `statusText` 来自服务器响应的 HTTP 状态信息
  statusText: 'OK',
  // `headers` 服务器响应的头
  headers: {},
   // `config` 是为请求提供的配置信息
  config: {},
 // 'request'
  // `request` is the request that generated this response
  // It is the last ClientRequest instance in node.js (in redirects)
  // and an XMLHttpRequest instance the browser
  request: {}
}


```

## 箭头函数
javascript中箭头函数就是匿名函数
x => x * x
等价于
function (x) {
    return x * x;
}


## 判定符号

a==b 先类型转换后，再左右判断
a===b 直接左右判断是否相等。

# 注意
1. html 中<div>里是没有逗号的，用空格分隔。