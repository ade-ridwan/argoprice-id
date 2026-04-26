<script setup lang="ts">
</script>

<template>
  <section class="py-20 bg-gray-50 dark:bg-zinc-950">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="bg-white dark:bg-zinc-900 rounded-3xl p-8 md:p-12 lg:p-16 flex flex-col lg:flex-row items-center justify-between shadow-sm border border-gray-100 dark:border-zinc-800 relative overflow-hidden">
        
        <!-- Decorative Background Element -->
        <div class="absolute top-0 right-0 -mr-20 -mt-20 w-64 h-64 bg-orange-100 dark:bg-orange-900/20 rounded-full blur-3xl opacity-50"></div>

        <div class="lg:w-1/2 relative z-10 mb-10 lg:mb-0 text-center lg:text-left">
          <div class="inline-flex items-center px-3 py-1 rounded-full bg-orange-100 dark:bg-orange-950/30 text-orange-600 dark:text-orange-400 text-xs font-bold uppercase tracking-wide mb-4">
            Become Our Partner
          </div>
          <h2 class="text-2xl md:text-3xl lg:text-4xl font-bold text-gray-900 dark:text-zinc-100 mb-4 leading-tight">
            Have a Harvest or an Agricultural Store?
          </h2>
          <p class="text-gray-500 dark:text-zinc-400 text-sm md:text-base mb-8 max-w-lg mx-auto lg:mx-0">
            Reach more buyers across the country. Join as a seller on #KomoditiKita, enjoy easy, secure transactions with no registration fees.
          </p>
          <div class="flex flex-col sm:flex-row items-center justify-center lg:justify-start gap-4">
            <button class="w-full sm:w-auto bg-[#1A7B44] hover:bg-[#156638] text-white px-6 py-3 rounded-xl font-medium transition-colors shadow-sm">
              Register as Partner
            </button>
            <button class="w-full sm:w-auto bg-white dark:bg-zinc-800 text-gray-700 dark:text-zinc-300 border border-gray-200 dark:border-zinc-700 hover:bg-gray-50 dark:hover:bg-zinc-700 px-6 py-3 rounded-xl font-medium transition-colors">
              Learn More
            </button>
          </div>
        </div>

        <!-- Illustration / Mockup -->
        <div class="lg:w-5/12 relative z-10">
          <div class="bg-gradient-to-tr from-green-50 to-emerald-100 dark:from-zinc-800 dark:to-zinc-800 rounded-3xl p-6 shadow-xl transform rotate-3 hover:rotate-0 transition-transform duration-500 border border-white/50 dark:border-zinc-700">
            <div class="bg-white dark:bg-zinc-900 rounded-xl p-5 shadow-sm">
              <div class="flex items-center gap-3 mb-4">
                <div class="w-10 h-10 rounded-full bg-[#1A7B44] flex items-center justify-center text-white">
                  <Icon name="lucide:store" class="w-5 h-5" />
                </div>
                <div>
                  <h4 class="font-bold text-gray-900 dark:text-zinc-100 text-sm">Success Farm Store</h4>
                  <p class="text-xs text-gray-500">Bandung, West Java</p>
                </div>
              </div>
              <div class="space-y-3">
                <div class="h-2 bg-gray-100 dark:bg-zinc-800 rounded-full w-full"></div>
                <div class="h-2 bg-gray-100 dark:bg-zinc-800 rounded-full w-5/6"></div>
                <div class="h-2 bg-gray-100 dark:bg-zinc-800 rounded-full w-4/6"></div>
              </div>
              <div class="mt-6 flex items-center justify-between p-3 bg-gray-50 dark:bg-zinc-800/50 rounded-lg">
                <span class="text-xs font-medium text-gray-500">Total Sales</span>
                <span class="font-bold text-[#1A7B44] text-sm">+250 Sold</span>
              </div>
            </div>
          </div>
        </div>

      </div>
    </div>
  </section>
</template>
