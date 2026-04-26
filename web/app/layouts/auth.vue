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
</script>

<template>
    <div class="min-h-screen flex">
        <!-- Left Side: Image -->
        <div class="hidden lg:block lg:w-1/2 relative bg-zinc-900 overflow-hidden">
            <img
                src="~/assets/images/bg-register.png" alt="Agriculture Farm"
                class="absolute inset-0 w-full h-full object-cover opacity-90 transition-transform duration-1000 hover:scale-105" >
            <!-- Optional Overlay if needed to match a specific vibe -->
            <div class="absolute inset-0 bg-gradient-to-t from-black/40 to-transparent pointer-events-none"/>
        </div>

        <!-- Right Side: Content -->
        <div class="w-full lg:w-1/2 flex flex-col items-center justify-center p-6 sm:p-12 bg-white dark:bg-zinc-950 relative">
            <!-- Dark Mode Toggle -->
            <button
                class="absolute top-6 right-6 h-9 w-9 p-2 rounded-full bg-gray-100 dark:bg-zinc-800 text-gray-600 dark:text-zinc-300 hover:bg-gray-200 dark:hover:bg-zinc-700 transition-colors focus:outline-none focus:ring-2 focus:ring-[#1A7B44]/20"
                @click="toggleDark()">
                <Icon :name="isDark ? 'lucide:moon' : 'lucide:sun'" class="h-5 w-5" />
            </button>
            
            <slot />
        </div>
    </div>
</template>
