<template>
  <div id="app">
    <header>
      <h1>{{ title }}</h1>
    </header>
    <main>
      <p>{{ message }}</p>
      <p class="deployment-info">🚀 Deployed via GitHub Actions CI/CD</p>
      <button @click="incrementCounter">Clicked {{ counter }} times</button>
    </main>
  </div>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      title: 'Demo Sierra Vista',
      message: 'Welcome to your Vue.js application!',
      counter: 0
    }
  },
  methods: {
    incrementCounter() {
      this.counter++
    }
  }
}
</script>

<style scoped>
#app {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

header {
  margin-bottom: 2rem;
}

h1 {
  font-size: 2.5rem;
  color: #42b983;
}

main {
  max-width: 600px;
  margin: 0 auto;
}

p {
  font-size: 1.2rem;
  margin-bottom: 1.5rem;
}

.deployment-info {
  font-size: 0.9rem;
  color: #666;
  font-style: italic;
  margin-bottom: 2rem;
}

button {
  background-color: #42b983;
  color: white;
  border: none;
  padding: 12px 24px;
  font-size: 1rem;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s;
}

button:hover {
  background-color: #35a372;
}
</style>
