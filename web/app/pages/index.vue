<script setup lang="ts">
import { ref } from 'vue';

// Define layout if needed, but since it has its own navbar and footer, 
// we'll just use the default layout without any wrappers or explicitly define it here.
definePageMeta({
  layout: false // We use our custom Navbar and Footer inside this page directly
})

// Dummy Data for Products
const products = ref([
  {
    id: 1,
    title: 'High Quality Organic Compost (NPK)',
    price: 'Rp 15.000',
    unit: 'kg',
    rating: 4.8,
    location: 'Bandung, West Java',
    category: 'Fertilizer & Medicine',
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
  }
]);

// Dummy Data for Articles
const articles = ref([
  {
    id: 1,
    title: 'Effective Ways to Make Your Own Compost in a Small Space',
    summary: 'Compost is very important for soil fertility. Learn how to make it with simple ingredients around the house.',
    date: 'May 10, 2026',
    tag: 'GUIDE',
    image: 'https://images.unsplash.com/photo-1625246333195-78d9c38ad449?q=80&w=800&auto=format&fit=crop'
  },
  {
    id: 2,
    title: 'Understanding Late Blight Disease in Potato Plants & Its Solutions',
    summary: 'Late blight often attacks potato plants during the rainy season. Recognize the symptoms and proper handling before it is too late.',
    date: 'May 08, 2026',
    tag: 'PEST INFO',
    image: '/posts/post-2.png'
  }
]);
</script>

<template>
  <div class="min-h-screen bg-gray-50 dark:bg-zinc-950 font-sans selection:bg-[#1A7B44]/30 selection:text-[#1A7B44]">
    <!-- Navigation -->
    <HomeNavbar />

    <!-- Main Content -->
    <main>
      <HomeHero />
      <HomeCategoryList />
      <HomeProductList :products="products" />
      <HomeEducationList :articles="articles" />
      <HomeCta />
    </main>

    <!-- Footer -->
    <HomeFooter />
  </div>
</template>