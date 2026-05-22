<script setup lang="ts">
import { ref, computed } from 'vue';
import HomeNavbar from '~/components/home/Navbar.vue';
import HomeFooter from '~/components/home/Footer.vue';

definePageMeta({
  layout: false
});

// Base historical data (in thousands: 110k, 115k, etc.)
const historicalData = [110, 115, 120, 125]; 
const labelsHistorical = ['Week -3', 'Week -2', 'Week -1', 'Current'];
const labelsPredicted = ['Week +1', 'Week +2', 'Week +3', 'Week +4'];

// Interactive Factors (using Number explicitly to avoid string concatenation)
const weatherFactor = ref<number>(0); // -10 (Perfect) to +30 (Extreme Weather)
const demandFactor = ref<number>(0);  // -10 (Low Demand) to +20 (High Demand)
const transportCost = ref<number>(0); // 0 (Normal) to +15 (High Fuel)

// Dynamically calculate predicted future prices based on factors
const predictedData = computed(() => {
  const basePrice = historicalData[historicalData.length - 1]; // Start from current price (125)
  
  // Force numeric types just in case DOM tries to pass strings
  const w = Number(weatherFactor.value) || 0;
  const d = Number(demandFactor.value) || 0;
  const t = Number(transportCost.value) || 0;
  
  // Create a realistic-looking curve where impact grows over time
  return [
    Math.round(basePrice + (w * 0.25) + (d * 0.3) + (t * 0.2)),
    Math.round(basePrice + (w * 0.5) + (d * 0.6) + (t * 0.5)),
    Math.round(basePrice + (w * 0.75) + (d * 0.8) + (t * 0.8)),
    Math.round(basePrice + w + d + t)
  ];
});

// Chart calculations
const allChartData = computed(() => [...historicalData, ...predictedData.value]);

// Calculate max dynamically, but add padding (e.g., +20) so bars never hit the absolute ceiling
const maxVal = computed(() => Math.max(...allChartData.value, 160) + 20); 
const getHeights = computed(() => allChartData.value.map(val => (val / maxVal.value) * 100));

// Formatted Final Predicted Price (Week +4)
const finalPredictedPrice = computed(() => {
  const finalVal = predictedData.value[3];
  return new Intl.NumberFormat('en-ID', { 
    style: 'currency', 
    currency: 'IDR', 
    minimumFractionDigits: 0 
  }).format(finalVal * 1000);
});

// Price trend analysis
const priceDifference = computed(() => {
  const diff = predictedData.value[3] - historicalData[historicalData.length - 1];
  return diff; // Will be positive for increase, negative for decrease
});

// Helper for resetting
const resetSimulation = () => {
  weatherFactor.value = 0;
  demandFactor.value = 0;
  transportCost.value = 0;
};
</script>

