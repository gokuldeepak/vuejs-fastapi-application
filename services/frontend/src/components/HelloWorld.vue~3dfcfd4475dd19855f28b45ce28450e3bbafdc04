<template>
  <div>
    <p>{{ msg }}</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'HelloWorld',
  data: function() {
    return {
      msg: msg,
    };
  },
  methods: {
    getMessage() {
      axios.get('/')
        .then((res) => {
          //this.msg = res.data;
          this.msg = 'Testingdata';
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