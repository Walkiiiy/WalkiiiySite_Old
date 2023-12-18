## position属性
* static：默认，按照正常的页面流排列，此时的top、bottom、left、right属性无效
* relative：相对于static进行偏移
* fixed：相对于浏览器窗口进行偏移，可以实现元素不随滚动而变化的效果
* absolute：相对于父元素进行偏移，如果父元素是static定位，则会相对于整个页面进行偏移，且会被正常页面流忽略
* sticky：初始为relative，滚动时与边界的距离如果达到阈值，就会成为fixed定位。