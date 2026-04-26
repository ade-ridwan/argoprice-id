<script setup lang="ts">
import type { Ref } from 'vue';
interface Props {
  images: string[];
  description: string;
}
const { images, description } = defineProps<Props>();
const idxImages: Ref<number> = ref(0);

const nextImages = () => {
  if (idxImages.value < images.length - 1) {
    idxImages.value++;
  }
}

const prevImages = () => {
  if (idxImages.value > 0) {
    idxImages.value--;
  }
}

const goToImage = (index: number) => {
  idxImages.value = index;
}

</script>

<template>
  <div class="flex flex-col gap-4 text-white">
    <!-- Main Image -->
    <div class="w-full aspect-[4/3] sm:aspect-video md:aspect-[4/3] rounded-2xl overflow-hidden bg-black/20 shadow-lg">
      <img :src="images[idxImages]" class="w-full h-full object-cover" alt="Commodity Image">
    </div>

    <!-- Thumbnails & Arrows -->
    <div class="flex items-center justify-between gap-4 mt-2">
      <button @click="prevImages" class="w-8 h-8 rounded-full bg-white/10 hover:bg-white/20 flex items-center justify-center transition-colors">
        <Icon name="lucide:arrow-left" class="w-4 h-4" />
      </button>
      
      <div class="flex gap-3 flex-1 overflow-x-auto no-scrollbar">
        <div v-for="(img, idx) in images" :key="idx" @click="goToImage(idx)" class="w-20 sm:w-24 aspect-video rounded-lg overflow-hidden border-2 border-transparent hover:border-white cursor-pointer transition-all shrink-0">
          <img :src="img" class="w-full h-full object-cover" alt="Thumbnail">
        </div>
      </div>

      <button @click="nextImages" class="w-8 h-8 rounded-full bg-white/10 hover:bg-white/20 flex items-center justify-center transition-colors">
        <Icon name="lucide:arrow-right" class="w-4 h-4" />
      </button>
    </div>

    <!-- Description -->
    <div class="mt-4">
      <h3 class="font-bold mb-2">Deskripsi Produk</h3>
      <p class="text-sm text-white/80 leading-relaxed">
        {{ description }}
      </p>
    </div>
  </div>
</template>

<style scoped>
.no-scrollbar::-webkit-scrollbar {
  display: none;
}
.no-scrollbar {
  -ms-overflow-style: none;
  scrollbar-width: none;
}
</style>
