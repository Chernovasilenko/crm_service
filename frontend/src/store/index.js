import { createStore } from 'vuex'

export default createStore({
  state: {
    isLoading: false,
    isAuthenticated: false,
    token: '',
    user: {
      id: 0,
      username: '',
    },
    team: {
      id: 0,
      name: '',
    }
  },
  getters: {
  },
  mutations: {
    initializeStore(state) {
      const token = localStorage.getItem('token');
      if (localStorage.getItem('token')) {
        state.token = localStorage.getItem('token');
        state.isAuthenticated = true;
        state.user.username = localStorage.getItem('username');
        state.user.id = localStorage.getItem('user_id');
        state.team.name = localStorage.getItem('team_name');
        state.team.id = localStorage.getItem('team_id');
      } else {
        state.token = '';
        state.isAuthenticated = false;
        state.user.id = 0;
        state.user.username = '';
        state.team.id = 0;
        state.team.name = '';
      }
    },
    setIsLoading(state, status) {
      state.isLoading = status
    },
    setToken(state, token) {
      state.token = token
      state.isAuthenticated = true
    },
    removeToken(state) {
      state.token = ''
      state.isAuthenticated = false
    },
    setUser(state, user) {
      state.user = user
    },
    setTeam(state, team) {
      state.team = team

      localStorage.setItem('team_name', team.name)
      localStorage.setItem('team_id', team.id)
    }
  },
  actions: {
  },
  modules: {
  }
})
