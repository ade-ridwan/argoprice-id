<script setup lang="ts">
import { ref, onMounted } from 'vue';

const isDark = ref(false)

onMounted(() => {
    if (localStorage.getItem('theme') === 'dark') {
        isDark.value = true;
        document.documentElement.classList.add('dark');
    } else {
        isDark.value = false;
        document.documentElement.classList.remove('dark');
    }
})

const toggleDark = () => {
    isDark.value = !isDark.value;
    if (isDark.value) {
        document.documentElement.classList.add('dark');
        localStorage.setItem('theme', 'dark');
    } else {
        document.documentElement.classList.remove('dark');
        localStorage.setItem('theme', 'light');
    }
}

const navItems = [
  { name: 'Home', path: '/' },
  { name: 'Products', path: '/products' },
  { name: 'Graphs', path: '/graph' },
  { name: 'Predictions', path: '#' },
];
</script>

<template>
  <nav class="sticky top-0 z-50 w-full bg-white/90 dark:bg-zinc-950/90 backdrop-blur-md border-b border-gray-100 dark:border-zinc-800">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex justify-between items-center h-16">
        <!-- Logo -->
        <div class="flex-shrink-0 flex items-center">
          <NuxtLink to="/" class="flex items-center gap-2">
            <AppLogo />
          </NuxtLink>
        </div>

        <!-- Desktop Menu -->
        <div class="hidden md:flex space-x-8">
          <NuxtLink 
            v-for="item in navItems" 
            :key="item.name" 
            :to="item.path"
            class="text-sm font-semibold text-gray-700 dark:text-zinc-300 hover:text-[#1A7B44] dark:hover:text-[#1A7B44] transition-colors"
            active-class="text-[#1A7B44] dark:text-[#1A7B44]"
          >
            {{ item.name }}
          </NuxtLink>
        </div>

        <!-- Auth Buttons -->
        <div class="hidden md:flex items-center space-x-4">
          <!-- Dark Mode Toggle -->
          <button
            class="p-2 rounded-full bg-gray-100 w-9 h-9 dark:bg-zinc-800 text-gray-600 dark:text-zinc-300 hover:bg-gray-200 dark:hover:bg-zinc-700 transition-colors focus:outline-none focus:ring-2 focus:ring-[#1A7B44]/20"
            @click="toggleDark()">
            <Icon :name="isDark ? 'lucide:moon' : 'lucide:sun'" class="h-4 w-4 sm:h-5 sm:w-5" />
          </button>
          
          <NuxtLink 
            to="/login" 
            class="text-sm font-semibold text-gray-700 dark:text-zinc-300 hover:text-[#1A7B44] transition-colors"
          >
            Login
          </NuxtLink>
          <NuxtLink 
            to="/register" 
            class="text-sm font-medium bg-[#1A7B44] hover:bg-[#156638] text-white px-4 py-2 rounded-lg transition-colors shadow-sm"
          >
            Register
          </NuxtLink>
        </div>

        <!-- Mobile Menu Button (Hamburger) -->
        <div class="flex items-center gap-3 md:hidden">
          <button
            class="p-2 rounded-full bg-gray-100 dark:bg-zinc-800 text-gray-600 dark:text-zinc-300 hover:bg-gray-200 dark:hover:bg-zinc-700 transition-colors focus:outline-none"
            @click="toggleDark()">
            <Icon :name="isDark ? 'lucide:moon' : 'lucide:sun'" class="h-5 w-5" />
          </button>
          <button type="button" class="text-gray-500 hover:text-gray-700 focus:outline-none">
            <Icon name="lucide:menu" class="h-6 w-6" />
          </button>
        </div>
      </div>
    </div>
  </nav>
</template>
