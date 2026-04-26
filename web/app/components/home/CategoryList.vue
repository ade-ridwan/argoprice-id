<script setup lang="ts">
interface Category {
  id: string | number;
  name: string;
  icon: string;
  bgColorClass: string;
  iconColorClass: string;
}

interface Props {
  categories?: Category[];
}

const props = withDefaults(defineProps<Props>(), {
  categories: () => [
    { id: 1, name: 'Vegetables', icon: 'lucide:leaf', bgColorClass: 'bg-green-50 dark:bg-green-950/30', iconColorClass: 'text-green-600 dark:text-green-400' },
    { id: 2, name: 'Fruits', icon: 'lucide:apple', bgColorClass: 'bg-blue-50 dark:bg-blue-950/30', iconColorClass: 'text-blue-500 dark:text-blue-400' },
    { id: 3, name: 'Grains & Crops', icon: 'lucide:wheat', bgColorClass: 'bg-red-50 dark:bg-red-950/30', iconColorClass: 'text-red-500 dark:text-red-400' },
    { id: 4, name: 'Farming Tools', icon: 'lucide:shovel', bgColorClass: 'bg-gray-100 dark:bg-zinc-800/50', iconColorClass: 'text-gray-600 dark:text-gray-400' },
    { id: 5, name: 'Seeds', icon: 'lucide:sprout', bgColorClass: 'bg-orange-50 dark:bg-orange-950/30', iconColorClass: 'text-orange-500 dark:text-orange-400' },
    { id: 6, name: 'Fertilizers & Meds', icon: 'lucide:flask-conical', bgColorClass: 'bg-lime-50 dark:bg-lime-950/30', iconColorClass: 'text-lime-600 dark:text-lime-400' },
  ]
});
</script>

<template>
  <section class="py-12 bg-white dark:bg-zinc-950 border-b border-gray-100 dark:border-zinc-800">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center mb-8">
        <h2 class="text-2xl font-bold text-gray-900 dark:text-zinc-100 mb-2">Featured Categories</h2>
        <p class="text-sm text-gray-500 dark:text-zinc-400">Find your needs based on commodity categories</p>
      </div>

      <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-6 gap-4 sm:gap-6">
        <NuxtLink 
          v-for="category in props.categories" 
          :key="category.id" 
          to="#"
          class="flex flex-col items-center justify-center p-4 rounded-2xl border border-gray-100 dark:border-zinc-800 hover:shadow-md transition-all duration-300 group dark:bg-zinc-900"
        >
          <div 
            :class="[
              'w-14 h-14 rounded-2xl flex items-center justify-center mb-3 transition-transform duration-300 group-hover:scale-110', 
              category.bgColorClass
            ]"
          >
            <Icon :name="category.icon" :class="['w-6 h-6', category.iconColorClass]" />
          </div>
          <span class="text-xs sm:text-sm font-semibold text-gray-700 dark:text-zinc-300 text-center">
            {{ category.name }}
          </span>
        </NuxtLink>
      </div>
    </div>
  </section>
</template>