<template>
  <div class="min-h-screen bg-gray-50 dark:bg-zinc-950 font-sans selection:bg-[#1A7B44]/30 selection:text-[#1A7B44]">
    <HomeNavbar />

    <!-- Header Section -->
    <div class="bg-[#1A7B44] pt-12 pb-24 transition-colors duration-500">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <!-- Breadcrumb -->
        <nav class="text-sm text-white/80 flex items-center gap-2 mb-6">
          <NuxtLink to="/" class="hover:text-white transition-colors">Home</NuxtLink>
          <Icon name="lucide:chevron-right" class="w-3.5 h-3.5" />
          <NuxtLink to="/products/chili" class="hover:text-white transition-colors cursor-pointer">Red Chili</NuxtLink>
          <Icon name="lucide:chevron-right" class="w-3.5 h-3.5" />
          <span class="text-white font-medium">Price Prediction</span>
        </nav>

        <div>
          <h1 class="text-3xl font-bold text-white mb-2">Interactive AI Price Prediction</h1>
          <p class="text-white/80 max-w-2xl text-sm sm:text-base">Simulate how market variables like weather, demand, and transport costs might affect the price trajectory of Red Chili over the next 4 weeks.</p>
        </div>
      </div>
    </div>

    <!-- Main Content -->
    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 -mt-12 pb-16">
      <div class="flex flex-col lg:flex-row gap-6">
        
        <!-- Left: Controls & Simulators -->
        <div class="w-full lg:w-4/12 flex flex-col gap-6">
          <div class="bg-white dark:bg-zinc-900 rounded-2xl p-6 shadow-lg border border-gray-100 dark:border-zinc-800">
            <div class="flex items-center justify-between mb-6">
              <h2 class="text-lg font-bold text-gray-900 dark:text-zinc-100 flex items-center gap-2">
                <Icon name="lucide:sliders-horizontal" class="w-5 h-5 text-[#1A7B44]" />
                Simulation Factors
              </h2>
              <button @click="resetSimulation" class="text-xs font-medium text-gray-500 hover:text-gray-900 dark:text-zinc-400 dark:hover:text-white transition-colors">
                Reset
              </button>
            </div>

            <!-- Weather Factor -->
            <div class="mb-6 group">
              <div class="flex justify-between mb-2">
                <label class="text-sm font-medium text-gray-700 dark:text-zinc-300">Weather Condition</label>
                <span class="text-xs font-bold px-2 py-0.5 rounded bg-gray-100 dark:bg-zinc-800 text-gray-600 dark:text-zinc-300 transition-colors" :class="{'text-orange-600 bg-orange-100 dark:bg-orange-500/20 dark:text-orange-400': weatherFactor > 15}">
                  {{ weatherFactor === 0 ? 'Normal' : (weatherFactor > 0 ? (weatherFactor > 15 ? 'Extreme' : 'Poor') : 'Optimal') }}
                </span>
              </div>
              <input 
                type="range" 
                min="-10" max="30" step="5" 
                v-model.number="weatherFactor" 
                class="w-full h-2 bg-gray-200 dark:bg-zinc-800 rounded-lg appearance-none cursor-pointer accent-[#1A7B44]"
              >
              <div class="flex justify-between text-[10px] text-gray-400 mt-1">
                <span>Perfect</span>
                <span>Drought/Flood</span>
              </div>
            </div>

            <!-- Demand Factor -->
            <div class="mb-6 group">
              <div class="flex justify-between mb-2">
                <label class="text-sm font-medium text-gray-700 dark:text-zinc-300">Market Demand</label>
                <span class="text-xs font-bold px-2 py-0.5 rounded bg-gray-100 dark:bg-zinc-800 text-gray-600 dark:text-zinc-300">
                  {{ demandFactor === 0 ? 'Stable' : (demandFactor > 0 ? 'High' : 'Low') }}
                </span>
              </div>
              <input 
                type="range" 
                min="-10" max="20" step="5" 
                v-model.number="demandFactor" 
                class="w-full h-2 bg-gray-200 dark:bg-zinc-800 rounded-lg appearance-none cursor-pointer accent-[#1A7B44]"
              >
              <div class="flex justify-between text-[10px] text-gray-400 mt-1">
                <span>Low</span>
                <span>Holiday Peak</span>
              </div>
            </div>

            <!-- Transport Cost -->
            <div class="mb-2 group">
              <div class="flex justify-between mb-2">
                <label class="text-sm font-medium text-gray-700 dark:text-zinc-300">Fuel & Transport</label>
                <span class="text-xs font-bold px-2 py-0.5 rounded bg-gray-100 dark:bg-zinc-800 text-gray-600 dark:text-zinc-300">
                  {{ transportCost === 0 ? 'Normal' : 'Elevated' }}
                </span>
              </div>
              <input 
                type="range" 
                min="0" max="15" step="3" 
                v-model.number="transportCost" 
                class="w-full h-2 bg-gray-200 dark:bg-zinc-800 rounded-lg appearance-none cursor-pointer accent-[#1A7B44]"
              >
              <div class="flex justify-between text-[10px] text-gray-400 mt-1">
                <span>Base Cost</span>
                <span>High Fuel Prices</span>
              </div>
            </div>
          </div>
          
          <!-- AI Insight Card -->
          <div 
            class="rounded-2xl p-6 shadow-lg text-white transition-all duration-500 relative overflow-hidden"
            :class="priceDifference > 15 ? 'bg-gradient-to-br from-red-500 to-red-700' : (priceDifference < 0 ? 'bg-gradient-to-br from-emerald-500 to-emerald-700' : 'bg-gradient-to-br from-[#1A7B44] to-[#11552f]')"
          >
            <!-- Decorative background pattern -->
            <div class="absolute inset-0 opacity-10" style="background-image: radial-gradient(circle at 2px 2px, white 1px, transparent 0); background-size: 16px 16px;"></div>

            <div class="relative z-10">
              <h3 class="text-sm font-medium text-white/80 mb-1 flex items-center gap-2">
                Estimated Price (Week +4)
                <Icon :name="priceDifference >= 0 ? 'lucide:trending-up' : 'lucide:trending-down'" class="w-4 h-4" />
              </h3>
              <div class="text-3xl font-bold mb-4 tracking-tight">{{ finalPredictedPrice }}</div>
              
              <div class="bg-black/10 backdrop-blur-sm rounded-xl p-4 border border-white/20">
                <div class="flex items-start gap-3">
                  <Icon name="lucide:bot" class="w-6 h-6 shrink-0" :class="priceDifference > 15 ? 'text-red-200' : 'text-green-200'" />
                  <p class="text-sm text-white/90 leading-relaxed">
                    Based on your simulation, the price is expected to <strong class="text-white">{{ priceDifference >= 0 ? 'increase' : 'decrease' }}</strong> by roughly <strong>{{ Math.abs(priceDifference) }}k IDR</strong> per kg over the next month. 
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Right: Chart -->
        <div class="w-full lg:w-8/12 bg-white dark:bg-zinc-900 rounded-2xl p-6 shadow-lg border border-gray-100 dark:border-zinc-800 flex flex-col min-h-[500px]">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4 mb-8">
            <div>
              <h2 class="text-xl font-bold text-gray-900 dark:text-zinc-100">8-Week Price Trajectory</h2>
              <p class="text-sm text-gray-500 dark:text-zinc-400">Historical data vs AI simulated forecast</p>
            </div>
            
            <!-- Legend -->
            <div class="flex items-center gap-4 text-xs sm:text-sm bg-gray-50 dark:bg-zinc-800/50 p-2 px-4 rounded-full border border-gray-100 dark:border-zinc-700">
              <div class="flex items-center gap-2">
                <div class="w-3 h-3 rounded-full bg-gray-300 dark:bg-zinc-600"></div>
                <span class="text-gray-600 dark:text-zinc-300 font-medium">Historical</span>
              </div>
              <div class="flex items-center gap-2">
                <div class="w-3 h-3 rounded-full bg-[#1A7B44]"></div>
                <span class="text-gray-600 dark:text-zinc-300 font-medium">Predicted</span>
              </div>
            </div>
          </div>

          <!-- Chart Area -->
          <div class="flex-1 relative flex flex-col pt-4 pb-8">
            <!-- Grid Lines -->
            <div class="absolute inset-0 flex flex-col justify-between pointer-events-none pb-10">
              <div v-for="i in 6" :key="i" class="w-full h-px border-t border-dashed border-gray-200 dark:border-zinc-800/80"></div>
            </div>

            <!-- Bars container -->
            <div class="flex-1 relative flex items-end justify-between gap-2 sm:gap-4 z-10 pb-10">
              <div 
                v-for="(height, idx) in getHeights" 
                :key="idx"
                class="group w-full h-full flex flex-col justify-end items-center relative cursor-pointer"
              >
                <!-- Tooltip -->
                <div class="absolute -top-10 bg-gray-900 dark:bg-white text-white dark:text-gray-900 text-xs font-bold px-3 py-1.5 rounded opacity-0 group-hover:opacity-100 transition-opacity pointer-events-none whitespace-nowrap shadow-md z-20">
                  Rp {{ allChartData[idx] }}.000
                  <div class="absolute -bottom-1 left-1/2 -translate-x-1/2 w-2 h-2 bg-gray-900 dark:bg-white rotate-45"></div>
                </div>
                
                <!-- Bar -->
                <div 
                  class="w-full rounded-t-lg transition-all duration-500 ease-out relative overflow-hidden"
                  :class="idx < 4 ? 'bg-gray-300 dark:bg-zinc-700 hover:bg-gray-400 dark:hover:bg-zinc-600' : 'bg-[#1A7B44]/90 hover:bg-[#1A7B44] shadow-[0_0_15px_rgba(26,123,68,0.2)]'"
                  :style="{ height: `${Math.max(height, 5)}%` }"
                >
                  <!-- Simulated prediction stripes -->
                  <div v-if="idx >= 4" class="absolute inset-0 opacity-20" style="background-image: repeating-linear-gradient(45deg, transparent, transparent 10px, rgba(255,255,255,0.4) 10px, rgba(255,255,255,0.4) 20px);"></div>
                  
                  <!-- Glossy highlight top -->
                  <div class="absolute top-0 left-0 right-0 h-2 bg-white/20"></div>
                </div>
                
                <!-- X-Axis Label -->
                <div class="text-[10px] sm:text-xs mt-3 absolute -bottom-8 whitespace-nowrap" :class="idx < 4 ? 'text-gray-500 dark:text-zinc-500 font-medium' : 'text-[#1A7B44] font-bold'">
                  {{ idx < 4 ? labelsHistorical[idx] : labelsPredicted[idx - 4] }}
                </div>
              </div>

              <!-- Separation Line between Past and Future -->
              <div class="absolute top-0 bottom-10 border-l-2 border-dashed border-orange-400 dark:border-orange-500/70 z-0 flex items-start -ml-px" style="left: 50%;">
                <div class="bg-orange-100 text-orange-700 dark:bg-orange-500/20 dark:text-orange-400 text-[10px] font-bold px-3 py-1 rounded-full -translate-x-1/2 -mt-4 shadow-sm border border-orange-200 dark:border-orange-500/30">
                  TODAY
                </div>
              </div>
            </div>
          </div>
          
        </div>
      </div>
    </main>

    <HomeFooter />
  </div>
</template>

<style scoped>
/* Range slider styling fallback for WebKit & Firefox */
input[type=range] {
  -webkit-appearance: none;
}
input[type=range]::-webkit-slider-thumb {
  -webkit-appearance: none;
  appearance: none;
  width: 18px;
  height: 18px;
  border-radius: 50%;
  background: #1A7B44;
  cursor: pointer;
  border: 2px solid white;
  box-shadow: 0 2px 5px rgba(0,0,0,0.2);
  transition: transform 0.1s;
}
input[type=range]::-webkit-slider-thumb:hover {
  transform: scale(1.15);
}

input[type=range]::-moz-range-thumb {
  width: 18px;
  height: 18px;
  border-radius: 50%;
  background: #1A7B44;
  cursor: pointer;
  border: 2px solid white;
  box-shadow: 0 2px 5px rgba(0,0,0,0.2);
  transition: transform 0.1s;
}
input[type=range]::-moz-range-thumb:hover {
  transform: scale(1.15);
}
</style>