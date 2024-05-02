<template>
    <div>
      <p class="greeting"> {{ msg }} </p>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  
  const msg = ref('Hello')
  
  </script>
  
  <!-- scoped는 현재 이 컴포넌트에서만 적용하겠다는 뜻 -->
  <style scoped>
    .greeting {
        color: crimson;
    }
  </style>
