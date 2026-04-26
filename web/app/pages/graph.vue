<script setup lang="ts">
import { ref } from 'vue';
import HomeNavbar from '~/components/home/Navbar.vue';
import HomeFooter from '~/components/home/Footer.vue';
import CommodityGallery from '~/components/graph/CommodityGallery.vue';
import PriceChart from '~/components/graph/PriceChart.vue';
import LocationCards from '~/components/graph/LocationCards.vue';
import ProductCard from '~/components/home/ProductCard.vue';
import type { Product } from '~/components/home/ProductCard.vue';

definePageMeta({
  layout: false
});

const commodityImages = ref([
  '/products/chili.png', // red chilies
  '/products/chili2.png', // field
  '/products/chili3.png'  // pile
]);

const commodityDescription = ref("Cabai merah segar berkualitas premium yang dipanen pada umur optimal sehingga menghasilkan rasa pedas yang kuat. Harga mulai dari Rp 125.000/kg, cocok untuk kebutuhan rumah tangga maupun usaha kuliner.");

const dummyChartData = ref([45, 60, 40, 75, 55, 80, 100]); // Fake heights for the bar chart

const similarProducts = ref<Product[]>([
  {
    id: 101,
    title: 'Cabai Merah Besar',
    price: 'Rp 124.000',
    unit: 'kg',
    rating: 4.8,
    location: '1.2 km',
    category: 'Sayuran',
    image: 'https://images.unsplash.com/photo-1596649303534-118e6cb0f455?q=80&w=800&auto=format&fit=crop'
  },
  {
    id: 102,
    title: 'Cabai Merah Fresh',
    price: 'Rp 127.000',
    unit: 'kg',
    rating: 4.9,
    location: '2.5 km',
    category: 'Sayuran',
    image: 'https://images.unsplash.com/photo-1588165171080-c89acfa5ee83?q=80&w=800&auto=format&fit=crop'
  },
  {
    id: 103,
    title: 'Cabai Merah',
    price: 'Rp 126.000',
    unit: 'kg',
    rating: 4.7,
    location: '3.1 km',
    category: 'Sayuran',
    image: 'https://images.unsplash.com/photo-1596649283437-6d6da84d62ea?q=80&w=800&auto=format&fit=crop'
  },
  {
    id: 104,
    title: 'Cabai Merah Besar Segar',
    price: 'Rp 125.500',
    unit: 'kg',
    rating: 5.0,
    location: '4.8 km',
    category: 'Sayuran',
    image: 'https://images.unsplash.com/photo-1598514982205-f36b96d1e8d4?q=80&w=800&auto=format&fit=crop'
  }
]);
</script>

<template>
  <div class="min-h-screen bg-white dark:bg-zinc-950 font-sans selection:bg-[#1A7B44]/30 selection:text-[#1A7B44]">
    <HomeNavbar />

    <!-- Green Hero Section -->
    <div class="bg-[#1A7B44] pt-12 pb-16">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        
        <!-- Breadcrumb -->
        <nav class="text-sm text-white/80 flex items-center gap-2 mb-8">
          <NuxtLink to="/" class="hover:text-white transition-colors">Home</NuxtLink>
          <Icon name="lucide:chevron-right" class="w-3.5 h-3.5" />
          <span class="hover:text-white transition-colors cursor-pointer">Grafik</span>
          <Icon name="lucide:chevron-right" class="w-3.5 h-3.5" />
          <span class="hover:text-white transition-colors cursor-pointer">Sayuran</span>
          <Icon name="lucide:chevron-right" class="w-3.5 h-3.5" />
          <span class="text-white font-medium">Cabai Merah</span>
        </nav>

        <!-- Main Content Split -->
        <div class="flex flex-col lg:flex-row gap-10">
          
          <!-- Left side: Gallery & Desc -->
          <div class="w-full lg:w-5/12 shrink-0">
            <CommodityGallery 
              :images="commodityImages" 
              :description="commodityDescription" 
            />
          </div>

          <!-- Right side: Chart & Locations -->
          <div class="w-full lg:w-7/12 flex flex-col gap-4">
            <div class="h-80">
              <PriceChart 
                price="Rp 125.000" 
                trend-percentage="+ 15%" 
                :is-positive="true" 
                :chart-data="dummyChartData" 
              />
            </div>
            
            <div class="mt-2">
               <LocationCards />
            </div>
          </div>

        </div>

      </div>
    </div>

    <!-- Similar Products Grid -->
    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
      <div class="flex items-center justify-between mb-8">
        <h2 class="text-2xl font-bold text-gray-900 dark:text-zinc-100">Produk Serupa di Wilayah ini</h2>
        <NuxtLink to="/products" class="text-sm text-[#1A7B44] hover:text-[#156638] font-medium flex items-center gap-1 transition-colors">
          Lihat Semua <Icon name="lucide:arrow-right" class="w-4 h-4" />
        </NuxtLink>
      </div>

      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
        <ProductCard 
          v-for="prod in similarProducts" 
          :key="prod.id" 
          :product="prod" 
        />
      </div>
    </main>

    <HomeFooter />
  </div>
</template>
