<template>
  <div class="pastearea">

    <div v-if="type === 'new'">
      <h1>
      New paste
      </h1>
      
      <br>
      <form v-on:submit.prevent="write_paste">
      <textarea rows=20, cols=100, name="pastearea" v-model="content">
      </textarea>
      <br><br>
      <button class="button">Submit</button>
      </form>

      <br>
      <p v-if="shortlink">
      Your content can be found at:
      <a :href="url_link">{{ url_link }}</a>
      </p>
    </div>

    <div v-if="type === 'existing'">
      <h1>{{ shortlink }}</h1>
      <textarea rows=20, cols=100 :value="content" style="background-color: light-grey" readonly>
      </textarea>

      <ul>
        <li>Created at: {{ created_at }}</li><br><br>
        <li>Expires at: {{ expires_at }}</li>
      </ul>
    </div>

  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Paste',
  data() {
    return {
      type: "new",
      content: "",
      shortlink: "",
      url_link: "",
    }
  },
  created() {
    let uri = window.location.search.substring(1); 
    let params = new URLSearchParams(uri);
    if(params.get("shortlink")) {
      this.type = "existing";
      this.shortlink = params.get("shortlink");
      this.urllink = uri;
      this.read_paste(this.shortlink);
    }
  },
  methods: {
    async write_paste() {
      let body = { "expiration_length_in_minutes": "43200", "paste_contents": this.content };
      axios.post("http://127.0.0.1:5000/api/v1/paste", JSON.stringify(body), {
        headers: { "Content-Type": "application/json"}
      })
      .then(response => {
        this.shortlink = response.data.shortlink;
        this.url_link = "http://localhost:8080?shortlink=" + this.shortlink;
      })
      .catch(error => console.log(error))
    },
    async read_paste(shortlink) {
      axios.get("http://127.0.0.1:5000/api/v1/paste?shortlink=" + shortlink, {
        headers: { "Content-Type": "application/json"}
      })
      .then(response => {
        this.content = response.data.paste_contents;
        this.created_at = response.data.created_at;
        this.expires_at = response.data.expires_at;
      })
      .catch(error => console.log(error))
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
