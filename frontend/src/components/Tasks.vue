<template>
  <div class="container">
    <div align="center">
      <div class="col-sm-8 col-md-6 col-lg-6">
      <p>タスクの登録</p>
        <b-form v-if="show">
          <b-form-group label="Title:"
                        label-for="title">
            <b-form-input id="title"
                          type="text"
                          required
                          placeholder="Enter title">
            </b-form-input>
          </b-form-group>
          <b-form-group label="Text:"
                        label-for="title">
            <b-form-textarea id="text"
                             placeholder="Enter something"
                             :rows="3"
                             :max-rows="6">
            </b-form-textarea>
          </b-form-group>
          <div align="center">
            <div class="col-sm-4 col-md-2 col-lg-2">
              <b-button block @click="addTask" variant="success">Add</b-button>
            </div>
          </div>
        </b-form>
      </div>
    </div>

    <b-list-group v-for="(task, index) in tasks" :key='index'>
      <b-list-group-item>
        {{ task.title }}<br>
        {{ task.text }}
        <b-button v-bind:src="task.id" block @click="deleteTasks(index, task.id)">削除</b-button>
      </b-list-group-item>
    </b-list-group>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  data () {
    return {
      randomNumber: 0,
      tasks: [],
      show: true
    }
  },
  methods: {
    getTasks () {
      const path = 'http://localhost:5000/api/get'
      axios.get(path)
        .then(response => {
          this.tasks = response.data
        })
        .catch(error => {
          console.log(error)
        })
    },
    addTask () {
      const path = 'http://localhost:5000/api/add'
      var title = document.getElementById('title')
      var text = document.getElementById('text')
      let params = new URLSearchParams()
      params.append('title', title.value)
      params.append('text', text.value)
      var titleValue = title.value
      var textValue = text.value
      title.value = ''
      text.value = ''
      axios.post(path, params)
        .then(response => {
          var id = response.data
          var task = {'id': id, 'text': textValue, 'title': titleValue}
          this.tasks.unshift(task)
          console.log(response)
        })
        .catch(error => {
          console.log(error)
        })
    },
    deleteTasks (taskIndex, taskId) {
      console.log(taskIndex)
      console.log(taskId)
      const path = 'http://localhost:5000/api/delete'
      let params = new URLSearchParams()
      params.append('id', taskId)
      this.tasks.splice(taskIndex, 1)
      axios.post(path, params)
        .then(response => {
          console.log(response)
        })
        .catch(error => {
          console.log(error)
        })
    }
  },
  created () {
    this.getTasks()
  }
}
</script>
