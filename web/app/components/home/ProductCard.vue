<script setup lang="ts">
export interface Product {
  id: string | number;
  title: string;
  price: string;
  unit: string;
  rating: number;
  location: string;
  image: string;
  category: string;
}

interface Props {
  product: Product;
}

const { product } = defineProps<Props>();

</script>

<template>
  <div
    class="bg-white dark:bg-zinc-900 rounded-2xl border border-gray-200 dark:border-zinc-800 overflow-hidden hover:shadow-lg transition-all duration-300 group flex flex-col">
    <!-- Image -->
    <div class="relative w-full h-48 overflow-hidden bg-gray-100 dark:bg-zinc-800">
      <img 
        :src="product.image" 
        :alt="product.title" 
        class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-110"
      >
      <div class="absolute top-3 left-3 bg-orange-500 text-white text-[10px] font-bold px-2 py-1 rounded-md uppercase tracking-wide shadow-sm">
        {{ product.category }}
      </div>
    </div>

    <!-- Content -->
    <div class="p-4 flex flex-col flex-1">
      <div class="flex items-center gap-1 text-yellow-500 mb-2">
        <Icon name="lucide:star" class="w-3.5 h-3.5 fill-current" />
        <span class="text-xs font-semibold text-gray-700 dark:text-zinc-300">{{ product.rating }}</span>
      </div>

      <h3 class="font-bold text-gray-900 dark:text-zinc-100 text-sm line-clamp-2 leading-tight mb-2 group-hover:text-[#1A7B44] transition-colors">
        {{ product.title }}
      </h3>

      <div class="flex items-center gap-1 text-gray-500 dark:text-zinc-400 mb-4 mt-auto">
        <Icon name="lucide:map-pin" class="w-3.5 h-3.5" />
        <span class="text-xs truncate">{{ product.location }}</span>
      </div>

      <div class="flex items-end justify-between mt-auto pt-4 border-t border-gray-100 dark:border-zinc-800">
        <div>
          <span class="text-[10px] text-gray-500 dark:text-zinc-400 block mb-0.5">Price</span>
          <div class="text-[#1A7B44] font-bold text-lg leading-none">
            {{ product.price }}<span class="text-xs text-gray-500 font-normal">/{{ product.unit }}</span>
          </div>
        </div>
        <NuxtLink 
          :to="`/products/${product.id}`"
          class="bg-[#1A7B44]/10 hover:bg-[#1A7B44] text-[#1A7B44] hover:text-white p-2 rounded-lg transition-colors"
        >
          <Icon name="lucide:shopping-cart" class="w-4 h-4" />
        </NuxtLink>
      </div>
    </div>
  </div>
</template>
