<script setup lang="ts">
import ProductCard from './ProductCard.vue';
import type { Product } from './ProductCard.vue';

interface Props {
  products: Product[];
}

const { products } = defineProps<Props>();
</script>

<template>
  <section class="py-16 bg-gray-50 dark:bg-zinc-950/50">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <!-- Header -->
      <div class="flex items-end justify-between mb-8">
        <div>
          <h2 class="text-2xl font-bold text-gray-900 dark:text-zinc-100">Our Products</h2>
          <div class="h-1 w-12 bg-[#1A7B44] mt-2 rounded-full"/>
        </div>
        <NuxtLink to="#" class="text-sm font-semibold text-[#1A7B44] hover:text-[#156638] flex items-center gap-1 group">
          View All 
          <Icon name="lucide:arrow-right" class="w-4 h-4 transition-transform group-hover:translate-x-1" />
        </NuxtLink>
      </div>

      <!-- Grid -->
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
        <ProductCard 
          v-for="product in products" 
          :key="product.id" 
          :product="product" 
        />
      </div>
    </div>
  </section>
</template>
