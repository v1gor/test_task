<template>
  <div class="hello">

    <h2>TTEST</h2>
    <div class="container">
      <div class="large-12 medium-12 small-12 cell">
        <label>File
          <input type="file" id="file" ref="file" v-on:change="handleFileUpload()"/>
        </label>
          <button v-on:click="submitFile()">Send</button>
      </div>
    </div>
  </div>
</template>

<script>
import { axios } from '@/plugins/axios'

export default {
  name: 'FileSender',
  data () {
    return {
      file: '',
      msg: 'Welcome to Your Vue.js App'
    }
  },

  methods: {
    handleFileUpload(){
      this.file = this.$refs.file.files[0];
    },
    submitFile(){
            /*
                    Initialize the form data
                */
                let formData = new FormData();

                /*
                    Add the form data we need to submit
                */
                formData.append('file', this.file);

            /*
              Make the request to the POST /single-file URL
            */
                axios.post( 'http://127.0.0.1:8000/api/upload_excel',
                    formData,
                    {
                    headers: {
                        'Content-Type': 'multipart/form-data'
                    }
                  }
                ).then(function(){
              console.log('SUCCESS!!');
            })
            .catch(function(){
              console.log('FAILURE!!');
            });
          },
    updateSuccessful(response){
      console.log('YES');
    }
  }
}
</script>
