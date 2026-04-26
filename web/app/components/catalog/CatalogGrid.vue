<script setup lang="ts">
import ProductCard from '../home/ProductCard.vue';
import type { Product } from '../home/ProductCard.vue';

interface Props {
  products: Product[];
  totalResults: number;
}

const { products, totalResults } = defineProps<Props>();
</script>

<template>
  <div class="flex flex-col">
    <!-- Header -->
    <div class="flex flex-col sm:flex-row items-start sm:items-center justify-between mb-6 gap-4">
      <h2 class="text-xl font-bold text-gray-900 dark:text-zinc-100">
        Showing <span class="text-[#1A7B44]">{{ totalResults }}</span> results
      </h2>
      
      <!-- Sort -->
      <div class="flex items-center gap-2">
        <span class="text-sm text-gray-500 dark:text-zinc-400">Sort by:</span>
        <div class="relative">
          <select class="pl-3 pr-8 py-2 bg-white dark:bg-zinc-900 border border-gray-200 dark:border-zinc-800 text-sm text-gray-700 dark:text-zinc-300 rounded-lg appearance-none cursor-pointer focus:ring-[#1A7B44]/20 focus:border-[#1A7B44]">
            <option value="newest">Newest</option>
            <option value="price_asc">Price: Low to High</option>
            <option value="price_desc">Price: High to Low</option>
            <option value="rating">Highest Rating</option>
          </select>
          <Icon name="lucide:chevron-down" class="absolute right-3 top-2.5 w-4 h-4 text-gray-400 pointer-events-none" />
        </div>
      </div>
    </div>

    <!-- Grid -->
    <div v-if="products.length > 0" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
      <ProductCard 
        v-for="product in products" 
        :key="product.id" 
        :product="product" 
      />
    </div>

    <!-- Empty State -->
    <div v-else class="flex flex-col items-center justify-center py-16 px-4 bg-white dark:bg-zinc-950 border border-gray-200 dark:border-zinc-800 rounded-2xl">
      <div class="w-16 h-16 bg-gray-100 dark:bg-zinc-900 rounded-full flex items-center justify-center mb-4">
        <Icon name="lucide:search-x" class="w-8 h-8 text-gray-400" />
      </div>
      <h3 class="text-lg font-bold text-gray-900 dark:text-zinc-100 mb-2">No products found</h3>
      <p class="text-gray-500 dark:text-zinc-400 text-center max-w-sm">
        We couldn't find any products matching your current filters. Try adjusting them or clearing the search.
      </p>
    </div>

    <!-- Pagination / Load More -->
    <div v-if="products.length > 0" class="mt-12 flex justify-center">
      <button class="bg-white dark:bg-zinc-900 text-gray-700 dark:text-zinc-300 border border-gray-200 dark:border-zinc-800 hover:bg-gray-50 dark:hover:bg-zinc-800 px-8 py-3 rounded-xl font-medium transition-colors shadow-sm">
        Load More Products
      </button>
    </div>
  </div>
</template>
