const express = require('express');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3001;

// 静态文件服务，指向 dist 目录
app.use(express.static(path.join(__dirname, 'dist')));

// 所有路由都指向 index.html，允许前端路由处理
app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, 'dist', 'index.html'));
});

// 启动服务器
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
