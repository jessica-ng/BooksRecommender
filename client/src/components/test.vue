<template>
  <div>
    <p>{{ msg }}</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Test',
  data() {
    return {
      msg: 'Hello!',
    };
  },
  methods: {
    getMessage() {
      const path = 'http://localhost:5000/test';
      axios.get(path)
        .then((res) => {
          this.msg = res.data;
          console.log(this.msg);
        })
        .catch((error) => {
          
          console.error(error);
        });
    },
  },
  created() {
    this.getMessage();
  },
};
</script>