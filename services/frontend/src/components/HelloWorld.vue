<template>
  <div>
    <h1> Hi Welcome, GokulDeepak</h1>
    <p>{{ msg }}</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'HelloWorld',
  data: function() {
    return {
      msg: '',
    };
  },
  methods: {
    getMessage() {
    axios.get(`http://192.168.0.106:5000/`)
    .then(response => {
      // JSON responses are automatically parsed.
      this.msg = response.data

      // axios.get('/')
      //   .then((res) => {
      //     this.msg = res;
      //     //this.msg = 'Testingdata';
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