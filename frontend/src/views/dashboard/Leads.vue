<template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">Leads</h1>

          <router-link class="button is-primary" to="/dashboard/leads/add">Add new lead</router-link>

          <hr>

          <form @submit.prevent="getLeads()">
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
          <table class="table is-fullwidth">
            <thead>
              <tr>
                <th>Company</th>
                <th>Contact person</th>
                <th>Assigned to</th>
                <th>Status</th>
                <th></th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="lead in leads" v-bind:key="lead.id">
                <td>{{ lead.company }}</td>
                <td>{{ lead.contact_name }}</td>
                <td>
                  <template v-if="lead.assigned_to">{{ lead.assigned_to.first_name }} {{ lead.assigned_to.last_name }}</template>
                </td>
                <td>{{ lead.status }}</td>
                <td><router-link v-bind:to="`/dashboard/leads/${lead.id}`">Details</router-link></td>
              </tr>
            </tbody>
          </table>

          <div class="buttons">
            <button class="button is-light" v-if="showPrevButton" @click="goToPrevPage()">Previous</button>
            <button class="button is-light" v-if="showNextButton" @click="goToNextPage()">Next</button>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
    import axios from 'axios'

    export default {
      name: 'Leads',
      data() {
        return {
          leads: [],
          showNextButton: false,
          showPrevButton: false,
          currentPage: 1,
          searchTerm: '',
        }
      },
      mounted() {
        this.getLeads()
      },
      methods: {
        async goToNextPage() {
          this.currentPage += 1
          this.getLeads()
        },
        async goToPrevPage() {
          this.currentPage -= 1
          this.getLeads()
        },
        async getLeads() {
          this.$store.commit('setIsLoading', true)

          await axios
            .get(`/api/v1/leads/?page=${this.currentPage}&search=${this.searchTerm}`)
            .then(response => {
              this.leads = response.data.results
              
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
        },
      }
    }
  </script>
