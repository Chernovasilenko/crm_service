<template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">Add lead</h1>
      </div>

      <div class="column is-12">
        <form @submit.prevent="submitForm">
          <div class="field">
            <label class="label">Company</label>
            <div class="control">
              <input class="input" type="text" placeholder="Company" v-model="company">
            </div>
          </div>

          <div class="field">
            <label class="label">Contact person</label>
            <div class="control">
              <input class="input" type="text" placeholder="Contact person" v-model="contact_person">
            </div>
          </div>

          <div class="field">
            <label class="label">Email</label>
            <div class="control">
              <input class="input" type="email" placeholder="Email" v-model="email">
            </div>
          </div>

          <div class="field">
            <label class="label">Phone</label>
            <div class="control">
              <input class="input" type="text" placeholder="Phone" v-model="phone">
            </div>
          </div>

          <div class="field">
            <label class="label">Website</label>
            <div class="control">
              <input class="input" type="text" placeholder="Website" v-model="website">
            </div>
          </div>

          <div class="field">
            <label class="label">Confidence</label>
            <div class="control">
              <input class="input" type="number" placeholder="Confidence" v-model="confidence">
            </div>
          </div>

          <div class="field">
            <label class="label">Estimated value</label>
            <div class="control">
              <input class="input" type="number" placeholder="Estimated value" v-model="estimated_value">
            </div>
          </div>

          <div class="field">
            <label class="label">Status</label>
            <div class="control">
              <div class="select">
                <select v-model="status">
                  <option value="new">New</option>
                  <option value="contacted">Contacted</option>
                  <option value="in_progress">In progress</option>
                  <option value="won">Won</option>
                  <option value="lost">Lost</option>
                </select>
              </div>
            </div>
          </div>

          <div class="field">
            <label class="label">Priority</label>
            <div class="control">
              <div class="select">
                <select class="select" v-model="priority">
                  <option value="low">Low</option>
                  <option value="medium">Medium</option>
                  <option value="high">High</option>
                </select>
              </div>
            </div>
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
  import { toast } from 'bulma-toast'

  export default {
    name: 'AddLead',
    data() {
      return {
        company: '',
        contact_person: '',
        email: '',
        phone: '',
        website: '',
        confidence: 0,
        estimated_value: 0,
        status: 'new',
        priority: 'medium'
      }
    },
    methods: {
      async submitForm() {
        this.$store.commit('setIsLoading', true)
        const lead = {
          company: this.company,
          contact_name: this.contact_person,
          email: this.email,
          phone: this.phone,
          website: this.website,
          confidence: this.confidence,
          estimated_value: this.estimated_value,
          status: this.status,
          priority: this.priority
        }

        await axios
          .post('/api/v1/leads/', lead)
          .then(response => {
            toast({
              message: 'Lead added',
              type: 'is-success',
              dismissible: true,
              pauseOnHover: true,
              duration: 2000,
              position: 'bottom-right',
            })
            this.$router.push('/dashboard/leads')
          })
          .catch(error => {
            console.log(JSON.stringify(error))
          })

        this.$store.commit('setIsLoading', false)
      }
    }
  }
</script>