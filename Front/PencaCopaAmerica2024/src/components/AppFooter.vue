<template>
    <div class="container">
    <footer class="py-3 my-4">
        <ul class="nav justify-content-center border-bottom pb-3 mb-3">
            <li class="nav-item"><a href="#" class="nav-link px-2 text-white">Features</a></li>
            <li class="nav-item"><router-link to="/pricing" class="nav-link px-2 text-white">Pricing</router-link></li>
            <li class="nav-item"><router-link to="/FAQs" class="nav-link px-2 text-white">FAQs</router-link></li>
            <li class="nav-item"><router-link to="/rules" class="nav-link px-2 text-white">Rules</router-link></li>
        </ul>
        <p class="text-center text-white">&copy; 2024 Penca UCU</p>
    </footer>
  </div>
</template>

<script>

export default {
  name: 'AppFooter'
}
</script>

<style scoped>

</style>