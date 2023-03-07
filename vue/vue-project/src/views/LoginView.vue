
<template>
    <div class="flex min-h-full items-center justify-center py-12 px-4 sm:px-6 lg:px-8">
        <div class="w-full max-w-md space-y-8">
            <div>
                <img class="mx-auto h-12 w-auto" src="../assets/logo.svg" alt="Your Company" />
                <h2 class="mt-6 text-center text-3xl font-bold tracking-tight text-gray-900">Please login</h2>
            </div>
            <form @submit.prevent="login" class="mt-8 space-y-6" action="#" method="POST">
                <input type="hidden" name="remember" value="true" />
                <div class="-space-y-px rounded-md shadow-sm">
                    <div>
                        <label for="username" class="sr-only">Username</label>
                        <input v-model="username" id="username" name="username" type="text" autocomplete="" required=""
                            class="relative block w-full rounded-t-md border-0 py-1.5 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:z-10 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
                            placeholder="Username" />
                    </div>
                    <div>
                        <label for="password" class="sr-only">Password</label>
                        <input v-model="password" id="password" name="password" type="password"
                            autocomplete="current-password" required=""
                            class="relative block w-full rounded-b-md border-0 py-1.5 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:z-10 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
                            placeholder="Password" />
                    </div>
                </div>

                <div>
                    <button type="submit"
                        class="group relative flex w-full justify-center rounded-md bg-green-600 py-2 px-3 text-sm font-semibold text-white hover:bg-green-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-green-600">
                        <span class="absolute inset-y-0 left-0 flex items-center pl-3">
                            <LockClosedIcon class="h-5 w-5 text-green-500 group-hover:text-green-400" aria-hidden="true" />
                        </span>
                        Sign in
                    </button>
                </div>
            </form>
        </div>
    </div>
</template>

<script>
// import axios from 'axios'
// import VueCookies from 'vue-cookies'

// export default {
//     name: 'Login',
//     data() {
//         return {
//             formData: {
//                 username: '',
//                 password: '',
//             }
//         }
//     },
//     methods: {
//         async loginUser() {
//             const response = await axios.post('http://127.0.0.1:5000/login', this.formData)
//                 .then()
//                 .catch((error) => (console.log(error)))
//             VueCookies.set("token", response.data.auth_token)
//             if(response.status == 200){
//                 this.$router.push('/home')

//             }
//         }
//     }
// }
import { LockClosedIcon } from '@heroicons/vue/20/solid'
import { useUserStore } from "../stores/auth";

export default {
    setup() {
        const userStore = useUserStore();
        return { userStore }
    },
    data() {
        return {
            username: "",
            password: "",
        }
    },
    methods: {
        async login() {
            await this.userStore.loginUser(this.username, this.password)
            this.$router.push('/home')
        }
    }
}
</script>