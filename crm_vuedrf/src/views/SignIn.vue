<template>
    <div class="container">
      <div class="columns">
        <div class="column is-4 is-offset-4">
          <h1 class="title">Sign In</h1>
  
          <form @submit.prevent="submitForm">
            <div class="field">
              <label class="label">Email</label>
              <div class="control">
                <input class="input" type="email" placeholder="Email" v-model="username">
              </div>
            </div>

            <div class="field">
              <label class="label">Password</label>
              <div class="control">
                <input class="input" type="password" name="password" placeholder="Password" v-model="password">
              </div>
            </div>

            <div class="notification is-danger" v-if="errors.length">
              <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
            </div>
            
            <div class="field">
              <div class="control">
                <button class="button is-success">Submit</button>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
  </template>
  
  <script>
    import axios from 'axios'

    export default {
      name: 'SignIn',
      data() {
        return {
          username: '',
          password: '',
          errors: []
        }
      },
      methods: {
        async submitForm() {
          this.$store.commit('setIsLoading', true)

          axios.defaults.headers.common['Authorization'] = ''
          localStorage.removeItem('token')

          const formData = {
            username: this.username,
            password: this.password
          }

          await axios
            .post('/api/v1/token/login/', formData)
            .then(response => {
              const token = response.data.auth_token

              this.$store.commit('setToken', token)

              axios.defaults.headers.common['Authorization'] = 'Token ' + token
              console.log(axios.defaults.headers.common['Authorization'])

              localStorage.setItem('token', token)
            })
            .catch(error => {
              if (error.response) {
                for (const property in error.response.data) {
                  this.errors.push(`${property}: ${error.response.data[property]}`)
                }
              } else if (error.message) {
                this.errors.push('Something went wrong. Please try again')
              }
            })

            await axios
              .get('/api/v1/users/me/')
              .then(response => {
                this.$store.commit('setUser', {'username': response.data.username, 'id': response.data.id})

                localStorage.setItem('username', response.data.username)
                localStorage.setItem('user_id', response.data.id)
              })
              .catch(error => {
                console.log(error)
              })

              await axios
                .get('/api/v1/teams/get_my_team/')
                .then(response => {
                  this.$store.commit('setTeams', {'id': response.data.id, 'name': response.data.name})

                  this.$router.push('/dashboard/my-account')
                })
                .catch(error => {
                  console.log(error)
                })

            this.$store.commit('setIsLoading', false)
          }
        }
      }
  </script>