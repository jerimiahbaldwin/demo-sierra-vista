import { createApp } from "vue";
import { createHead } from "@vueuse/head";
import App from "./App.vue";
import router from "./router";

// Import global styles
import './assets/styles/variables.css'
import './assets/styles/base.css'
import './assets/styles/layout.css'
import './assets/styles/components.css'
import './assets/styles/sections.css'
import './assets/styles/responsive.css'

const app = createApp(App);
const head = createHead();

app.use(router);
app.use(head);
app.mount("#app");
