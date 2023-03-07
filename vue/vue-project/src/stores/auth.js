import { defineStore } from "pinia";
import axios from 'axios'

export const useUserStore = defineStore('user', {
    state: () => ({
        token: null,
        username: null
    }),

    actions: {
        async fetchUser() { },
        async registerUser(username, password) { },
        async loginUser(username, password) {
            const res = await axios.post("http://127.0.0.1:5000/login", JSON.stringify({ username, password }), {
                headers: {
                    'Content-Type': 'application/json'
                }
            });
            console.log(res)
            this.$state.username = this.username
            // const user = await res.data.username;
            this.$state.token = res.data.auth_token;    
        },

    }
})