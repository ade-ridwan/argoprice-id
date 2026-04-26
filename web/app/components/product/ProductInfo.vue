<script setup lang="ts">
export interface ProductData {
  title: string;
  price: string;
  unit: string;
  rating: number;
  soldCount: number;
  category: string;
  condition: string;
  minOrder: number;
  weight: string;
}

const { product } = defineProps<{ product: ProductData }>();
</script>

<template>
  <div>
    <!-- Title & Basic Info -->
    <div class="mb-6 border-b border-gray-200 dark:border-zinc-800 pb-6">
      <div class="flex items-center gap-2 text-sm text-gray-500 dark:text-zinc-400 mb-2">
        <NuxtLink to="/products" class="hover:text-[#1A7B44] transition-colors">Products</NuxtLink>
        <Icon name="lucide:chevron-right" class="w-4 h-4" />
        <span class="text-gray-900 dark:text-zinc-100 font-medium">{{ product.category }}</span>
      </div>
      
      <h1 class="text-2xl sm:text-3xl font-bold text-gray-900 dark:text-zinc-100 mb-4 leading-tight">
        {{ product.title }}
      </h1>

      <div class="flex items-center gap-4 text-sm">
        <div class="flex items-center gap-1 text-yellow-500">
          <Icon name="lucide:star" class="w-4 h-4 fill-current" />
          <span class="font-bold text-gray-900 dark:text-zinc-100">{{ product.rating }}</span>
          <span class="text-gray-500 dark:text-zinc-400">(45 reviews)</span>
        </div>
        <div class="w-1 h-1 rounded-full bg-gray-300 dark:bg-zinc-700"></div>
        <div class="text-gray-600 dark:text-zinc-300">
          <span class="font-bold">{{ product.soldCount }}+</span> Sold
        </div>
      </div>
    </div>

    <!-- Price -->
    <div class="mb-8">
      <div class="text-3xl sm:text-4xl font-bold text-[#1A7B44] mb-1">
        {{ product.price }}<span class="text-lg font-normal text-gray-500 dark:text-zinc-400">/{{ product.unit }}</span>
      </div>
    </div>

    <!-- Details Grid -->
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-4 py-4 border-y border-gray-200 dark:border-zinc-800 mb-8">
      <div>
        <span class="block text-xs text-gray-500 dark:text-zinc-400 mb-1">Condition</span>
        <span class="font-medium text-gray-900 dark:text-zinc-100">{{ product.condition }}</span>
      </div>
      <div>
        <span class="block text-xs text-gray-500 dark:text-zinc-400 mb-1">Min. Order</span>
        <span class="font-medium text-gray-900 dark:text-zinc-100">{{ product.minOrder }} {{ product.unit }}</span>
      </div>
      <div>
        <span class="block text-xs text-gray-500 dark:text-zinc-400 mb-1">Weight</span>
        <span class="font-medium text-gray-900 dark:text-zinc-100">{{ product.weight }}</span>
      </div>
      <div>
        <span class="block text-xs text-gray-500 dark:text-zinc-400 mb-1">Category</span>
        <span class="font-medium text-[#1A7B44]">{{ product.category }}</span>
      </div>
    </div>
  </div>
</template>
