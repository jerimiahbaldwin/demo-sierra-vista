<template>
  <header class="site-header">
    <div class="container">
      <div class="header-content">
        <div class="logo">
          <router-link to="/">
            <img src="/download/files/2019/03/sierra_vista_new.png" alt="Sierra Vista Plumbing, Inc." />
          </router-link>
        </div>
        <button type="button" class="mobile-menu-toggle" :class="{ 'is-open': isMenuOpen }"
          aria-label="Toggle main menu" :aria-expanded="isMenuOpen" @click="toggleMenu">
          <span class="menu-toggle-label">Menu</span>
          <span class="menu-toggle-icon" aria-hidden="true"></span>
        </button>

        <nav class="main-nav" :class="{ 'is-open': isMenuOpen }" :aria-hidden="isMobileView && !isMenuOpen">
          <template v-for="item in navigationMenu" :key="item.label">
            <router-link v-if="item.type === 'link'" :to="item.path" @click="handleNavLinkClick">
              {{ item.label }}
            </router-link>
            <div v-else-if="item.type === 'dropdown'" class="nav-dropdown"
              :class="{ 'is-open': isDropdownOpen(item.label) }">
              <button type="button" class="nav-dropdown-toggle" :aria-expanded="isDropdownOpen(item.label)"
                @click="toggleDropdown(item.label)">
                <span>{{ item.label }}</span>
                <span class="dropdown-caret" aria-hidden="true">▾</span>
              </button>
              <div class="nav-dropdown-menu">
                <router-link v-for="subItem in item.items" :key="subItem.path" :to="subItem.path"
                  @click="handleNavLinkClick">
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
import { onBeforeUnmount, onMounted, ref, watch } from 'vue'
import { useRoute } from 'vue-router'
import { navigationMenu, contactInfo } from '../config/navigation'

const route = useRoute()
const isMenuOpen = ref(false)
const isMobileView = ref(false)
const openDropdownLabel = ref('')

const updateViewportState = () => {
  const mobile = window.innerWidth <= 960
  isMobileView.value = mobile

  if (!mobile) {
    isMenuOpen.value = false
    openDropdownLabel.value = ''
    document.body.style.overflow = ''
  }
}

const closeMenu = () => {
  isMenuOpen.value = false
  openDropdownLabel.value = ''
}

const toggleMenu = () => {
  isMenuOpen.value = !isMenuOpen.value

  if (!isMenuOpen.value) {
    openDropdownLabel.value = ''
  }
}

const toggleDropdown = (label) => {
  if (!isMobileView.value) {
    return
  }

  openDropdownLabel.value = openDropdownLabel.value === label ? '' : label
}

const isDropdownOpen = (label) => {
  if (!isMobileView.value) {
    return false
  }

  return openDropdownLabel.value === label
}

const handleNavLinkClick = () => {
  if (isMobileView.value) {
    closeMenu()
  }
}

watch(isMenuOpen, (isOpen) => {
  if (isMobileView.value) {
    document.body.style.overflow = isOpen ? 'hidden' : ''
  }
})

watch(
  () => route.fullPath,
  () => {
    closeMenu()
  }
)

onMounted(() => {
  updateViewportState()
  window.addEventListener('resize', updateViewportState)
})

onBeforeUnmount(() => {
  window.removeEventListener('resize', updateViewportState)
  document.body.style.overflow = ''
})
</script>
