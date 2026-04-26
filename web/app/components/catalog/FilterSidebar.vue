<script setup lang="ts">
import { ref } from 'vue';

const categories = [
  'All', 'Vegetables', 'Fruits', 'Grains & Crops', 'Farming Tools', 'Seeds', 'Fertilizers & Meds'
];

const locations = [
  'All Locations', 'West Java', 'East Java', 'Central Java', 'Jakarta', 'Banten'
];

const selectedCategory = ref('All');
const selectedLocation = ref('All Locations');
const priceRange = ref(500000);

const emit = defineEmits(['filter']);

const applyFilters = () => {
  emit('filter', {
    category: selectedCategory.value,
    location: selectedLocation.value,
    maxPrice: priceRange.value
  });
};

const resetFilters = () => {
  selectedCategory.value = 'All';
  selectedLocation.value = 'All Locations';
  priceRange.value = 500000;
  applyFilters();
}
</script>

<template>
  <aside class="w-full bg-white dark:bg-zinc-950 border border-gray-200 dark:border-zinc-800 rounded-2xl p-6 shadow-sm">
    <div class="flex items-center justify-between mb-6">
      <h3 class="font-bold text-lg text-gray-900 dark:text-zinc-100 flex items-center gap-2">
        <Icon name="lucide:filter" class="w-5 h-5 text-[#1A7B44]" />
        Filters
      </h3>
      <button @click="resetFilters" class="text-sm text-gray-500 hover:text-[#1A7B44] dark:text-zinc-400 dark:hover:text-[#1A7B44] transition-colors">
        Reset
      </button>
    </div>

    <!-- Category Filter -->
    <div class="mb-6">
      <h4 class="font-semibold text-sm text-gray-700 dark:text-zinc-300 mb-3">Category</h4>
      <div class="space-y-2">
        <label v-for="cat in categories" :key="cat" class="flex items-center gap-3 cursor-pointer group">
          <input 
            type="radio" 
            :value="cat" 
            v-model="selectedCategory" 
            name="category"
            class="w-4 h-4 text-[#1A7B44] border-gray-300 focus:ring-[#1A7B44] dark:border-zinc-700 dark:bg-zinc-900 dark:checked:bg-[#1A7B44]"
          />
          <span class="text-sm text-gray-600 dark:text-zinc-400 group-hover:text-gray-900 dark:group-hover:text-zinc-200 transition-colors">
            {{ cat }}
          </span>
        </label>
      </div>
    </div>

    <!-- Location Filter -->
    <div class="mb-6">
      <h4 class="font-semibold text-sm text-gray-700 dark:text-zinc-300 mb-3">Location</h4>
      <div class="relative">
        <select 
          v-model="selectedLocation"
          class="w-full bg-gray-50 dark:bg-zinc-900 border border-gray-200 dark:border-zinc-800 text-gray-700 dark:text-zinc-300 text-sm rounded-lg focus:ring-[#1A7B44]/20 focus:border-[#1A7B44] p-2.5 appearance-none cursor-pointer"
        >
          <option v-for="loc in locations" :key="loc" :value="loc">{{ loc }}</option>
        </select>
        <Icon name="lucide:chevron-down" class="absolute right-3 top-3 w-4 h-4 text-gray-400 pointer-events-none" />
      </div>
    </div>

    <!-- Price Range -->
    <div class="mb-6">
      <h4 class="font-semibold text-sm text-gray-700 dark:text-zinc-300 mb-3 flex justify-between items-center">
        <span>Max Price</span>
        <span class="text-[#1A7B44]">Rp {{ priceRange.toLocaleString('id-ID') }}</span>
      </h4>
      <input 
        type="range" 
        v-model="priceRange" 
        min="0" 
        max="1000000" 
        step="10000"
        class="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer dark:bg-zinc-800 accent-[#1A7B44]"
      />
      <div class="flex justify-between text-xs text-gray-500 dark:text-zinc-500 mt-2">
        <span>Rp 0</span>
        <span>Rp 1.000.000+</span>
      </div>
    </div>

    <button 
      @click="applyFilters"
      class="w-full bg-[#1A7B44] hover:bg-[#156638] text-white font-medium rounded-xl py-3 text-sm transition-colors shadow-sm"
    >
      Apply Filters
    </button>
  </aside>
</template>
