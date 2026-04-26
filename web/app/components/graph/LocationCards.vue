<script setup lang="ts">
// Simple static UI for the location info below the chart
</script>

<template>
  <div class="flex flex-col gap-4">
    <!-- Two small cards -->
    <div class="grid grid-cols-2 gap-4">
      <div class="bg-white dark:bg-zinc-900 p-4 rounded-xl shadow-sm flex items-center gap-3">
        <div class="bg-gray-100 dark:bg-zinc-800 p-2 rounded-full text-gray-600 dark:text-zinc-300">
          <Icon name="lucide:map-pin" class="w-5 h-5" />
        </div>
        <div>
          <div class="text-xs text-gray-500 dark:text-zinc-400">Provinsi</div>
          <div class="text-sm font-bold text-gray-900 dark:text-zinc-100">Jawa Barat</div>
        </div>
      </div>
      
      <div class="bg-white dark:bg-zinc-900 p-4 rounded-xl shadow-sm flex items-center gap-3">
        <div class="bg-gray-100 dark:bg-zinc-800 p-2 rounded-full text-gray-600 dark:text-zinc-300">
          <Icon name="lucide:map" class="w-5 h-5" />
        </div>
        <div>
          <div class="text-xs text-gray-500 dark:text-zinc-400">Kota</div>
          <div class="text-sm font-bold text-gray-900 dark:text-zinc-100">Tasikmalaya</div>
        </div>
      </div>
    </div>

    <!-- Long address card -->
    <div class="bg-white dark:bg-zinc-900 p-4 rounded-xl shadow-sm flex items-start gap-3">
      <div class="text-gray-600 dark:text-zinc-300 mt-1">
        <Icon name="lucide:map-pin" class="w-5 h-5" />
      </div>
      <div class="flex-1">
        <div class="text-xs text-gray-500 dark:text-zinc-400">Alamat</div>
        <div class="text-sm font-medium text-gray-900 dark:text-zinc-100 leading-tight">
          Jl. Agrikultur No. 45, Ciaimus,<br/>
          Cipedes, Kota Tasikmalaya<br/>
          46131
        </div>
      </div>
      <div class="w-16 h-16 bg-gray-200 dark:bg-zinc-800 rounded-lg shrink-0 overflow-hidden">
        <img src="https://images.unsplash.com/photo-1524661135-423995f22d0b?q=80&w=200&auto=format&fit=crop" class="w-full h-full object-cover opacity-80" alt="Map" />
      </div>
    </div>

    <!-- Buttons -->
    <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 mt-2">
      <button class="bg-transparent border border-white text-white hover:bg-white/10 py-3 rounded-xl font-medium text-sm transition-colors shadow-sm">
        Hubungi Penjual
      </button>
      <button class="bg-white text-[#1A7B44] hover:bg-gray-50 py-3 rounded-xl font-medium text-sm transition-colors shadow-sm">
        Prediksi Harga Bulan Depan
      </button>
    </div>
  </div>
</template>
