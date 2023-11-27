const express = require('express');
const MarkdownIt = require('markdown-it');
const fs = require('fs');
const app = express();
const port = 3000;
//设置CORS
app.all('*',function (req, res, next) {
  res.header('Access-Control-Allow-Origin','*'); //当允许携带cookies此处的白名单不能写’*’
  res.header('Access-Control-Allow-Headers','content-type,Content-Length, Authorization,Origin,Accept,X-Requested-With'); //允许的请求头
  res.header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS, PUT'); //允许的请求方法
  next();
});

// 处理 GET 请求，获取blog内容
app.get('/blog_content', (req, res) => {
    console.log('path:',req.query.path)
    fs.readFile('../blog/'+req.query.path, function (err, data) {
      if (err) {
          return console.error(err);
      }
      var md = new MarkdownIt();
      var result = md.render(data.toString());
      res.send(result);
    });
});
//获取blog列表
app.get('/blog_list',(req,res)=>{
  fs.readdir('../blog/', function (err, files) {
    if (err) {
      return console.log('目录不存在');
    }
    console.log(files);
    res.send(files);
  })
});
app.get('/photos-list', (req, res) => {
  fs.readdir('../photos/', function (err, files) {
    if (err) {
      return console.log('目录不存在');
    }
    console.log(files);
    res.send(files);
  })
});

app.use('/photos', express.static('../photos'));

// 启动服务器
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
