const fs = require('fs');
fs.readdir('../blog/', function (err, files) {
    if (err) {
      return console.log('目录不存在')
    }
    console.log(files)
  })