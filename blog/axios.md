# Axios 使用方法

## 安装 `axios`

```bash
npm install axios
# 或者
yarn add axios
```
* get：
``` js
axios.get('https://example.com')
     .then(response => {
         console.log(response.data);
     })
     .catch(error => {
         console.error('Error fetching data: ', error);
     })
     .then(() => {
         // 总是会执行
     });
```
* post
``` js
axios.post('https://example.com', {
    firstName: 'Fred',
    lastName: 'Flintstone'
})
.then(response => {
    console.log(response.data);
})
.catch(error => {
    console.error('Error posting data: ', error);
});
```
* 异步等待
``` js
async function getUserData() {
    try {
        const response = await axios.get('https://example.com');
        console.log(response.data);
    } catch (error) {
        console.error('Error fetching data: ', error);
    }
}
```
* 配置请求：
```js
axios({
    method: 'post',
    url: 'https://example.com',
    data: {
        firstName: 'Fred',
        lastName: 'Flintstone'
    },
    timeout: 1000,  // 1000 毫秒
    headers: {'X-Custom-Header': 'foobar'}
});
```
* 拦截请求：
```js
// 添加请求拦截器
axios.interceptors.request.use(function (config) {
    // 在发送请求之前做些什么
    return config;
}, function (error) {
    // 对请求错误做些什么
    return Promise.reject(error);
});

// 添加响应拦截器
axios.interceptors.response.use(function (response) {
    // 对响应数据做点什么
    return response;
}, function (error) {
    // 对响应错误做点什么
    return Promise.reject(error);
});
```