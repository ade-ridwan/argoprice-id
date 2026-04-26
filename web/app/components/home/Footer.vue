<script setup lang="ts">
import Logo from '~/components/logo.vue';
</script>

<template>
  <footer class="bg-[#156638] text-white pt-16 pb-8">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 md:grid-cols-3 gap-12 mb-12">
        <!-- Brand / About -->
        <div>
          <div class="flex items-center gap-2 mb-6">
            <Icon name="lucide:clover" class="h-8 w-8 text-white" />
            <div class="flex flex-col leading-none text-left">
              <span class="text-[15px] font-bold tracking-wider uppercase text-white">Komoditi</span>
              <span class="text-[15px] font-bold tracking-wider uppercase text-white">Kita</span>
            </div>
          </div>
          <p class="text-sm text-white/80 leading-relaxed mb-6 pr-4">
            A trusted platform connecting local farmers with buyers across Indonesia. Get fresh products at fair prices.
          </p>
          <div class="flex space-x-4">
            <a href="#" class="w-8 h-8 rounded-full bg-white/10 flex items-center justify-center hover:bg-white/20 transition-colors">
              <Icon name="lucide:facebook" class="w-4 h-4" />
            </a>
            <a href="#" class="w-8 h-8 rounded-full bg-white/10 flex items-center justify-center hover:bg-white/20 transition-colors">
              <Icon name="lucide:twitter" class="w-4 h-4" />
            </a>
            <a href="#" class="w-8 h-8 rounded-full bg-white/10 flex items-center justify-center hover:bg-white/20 transition-colors">
              <Icon name="lucide:instagram" class="w-4 h-4" />
            </a>
          </div>
        </div>

        <!-- Links -->
        <div class="md:pl-12">
          <h4 class="text-lg font-bold mb-6">Quick Links</h4>
          <ul class="space-y-3 text-sm text-white/80">
            <li><NuxtLink to="#" class="hover:text-white transition-colors">Home</NuxtLink></li>
            <li><NuxtLink to="#" class="hover:text-white transition-colors">Products</NuxtLink></li>
            <li><NuxtLink to="#" class="hover:text-white transition-colors">Commodity Prices</NuxtLink></li>
            <li><NuxtLink to="#" class="hover:text-white transition-colors">Farmer Education</NuxtLink></li>
            <li><NuxtLink to="#" class="hover:text-white transition-colors">About Us</NuxtLink></li>
          </ul>
        </div>

        <!-- Contact -->
        <div>
          <h4 class="text-lg font-bold mb-6">Contact Us</h4>
          <ul class="space-y-4 text-sm text-white/80">
            <li class="flex items-start gap-3">
              <Icon name="lucide:map-pin" class="w-5 h-5 shrink-0 mt-0.5 opacity-70" />
              <span>Agricultural Innovation Building, 3rd Floor<br/>Jl. Gatot Subroto No. 12, Jakarta</span>
            </li>
            <li class="flex items-center gap-3">
              <Icon name="lucide:mail" class="w-5 h-5 shrink-0 opacity-70" />
              <span>halo@komoditikita.com</span>
            </li>
            <li class="flex items-center gap-3">
              <Icon name="lucide:phone" class="w-5 h-5 shrink-0 opacity-70" />
              <span>+62 811 2345 6789</span>
            </li>
          </ul>
        </div>
      </div>

      <!-- Copyright -->
      <div class="border-t border-white/20 pt-8 flex flex-col md:flex-row items-center justify-between gap-4 text-xs text-white/60">
        <p>&copy; 2026 Komoditi Kita. All Rights Reserved.</p>
        <div class="flex gap-4">
          <NuxtLink to="#" class="hover:text-white transition-colors">Terms & Conditions</NuxtLink>
          <NuxtLink to="#" class="hover:text-white transition-colors">Privacy Policy</NuxtLink>
        </div>
      </div>
    </div>
  </footer>
</template>
