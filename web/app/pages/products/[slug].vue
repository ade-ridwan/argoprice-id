<script setup lang="ts">
import { ref } from 'vue';
import HomeNavbar from '~/components/home/Navbar.vue';
import HomeFooter from '~/components/home/Footer.vue';
import ProductGallery from '~/components/product/ProductGallery.vue';
import ProductInfo from '~/components/product/ProductInfo.vue';
import ProductActionCard from '~/components/product/ProductActionCard.vue';
import ProductCard from '~/components/home/ProductCard.vue';
import type { ProductData } from '~/components/product/ProductInfo.vue';

definePageMeta({
  layout: false
});

// Dummy Data for the specific product
const productDetails = ref<ProductData>({
  title: 'Fresh Red Tomatoes Directly from Farmers',
  price: 'Rp 8.000',
  unit: 'kg',
  rating: 4.9,
  soldCount: 1250,
  category: 'Vegetables',
  condition: 'Fresh',
  minOrder: 1,
  weight: '1 kg'
});

const productImages = ref([
  'https://images.unsplash.com/photo-1518977676601-b53f82aba655?q=80&w=800&auto=format&fit=crop',
  'https://images.unsplash.com/photo-1582284540020-8acbe03f4924?q=80&w=800&auto=format&fit=crop',
  'https://images.unsplash.com/photo-1592924357228-91a4daadcfea?q=80&w=800&auto=format&fit=crop'
]);

// Dummy Related Products
const relatedProducts = ref([
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

const description = ref(`
Our fresh red tomatoes are grown naturally without the use of harmful pesticides in the cool climate of Lembang. 
They are hand-picked at peak ripeness to ensure maximum sweetness and juiciness. 

**Why choose our tomatoes?**
- Rich in antioxidants and Vitamin C
- Harvested on the day of delivery
- Carefully sorted (Grade A quality)
- Lasts up to 1 week in the refrigerator

Perfect for salads, sambal, or cooking! By buying directly from us, you are supporting local farmers and getting the best possible price.
`);
</script>

<template>
  <div class="min-h-screen bg-gray-50 dark:bg-zinc-950 font-sans selection:bg-[#1A7B44]/30 selection:text-[#1A7B44]">
    <HomeNavbar />

    <!-- Breadcrumb (Simple) -->
    <div class="bg-white dark:bg-zinc-950 border-b border-gray-200 dark:border-zinc-800">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
        <nav class="text-sm text-gray-500 dark:text-zinc-400 flex items-center gap-2">
          <NuxtLink to="/" class="hover:text-[#1A7B44] transition-colors">Home</NuxtLink>
          <Icon name="lucide:chevron-right" class="w-3.5 h-3.5" />
          <NuxtLink to="/products" class="hover:text-[#1A7B44] transition-colors">Products</NuxtLink>
          <Icon name="lucide:chevron-right" class="w-3.5 h-3.5" />
          <span class="text-gray-900 dark:text-zinc-100 truncate">{{ productDetails.title }}</span>
        </nav>
      </div>
    </div>

    <!-- Main Content -->
    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 lg:py-12">
      <div class="flex flex-col lg:flex-row gap-8">
        
        <!-- Left Column: Gallery & Info -->
        <div class="flex-1 w-full flex flex-col gap-8 lg:max-w-[70%]">
          <!-- Gallery and Info Top -->
          <div class="flex flex-col md:flex-row gap-8">
            <div class="w-full md:w-2/5 shrink-0">
              <ProductGallery :images="productImages" />
            </div>
            <div class="w-full md:w-3/5">
              <ProductInfo :product="productDetails" />
            </div>
          </div>

          <!-- Description Section -->
          <div class="bg-white dark:bg-zinc-950 border border-gray-200 dark:border-zinc-800 rounded-2xl p-6 shadow-sm">
            <h3 class="font-bold text-lg text-gray-900 dark:text-zinc-100 mb-4 pb-4 border-b border-gray-200 dark:border-zinc-800">
              Product Description
            </h3>
            <div class="prose prose-sm dark:prose-invert max-w-none text-gray-600 dark:text-zinc-400 leading-relaxed whitespace-pre-line">
              {{ description }}
            </div>
          </div>

          <!-- Store Info Section -->
          <div class="bg-white dark:bg-zinc-950 border border-gray-200 dark:border-zinc-800 rounded-2xl p-6 shadow-sm flex items-center gap-4">
            <div class="w-16 h-16 bg-[#1A7B44] text-white rounded-full flex items-center justify-center shrink-0 text-xl font-bold">
              TJ
            </div>
            <div class="flex-1">
              <h4 class="font-bold text-gray-900 dark:text-zinc-100 flex items-center gap-1.5">
                Tani Jaya <Icon name="lucide:badge-check" class="w-4 h-4 text-[#1A7B44]" />
              </h4>
              <p class="text-sm text-gray-500 dark:text-zinc-400 mb-2">Lembang, West Java</p>
              <div class="flex items-center gap-4 text-xs">
                <span class="bg-gray-100 dark:bg-zinc-900 px-2 py-1 rounded font-medium text-gray-700 dark:text-zinc-300">
                  <Icon name="lucide:star" class="w-3.5 h-3.5 inline text-yellow-500 mr-0.5" /> 4.9 (Store)
                </span>
                <span class="bg-gray-100 dark:bg-zinc-900 px-2 py-1 rounded font-medium text-gray-700 dark:text-zinc-300">
                  Responds in ~15 mins
                </span>
              </div>
            </div>
            <button class="hidden sm:flex border border-[#1A7B44] text-[#1A7B44] hover:bg-[#1A7B44]/5 px-4 py-2 rounded-xl text-sm font-medium transition-colors">
              Visit Store
            </button>
          </div>
        </div>

        <!-- Right Column: Action Card -->
        <div class="w-full lg:w-1/3 xl:w-1/4 shrink-0">
          <ProductActionCard 
            :price-string="productDetails.price" 
            :unit="productDetails.unit" 
            :stock="150" 
          />
        </div>

      </div>

      <!-- Related Products -->
      <div class="mt-16 pt-16 border-t border-gray-200 dark:border-zinc-800">
        <h2 class="text-2xl font-bold text-gray-900 dark:text-zinc-100 mb-8">Related Products</h2>
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
          <ProductCard 
            v-for="prod in relatedProducts" 
            :key="prod.id" 
            :product="prod" 
          />
        </div>
      </div>
    </main>

    <HomeFooter />
  </div>
</template>
