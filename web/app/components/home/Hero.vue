<script setup lang="ts">
import { ref } from 'vue';

const searchQuery = ref('');
</script>

<template>
  <div class="relative w-full min-h-[500px] flex items-center justify-center pb-8 md:py-16 bg-zinc-900 overflow-hidden">
    <!-- Background Image -->
    <img src="~/assets/images/bg-home.png" alt="Agriculture Farm" class="absolute inset-0 w-full h-full object-cover opacity-100">
    
    <!-- Gradient Overlay for better text readability -->
    <div class="absolute inset-0 bg-gradient-to-b from-black/30 via-black/30 to-black/10"/>

    <!-- Content -->
    <div class="relative z-10 w-full max-w-4xl mx-auto px-4 sm:px-6 text-center pt-8">
      <!-- Tag -->
      <div class="inline-flex items-center px-3 py-1 rounded-full bg-orange-400 border border-orange-400 text-white text-xs font-semibold uppercase tracking-wider mb-6">
        <!-- <Icon name="lucide:sparkles" class="w-3 h-3 mr-1.5" /> -->
        #1 Local Agriculture Marketplace
      </div>

      <!-- Headline -->
      <h1 class="text-3xl md:text-5xl lg:text-6xl font-bold text-white mb-4 leading-tight">
        Buy Agricultural Products & Needs <br class="hidden md:block">
        <span class="text-orange-400">Directly from Local Farmers</span>
      </h1>

      <!-- Subheadline -->
      <p class="mt-4 text-base md:text-lg text-gray-200 max-w-2xl mx-auto mb-8 font-light">
        A platform that connects farmers directly with buyers. 
        Get fair prices and fresh products easily & quickly.
      </p>

      <!-- Search Bar -->
      <div class="max-w-2xl mx-auto bg-white dark:bg-zinc-900 rounded-2xl p-2 flex flex-col sm:flex-row items-center shadow-lg border border-white/20 gap-2 sm:gap-0">
        <div class="flex items-center w-full flex-1">
          <div class="flex items-center pl-3 text-gray-400">
            <Icon name="lucide:search" class="w-5 h-5" />
          </div>
          <input 
            v-model="searchQuery"
            type="text" 
            placeholder="Search commodity name or city..." 
            class="flex-1 bg-transparent border-none focus:ring-0 text-sm md:text-base text-gray-900 dark:text-zinc-100 px-3 py-2 sm:py-3 outline-none min-w-0"
          >
        </div>
        <button class="w-full sm:w-auto bg-[#1A7B44] hover:bg-[#156638] text-white px-6 py-3 rounded-xl font-medium transition-colors text-sm md:text-base shrink-0">
          Search Now
        </button>
      </div>

      <!-- Quick Stats / Trust Indicators -->
      <div class="mt-8 flex flex-wrap items-center justify-center gap-4 sm:gap-6 text-sm text-gray-300">
        <div class="flex items-center gap-2">
          <Icon name="lucide:check-circle-2" class="w-4 h-4 text-[#1A7B44] shrink-0" />
          <span>Transparent Pricing</span>
        </div>
        <div class="flex items-center gap-2">
          <Icon name="lucide:check-circle-2" class="w-4 h-4 text-[#1A7B44] shrink-0" />
          <span>Directly from the Farm</span>
        </div>
      </div>
    </div>
  </div>
</template>
