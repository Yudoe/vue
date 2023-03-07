<template>
  <h1 class="text-center text-gray-700">Hello, {{ userStore.user }}</h1>
</template>

<script>
import { useUserStore } from '../stores/auth';
export default {
  setup() {
    const userStore = useUserStore;
    return { userStore };
  }
}
</script>