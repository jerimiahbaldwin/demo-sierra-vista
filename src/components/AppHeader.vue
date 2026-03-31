<template>
  <header class="site-header">
    <div class="container">
      <div class="header-content">
        <div class="logo">
          <router-link to="/">
            <img src="/download/files/2019/03/sierra_vista_new.png" alt="Sierra Vista Plumbing, Inc." />
          </router-link>
        </div>
        <nav class="main-nav">
          <template v-for="item in navigationMenu" :key="item.label">
            <router-link v-if="item.type === 'link'" :to="item.path">
              {{ item.label }}
            </router-link>
            <div v-else-if="item.type === 'dropdown'" class="nav-dropdown">
              <span class="nav-dropdown-toggle">{{ item.label }} ▾</span>
              <div class="nav-dropdown-menu">
                <router-link v-for="subItem in item.items" :key="subItem.path" :to="subItem.path">
                  {{ subItem.label }}
                </router-link>
              </div>
            </div>
          </template>
        </nav>
        <div class="header-contact">
          <div class="phone-number">
            <span class="label">Call Us Today!</span>
            <a :href="`tel:${contactInfo.phoneRaw}`" class="phone">{{ contactInfo.phone }}</a>
          </div>
        </div>
      </div>
    </div>
  </header>
</template>

<script setup>
import { navigationMenu, contactInfo } from '../config/navigation'
</script>
