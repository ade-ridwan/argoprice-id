<script setup lang="ts">
interface Props {
  price: string;
  trendPercentage: string;
  isPositive: boolean;
  chartData: number[];
}
const props = defineProps<Props>();

// Simple math to make bars scale
const maxVal = Math.max(...props.chartData);
const getHeights = () => props.chartData.map(val => (val / maxVal) * 100);

const days = ['Sen', 'Sel', 'Rab', 'Kam', 'Jum', 'Sab', 'Min'];
</script>

<template>
  <div class="bg-white dark:bg-zinc-900 rounded-2xl p-6 shadow-lg h-full flex flex-col">
    <div class="mb-4">
      <div class="text-sm text-gray-500 dark:text-zinc-400 font-medium mb-1">Harga per kg</div>
      <div class="text-3xl font-bold text-[#1A7B44] dark:text-[#22A05B] flex items-baseline gap-2">
        {{ price }}
        <span class="text-sm font-semibold flex items-center" :class="isPositive ? 'text-orange-500' : 'text-[#1A7B44]'">
          <Icon :name="isPositive ? 'lucide:trending-up' : 'lucide:trending-down'" class="w-4 h-4 mr-1" />
          {{ trendPercentage }}
        </span>
      </div>
      <div class="text-xs text-gray-400 dark:text-zinc-500 mt-2 font-medium">Tren Harga 7 Hari Terakhir</div>
    </div>

    <!-- Custom CSS Bar Chart -->
    <div class="flex-1 relative mt-auto flex flex-col min-h-[160px] pt-4">
      <!-- Grid Lines -->
      <div class="absolute inset-0 flex flex-col justify-between pointer-events-none pb-6">
        <div class="w-full h-px border-t border-dashed border-gray-200 dark:border-zinc-800 mt-4"></div>
        <div class="w-full h-px border-t border-dashed border-gray-200 dark:border-zinc-800"></div>
        <div class="w-full h-px border-t border-dashed border-gray-200 dark:border-zinc-800"></div>
        <div class="w-full h-px border-t border-gray-300 dark:border-zinc-700"></div>
      </div>

      <!-- Bars Area -->
      <div class="flex-1 relative flex items-end justify-between gap-3 sm:gap-4 z-10 pb-6">
        <div 
          v-for="(height, idx) in getHeights()" 
          :key="idx"
          class="group w-full h-full flex flex-col justify-end items-center relative cursor-pointer"
        >
          <!-- Tooltip on hover -->
          <div class="absolute -top-8 bg-gray-900 dark:bg-white text-white dark:text-gray-900 text-xs font-bold px-2 py-1 rounded opacity-0 group-hover:opacity-100 transition-opacity pointer-events-none whitespace-nowrap shadow-md">
            {{ chartData[idx] }}k
          </div>
          
          <!-- Bar -->
          <div 
            class="w-full bg-[#1A7B44]/20 dark:bg-[#1A7B44]/30 rounded-t-lg transition-all duration-300 group-hover:bg-[#1A7B44] dark:group-hover:bg-[#1A7B44] relative overflow-hidden"
            :style="{ height: `${Math.max(height, 5)}%` }"
          >
            <div class="absolute inset-0 bg-gradient-to-t from-transparent to-white/20 opacity-0 group-hover:opacity-100 transition-opacity"></div>
          </div>
          
          <!-- Label -->
          <div class="text-[10px] sm:text-xs text-gray-500 dark:text-zinc-400 mt-2 font-medium absolute -bottom-6">
            {{ days[idx] }}
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
