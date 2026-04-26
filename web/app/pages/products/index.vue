<script setup lang="ts">
import { ref, computed } from 'vue';
import HomeNavbar from '~/components/home/Navbar.vue';
import HomeFooter from '~/components/home/Footer.vue';
import FilterSidebar from '~/components/catalog/FilterSidebar.vue';
import CatalogGrid from '~/components/catalog/CatalogGrid.vue';
import type { Product } from '~/components/home/ProductCard.vue';

definePageMeta({
  layout: false // Custom layout
})

interface CurrentFilter {
  category: string;
  location: string;
  maxPrice: number;
}

// Extended Dummy Data for Products
const allProducts = ref<Product[]>([
  {
    id: 1,
    title: 'High Quality Organic Compost (NPK)',
    price: 'Rp 15.000',
    unit: 'kg',
    rating: 4.8,
    location: 'Bandung, West Java',
    category: 'Fertilizers & Meds',
    image: '/products/compost.png'
  },
  {
    id: 2,
    title: 'Fresh Red Tomatoes Directly from Farmers',
    price: 'Rp 8.000',
    unit: 'kg',
    rating: 4.9,
    location: 'Lembang, West Java',
    category: 'Vegetables',
    image: 'https://images.unsplash.com/photo-1518977676601-b53f82aba655?q=80&w=800&auto=format&fit=crop'
  },
  {
    id: 3,
    title: 'Superior Rice Seeds Mapan P5 Anti-Pest',
    price: 'Rp 65.000',
    unit: 'pack',
    rating: 4.7,
    location: 'Subang, West Java',
    category: 'Seeds',
    image: '/products/rice.png'
  },
  {
    id: 4,
    title: 'Sweet Malang Apples Grade A Ready to Harvest',
    price: 'Rp 25.000',
    unit: 'kg',
    rating: 5.0,
    location: 'Batu, East Java',
    category: 'Fruits',
    image: '/products/apple.png'
  },
  {
    id: 5,
    title: 'Premium Local Corn (Pipil)',
    price: 'Rp 6.000',
    unit: 'kg',
    rating: 4.6,
    location: 'Garut, West Java',
    category: 'Grains & Crops',
    image: 'https://images.unsplash.com/photo-1551754655-cd27e38d2076?q=80&w=800&auto=format&fit=crop'
  },
  {
    id: 6,
    title: 'Hydroponic Lettuce (Selada Air)',
    price: 'Rp 12.000',
    unit: 'pack',
    rating: 4.9,
    location: 'Bogor, West Java',
    category: 'Vegetables',
    image: 'https://images.unsplash.com/photo-1622206151226-18ca2c9ab4a1?q=80&w=800&auto=format&fit=crop'
  }
]);

const currentFilters = ref({
  category: 'All',
  location: 'All Locations',
  maxPrice: 1000000
});

const handleFilterUpdate = (newFilters: CurrentFilter) => {
  currentFilters.value = newFilters;
};

// Filter logic (simulated)
const filteredProducts = computed(() => {
  return allProducts.value.filter(product => {
    // Note: Parsing price is hacky here just for simulation.
    // In real app, price should be a number field.
    const priceNum = parseInt(product.price.replace(/\D/g, ''));

    const matchCategory = currentFilters.value.category === 'All' || product.category === currentFilters.value.category;
    // Location matching is simple substring match for simulation
    const matchLocation = currentFilters.value.location === 'All Locations' || product.location.includes(currentFilters.value.location);
    const matchPrice = priceNum <= currentFilters.value.maxPrice;

    return matchCategory && matchLocation && matchPrice;
  });
});
</script>

<template>
  <div class="min-h-screen bg-gray-50 dark:bg-zinc-950 font-sans selection:bg-[#1A7B44]/30 selection:text-[#1A7B44]">
    <HomeNavbar />

    <!-- Page Header -->
    <div class="bg-[#1A7B44] dark:bg-zinc-900 pt-32 pb-16 px-4 sm:px-6 lg:px-8 relative overflow-hidden">
      <!-- Decoratives -->
      <div class="absolute -top-24 -right-24 w-96 h-96 bg-white/10 dark:bg-[#1A7B44]/20 rounded-full blur-3xl"/>
      <div class="absolute -bottom-24 -left-24 w-72 h-72 bg-black/10 dark:bg-black/40 rounded-full blur-3xl"/>

      <div class="max-w-7xl mx-auto relative z-10 text-center">
        <h1 class="text-3xl md:text-5xl font-bold text-white mb-4">Catalog Products</h1>
        <p class="text-white/80 max-w-2xl mx-auto text-sm md:text-base">Explore thousands of agricultural products and farming needs directly from trusted local farmers.</p>
      </div>
    </div>

    <!-- Main Content Layout -->
    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
      <div class="flex flex-col lg:flex-row gap-8">
        
        <!-- Sidebar -->
        <div class="w-full lg:w-1/4 shrink-0">
          <div class="sticky top-24">
            <FilterSidebar @filter="handleFilterUpdate" />
          </div>
        </div>

        <!-- Catalog Grid -->
        <div class="w-full lg:w-3/4">
          <CatalogGrid :products="filteredProducts" :total-results="filteredProducts.length" />
        </div>

      </div>
    </main>

    <HomeFooter />
  </div>
</template>
