<script setup lang="ts">
import ArticleCard from './ArticleCard.vue';
import type { Article } from './ArticleCard.vue';

interface Props {
  articles: Article[];
}

const props = defineProps<Props>();
</script>

<template>
  <section class="py-16 bg-[#1A7B44]">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <!-- Header -->
      <div class="mb-10 text-white">
        <div class="inline-block px-3 py-1 rounded-full bg-white/10 border border-white/20 text-xs font-semibold tracking-wide mb-3">
          FARMER TIPS
        </div>
        <h2 class="text-2xl md:text-3xl font-bold mb-2">Latest Agricultural Education</h2>
        <p class="text-white/80 text-sm md:text-base max-w-2xl">
          Increase your harvest with guides, farming methods, and the latest news about agriculture.
        </p>
      </div>

      <!-- Grid -->
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <ArticleCard 
          v-for="article in articles" 
          :key="article.id" 
          :article="article" 
        />
      </div>
    </div>
  </section>
</template>
