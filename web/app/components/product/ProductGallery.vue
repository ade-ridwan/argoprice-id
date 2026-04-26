<script setup lang="ts">
import { ref } from 'vue';

interface Props {
  images: string[];
}
const props = defineProps<Props>();

const activeIndex = ref(0);
</script>

<template>
  <div class="flex flex-col gap-4">
    <!-- Main Image -->
    <div class="w-full aspect-square rounded-2xl overflow-hidden bg-gray-100 dark:bg-zinc-900 border border-gray-200 dark:border-zinc-800">
      <img :src="images[activeIndex]" class="w-full h-full object-cover" alt="Product Image" />
    </div>

    <!-- Thumbnails -->
    <div v-if="images.length > 1" class="grid grid-cols-4 sm:grid-cols-5 gap-3">
      <button 
        v-for="(img, index) in images" 
        :key="index"
        @click="activeIndex = index"
        :class="[
          'aspect-square rounded-xl overflow-hidden border-2 transition-all',
          activeIndex === index 
            ? 'border-[#1A7B44] opacity-100' 
            : 'border-transparent opacity-60 hover:opacity-100 hover:border-gray-300 dark:hover:border-zinc-700'
        ]"
      >
        <img :src="img" class="w-full h-full object-cover" alt="Thumbnail" />
      </button>
    </div>
  </div>
</template>
