<template>
    <div class="photo-wall">
      <img v-for="image in images" :src="'http://111.231.21.55:3000/photos/' + image" :key="image" />
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        images: []
      };
    },
    created() {
      axios.get('http://111.231.21.55:3000/photos-list')
        .then(response => {
          this.images = response.data;
        })
        .catch(error => {
          console.error('Error fetching images:', error);
        });
    }
  };
  </script>
  
  <style>
  .photo-wall {
    margin-top: 20px;
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); /* 创建动态列数，每列最小宽度为150px，最大为1fr */
    grid-auto-rows: 150px; /* 每行的高度，调整以满足需求 */
    gap: 0; /* 设置网格间的间隙为0 */
  }
  
  .photo-wall img {
    width: 100%; /* 让图片充满其网格单元的宽度 */
    height: 100%; /* 让图片充满其网格单元的高度 */
    object-fit: cover; /* 裁剪图片以填充整个网格单元，保持图片比例 */
  }
  
  </style>
  