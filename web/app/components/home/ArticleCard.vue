<script setup lang="ts">
export interface Article {
  id: string | number;
  title: string;
  summary: string;
  date: string;
  tag: string;
  image: string;
}

interface Props {
  article: Article;
}

const props = defineProps<Props>();
</script>

<template>
  <div class="bg-[#156638] rounded-2xl overflow-hidden border border-white/10 flex flex-col md:flex-row group hover:bg-[#1A7B44] transition-colors duration-300">
    <!-- Image -->
    <div class="w-full md:w-2/5 h-48 md:h-auto relative overflow-hidden">
      <img 
        :src="article.image" 
        :alt="article.title" 
        class="absolute inset-0 w-full h-full object-cover transition-transform duration-700 group-hover:scale-105"
      />
    </div>

    <!-- Content -->
    <div class="p-6 w-full md:w-3/5 flex flex-col justify-center">
      <div class="flex items-center gap-3 mb-3">
        <span class="bg-orange-500 text-white text-[10px] font-bold px-2 py-1 rounded-md uppercase tracking-wide">
          {{ article.tag }}
        </span>
        <span class="text-xs text-white/70">{{ article.date }}</span>
      </div>

      <h3 class="text-lg font-bold text-white leading-snug mb-2 line-clamp-2">
        {{ article.title }}
      </h3>
      
      <p class="text-sm text-white/80 line-clamp-2 mb-4 font-light">
        {{ article.summary }}
      </p>

      <NuxtLink to="#" class="text-xs font-semibold text-white flex items-center gap-1 group/link mt-auto w-fit">
        Baca Selengkapnya
        <Icon name="lucide:arrow-right" class="w-3.5 h-3.5 transition-transform group-hover/link:translate-x-1" />
      </NuxtLink>
    </div>
  </div>
</template>
