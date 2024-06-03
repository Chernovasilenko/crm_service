<template>
  <div class="container">
    <div class="columns">
      <div class="column is-4 is-offset-4">
        <h1 class="title">Sign Up</h1>

        <form>
          <div class="field">
            <label class="label">Email</label>
            <div class="control">
              <input class="input" type="email" placeholder="Email">
            </div>
          </div>
          <div class="field">
            <label class="label">Password</label>
            <div class="control">
              <input class="input" type="password" name="password1" placeholder="Password">
            </div>
          </div>
          <div class="field">
            <label class="label">Repeat Password</label>
            <div class="control">
              <input class="input" type="password" name="password2" placeholder="Repeat Password">
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
  export default {
    name: 'SignUp'
  }
</script>