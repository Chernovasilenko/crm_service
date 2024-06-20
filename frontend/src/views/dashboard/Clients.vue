<template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">Clients</h1>

          <router-link class="button is-primary" to="/dashboard/clients/add">Add client</router-link>

          <hr>

          <form @submit.prevent="getClients()">
            <div class="field has-addons">
              <div class="control">
                <input class="input" type="text" placeholder="Search" v-model="searchTerm">
              </div>
              <div class="control">
                <button class="button is-primary">Search</button>
              </div>
            </div>
          </form>

        </div>

        <div class="column is-12">
          <template v-if="clients.length">
            <table class="table is-fullwidth">
              <thead>
                <tr>
                  <th>Name</th>
                  <th>Contact person</th>
                  <th></th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="client in clients" v-bind:key="client.id">
                  <td>{{ client.name }}</td>
                  <td>{{ client.contact_name }}</td>
                  <td><router-link :to="{name: 'Client', params: {id: client.id}}">Details</router-link></td>
                </tr>
              </tbody>
            </table>
            <div class="buttons">
              <button class="button is-light" v-if="showPrevButton" @click="goToPrevPage()">Previous</button>
              <button class="button is-light" v-if="showNextButton" @click="goToNextPage()">Next</button>
            </div>
          </template>
          <template v-else>
            <p>No clients found</p>
          </template>
        </div>
      </div>
    </div>
  </template>
    
    <script>
      import axios from 'axios'
  
      export default {
        name: 'Clients',
        data() {
          return {
            clients: [],
          showNextButton: false,
          showPrevButton: false,
          currentPage: 1,
          searchTerm: '',
          }
        },
        mounted() {
          this.getClients()
        },
        methods: {
          async goToNextPage() {
            this.currentPage += 1
            this.getClients()
          },
          async goToPrevPage() {
            this.currentPage -= 1
            this.getClients()
          },
          async getClients() {
            this.$store.commit('setIsLoading', true)
  
            await axios
              .get(`/api/v1/clients/?page=${this.currentPage}&search=${this.searchTerm}`)
              .then(response => {
                this.clients = response.data.results

                if (response.data.next) {
                  this.showNextButton = true
                } else {
                  this.showNextButton = false
                }

                if (response.data.previous) {
                  this.showPrevButton = true
                } else {
                  this.showPrevButton = false
                }
              })
              .catch(error => {
                console.log(JSON.stringify(error))
              })
            this.$store.commit('setIsLoading', false)
          }
        }
      }
    </script>
  